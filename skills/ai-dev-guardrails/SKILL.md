---
name: ai-dev-guardrails
description: >-
  Installs and runs the Ai-dev-guardrails pack — SRS task board, Rules.md
  standards (CS/SS/SEC/OPS), and lifecycle skills. Use when starting a project
  with this pack, when the user mentions guardrails, SRS.md, Rules.md, or wants
  AI coding rules plus skills for Cursor, Claude, Copilot, or any agent.
---

# Ai-dev-guardrails

## Overview

This skill is the entrypoint for the **ai-dev-guardrails** pack: reusable **rules** and **skills** for any AI coding assistant.

| Layer | Location | Role |
|-------|----------|------|
| **SRS** | `SRS.md` | Project description + living task board |
| **Rules** | `Rules.md` + YAML packs | Quality / security / DevOps standards |
| **Lifecycle skills** | `skills/*` | Spec → plan → build → test → review → ship |

## When to use

- User asks to follow project guardrails, SRS, or Rules.md
- Starting work in a repo that includes this pack
- Installing or explaining how to use ai-dev-guardrails with any AI tool

## Process

### 1. Read the board

1. Open and read `SRS.md`.
2. State the task ID you will execute; set it to `in_progress`.
3. If `SRS.md` is missing, scaffold from this pack’s template and confirm with the human before large work.

### 2. Pick lifecycle skills

1. If unsure which skill applies, follow `using-agent-skills`.
2. Match the phase: define → plan → build → verify → review → ship.
3. Follow that skill’s process and verification — do not invent a weaker path.

### 3. Apply rules by project type

1. Detect frontend / backend / full-stack / library / deploy target.
2. Apply only applicable sections of `Rules.md` (CS-*, SS-*, SEC-*, OPS-*).
3. Mark unused sections `N/A` in the compliance report — never invent backend/deploy work for a frontend-only task.

### 4. Complete and report

1. Mark the task `done` in `SRS.md` (Completed date + Notes); bump Last updated.
2. Extend the board by version and/or date when scope grows.
3. Emit the compliance report template from the pack README.

## Install (any AI)

```bash
# Universal installer (Cursor, Claude Code, Codex, Gemini, …)
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails

# Browse before install
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails --list

# One skill only
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails --skill ai-dev-guardrails
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails --skill test-driven-development
```

**Manual / any agent:** copy `skills/<name>/SKILL.md` into the agent’s system prompt, rules file, or skills directory. Keep `SRS.md` + `Rules.md` at the project root.

**Cursor sync from a local clone:**

```bash
mkdir -p .cursor/skills && rsync -a skills/ .cursor/skills/
```

## Verification

- [ ] `SRS.md` was read and the active task ID announced
- [ ] Matching lifecycle skill(s) were followed when applicable
- [ ] Only fitting rule packs were applied; others marked `N/A`
- [ ] Finished tasks updated in `SRS.md`
- [ ] Compliance report emitted for reviewable slices

## Red flags

- Coding from chat alone while ignoring an existing `SRS.md`
- Loading every rule pack on a library or frontend-only task
- Skipping tests / review skills “to go faster”
- Marking compliance `PASS` without checking
