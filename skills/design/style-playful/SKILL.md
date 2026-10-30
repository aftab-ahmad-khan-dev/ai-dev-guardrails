---
name: style-playful
description: >-
  Playful Product design approach. Use when the user wants playful UI, friendly product, consumer fun interface, or when
  using-design-skills routes to this approach.
---

# Playful Product


## ⚡ Command

```text
/style-playful
# or ask the agent:
use skill style-playful
```

## Family
`style` · part of the ai-dev-guardrails design approach pack.

## Overview
Apply this approach on top of `anti-slop-frontend` + `safe-file-ops`. Do not invent a second design system when the repo already has tokens.

## When to use
Consumer apps for younger or lighthearted brands.

## Direction rules
- Rounded where brand allows; vivid but curated accents
- Illustration OK; emoji not primary icons
- Delight rare (see motion-craft frequency)
- Still pass slop catalog

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
