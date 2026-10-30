# Slop catalog — AI frontend tells

Run this checklist before shipping UI. A finding is anything that would still look “generated” after removing the brand name.

## A. Palette & atmosphere

| ID | Tell | Fix |
|----|------|-----|
| S-01 | Purple / indigo / violet as default brand | Commit to a product-specific hue; avoid gradient-to-indigo defaults |
| S-02 | Warm cream `#F4F1EA` + serif display + terracotta accent cluster | Pick a different direction; do not stack all three |
| S-03 | Broadsheet / hairline rules / zero radius / dense newspaper columns as default | Only when the brand is editorial-news; otherwise avoid |
| S-04 | Pure `#000` / `#fff` / raw gray with no tint | Tint neutrals toward brand hue (even 2–4% chroma) |
| S-05 | Gray text on colored / busy backgrounds | Raise contrast; use solid surface under text |
| S-06 | Glow / neon blur / glassmorphism as decoration | Reserve for brand-true effects; default to clean surfaces |
| S-07 | Flat single-color page with no atmosphere | Add subtle gradient, pattern, or real imagery plane |

## B. Typography

| ID | Tell | Fix |
|----|------|-----|
| S-10 | Inter / Roboto / Arial / system-ui as “design choice” | Choose expressive, purposeful fonts for brand surfaces |
| S-11 | Italic serif kicks on every marketing headline | One intentional voice; don’t costume every H1 |
| S-12 | Skipped heading levels / styled divs as headings | Real `h1`→`h2` hierarchy; one `h1` per view |
| S-13 | Everything same weight / same size | Establish clear display / title / body / meta scale |
| S-14 | Line length > ~75ch or cramped < ~35ch for body | Target ~45–75ch for reading surfaces |

## C. Layout & composition

| ID | Tell | Fix |
|----|------|-----|
| S-20 | Hero as inset card / side panel / floating media | Full-bleed hero plane on landing / promo surfaces |
| S-21 | Cards nested in cards / everything wrapped in a card | Cards only for interactive containers; remove decorative chrome |
| S-22 | Uniform 3-column “feature grid” with icon tiles | Purpose-driven layout; vary hierarchy |
| S-23 | Stat strips, pill clusters, badge soups in the first viewport | Hero budget: brand, one headline, one support line, one CTA group, one visual |
| S-24 | Detached labels / floating stickers on hero media | No overlays on hero imagery |
| S-25 | Dashboard-looking first viewport on a marketing page | One composition, not a control panel |
| S-26 | Brand only in nav / eyebrow | Brand must survive the “remove the nav” test on branded pages |
| S-27 | Multiple competing jobs in one section | One purpose, one headline, one short support line |

## D. Components & chrome

| ID | Tell | Fix |
|----|------|-----|
| S-30 | `rounded-2xl` / `rounded-full` on everything | Radius scale with intent (sharp product vs soft consumer) |
| S-31 | Multi-layer drop shadows as depth theater | Subtle or token-driven elevation only |
| S-32 | Side-tab / thick accent borders as fake hierarchy | Use type, spacing, and color — not decorative rails |
| S-33 | Status-chip soup (Live / New / Beta everywhere) | One status max unless the product is status-heavy |
| S-34 | Icon-in-rounded-square above every section title | Drop the tile; let type lead |
| S-35 | Generic CTA copy (“Get started”, “Unlock your potential”) | Specific verbs tied to the outcome |

## E. Motion

| ID | Tell | Fix |
|----|------|-----|
| S-40 | Bounce / elastic easing on UI | Use strong ease-out / custom curves; see motion-standards |
| S-41 | `transition: all` | List properties: `transform`, `opacity`, colors as needed |
| S-42 | `scale(0)` entrances | Start ~`0.92–0.97` + opacity |
| S-43 | Motion on keyboard / 100+/day actions | Delete the animation |
| S-44 | Missing `prefers-reduced-motion` | Keep opacity/color; drop movement |
| S-45 | Hover motion without fine-pointer gate | `@media (hover: hover) and (pointer: fine)` |

## F. Content & completeness

| ID | Tell | Fix |
|----|------|-----|
| S-50 | Lorem / “Acme Labs” / fake metrics | Realistic copy; sourced stats only |
| S-51 | Placeholder images / empty sections / TODO blocks | Finish or cut the section |
| S-52 | Decorative gradients standing in for product imagery | Real product, place, or atmosphere |
| S-53 | Emoji as primary iconography | Prefer SVG / system icons unless brand is emoji-native |

## Pre-ship gate

- [ ] No S-01…S-07 palette tells remain (or consciously accepted with reason)
- [ ] No S-10…S-14 type tells
- [ ] No S-20…S-27 composition tells on marketing surfaces
- [ ] No S-30…S-35 chrome tells
- [ ] No S-40…S-45 motion tells
- [ ] No S-50…S-53 content tells
- [ ] Light + dark parity if dual-mode is on
- [ ] Keyboard + contrast checked (pair with `references/accessibility-checklist.md`)
