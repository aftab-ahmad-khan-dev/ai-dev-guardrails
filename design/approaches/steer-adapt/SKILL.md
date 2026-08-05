---
name: steer-adapt
description: >-
  Steer: Adapt design approach. Use when the user wants responsive adapt, mobile layout fix, density breakpoints, or when
  using-design-skills routes to this approach.
---

# Steer: Adapt


## ⚡ Command

```text
/steer-adapt
# or ask the agent:
use skill steer-adapt
```

## Family
`steer` · part of the ai-dev-guardrails design approach pack.

## Overview
Apply this approach on top of `anti-slop-frontend` + `safe-file-ops`. Do not invent a second design system when the repo already has tokens.

## When to use
Breakpoint and device adaptation.

## Direction rules
- Mobile-first stacks
- No hover-only
- Tablet density
- Test 320 / 768 / 1024 / 1440

## Process
1. Load `PRODUCT.md` / `DESIGN.md` if present; else run `design-context` briefly.
2. State this approach name and one direction sentence.
3. Implement the slice; prefer inherit-over-invent.
4. Run `design/references/slop-catalog.md` (or `references/design-slop-catalog.md`).
5. Close with `ship-complete-ui` checks for the touched surface.

## Safety
Follow `safe-file-ops`. “Remove” means edit styles/structure in scoped files — never wipe the repo or delete unrelated directories.

## Verification
- [ ] Approach named in session
- [ ] Slop catalog clean on touched UI
- [ ] No destructive file ops
