# Motion standards

Use with [`motion-craft`](../design/motion-craft/SKILL.md) and [`review-motion`](../design/review-motion/SKILL.md).

## Frequency gate (decide first)

| How often seen | Decision |
|----------------|----------|
| 100+/day (keyboard shortcuts, command palette) | **No animation** |
| Tens/day (hover, list nav) | Remove or drastically reduce |
| Occasional (modal, drawer, toast) | Standard UI motion |
| Rare / first-time (onboarding, celebration) | Delight allowed |

## Purpose (required)

Valid: spatial consistency · state indication · explanation · feedback · prevent jarring change.  
Invalid for frequent UI: “looks cool.”

## Easing

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
```

| Situation | Curve |
|-----------|-------|
| Enter / exit UI | `ease-out` / `--ease-out` |
| Move / morph on screen | `--ease-in-out` |
| Hover / color | `ease` or short custom |
| Continuous (marquee, indeterminate) | `linear` |

**Never** use `ease-in` on UI interactions. **Avoid** bounce / elastic on product UI.

## Duration budgets

| Element | Duration |
|---------|----------|
| Button press | 100–160ms |
| Tooltip / small popover | 125–200ms |
| Dropdown / select | 150–250ms |
| Modal / drawer | 200–500ms |
| Marketing / explanatory | Longer OK if purposeful |

UI interactions should usually stay **under 300ms**.

## Physicality

- Popovers / dropdowns / tooltips: scale from **trigger** (`transform-origin`), not center (modals stay centered).
- Never enter from `scale(0)` — use ~`0.92–0.97` + opacity.
- Rapid / gesture motion must be **interruptible** (transitions or springs, not restarting keyframes).
- Animate **`transform` + `opacity`** only. No `width` / `height` / `top` / `left` / `margin` for motion.
- Avoid `transition: all`.

## Asymmetry

Deliberate user actions can be slightly slower; system responses snap. Symmetric press-and-release often feels wrong.

## Accessibility

```css
@media (prefers-reduced-motion: reduce) {
  /* Keep opacity/color; drop movement / large transforms */
}
@media (hover: hover) and (pointer: fine) {
  /* Hover-only motion */
}
```

## Stagger

Group entrances: 30–80ms stagger. Avoid everything-at-once fireworks on dense UIs.

## Remedial hierarchy

1. Delete → 2. Reduce → 3. Fix easing → 4. Fix origin → 5. Interruptible → 6. GPU props → 7. Asymmetric timing → 8. Polish (blur bridge, spring) → 9. a11y + cohesion
