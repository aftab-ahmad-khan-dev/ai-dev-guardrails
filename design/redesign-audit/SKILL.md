---
name: redesign-audit
description: >-
  Audit-first visual redesign for existing products — preserve what works,
  name modernization levers, then restyle without losing brand or usability.
  Use when redesigning, refreshing, or modernizing an existing UI, or when the
  user asks for a visual audit before changes.
---

# Redesign Audit


## ⚡ Command

```text
/redesign-audit
# or ask the agent:
use skill redesign-audit
```

## Overview

Existing products already have users, habits, and equity. Audit before paint. Modernize with explicit levers — do not silently replace the design system with AI defaults.

## When to use

- “Redesign this”, “visual refresh”, “modernize the UI”
- Legacy CSS / inconsistent components
- Before a large restyle PR

**Not for:** greenfield (`anti-slop-frontend`); tiny polish (`design-steer polish`).

## Process

### 1. Inventory (no restyle yet)

Capture:

- Brand assets, fonts, colors in use  
- Component library / token files  
- Layout patterns (nav, density, radius)  
- Accessibility debt (contrast, focus, headings)  
- Motion personality currently in the product  
- What users praise or depend on (if known)

### 2. Audit report

Produce:

| Area | Keep | Fix | Drop |
|------|------|-----|------|
| Color | | | |
| Type | | | |
| Layout | | | |
| Components | | | |
| Motion | | | |
| Copy | | | |

Plus slop catalog hits on the current UI ([`../references/slop-catalog.md`](../references/slop-catalog.md)).

### 3. Modernization levers (pick explicitly)

Name which levers you will pull — examples:

- Tint neutrals / dual-mode parity  
- Tighten type scale  
- Reduce card chrome  
- Normalize radius / elevation  
- Replace decorative gradients with real imagery  
- Motion: delete high-frequency noise; keep purposeful feedback  

Do **not** change all levers at once unless asked.

### 4. Preservation rules

- Keep interaction model unless UX critique demands change  
- Keep information architecture unless scoped  
- Prefer restyling primitives over inventing parallel components  
- Update DESIGN.md / PRODUCT.md to match the new direction  

### 5. Execute

Hand implementation to `anti-slop-frontend` (direction) + `design-steer` (passes) + `frontend-ui-engineering` (a11y/state). Re-run audit on the result.

## Common rationalizations

| Rationalization | Reality |
|-----------------|---------|
| “Faster to rebuild from scratch” | You will reintroduce slop and break muscle memory. |
| “Keep nothing — it’s all dated” | Equity hides in spacing, IA, and copy. Audit first. |

## Verification

- [ ] Inventory + keep/fix/drop table delivered before big code changes  
- [ ] Levers named and scoped  
- [ ] DESIGN.md / PRODUCT.md updated  
- [ ] Post-change slop catalog clean  
