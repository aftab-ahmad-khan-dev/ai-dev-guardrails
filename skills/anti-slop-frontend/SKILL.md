---
name: anti-slop-frontend
description: >-
  Infers brief and design direction, then ships distinctive frontends that avoid
  generic AI aesthetics. Use when building or restyling UI, landing pages,
  dashboards, or marketing surfaces, or when the user asks to remove AI slop,
  add taste, or make the interface feel designed.
---

# Anti-Slop Frontend


## ⚡ Command

```text
/anti-slop-frontend
# or ask the agent:
use skill anti-slop-frontend
```

## Overview

Read the room before generating pixels. Infer industry, audience, mood, motion depth, and layout family — then commit to a direction that could not be swapped onto another brand unchanged. Pair with `design-context` and close with the slop catalog.

## When to use

- New UI, landing pages, marketing sites, product shells
- “Make it not look AI-generated”
- Visual pass where no existing DESIGN.md direction exists

**Not for:** pure backend work; motion-only reviews (`review-motion`); named micro-steers (`design-steer polish`).

## Process

### 0. Brief inference (mandatory)

Before code, state in chat (short):

| Field | Infer from |
|-------|------------|
| Industry / domain | Product, copy, repo |
| Audience | Who uses it, under what stress |
| Surface mode | Persuade · Operate · Read · Experience |
| Mood | e.g. clinical, warm, mechanical, editorial |
| Motion depth | none · subtle · expressive |
| Layout family | e.g. full-bleed brand · dense ops · editorial · bento (only if earned) |
| System choice | Inherit repo tokens **or** propose native CSS / existing lib |

If `PRODUCT.md` / `DESIGN.md` exist, **load them** and treat as source of truth. If missing on a design-heavy task, run `design-context` first or write minimal stubs.

### 1. Direction commitment

Write one sentence the implementation must obey. Example: “Fintech ops: cool gray-blue neutrals, 4px radius, tabular numbers, zero marketing cards.”

Refuse default clusters unless the brief truly demands them:

1. Purple-on-white / purple→indigo gradients  
2. Cream ground + high-contrast serif + terracotta accent  
3. Broadsheet hairlines / zero-radius newspaper grid  

### 2. Design system map

| Situation | Prefer |
|-----------|--------|
| Repo already has tokens / components | **Inherit** — do not invent a parallel system |
| Enterprise / dense admin | Match existing (Carbon, Polaris, Primer, …) if present |
| Greenfield marketing | Native CSS or project stack; distinctive type + color |
| Greenfield app with shadcn/Radix already | Extend those primitives; restyle, don’t replace |
| Regulated / gov | Existing USWDS / GOV.UK patterns if in play |

### 3. Composition rules (hard)

**Landing / promo (Persuade):**

- First viewport = one composition: brand (hero-level), one headline, one support sentence, one CTA group, one dominant visual plane.
- Full-bleed hero by default — not inset cards, side panels, or floating media.
- No hero overlays (badges, chips, stickers).
- No stats / schedules / promo grids in the first viewport.
- Brand test: remove the nav — the first viewport must still own the brand.

**Product / ops (Operate):**

- Clarity and speed over spectacle.
- Cards only when they bound an interaction.
- One job per section.

**All surfaces:**

- Real imagery (product, place, atmosphere) beats abstract mesh gradients as the main idea.
- Ship 2–3 intentional motions on visually led work — not noise (see `motion-craft`).
- Dual-mode (light/dark) when the product has themes: contrast and hierarchy parity.

### 4. Build

Implement against the committed direction. Prefer the project’s stack. No placeholder sections — use `ship-complete-ui` if tempted to stub.

### 5. Hard pre-flight (every checkbox honest)

- [ ] Brief inference stated and followed  
- [ ] Direction sentence still true after implementation  
- [ ] Existing design system inherited when present  
- [ ] Slop catalog: zero unexplained fails ([`../../design/references/slop-catalog.md`](../../design/references/slop-catalog.md))  
- [ ] Hero / first-viewport budget respected for Persuade  
- [ ] Typography is purposeful (not Inter/Roboto/Arial by default on brand surfaces)  
- [ ] Spacing on a scale; radii intentional  
- [ ] Keyboard + contrast basics OK  
- [ ] `prefers-reduced-motion` if movement exists  
- [ ] No lorem, fake metrics, or TODO UI  

## Redesign note

On existing products, prefer `redesign-audit` first — preserve what works, then modernize with explicit levers.

## Common rationalizations

| Rationalization | Reality |
|-----------------|---------|
| “Purple is fine for a prototype” | Prototypes leak. Pick the real direction now. |
| “Cards make it organized” | Spacing and type organize; cards are chrome. |
| “We’ll add brand later” | Brand-weak first viewport fails the brand test. |
| “Gradients add polish” | Atmosphere needs a real visual idea, not mesh fill. |

## Red flags

- First viewport could belong to another SaaS after removing the logo
- Icon tiles above every heading
- Nested cards, pill clusters, status-chip soup
- Bounce easing, `transition: all`, `scale(0)`
- Dark-mode afterthought with crushed contrast

## Verification

- [ ] Inference + direction recorded in the session  
- [ ] Pre-flight all honestly checked  
- [ ] Slop catalog clean or waivers listed with reason  
- [ ] Pair `frontend-ui-engineering` verification for a11y / responsive / states  
