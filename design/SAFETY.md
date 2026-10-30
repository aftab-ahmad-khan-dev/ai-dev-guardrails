# Design & install SAFETY — never wipe a repo

## Incident class

After installing this pack, agents sometimes **delete large parts of a consuming repo**. Root causes in practice:

1. **Over-broad “delete” language** in design skills (e.g. “delete losing variants”, “delete the animation”) interpreted as file/repo cleanup.
2. **Unsafe install commands** — `rsync --delete` or syncing into the project root instead of `.cursor/skills/`.
3. **Hook cache edge cases** — `simplify-ignore` rewrites files in-place; a crash mid-session can leave placeholders (not a full wipe, but looks like corruption).
4. **Destructive git advice** — `git reset --hard` / `git clean -fdx` applied too eagerly by an agent.

This pack **forbids** those behaviors. Follow [`safe-file-ops`](safe-file-ops/SKILL.md) always.

## Hard bans (agents)

| Never | Do instead |
|-------|------------|
| `rm -rf` on a project / `src` / `.git` | Delete only paths you created in this turn, after naming them |
| `git clean -fdx` / `git reset --hard` without explicit user ask | Ask; prefer stash or revert single files |
| `rsync --delete` into a project root | Sync **only** into `.cursor/skills/` or `.agents/skills/` **without** `--delete` unless user insists |
| “Clean up the repo” / remove “unused” folders by guess | List candidates; wait for approval |
| Delete prototype “losers” outside `*.prototype.*` / `prototypes/` | Only remove dirs created for this variant session |
| Empty the working tree to “start fresh” | New branch or new folder — never wipe local clone |

## Safe install (copy these exactly)

```bash
# Universal installer (preferred)
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails

# Cursor local sync — DESTINATION must be .cursor/skills/ ONLY
mkdir -p .cursor/skills
rsync -a /path/to/ai-dev-guardrails/skills/ .cursor/skills/
# NEVER: rsync … ./ 
# NEVER: rsync --delete …
```

## If a wipe already happened

1. Do **not** write new files over recovery options.
2. Try: `git status` → `git reflog` → `git fsck --lost-found`.
3. Restore from remote: `git fetch origin && git reset --hard origin/<branch>` only if remote is known-good **and** user approves losing local commits.
4. Time Machine / cloud backup / IDE Local History if git cannot recover.
