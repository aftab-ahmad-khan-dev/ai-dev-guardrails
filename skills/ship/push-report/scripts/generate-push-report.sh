#!/usr/bin/env bash
# Append a push/security section to REPORT.md at the git repo root.
# Safe: never deletes project files; only creates/updates REPORT.md.
set -euo pipefail

if git rev-parse --show-toplevel >/dev/null 2>&1; then
  ROOT="$(git rev-parse --show-toplevel)"
else
  echo "error: not inside a git repository" >&2
  exit 1
fi
cd "$ROOT"

REPORT="$ROOT/REPORT.md"
TS="$(date '+%Y-%m-%d %H:%M %z')"
BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo unknown)"
HEAD="$(git rev-parse --short HEAD 2>/dev/null || echo unknown)"
STATUS_SB="$(git status -sb 2>/dev/null | tr '\n' ' ' || true)"
PORCELAIN="$(git status --porcelain 2>/dev/null || true)"
DIRTY_COUNT=0
if [ -n "$PORCELAIN" ]; then
  DIRTY_COUNT="$(printf '%s\n' "$PORCELAIN" | grep -c . || true)"
fi

COMMITS_TXT="(none)"
AHEAD="n/a"
if git rev-parse --abbrev-ref '@{u}' >/dev/null 2>&1; then
  UPSTREAM="$(git rev-parse --abbrev-ref '@{u}')"
  COMMITS_TXT="$(git log --oneline "${UPSTREAM}..HEAD" 2>/dev/null || true)"
  [ -n "$COMMITS_TXT" ] || COMMITS_TXT="(none — already synced)"
  AHEAD="$(git rev-list --count "${UPSTREAM}..HEAD" 2>/dev/null || echo 0)"
  CHANGED="$(git diff --stat "${UPSTREAM}...HEAD" 2>/dev/null || echo "(could not diff)")"
else
  COMMITS_TXT="$(git log --oneline -5 2>/dev/null || true)"
  AHEAD="no upstream set"
  CHANGED="$(git diff --stat HEAD~3..HEAD 2>/dev/null || echo "(could not diff)")"
fi

LINT_STATUS="NOT RUN"
TYPE_STATUS="NOT RUN"
TEST_STATUS="NOT RUN"
BUILD_STATUS="NOT RUN"
AUDIT_STATUS="NOT RUN"
SECRETS_STATUS="NOT RUN"
WARNINGS=()

if [ -f package.json ] && command -v npm >/dev/null 2>&1; then
  if grep -q '"lint"' package.json 2>/dev/null; then
    if npm run lint --if-present >/tmp/push-report-lint.txt 2>&1; then LINT_STATUS="PASS"; else LINT_STATUS="FAIL"; WARNINGS+=("npm lint failed"); fi
  else LINT_STATUS="N/A"; fi
  if grep -q '"typecheck"' package.json 2>/dev/null; then
    if npm run typecheck >/tmp/push-report-type.txt 2>&1; then TYPE_STATUS="PASS"; else TYPE_STATUS="FAIL"; WARNINGS+=("typecheck failed"); fi
  else TYPE_STATUS="N/A"; fi
  if grep -q '"test"' package.json 2>/dev/null; then
    if npm test --if-present >/tmp/push-report-test.txt 2>&1; then TEST_STATUS="PASS"; else TEST_STATUS="WARN"; WARNINGS+=("tests did not clearly pass"); fi
  else TEST_STATUS="N/A"; fi
  if grep -q '"build"' package.json 2>/dev/null; then
    if npm run build >/tmp/push-report-build.txt 2>&1; then BUILD_STATUS="PASS"; else BUILD_STATUS="FAIL"; WARNINGS+=("build failed"); fi
  else BUILD_STATUS="N/A"; fi
  if npm audit --omit=dev --audit-level=critical >/tmp/push-report-audit.txt 2>&1; then AUDIT_STATUS="PASS"
  else AUDIT_STATUS="WARN"; WARNINGS+=("npm audit reported issues"); fi
else
  LINT_STATUS="N/A"; TYPE_STATUS="N/A"; TEST_STATUS="N/A"; BUILD_STATUS="N/A"; AUDIT_STATUS="N/A"
fi

if command -v gitleaks >/dev/null 2>&1; then
  if gitleaks detect --source . >/tmp/push-report-gitleaks.txt 2>&1; then SECRETS_STATUS="PASS"
  else SECRETS_STATUS="FAIL"; WARNINGS+=("gitleaks findings — BLOCK push until reviewed"); fi
