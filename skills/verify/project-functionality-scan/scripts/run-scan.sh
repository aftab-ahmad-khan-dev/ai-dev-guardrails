#!/usr/bin/env bash
# Safe wrapper: run functionality scan; never deletes project source.
set -euo pipefail
ROOT="."
while [ $# -gt 0 ]; do
  case "$1" in
    --root) ROOT="$2"; shift 2 ;;
    *) echo "usage: run-scan.sh [--root DIR]"; exit 1 ;;
  esac
done
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
python3 "$SCRIPT_DIR/scan_project.py" --root "$ROOT"
echo ""
echo "Open SCAN-REPORT.md and SCAN-REPORT.svg in the project root."
