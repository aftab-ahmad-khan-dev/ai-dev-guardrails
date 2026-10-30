---
name: steer-polish
description: >-
  Steer: Polish design approach. Use when the user wants polish UI, final design pass, ship-ready visuals, or when
  using-design-skills routes to this approach.
---

# Steer: Polish


## ⚡ Command

```text
/steer-polish
# or ask the agent:
use skill steer-polish
```

## Family
`steer` · part of the ai-dev-guardrails design approach pack.

## Overview
Apply this approach on top of `anti-slop-frontend` + `safe-file-ops`. Do not invent a second design system when the repo already has tokens.

## When to use
Final visual pass before merge/ship.

## Direction rules
- Align to DESIGN.md / tokens
- Run slop catalog
- Fix orphans: spacing, type, radius
- No new system inventing

## Process
1. Load `PRODUCT.md` / `DESIGN.md` if present; else run `design-context` briefly.
2. State this approach name and one direction sentence.
3. Implement the slice; prefer inherit-over-invent.
4. Run `../../../design/references/slop-catalog.md` (or `../../../references/design-slop-catalog.md`).
5. Close with `ship-complete-ui` checks for the touched surface.

## Safety
Follow `safe-file-ops`. “Remove” means edit styles/structure in scoped files — never wipe the repo or delete unrelated directories.

## Verification
- [ ] Approach named in session
- [ ] Slop catalog clean on touched UI
- [ ] No destructive file ops
