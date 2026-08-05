---
name: design-context
description: >-
  Captures product and visual context into PRODUCT.md and DESIGN.md so later
  design commands inherit audience, surface mode, brand voice, and tokens. Use
  when starting design work on a project, running design init, or when anti-slop
  / steer skills lack context files.
---

# Design Context


## ⚡ Command

```text
/design-context
# or ask the agent:
use skill design-context
```

## Overview

One setup pass so every later design skill stops inventing a new aesthetic. Writes portable context at the app root.

## When to use

- First visual session on a repo
- User says init / document design system / “remember our brand”
- `anti-slop-frontend` or `design-steer` finds no PRODUCT.md / DESIGN.md

**Not for:** implementing pixels (hand off to `anti-slop-frontend` or `design-steer`).

## Process

### 1. Detect what exists

Scan for: token files, `tailwind.config.*`, theme providers, component libraries, existing `DESIGN.md` / `PRODUCT.md`, brand assets.

State aloud: **inherit** vs **document-then-extend** vs **greenfield propose**.

### 2. Interview (short)

Ask only what you cannot infer. Cover:

1. Surface mode — Persuade / Operate / Read / Experience  
2. Users + job to be done  
3. Brand voice + anti-references  
4. Light/dark requirement  
5. Motion personality (none / subtle / expressive)

### 3. Write files

Use templates in [`../references/context-templates.md`](../references/context-templates.md).

- Always write or update **PRODUCT.md**
- Write **DESIGN.md** when tokens are unclear or the user wants a portable system
- Prefer extracting real token values from code over inventing new ones (`document` mode)

### 4. Confirm

Show a 5-line summary: mode, audience, direction sentence, anti-references, next skill (`anti-slop-frontend` or `design-steer craft`).

## Document mode (existing code)

When the user wants DESIGN.md from code:

1. Walk tokens, fonts, radii, component variants  
2. Record facts, not aspirations  
3. List gaps (“no dark tokens”, “three conflicting radii”)  
4. Do not restyle until the user asks

## Common rationalizations

| Rationalization | Reality |
|-----------------|---------|
| “I’ll just remember the brand” | Next turn won’t. Write the file. |
| “DESIGN.md will slow us down” | Reworking purple defaults costs more. |
| “We have Tailwind, that’s enough” | Tailwind without direction still yields slop. |

## Verification

- [ ] PRODUCT.md at project/app root with surface mode + anti-references  
- [ ] DESIGN.md present **or** explicit inherit-from-code note in PRODUCT.md  
- [ ] Summary confirmed with the human when brand is ambiguous  
