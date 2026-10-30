---
name: style-editorial
description: >-
  Editorial / Magazine design approach. Use when the user wants editorial layout, magazine UI, typographic landing page, or when
  using-design-skills routes to this approach.
---

# Editorial / Magazine


## ⚡ Command

```text
/style-editorial
# or ask the agent:
use skill style-editorial
```

## Family
`style` · part of the ai-dev-guardrails design approach pack.

## Overview
Apply this approach on top of `anti-slop-frontend` + `safe-file-ops`. Do not invent a second design system when the repo already has tokens.

## When to use
Content-led brands, publishers, storytelling landings.

## Direction rules
- Type-led composition; long measure discipline
- Photography or illustration as story
- Sparse chrome; pull quotes / rules sparingly
- Avoid SaaS feature-card grids

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
