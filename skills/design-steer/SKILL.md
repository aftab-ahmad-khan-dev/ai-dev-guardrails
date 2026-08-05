---
name: design-steer
description: >-
  Applies a shared design command vocabulary (polish, distill, audit, typeset,
  layout, animate, harden, and more) to steer UI without rewriting the design
  system. Use when the user names a design command, asks to polish or distill a
  surface, or wants iterative visual refinement on existing UI.
---

# Design Steer


## ⚡ Command

```text
/design-steer
# or ask the agent:
use skill design-steer
```

## Overview

One intervention per command. Inherit PRODUCT.md / DESIGN.md and existing tokens — do not replace the system unless the command is explicitly a redesign (`redesign-audit`).

Full command list: [`../../design/references/command-vocabulary.md`](../../design/references/command-vocabulary.md).

## When to use

- User says polish / distill / audit / critique / typeset / layout / colorize / animate / harden / quieter / bolder / clarify / adapt / onboard  
- Iterative refinement on an existing screen  
- Final quality pass before ship

**Not for:** greenfield art direction (`anti-slop-frontend`); animation-only strict review (`review-motion`).

## Process

### 1. Parse the command

```
design-steer <command> [target]
```

If the user gives freeform (“make the pricing page quieter”), map to the closest command (`quieter`) and state the mapping.

### 2. Load context

1. PRODUCT.md / DESIGN.md if present  
2. Local tokens + components for the target  
3. Surface mode — Persuade vs Operate changes what “bold” means  

### 3. Execute the lever

| Command | Focus |
|---------|--------|
| `polish` | System alignment + slop kill + ship readiness |
| `distill` | Remove competing jobs; one idea per section |
| `audit` | a11y, contrast, responsive, touch targets, heading order |
| `critique` | Hierarchy, clarity, emotional fit to PRODUCT.md |
| `typeset` | Font choice, scale, measure, weight hierarchy |
| `layout` | Spacing rhythm, alignment, density |
| `colorize` | Strategic accent; tint neutrals; dual-mode parity |
| `bolder` / `quieter` | Amplitude without changing product identity |
| `harden` | Empty, error, overflow, i18n, disabled, loading |
| `onboard` | First-run paths and empty states |
| `animate` | Hand off rules to `motion-craft`; keep purposeful |
| `clarify` | Specific CTAs and UX copy |
| `adapt` | Breakpoints, touch, density |
| `craft` | shape → build → polish → slop catalog |
| `shape` | Plan only — no code until approved |

### 4. Preserve

- Do not introduce a new font/color system on `polish` unless tokens are absent  
- Do not nest cards to “fix” a distill  
- Do not add bounce / glow / purple defaults as “energy”

### 5. Close

1. Run [`../../design/references/slop-catalog.md`](../../design/references/slop-catalog.md)  
2. Summarize what changed in ≤5 bullets  
3. For `audit` / `critique`, prefer a findings table:

| Finding | Severity | Fix |
|---------|----------|-----|

## Common rationalizations

| Rationalization | Reality |
|-----------------|---------|
| “Polish means add more visual effects” | Polish means remove tells and align to the system. |
| “Distill can wait until after launch” | Clutter ships and stays. |
| “Audit is the same as polish” | Audit is evidence-based quality; polish is taste + system fit. |

## Red flags

- Rewriting the design system during `polish`  
- Adding sections during `distill`  
- Ignoring PRODUCT.md anti-references  
- Motion added without frequency gate  

## Verification

- [ ] Command named and matched  
- [ ] Context loaded or explicitly absent  
- [ ] System preserved (unless redesign)  
- [ ] Slop catalog clean on touched surfaces  
