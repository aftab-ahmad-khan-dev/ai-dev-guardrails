---
name: dependency-review
description: Use before installing or upgrading any npm/package dependency, or when reviewing a package's safety. Covers inspect-first, --ignore-scripts install, and stop-on-suspicious.
---
# Dependency work

1. Inspect first: metadata, lifecycle scripts, source.
2. Install with `--ignore-scripts`.
3. Scan, then enable scripts only if clearly justified.
4. Stop on anything suspicious (preinstall network/exec, credential access, obfuscation). Prefer established alternatives.
