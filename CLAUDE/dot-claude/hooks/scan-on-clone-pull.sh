#!/bin/bash
# scan-on-clone-pull.sh
# Claude Code PostToolUse(Bash) hook: right after a `git clone` or `git pull`,
# scan the affected repo and feed a short security report back into Claude's context.
#
# Install: <repo>/.claude/hooks/scan-on-clone-pull.sh  (chmod +x)
# Wire up: .claude/settings.json (see INSTALL.md)
# Needs:   jq  (brew install jq)  and the repo scanner (resolved from candidate paths below).
#
# It never blocks git. On any problem it exits 0 silently so your workflow is unaffected.

# Resolve the scanner from the first path that exists.
SCANNER=""
for c in \
    "$REPO_SCANNER" \
    "$CLAUDE_PROJECT_DIR/.claude/tools/repo-malware-scan.sh" \
    "$HOME/.claude/tools/repo-malware-scan.sh" \
    "$HOME/.security-tools/repo-malware-scan.sh"
do
    [[ -n "$c" && -x "$c" ]] && { SCANNER="$c"; break; }
done

input=$(cat)
command -v jq >/dev/null 2>&1 || exit 0
[[ -n "$SCANNER" ]] || exit 0

cmd=$(jq -r '.tool_input.command // empty' <<<"$input" 2>/dev/null)
cwd=$(jq -r '.cwd // empty'               <<<"$input" 2>/dev/null)
[[ -z "$cmd" ]] && exit 0
[[ -z "$cwd" ]] && cwd="$PWD"

echo "$cmd" | grep -qE '\bgit\b.*\b(clone|pull)\b' || exit 0

target="$cwd"
if echo "$cmd" | grep -qE '\bclone\b'; then
    after=$(echo "$cmd" | sed -E 's/.*\bclone\b//')
    url=""; dir=""
    # shellcheck disable=SC2086
    set -- $after
    while [[ $# -gt 0 ]]; do
        case "$1" in
            -b|--branch|-o|--origin|--depth|-j|--jobs|-c|--config|-u|--upload-pack|--reference|--separate-git-dir|--template)
                shift 2 2>/dev/null || shift; continue ;;
            -*) shift; continue ;;
            *)  if   [[ -z "$url" ]]; then url="$1"
                elif [[ -z "$dir" ]]; then dir="$1"; fi
                shift ;;
        esac
    done
    if   [[ -n "$dir" ]]; then target="$cwd/$dir"
    elif [[ -n "$url" ]]; then base=$(basename "$url"); target="$cwd/${base%.git}"; fi
    [[ -d "$target" ]] || target=$(find "$cwd" -maxdepth 1 -mindepth 1 -type d 2>/dev/null \
        | xargs -I{} stat -f '%m %N' {} 2>/dev/null | sort -rn | head -1 | cut -d' ' -f2-)
    [[ -z "$target" || ! -d "$target" ]] && target="$cwd"
fi

report=$("$SCANNER" --report-only "$target" 2>/dev/null | perl -pe 's/\e\[[0-9;]*m//g')

if echo "$report" | grep -q 'no malware'; then
    msg="Automated repository security scan ran after a git clone/pull on ${target}. Result: clean — no malware indicators were found."
else
    summary=$(echo "$report" | sed -n '/REPORT/,/auto-edited/p' | head -c 6000)
    msg="Automated repository security scan ran after a git clone/pull on ${target} and found indicators that need review. The repo should not be opened in an editor, and its install scripts should not be run, until a human has reviewed these findings. Scan report:

${summary}"
fi

jq -n --arg m "$msg" '{hookSpecificOutput:{hookEventName:"PostToolUse", additionalContext:$m}}'
exit 0
