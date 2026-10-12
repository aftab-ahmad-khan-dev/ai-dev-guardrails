---
name: security-scan
description: Scan a project repo for malware on demand (VS Code auto-run tasks, fake-asset payloads, obfuscated code, curl|bash, malicious npm lifecycle scripts, custom git hooks, known C2). Use when asked to security-scan/audit a repo, before trusting a newly cloned or handed-over project, or before enabling a dependency's install scripts. Clone/pull is already scanned automatically by the scan-on-clone-pull hook.
---
# Security scan (on demand)

Run the scanner, read the report, act only with the user's go-ahead.

```bash
~/.security-tools/repo-malware-scan.sh <repo-path>              # report, then prompt y/n to quarantine
~/.security-tools/repo-malware-scan.sh --report-only <repo>    # report only, no changes
~/.security-tools/repo-malware-scan.sh --yes <repo>           # remove without asking (only if user said so)
```

Rules:
- Removal = quarantine (reversible move to ~/.security-tools/quarantine/), never hard delete.
- Embedded issues (package.json scripts, C2 strings in source) are reported, never auto-edited.
- On any finding: stop, surface it, do not open the repo in an editor or run its install scripts until reviewed.
- Baseline always holds: never weaken security for a feature; no curl|bash or tarball installs without review.
