---
name: visual-prototype
description: >-
  Builds multiple genuinely different UI directions for the same brief and
  presents them for comparison so a winner can be committed. Use when exploring
  design directions, A/B-ing layouts, or when the user asks for variants that
  are not slight tweaks of the same template.
---

# Visual Prototype


## ⚡ Command

```text
/visual-prototype
# or ask the agent:
use skill visual-prototype
```

## Overview

Models default to one favorite aesthetic. Force divergence: several complete directions with different layout families, type, and mood — then commit one. Remove losing **variants only** from the sandbox paths listed below — never wipe the repo.

## When to use

- “Show me options”, “different directions”, “prototype variants”  
- Stuck in a templated look  
- Before locking DESIGN.md on a greenfield surface  

**Not for:** tiny polish on a locked system (`design-steer`); production hardening.

## Process

### 1. Lock the brief

From PRODUCT.md or a short inference: audience, mode, constraints, anti-references. All variants must solve the **same** job.

### 2. Deal distinct directions (default 3)

Each variant needs a one-line law, e.g.:

1. **Editorial** — strong type, quiet chrome, photography-led  
2. **Mechanical** — sharp radii, mono accents, dense structure  
3. **Soft product** — airy space, restrained color, gentle motion  

Reject near-duplicates (same layout, recolored). If two share structure and type, redo one.

### 3. Build comparable slices

Implement the **same slice** (e.g. hero + one section, or one key screen) for each variant — complete enough to judge, not a whole app × 3.

Include a simple switcher when in-app:

```tsx
// PrototypeSwitcher: local state selects variant A | B | C
```

Keep variants isolated under sandbox paths only:

- `prototypes/<session>/variant-a|b|c/` **or**
- files named `*.prototype.tsx` / `*.prototype.css`

Never put production routes in those folders.

### 4. Compare

Present a table:

| Variant | Strength | Risk | Fits PRODUCT.md? |
|---------|----------|------|------------------|
| A | | | |
| B | | | |
| C | | | |

Recommend a winner; wait for human commit unless they already picked.

### 5. Commit

1. Promote winner into the real routes/components  
2. Remove **only** sandbox loser paths you created this session (`prototypes/…` or `*.prototype.*`) — follow `safe-file-ops`  
3. Update DESIGN.md direction sentence  
4. Run slop catalog + `ship-complete-ui` on the winner  

## Safety (critical)

- **Never** `rm -rf` the project, `src/`, or unrelated folders because a variant “lost”.  
- **Never** interpret “delete the rest” as cleaning the git worktree.  
- If unsure whether a path is sandbox → **do not delete**; ask.

## Common rationalizations

| Rationalization | Reality |
|-----------------|---------|
| “Three shades of the same card grid” | Not variants — redo with different layout families. |
| “Keep all variants in production” | Ships confusion. Commit one. |
| “Clean the repo of unused UI” | Forbidden without an explicit path list + approval. |

## Verification

- [ ] ≥2 (prefer 3) genuinely different directions  
- [ ] Same job / same content constraints  
- [ ] Winner committed; only sandbox losers removed  
- [ ] DESIGN.md updated  
- [ ] `safe-file-ops` respected
