---
description: Full project functionality scan — broken CTAs, workflows, APIs, crash risks. Writes SCAN-REPORT.md + SCAN-REPORT.svg.
---

Invoke the project-functionality-scan skill (and safe-file-ops — read only).

1. Run: `bash skills/verify/project-functionality-scan/scripts/run-scan.sh --root .`
2. Open `SCAN-REPORT.md` and review every critical/high finding (confirm or false-positive).
3. Open `SCAN-REPORT.svg` and summarize severity + top issues for the user.
4. List the top fixes in priority order. Do not delete project files.