elif command -v ggshield >/dev/null 2>&1; then
  if ggshield secret scan repo . >/tmp/push-report-ggshield.txt 2>&1; then SECRETS_STATUS="PASS"
  else SECRETS_STATUS="FAIL"; WARNINGS+=("ggshield findings"); fi
else
  SECRETS_STATUS="NOT RUN"
  WARNINGS+=("No gitleaks/ggshield on PATH — run pack security scan manually")
fi

EXPOSURE_STATUS="PASS"
if git ls-files | grep -E '(^\.env$|\.env\.local$|\.env\.production$)' >/dev/null 2>&1; then
  EXPOSURE_STATUS="FAIL"
  WARNINGS+=("Tracked .env file(s) — remove from git")
elif git ls-files | grep -E '\.pem$|id_rsa|credentials\.json$' >/dev/null 2>&1; then
  EXPOSURE_STATUS="WARN"
  WARNINGS+=("Possible credential filenames tracked")
fi

VERDICT="PUSH OK"
if [ "$SECRETS_STATUS" = "FAIL" ] || [ "$EXPOSURE_STATUS" = "FAIL" ]; then
  VERDICT="BLOCKED — security failure"
elif [ "$BUILD_STATUS" = "FAIL" ]; then
  VERDICT="WARN — build failed; push only if intentional"
fi

WARN_MD="- (none)"
if [ "${#WARNINGS[@]}" -gt 0 ]; then
  WARN_MD="$(printf -- '- %s\n' "${WARNINGS[@]}")"
fi

SECTION_FILE="$(mktemp)"
cat > "$SECTION_FILE" <<EOF
## Push — ${TS}

| Field | Value |
|-------|-------|
| Branch | \`${BRANCH}\` |
| HEAD | \`${HEAD}\` |
| Ahead of upstream | ${AHEAD} |
| Dirty files | ${DIRTY_COUNT} |
| Status | ${STATUS_SB} |

### Git commits (to push)

\`\`\`
${COMMITS_TXT}
\`\`\`

### Diffstat

\`\`\`
${CHANGED}
\`\`\`

### Security

| Check | Status | Evidence |
|-------|--------|----------|
| Secrets scan | ${SECRETS_STATUS} | gitleaks/ggshield or NOT RUN |
| Dependency audit | ${AUDIT_STATUS} | npm audit / equivalent |
| Client / env exposure | ${EXPOSURE_STATUS} | tracked env or key files |

### Quality

| Check | Status | Evidence |
|-------|--------|----------|
| Lint | ${LINT_STATUS} | package.json scripts |
| Typecheck | ${TYPE_STATUS} | package.json scripts |
| Tests | ${TEST_STATUS} | package.json scripts |
| Build | ${BUILD_STATUS} | package.json scripts |

### Warnings

${WARN_MD}

### Design / UI

| Check | Status | Notes |
|-------|--------|-------|
| Slop catalog | NOT RUN | Run via design skills when UI changed |
| a11y smoke | NOT RUN | Pair accessibility-checklist when UI changed |

### Verdict

**${VERDICT}**

---
EOF

if [ ! -f "$REPORT" ]; then
  cat > "$REPORT" <<'EOF'
# REPORT.md — Push & Security Log

> Newest sections first. Generated by skill `push-report` / `generate-push-report.sh`.
> Legend: `PASS` · `FAIL` · `WARN` · `N/A` · `NOT RUN`

## Legend

| Status | Meaning |
|--------|---------|
| PASS | Check ran and succeeded |
| FAIL | Check ran and failed — block push if security-critical |
| WARN | Non-blocking issue recorded |
| N/A | Not applicable to this project |
| NOT RUN | Tool/script not executed this cycle |

---
EOF
fi

# Insert newest section after the first --- marker
python3 - "$REPORT" "$SECTION_FILE" <<'PY'
import sys
from pathlib import Path
report, section = Path(sys.argv[1]), Path(sys.argv[2])
text = report.read_text()
sec = section.read_text().rstrip() + "\n\n"
marker = "\n---\n"
if marker in text:
    pre, post = text.split(marker, 1)
    report.write_text(pre + marker + "\n" + sec + post.lstrip("\n"))
else:
    report.write_text(text.rstrip() + "\n\n" + sec)
PY
rm -f "$SECTION_FILE"

echo "Updated $REPORT"
echo "Verdict: $VERDICT"
case "$VERDICT" in
  BLOCKED*) exit 2 ;;
esac
exit 0
