---
name: motion-stagger
description: >-
  Stagger & Orchestration design approach. Use when the user wants stagger animation, orchestrate entrances, sequenced UI motion, or when
  using-design-skills routes to this approach.
---

# Stagger & Orchestration


## ⚡ Command

```text
/motion-stagger
# or ask the agent:
use skill motion-stagger
```

## Family
`motion` · part of the ai-dev-guardrails design approach pack.

## Overview
Apply this approach on top of `anti-slop-frontend` + `safe-file-ops`. Do not invent a second design system when the repo already has tokens.

## When to use
Group entrances and sequenced reveals.

## Direction rules
- 30–80ms stagger
- Parent orchestrates; children don’t fight
- Cancel on navigate
- Never everything-at-once fireworks

## Process
1. Load `PRODUCT.md` / `DESIGN.md` if present; else run `design-context` briefly.
2. State this approach name and one direction sentence.
3. Implement the slice; prefer inherit-over-invent.
4. Run `../../design/references/slop-catalog.md` (or `../../references/design-slop-catalog.md`).
5. Close with `ship-complete-ui` checks for the touched surface.

## Safety
Follow `safe-file-ops`. “Remove” means edit styles/structure in scoped files — never wipe the repo or delete unrelated directories.

## Verification
- [ ] Approach named in session
- [ ] Slop catalog clean on touched UI
- [ ] No destructive file ops
