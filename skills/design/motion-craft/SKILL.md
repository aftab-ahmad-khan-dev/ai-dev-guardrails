---
name: motion-craft
description: >-
  Designs and implements purposeful UI motion with frequency gates, strong
  easing, duration budgets, GPU-safe properties, and reduced-motion support.
  Use when adding animations, transitions, micro-interactions, or when the user
  asks for motion that feels right rather than decorative.
---

# Motion Craft


## ⚡ Command

```text
/motion-craft
# or ask the agent:
use skill motion-craft
```

## Overview

Taste in motion is mostly subtraction. Animate only when purpose and frequency allow; then pick curve, duration, origin, and interruptibility deliberately. Standards: [`../../../design/references/motion-standards.md`](../../../design/references/motion-standards.md).

## When to use

- Adding or rewriting transitions / animations  
- `design-steer animate`  
- Marketing motion that must still feel engineered  

**Not for:** reviewing someone else’s motion diff only (`review-motion`); scanning for opportunities (`find-motion`).

## Process

### 1. Frequency gate

| Frequency | Action |
|-----------|--------|
| 100+/day or keyboard-initiated | **Do not animate** |
| Tens/day | Tiny or none |
| Occasional | Standard budgets |
| Rare / first-time | Delight OK |

### 2. Purpose test

Answer: why does this animate?  
Valid: spatial continuity · state · explanation · feedback · avoid jarring change.  
If only “cool” and frequent → delete.

### 3. Choose ingredients

1. **Easing** — enter/exit → strong ease-out; never ease-in on UI  
2. **Duration** — stay under 300ms for typical UI  
3. **Properties** — `transform` + `opacity` only  
4. **Origin** — trigger-anchored for popovers; centered modals  
5. **Interruptibility** — transitions/springs for rapid retrigger  
6. **Asymmetry** — deliberate acts can be slower; responses snap  
7. **a11y** — `prefers-reduced-motion`; hover gated to fine pointers  

Default curves:

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
```

Prefer CSS transitions / `@starting-style` / WAAPI for predetermined motion; springs for gesture-driven.

### 4. Implement

Match project stack (CSS, Motion library, GSAP). Keep personality cohesive with PRODUCT.md / DESIGN.md. On visually led marketing, ship 2–3 intentional motions — not a cascade of fades.

### 5. Self-review

Use Before/After/Why table for anything you had to correct:

| Before | After | Why |
|--------|-------|-----|
| `ease-in` 300ms | `--ease-out` 180ms | Instant feedback; less sluggish |

Then run `review-motion` mindset (or the skill) before merge.

## Common rationalizations

| Rationalization | Reality |
|-----------------|---------|
| “Every entrance needs motion” | High-frequency entrances should be instant. |
| “ease-in feels cinematic” | On UI it feels laggy. |
| “scale(0) is fine” | Nothing real appears from nothing. |
| “We’ll add reduced-motion later” | Add it with the animation. |

## Red flags

- `transition: all`  
- Bounce / elastic on product chrome  
- Layout property animation  
- Hover motion on touch-primary UIs without gating  

## Verification

- [ ] Frequency + purpose stated  
- [ ] Budgets and GPU props respected  
- [ ] Reduced-motion + hover gates present when needed  
- [ ] Cohesive with product personality  
