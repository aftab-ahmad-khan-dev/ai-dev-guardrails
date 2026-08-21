# Design steer — command vocabulary

Use with [`design-steer`](../design/design-steer/SKILL.md). Each command is one intervention. Prefer naming the command explicitly in chat.

## Setup & context

| Command | Does |
|---------|------|
| `init` | Gather audience, surface mode, brand lane; write PRODUCT.md (+ DESIGN.md if needed) |
| `document` | Extract DESIGN.md from existing tokens / components |
| `extract` | Pull reusable tokens and components into the system |

## Shape & build

| Command | Does |
|---------|------|
| `shape` | Plan UX/UI before code — hierarchy, modes, anti-references |
| `craft` | Full shape → build → slop check loop |
| `prototype` | Multiple genuinely different variants (pair with `visual-prototype`) |

## Quality passes

| Command | Does |
|---------|------|
| `critique` | UX review: hierarchy, clarity, emotional fit |
| `audit` | Technical quality: a11y, responsive, contrast, performance |
| `polish` | Final pass: system alignment, slop kill, ship readiness |
| `harden` | Empty / error / overflow / i18n / edge cases |
| `onboard` | First-run, empty states, activation paths |

## Visual levers

| Command | Does |
|---------|------|
| `bolder` | Amplify weak / timid designs |
| `quieter` | Tone down noisy / overstyled designs |
| `distill` | Strip to essence; remove competing jobs |
| `typeset` | Fonts, scale, rhythm, hierarchy |
| `layout` | Spacing, alignment, visual rhythm |
| `colorize` | Strategic color (not rainbow decoration) |
| `adapt` | Device / breakpoint / density adaptation |

## Motion & delight

| Command | Does |
|---------|------|
| `animate` | Purposeful motion only (pair with `motion-craft`) |
| `delight` | Rare, justified moments of joy |
| `overdrive` | High-craft extraordinary effects — opt-in only |

## Copy

| Command | Does |
|---------|------|
| `clarify` | Fix unclear UX copy and CTA verbs |

## Usage

```
design-steer polish pricing
design-steer distill the hero
design-steer audit settings
design-steer typeset onboarding
```

Always load PRODUCT.md / DESIGN.md when present. Always run the [slop catalog](design-slop-catalog.md) before declaring done.
