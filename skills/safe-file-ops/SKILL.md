---
name: safe-file-ops
description: >-
  Hard safety rules that prevent agents from deleting or wiping local repositories
  when using design or lifecycle skills. Use always with this pack; especially when
  prototyping, simplifying, installing skills, cleaning variants, or running hooks.
---

# Safe File Ops


## ⚡ Command

```text
/safe-file-ops
# or ask the agent:
use skill safe-file-ops
```

## Overview

**Never destroy a consuming repo.** Design skills talk about deleting *animations*, *variants*, or *sections* — that means code *inside* scoped files, not wiping directories or the git worktree.

Load this skill whenever doing UI work with this pack. Treat violations as **Block**.

## Hard bans

1. **No recursive project deletes** — never `rm -rf`, never delete `.git`, `src/`, `app/`, `packages/`, or the repo root.
2. **No destructive git** — never `git clean -fdx`, `git reset --hard`, `git checkout -- .`, or force-push unless the user typed that request explicitly in the current message.
3. **No dangerous sync** — never `rsync --delete` into a project root. Skill install targets are only `.cursor/skills/`, `.agents/skills/`, `.claude/skills/`, or the user’s home skill dir.
4. **No guessed cleanup** — never remove “unused” folders/files you did not create in this session without listing paths and getting approval.
5. **Prototype losers only in sandbox paths** — only delete paths matching `**/prototypes/**`, `**/*.prototype.*`, or a directory *you created this session* named for variants. Never delete production routes/components as “losers”.
6. **Motion “delete” means remove the animation** — strip `transition` / motion props from the component; do not delete the component file or parent folder.
7. **Section “cut” means unmount or don’t render** — edit the page; do not `rm` the route file unless the user asked to remove that feature.

## Allowed deletes (narrow)

- Files **you created in this conversation** for throwaway prototypes, after naming them in chat
- Single-file reverts the user requested
- Cache dirs the pack owns: `.claude/.simplify-ignore-cache`, `.claude/sdd-cache` (contents only)

## Install rules

```bash
# OK
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails
mkdir -p .cursor/skills && rsync -a "$PACK/skills/" .cursor/skills/
bash "$PACK/scripts/ensure-skills-gitignore.sh" .   # mandatory — ignore installed copies

# FORBIDDEN
rsync -a --delete ... ./
rsync -a "$PACK/" ./
rm -rf ./* 
git add .cursor/skills .agents/skills   # never commit vendor skill installs
```

See [`../SAFETY.md`](../../design/SAFETY.md).

## Verification

Before any delete operation:

- [ ] Path list shown to the user (or created by you this session)
- [ ] Not `.git`, not package roots, not entire `src/`
- [ ] Not `rsync --delete` to project root
- [ ] User explicitly asked **or** path is a sandbox prototype you created
