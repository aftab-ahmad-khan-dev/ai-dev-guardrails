---
name: review-motion
description: >-
  Strictly reviews animation and transition code against a high craft bar.
  Default to flagging; approval is earned. Use when reviewing motion diffs,
  animation PRs, or when asked to critique transitions and micro-interactions.
disable-model-invocation: true
---

# Review Motion


## ⚡ Command

```text
/review-motion
# or ask the agent:
use skill review-motion
```

## Overview

You review **motion only**. Decline general code review and point to `code-review-and-quality`. Bias: flag by default. Standards: [`../references/motion-standards.md`](../references/motion-standards.md).

## When to use

- Diff or files include animation / transition / spring code  
- User asks for a strict motion review  

## Non-negotiables

1. Justified purpose  
2. Frequency-appropriate (no keyboard / 100+/day motion)  
3. Responsive easing (`ease-out` / custom — never `ease-in` on UI)  
4. Sub-300ms typical UI  
5. Correct origin / no `scale(0)`  
6. Interruptible when rapidly retriggered  
7. GPU props only (`transform` / `opacity`)  
8. `prefers-reduced-motion` + hover gating  
9. Asymmetric enter/exit where deliberate  
10. Cohesion with product personality  

## Escalation (hard flags)

- `transition: all`  
- `scale(0)` / pure fade with no transform  
- `ease-in` on UI; bounce/elastic on chrome  
- Motion on keyboard / command-palette toggles  
- UI duration > 300ms without reason  
- Center origin on trigger-anchored overlays  
- Keyframes on toasts/toggles that must interrupt  
- Animating layout properties  
- Missing reduced-motion on movement  

## Remedial order

Delete → reduce → easing → origin → interruptible → GPU → asymmetry → polish → a11y/cohesion.

## Required output

### 1. Findings table (required)

| Before | After | Why |
|--------|-------|-----|
| … | … | … |

One row per issue. Cite `file:line` in Before or Why.

### 2. Verdict (required)

Tier commentary (omit empty): feel-breaking → missed deletions → performance → interruptibility/timing → origin/cohesion → a11y.

Close with **Block** or **Approve**.

**Block if:** feel-breaking regression, high-frequency/keyboard motion, `scale(0)` / `ease-in` on UI, or easy GPU fix ignored.

## Verification

- [ ] Table + verdict emitted  
- [ ] Only motion in scope  
- [ ] Standards cited for numeric claims  
