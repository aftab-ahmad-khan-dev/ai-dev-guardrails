---
name: block-library
description: >-
  Block Library Schema design approach. Use when the user wants block library, page blocks, section components contract, or when
  using-design-skills routes to this approach.
---

# Block Library Schema


## ⚡ Command

```text
/block-library
# or ask the agent:
use skill block-library
```

## Family
`workflow` · part of the ai-dev-guardrails design approach pack.

## Overview
Apply this approach on top of `anti-slop-frontend` + `safe-file-ops`. Do not invent a second design system when the repo already has tokens.

## When to use
Growing a landing/page block library.

## Direction rules
- Name blocks; props contract
- Composition rules
- Keep library coherent across additions
- No one-off snowflake sections

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
