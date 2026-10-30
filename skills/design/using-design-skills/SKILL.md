---
name: using-design-skills
description: >-
  Routes UI and visual work to the right design pack skill across 60+ approaches
  (anti-slop, steer, styles, motion, workflows). Use when starting frontend design
  work, when the user mentions AI slop, polish, distill, motion craft, or when
  unsure which design/* skill to load.
---

# Using Design Skills


## ⚡ Command

```text
/using-design-skills
# or ask the agent:
use skill using-design-skills
```

## Overview

This pack’s `design/` skills cover **taste, steering, styles, motion, and workflows** (~70 approaches). They complement lifecycle `frontend-ui-engineering`. **Always** load `safe-file-ops` for any design session.

Full index: [`approaches/README.md`](../../../design/approaches/README.md) · Safety: [`SAFETY.md`](../../../design/SAFETY.md)

## When to use

- Starting any visual / UI task and unsure which design skill applies
- User mentions slop, polish, distill, redesign, animation craft, variants, or a named style
- After `design-context` is missing on a greenfield UI project

## Router (core)

| Signal | Load |
|--------|------|
| Any design session | `safe-file-ops` (always) |
| No PRODUCT.md / DESIGN.md | `design-context` |
| New page / “looks AI” | `anti-slop-frontend` |
| Named steer: polish, audit, distill, … | `design-steer` or `steer-*` approach |
| Style direction (soft, brutalist, …) | `style-*` approach |
| Existing product overhaul | `redesign-audit` |
| Motion add / review / find | `motion-craft` / `review-motion` / `find-motion` |
| Image → code / brand kit / stitch | `image-to-code` / `brand-kit` / `stitch-export` |
| Variants | `visual-prototype` or `worlds-commit` |
| Placeholders | `ship-complete-ui` |
| Before git push | `push-report` → `REPORT.md` |
| Engineering a11y / state | `frontend-ui-engineering` |

## Process

1. Read `SRS.md` if present; note the active task.
2. Affirm `safe-file-ops` — no repo wipes, no `rsync --delete` to project root.
3. Check for `PRODUCT.md` / `DESIGN.md` — run `design-context` if missing.
4. Pick **one primary** approach; add closing gates (`ship-complete-ui`, `review-motion`, `push-report`) as needed.
5. Run the [slop catalog](../../../design/references/slop-catalog.md) before claiming UI is done.

## Anti-patterns

- Loading every approach at once
- Skipping brief inference → purple gradients
- Deleting production folders as “cleanup” or “losing variants”
- Animating before the frequency gate

## Verification

- [ ] `safe-file-ops` acknowledged
- [ ] Primary skill/approach named and followed
- [ ] Slop catalog run on visual output
- [ ] No destructive file ops
