---
name: ship-complete-ui
description: >-
  Finishes UI surfaces completely — no placeholders, skipped sections, fake
  copy, or missing interaction states. Use when output looks half-done, when
  shipping a page, or when the user asks to remove TODOs and stub content from
  the interface.
---

# Ship Complete UI


## ⚡ Command

```text
/ship-complete-ui
# or ask the agent:
use skill ship-complete-ui
```

## Overview

Incomplete UI is a design failure. Close every section you opened: real copy, real states, real empty/error/loading paths — or cut the section entirely.

## When to use

- Before declaring a page/component done  
- Placeholders, “Lorem”, “Coming soon”, TODO comments in UI  
- After `anti-slop-frontend` / `design-steer` / `visual-prototype`  

## Process

### 1. Surface inventory

List every section, route, and interactive element in scope. Mark each: **complete** / **stub** / **missing states**.

### 2. Ban list (must be gone)

- Lorem / ipsum / “Acme” fake companies (unless fixture tests)  
- `TODO`, `FIXME`, “replace this” visible in UI  
- Empty image boxes / gray rectangles as final art  
- Buttons with no handler or dead `#` links on ship paths  
- Sections that only exist to fill a template  
- Unsourced metrics / vanity stats  

### 3. State completeness

For each interactive flow in scope:

| State | Required |
|-------|----------|
| Loading | Skeleton or honest pending |
| Empty | Explanation + next action |
| Error | Recoverable message + retry when possible |
| Success | Confirmation that matches the action |
| Disabled | Clear why, when relevant |
| Overflow | Long names, small screens, zoom |

### 4. Content honesty

- CTAs name the outcome  
- Stats only if sourced (pair with pack stats rules)  
- Imagery is real product/place/atmosphere or intentionally cut  

### 5. Final gates

1. Slop catalog ([`../../../design/references/slop-catalog.md`](../../../design/references/slop-catalog.md))  
2. `frontend-ui-engineering` verification (a11y, responsive)  
3. No console errors on the happy path  

## Common rationalizations

| Rationalization | Reality |
|-----------------|---------|
| “Placeholder is fine for review” | Reviewers judge the placeholder. |
| “We’ll add empty states later” | Later becomes never; add or cut. |
| “Fake stats show the layout” | Fake stats train the wrong hierarchy. |

## Red flags

- Gray boxes labeled “image”  
- Three feature cards with identical copy structure and icon tiles  
- Primary CTA does nothing  

## Verification

- [ ] Inventory has zero stubs in ship scope  
- [ ] Loading / empty / error covered for primary flows  
- [ ] Slop catalog clean  
- [ ] No TODO/lorem in user-visible UI  
