---
name: self-validate
description: >-
  Lints this pack's own content — YAML rule-pack schema (unique ids, required
  fields, valid severities) and every SKILL.md (frontmatter, name/folder match,
  category placement, Command section). Writes VALIDATION-REPORT.md and exits
  non-zero on failure. Use when the pack itself changed — a rule added to a
  YAML pack, a skill added or moved — not for scanning a consuming project's
  code (see project-functionality-scan for that).
---

# Self-Validate

## ⚡ Command

```text
/self-validate
# or ask the agent:
use skill self-validate
```

## Overview

This pack claims internal consistency — `Rules.md` in sync with the YAML packs, every skill
correctly categorized, every `SKILL.md` carrying valid frontmatter — but nothing enforced any
of that until now. `scripts/validate.js` checks it deterministically instead of leaving it to
manual review, and writes `VALIDATION-REPORT.md`.

Scope: **this repo's own content only.** It does not scan a consuming project's code — that's
`project-functionality-scan`.

## When to use

- After adding or editing a rule in `client/`, `server/`, `security/`, or `devops/` YAML packs
- After adding, moving, or renaming a skill under `skills/`
- Before a push that touches any of the above
- As part of the local pre-push gate (Rules §6)

## What it checks

| Area | Checks |
|------|--------|
| YAML rule packs | Valid YAML; top-level `rules` list; each rule has `id`, `title`, `status`, `severity`, `summary`, `rules`, `do`, `dont`, `ai_directive`; `severity` is one of `critical/high/medium/low`; `id` unique within and across packs |
| Skills | `skills/<category>/<name>/SKILL.md` depth; `<category>` is one of `meta/define/plan/build/design/verify/review/ship`; frontmatter present with `name` (matching the folder) and `description`; `## ⚡ Command` section present |

## Process

### 1. Run the validator

```bash
node scripts/validate.js
# or: npm run validate
```

### 2. Read `VALIDATION-REPORT.md`

Per-pack and per-skill PASS/FAIL table plus a one-line verdict.

### 3. Fix and re-run

Fix every `FAIL` line, then re-run until clean. Do not hand-edit `VALIDATION-REPORT.md` — it is
regenerated on every run.

## Safety

- Read-only against everything except `VALIDATION-REPORT.md` itself (Rules §6 — no other files touched)
- Follow `safe-file-ops` regardless

## Verification

- [ ] `node scripts/validate.js` exits `0`
- [ ] `VALIDATION-REPORT.md` verdict is ✅
- [ ] Any `FAIL` rows fixed at the source (YAML pack or `SKILL.md`), not by editing the report
