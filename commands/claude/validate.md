---
description: Self-lint this pack's YAML rule packs and SKILL.md files. Writes VALIDATION-REPORT.md.
---

Invoke the self-validate skill.

1. Run: `node scripts/validate.js`
2. Open `VALIDATION-REPORT.md` and report the verdict.
3. If any FAIL rows exist, fix them at the source (YAML pack or `SKILL.md`) and re-run until clean.
