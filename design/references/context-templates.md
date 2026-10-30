# Design context templates

Write these at the **project root** (or app package root in a monorepo). Every design skill reads them before inventing visuals.

## PRODUCT.md

```markdown
# PRODUCT.md

## Surface mode
<!-- Persuade | Operate | Read | Experience -->
Operate

## Users
Who they are, context of use, constraints (time, light, device).

## Job to be done
What success looks like in one sentence.

## Brand voice
Tone adjectives. What we never sound like.

## Anti-references
Visual / copy patterns we refuse (e.g. purple gradients, glassmorphism, "boost productivity").

## Constraints
Design system? Existing tokens? Framework? Accessibility target?
```

## DESIGN.md

```markdown
# DESIGN.md

## Direction (one sentence)
e.g. "Clinical ops tool: cool neutrals, sharp 4px radius, no marketing chrome."

## Color
- Brand / accent:
- Surfaces (light / dark):
- Text / muted / danger / success:
- Notes on tinting neutrals:

## Typography
- Display:
- Body / UI:
- Mono (if any):
- Scale (rem / tokens):

## Space & radius
- Spacing scale:
- Radius scale:
- Elevation:

## Components
Key primitives and variants already in the repo.

## Motion
Personality (crisp / soft / playful). Default durations. Reduced-motion policy.

## Do / Don't
- Do:
- Don't:
```

## Surface modes

| Mode | Goal | Design bias |
|------|------|-------------|
| **Persuade** | Win attention / convert | Strong brand, hero discipline, one idea |
| **Operate** | Complete a task | Density, clarity, speed, calm chrome |
| **Read** | Build understanding | Type hierarchy, measure, quiet UI |
| **Experience** | Let the work lead | Immersive, motion-capable, content-first |

## Init checklist

- [ ] PRODUCT.md exists and names a surface mode
- [ ] Anti-references listed
- [ ] DESIGN.md exists **or** project already has tokens the agent must inherit
- [ ] Agent stated whether it will **inherit** an existing system vs **propose** one
