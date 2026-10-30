---
name: style-soft
description: >-
  Soft / Quiet Luxury design approach. Use when the user wants soft UI, quiet luxury, calm expensive interfaces, airy whitespace, or when
  using-design-skills routes to this approach.
---

# Soft / Quiet Luxury


## ⚡ Command

```text
/style-soft
# or ask the agent:
use skill style-soft
```

## Family
`style` · part of the ai-dev-guardrails design approach pack.

## Overview
Apply this approach on top of `anti-slop-frontend` + `safe-file-ops`. Do not invent a second design system when the repo already has tokens.

## When to use
Marketing and premium product UI that should feel calm and expensive.

## Direction rules
- Low contrast-but-accessible surfaces
- Generous whitespace; soft radii (8–16)
- Restrained accent; no neon
- Smooth short motion (150–220ms ease-out)

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
