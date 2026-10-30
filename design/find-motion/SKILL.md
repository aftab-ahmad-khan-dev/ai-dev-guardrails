---
name: find-motion
description: >-
  Scans UI for places that would genuinely benefit from motion and explicitly
  lists what must not be animated. Use when planning micro-interactions,
  searching for animation opportunities, or deciding where motion adds clarity.
---

# Find Motion


## ⚡ Command

```text
/find-motion
# or ask the agent:
use skill find-motion
```

## Overview

Opportunity scan with a subtraction bias. Output a prioritized plan any agent can execute with `motion-craft` — and a hard “do not animate” list.

## When to use

- “Where should we add animation?”  
- Motion pass planning before implementation  
- Auditing a marketing page for intentional motion (2–3 moments)

## Process

### 1. Map the surface

Identify: navigation, overlays, feedback, lists, marketing story, drag/gesture targets, first-run moments.

### 2. Score candidates

For each candidate:

| Field | Notes |
|-------|-------|
| Element / flow | |
| Purpose | spatial / state / explain / feedback / anti-jar |
| Frequency | 100+ / tens / occasional / rare |
| Decision | animate · reduce · **never** |
| Suggested recipe | duration, easing, props (from motion-standards) |
| Priority | P0 / P1 / P2 |

### 3. Do-not-animate list (required)

Always include:

- Keyboard shortcuts / command palette open-close  
- High-frequency toggles if they already feel snappy  
- Pure decoration with no purpose  
- Anything that would violate reduced-motion badly if forgotten  

### 4. Hand-off plan

Emit self-contained tasks:

```
P0 — Toast enter/exit from same edge (180ms, ease-out, transform+opacity)
P1 — Modal: opacity + slight scale 0.96→1, 200ms
NEVER — Sidebar keyboard toggle
```

Implementation → `motion-craft`. Review → `review-motion`.

## Common rationalizations

| Rationalization | Reality |
|-----------------|---------|
| “More motion = more premium” | Wrong frequency makes it feel slower. |
| “Animate all list items on load” | Usually noise; prefer subtle stagger or none. |

## Verification

- [ ] Prioritized animate list with recipes  
- [ ] Explicit never-animate list  
- [ ] Frequency gate applied to every candidate  
