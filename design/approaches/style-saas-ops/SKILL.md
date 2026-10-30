---
name: style-saas-ops
description: >-
  SaaS Ops Density design approach. Use when the user wants saas dashboard, ops density, B2B admin UI, or when
  using-design-skills routes to this approach.
---

# SaaS Ops Density


## ⚡ Command

```text
/style-saas-ops
# or ask the agent:
use skill style-saas-ops
```

## Family
`style` · part of the ai-dev-guardrails design approach pack.

## Overview
Apply this approach on top of `anti-slop-frontend` + `safe-file-ops`. Do not invent a second design system when the repo already has tokens.

## When to use
B2B admin, billing, internal tools.

## Direction rules
- Operate mode: speed + scanability
- Tables over card grids for data
- Filters in URL state
- Chrome quiet; status sparse

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
