#!/usr/bin/env bash
# Ensure installed agent-skill directories are gitignored in a consuming repo.
# Safe: only appends to .gitignore; never deletes project files.
set -euo pipefail

ROOT="${1:-.}"
if git -C "$ROOT" rev-parse --show-toplevel >/dev/null 2>&1; then
  ROOT="$(git -C "$ROOT" rev-parse --show-toplevel)"
fi
GI="$ROOT/.gitignore"
MARKER_BEGIN="# ai-dev-guardrails-skills-ignore-start"
MARKER_END="# ai-dev-guardrails-skills-ignore-end"

BLOCK=$(cat <<'EOF'
# ai-dev-guardrails-skills-ignore-start
# Installed Agent Skills — local/runtime only; do not commit vendor copies.
# Reinstall with: npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails
.cursor/skills/
.claude/skills/
.agents/skills/
.codex/skills/
.gemini/skills/
.github/skills/
.opencode/skills/
.windsurf/skills/
.trae/skills/
.trae-cn/skills/
.rovodev/skills/
.qoder/skills/
.vibe/skills/
.grok/skills/
.pi/skills/
.agent/skills/
skills-lock.json
**/skills-lock.json
# ai-dev-guardrails-skills-ignore-end
EOF
)

mkdir -p "$ROOT"
touch "$GI"

if grep -qF "$MARKER_BEGIN" "$GI" 2>/dev/null; then
  # Refresh block in place
  tmp="$(mktemp)"
  awk -v begin="$MARKER_BEGIN" -v end="$MARKER_END" -v block="$BLOCK" '
    $0 == begin { print block; skip=1; next }
    $0 == end { skip=0; next }
    !skip { print }
  ' "$GI" > "$tmp"
  # If markers were malformed, just append
  if ! grep -qF "$MARKER_BEGIN" "$tmp"; then
    printf '\n%s\n' "$BLOCK" >> "$GI"
    rm -f "$tmp"
  else
    mv "$tmp" "$GI"
  fi
  echo "Refreshed skills ignore block in $GI"
else
  printf '\n%s\n' "$BLOCK" >> "$GI"
  echo "Added skills ignore block to $GI"
fi

# Untrack if already staged/committed (index only — keeps local files)
cd "$ROOT"
paths=(
  .cursor/skills
  .claude/skills
  .agents/skills
  .codex/skills
  .gemini/skills
  .github/skills
  skills-lock.json
)
for p in "${paths[@]}"; do
  if git ls-files --error-unmatch "$p" >/dev/null 2>&1 || git ls-files "$p" | grep -q .; then
    git rm -r --cached --ignore-unmatch "$p" >/dev/null 2>&1 || true
  fi
done

echo "Done. Installed skills stay local; .gitignore updated."
