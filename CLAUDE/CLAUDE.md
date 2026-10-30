# CLAUDE.md — operating brain (always loaded, kept tiny on purpose)

Keep this file small — it is read every turn. Detailed know-how lives in the **skills library**
under `.claude/skills/` and loads only when a task matches a skill's description. Do not paste
skill detail back into this file.

## Always on (never skip)
1. Understand before acting. No implementing on a guess; ask 1–3 short questions if unclear.
2. Minimize tokens: concise output, no process narration, no unsolicited extras.
3. Surgical scope: exactly what was asked. No invented features, no drive-by refactors.
4. Security is top priority and is never weakened for a feature.
5. No destructive commands, no `curl|bash`, no tarball installs without explicit approval.
6. Never commit, push, or self-attribute unless asked.
7. Files ≤ ~400 lines. Dates in PKT. Resolve author via `gh` → remote → `git config` (never invent).

## Scan on clone/pull (reflex)
Right after any `git clone` / `git pull`, run the repo scanner and report `Clean` or `Issues Found — <list>`:
`.claude/tools/repo-malware-scan.sh --report-only <repo>`
If issues: STOP — don't open the repo in an editor or run its install scripts — surface them and wait.
(The `scan-on-clone-pull` hook does this automatically when installed; this is the fallback instruction.)

## Skills library (load the matching skill, don't restate it)
A library of skills is installed under `.claude/skills/`. When a task matches a skill's description,
load that skill and follow it. House skills for this team:
`tracker` · `dependency-review` · `design-work` · `tool-install` · `srs` · `tauri2` ·
`model-routing` · `security-scan`.
Engineering-lifecycle skills (define → plan → build → verify → review → ship) are also installed —
use them when the task fits. For simple questions, chat, or one-liners, skip skills and answer directly.

## Agents
Specialist agents live in `.claude/agents/` (`security-auditor`, `code-reviewer`, `test-engineer`,
`web-performance-auditor`). Dispatch one when its specialty matches the task.

## Delegation (always on)
Dispatch a sub-agent for real work — one per discrete task, always passing `model` (cheapest capable).
Pure conversation / one-liners → answer directly. Routing table: `model-routing` skill.

==================================================
Below this line is project work, not instructions. Begin here.
