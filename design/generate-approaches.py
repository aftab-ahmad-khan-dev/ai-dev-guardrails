#!/usr/bin/env python3
"""Generate 50+ design approach SKILL.md files under design/approaches/."""
from __future__ import annotations

import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "approaches"

# name, title, family, description_triggers, body_bullets, when, process_extra
APPROACHES: list[dict] = [
  # —— Style directions (Taste-class) ——
  ("style-soft", "Soft / Quiet Luxury", "style",
   "soft UI, quiet luxury, calm expensive interfaces, airy whitespace",
   ["Low contrast-but-accessible surfaces", "Generous whitespace; soft radii (8–16)", "Restrained accent; no neon", "Smooth short motion (150–220ms ease-out)"],
   "Marketing and premium product UI that should feel calm and expensive."),
  ("style-minimalist", "Minimalist Editorial Product", "style",
   "minimalist UI, editorial product, restrained color, tight hierarchy",
   ["Few colors; strong type hierarchy", "Sharp structure; avoid card soup", "Whitespace as structure, not emptiness", "One accent max"],
   "Product UI that should feel clean, editorial, and deliberate."),
  ("style-brutalist", "Brutalist / Mechanical", "style",
   "brutalist UI, swiss typography, raw structure, hard contrast",
   ["Hard contrast; visible structure", "Swiss/grotesk type; mono accents OK", "Hairlines or raw borders over soft shadows", "Motion crisp, not bouncy"],
   "Campaigns, portfolios, and tools that want mechanical honesty."),
  ("style-editorial", "Editorial / Magazine", "style",
   "editorial layout, magazine UI, typographic landing page",
   ["Type-led composition; long measure discipline", "Photography or illustration as story", "Sparse chrome; pull quotes / rules sparingly", "Avoid SaaS feature-card grids"],
   "Content-led brands, publishers, storytelling landings."),
  ("style-swiss", "Swiss International", "style",
   "swiss design, international typographic style, grid UI",
   ["Modular grid; asymmetric balance", "Helvetica-like grotesk; flush hierarchy", "Primary colors as accents, not fills", "No skeuomorphism"],
   "Systems, institutions, and brands that want clarity + rigor."),
  ("style-neo-brutal", "Neo-Brutal", "style",
   "neo-brutalism, thick borders, flat color blocks, playful hard UI",
   ["Thick borders; flat fills; hard offsets (not soft shadows)", "Bold type; limited palette", "Interactive affordances obvious", "Keep a11y contrast"],
   "Playful product marketing — not enterprise ops."),
  ("style-industrial", "Industrial / Utility", "style",
   "industrial UI, utility aesthetic, hardware dashboard look",
   ["Dense but legible; tabular numbers", "Muted metals / ink; warning colors semantic", "Panels over cards", "Motion minimal"],
   "Ops, hardware, logistics, SCADA-adjacent tools."),
  ("style-organic", "Organic / Natural", "style",
   "organic UI, natural textures, warm human brand",
   ["Warm tinted neutrals; real textures sparingly", "Humanist type; soft curves with intent", "Nature/product photography over mesh gradients", "Avoid purple AI defaults"],
   "Wellness, food, outdoor, human-centered brands."),
  ("style-luxury", "Luxury / Couture", "style",
   "luxury UI, couture web, high-end brand site",
   ["Slow scroll rhythm; generous margins", "Display serif or custom; meticulous kerning", "Black/ivory/metal accents; rare color", "Motion elegant, never bounce"],
   "Fashion, hospitality, premium goods."),
  ("style-playful", "Playful Product", "style",
   "playful UI, friendly product, consumer fun interface",
   ["Rounded where brand allows; vivid but curated accents", "Illustration OK; emoji not primary icons", "Delight rare (see motion-craft frequency)", "Still pass slop catalog"],
   "Consumer apps for younger or lighthearted brands."),
  ("style-clinical", "Clinical / Healthcare", "style",
   "clinical UI, healthcare product, calm medical interface",
   ["Cool neutrals; high legibility", "Zero decorative noise", "Status colors semantic + labeled", "Trust > cleverness"],
   "Health, biotech, clinical ops."),
  ("style-terminal", "Terminal / Developer", "style",
   "terminal UI, developer aesthetic, monospace product shell",
   ["Mono for data; clear density controls", "Dark-first OK if contrast holds", "No fake matrix rain", "Keyboard-first; motion almost none"],
   "Devtools, CLIs-in-UI, infra consoles."),
  ("style-magazine", "Longform Magazine", "style",
   "longform reading UI, article design, blog typography",
   ["45–75ch measure; comfortable leading", "Quiet chrome; progress optional", "Pull quotes restrained", "Dark mode parity for reading"],
   "Blogs, docs reading mode, essays."),
  ("style-saas-ops", "SaaS Ops Density", "style",
   "saas dashboard, ops density, B2B admin UI",
   ["Operate mode: speed + scanability", "Tables over card grids for data", "Filters in URL state", "Chrome quiet; status sparse"],
   "B2B admin, billing, internal tools."),
  ("style-consumer-mobile", "Consumer Mobile Web", "style",
   "mobile-first consumer UI, thumb-friendly web app",
   ["Thumb zones; 44px targets", "Bottom nav sparingly", "Full-bleed media OK", "No hover-only actions"],
   "Mobile web apps and responsive consumer surfaces."),
  ("style-fintech", "Fintech Trust", "style",
   "fintech UI, banking design, money product interface",
   ["Tabular nums; stable layouts (no CLS)", "Trust blues/greens earned, not purple", "Clear destructive confirms", "Motion subtle"],
   "Banking, payments, investing."),
  ("style-gov", "Public Sector Clarity", "style",
   "government UI, public sector design, accessible civic interface",
   ["Inherit USWDS/GOV.UK if present", "Plain language; high contrast", "No trend-chasing chrome", "WCAG AA+"],
   "Civic, gov, regulated public services."),
  ("style-data-viz", "Data Visualization UI", "style",
   "data viz UI, chart-heavy dashboard, analytics design",
   ["Chart first; chrome second", "Colorblind-safe palettes", "Empty/loading for every chart", "No card-in-card around every widget"],
   "Analytics and research tools."),
  ("style-docs", "Documentation System", "style",
   "docs site design, documentation UI, API reference layout",
   ["Sidebar + prose measure", "Code blocks first-class", "Anchor headings; TOC", "Search affordance obvious"],
   "Docs, API references, knowledge bases."),
  ("style-onboarding", "Activation / Onboarding", "style",
   "onboarding UI, activation flow, first-run experience",
   ["One decision per step", "Progress honest", "Skip paths when safe", "Empty states teach"],
   "First-run, trials, setup wizards."),

  # —— Steer micro-skills (Impeccable-class) ——
  ("steer-polish", "Steer: Polish", "steer",
   "polish UI, final design pass, ship-ready visuals",
   ["Align to DESIGN.md / tokens", "Run slop catalog", "Fix orphans: spacing, type, radius", "No new system inventing"],
   "Final visual pass before merge/ship."),
  ("steer-distill", "Steer: Distill", "steer",
   "distill UI, simplify layout, remove clutter",
   ["One job per section", "Remove competing CTAs", "Cut decorative chrome", "Do not add new sections"],
   "When the page is noisy or overbuilt."),
  ("steer-audit", "Steer: Audit", "steer",
   "design audit, a11y audit UI, responsive quality check",
   ["Headings, contrast, focus, targets", "Responsive breakpoints", "Findings table with severity", "Evidence over vibes"],
   "Technical design quality checks."),
  ("steer-critique", "Steer: Critique", "steer",
   "UX critique, design review hierarchy clarity",
   ["Hierarchy / clarity / emotional fit", "Match PRODUCT.md mode", "Findings + recommended lever", "Not a full restyle unless asked"],
   "UX design review without code thrash."),
  ("steer-typeset", "Steer: Typeset", "steer",
   "typeset, typography hierarchy, font pairing UI",
   ["Purposeful fonts; avoid Inter/Arial defaults on brand", "Scale + measure + weight", "One display voice", "Fix skipped headings"],
   "Typography problems."),
  ("steer-layout", "Steer: Layout", "steer",
   "fix layout, spacing rhythm, visual alignment",
   ["Spacing scale only", "Alignment + proximity", "Density for Operate; air for Persuade", "Kill nested cards"],
   "Spacing and structure issues."),
  ("steer-colorize", "Steer: Colorize", "steer",
   "colorize UI, brand color pass, tint neutrals",
   ["Strategic accent; tint neutrals", "Dual-mode parity", "No purple default cluster", "Semantic status colors labeled"],
   "Color system weak or generic."),
  ("steer-bolder", "Steer: Bolder", "steer",
   "make UI bolder, amplify weak design, stronger visual",
   ["Increase contrast/type punch", "Keep identity; don’t rebrand", "Hero must pass brand test", "Avoid glow/neon crutches"],
   "Timid or washed-out UI."),
  ("steer-quieter", "Steer: Quieter", "steer",
   "make UI quieter, tone down design, reduce visual noise",
   ["Reduce accents, chips, shadows", "Calm motion", "Preserve hierarchy", "Distill competing jobs"],
   "Overstyled or frantic UI."),
  ("steer-harden", "Steer: Harden", "steer",
   "harden UI, edge cases, overflow error empty states",
   ["Loading/empty/error/disabled", "Text overflow + i18n length", "Form errors inline", "Touch targets"],
   "Production edge-case readiness."),
  ("steer-onboard", "Steer: Onboard", "steer",
   "onboard UX, empty state design, activation path",
   ["First-run path clear", "Empty states with next action", "Progressive disclosure", "No dead ends"],
   "Activation and empty-product moments."),
  ("steer-clarify", "Steer: Clarify", "steer",
   "clarify copy, UX writing, CTA verbs",
   ["Specific CTAs", "Plain language", "Kill vague headlines", "Match brand voice in PRODUCT.md"],
   "Unclear UX copy."),
  ("steer-adapt", "Steer: Adapt", "steer",
   "responsive adapt, mobile layout fix, density breakpoints",
   ["Mobile-first stacks", "No hover-only", "Tablet density", "Test 320 / 768 / 1024 / 1440"],
   "Breakpoint and device adaptation."),
  ("steer-delight", "Steer: Delight", "steer",
   "delight moments, micro-joy UI, celebratory feedback",
   ["Rare + justified only", "Frequency gate (motion-craft)", "Reduced-motion fallback", "Never on 100+/day actions"],
   "Adding joy without slop."),
  ("steer-animate", "Steer: Animate", "steer",
   "animate UI command, add purposeful motion",
   ["Hand off to motion-craft rules", "Purpose + frequency first", "GPU props only", "Review with review-motion"],
   "When user asks to animate a surface."),
  ("steer-shape", "Steer: Shape", "steer",
   "shape UX before code, plan UI structure",
   ["No code until plan approved (unless user says build)", "Wire hierarchy + anti-refs", "Name surface mode", "Exit: outline + next skill"],
   "Plan UX/UI before implementation."),
  ("steer-craft", "Steer: Craft", "steer",
   "craft full UI flow, shape then build polish",
   ["shape → build → polish → slop catalog", "Load design-context first", "safe-file-ops always", "ship-complete-ui at end"],
   "End-to-end visual build of a slice."),
  ("steer-overdrive", "Steer: Overdrive", "steer",
   "overdrive effects, extraordinary UI craft, advanced visuals",
   ["Opt-in only; ask if unclear", "Still pass a11y + performance", "No uncontrolled WebGL novelty for ops tools", "Document what is extraordinary"],
   "High-craft experimental effects when requested."),

  # —— Motion (Emil-class) ——
  ("motion-improve", "Improve Animations", "motion",
   "improve animations, audit motion codebase, prioritize motion fixes",
   ["Scan for transition/animation usage", "Prioritized P0/P1 plans", "Remedial hierarchy from motion-standards", "Self-contained tasks for any agent"],
   "Codebase motion debt."),
  ("motion-vocabulary", "Animation Vocabulary", "motion",
   "animation vocabulary, describe motion to AI, easing words",
   ["Teach precise language: snappy, settle, morph, stagger", "Map words → curves/durations", "User phrases → recipes", "Avoid vague 'make it smooth'"],
   "Getting better motion from prompts."),
  ("motion-apple", "Apple-like Motion", "motion",
   "apple design motion, fluid interface, WWDC-like animation web",
   ["Fluid continuity; shared-element thinking", "Soft springs for gestures", "Respect reduced-motion", "Translate to CSS/WAAPI/web, don’t cargo-cult iOS APIs"],
   "Product UI aiming for Apple-level fluidity on the web."),
  ("motion-stagger", "Stagger & Orchestration", "motion",
   "stagger animation, orchestrate entrances, sequenced UI motion",
   ["30–80ms stagger", "Parent orchestrates; children don’t fight", "Cancel on navigate", "Never everything-at-once fireworks"],
   "Group entrances and sequenced reveals."),
  ("motion-gesture", "Gesture & Drag Motion", "motion",
   "gesture animation, drag interactions, swipe dismiss",
   ["Interruptible springs", "Finger tracking > keyframes", "Spatial exit = enter reverse", "Fallback for reduced-motion"],
   "Drag, swipe, dismissible surfaces."),

  # —— Workflows ——
  ("image-to-code", "Image → Code", "workflow",
   "image to code, implement from mockup, screenshot to frontend",
   ["Analyze hierarchy/type/color/spacing first", "Tokenize before components", "Pixel-close where system allows", "No inventing extra sections"],
   "Implementing from a design image or screenshot."),
  ("brand-kit", "Brand Kit Pass", "workflow",
   "brand kit, logo color type system, brand overview",
   ["Logo concepts / clearspace", "Color roles + type roles", "Do/don’t", "Export notes for DESIGN.md"],
   "Defining or refreshing a brand kit for UI."),
  ("stitch-export", "Stitch / DESIGN.md Export", "workflow",
   "stitch export, DESIGN.md portable, design tokens document",
   ["Write portable DESIGN.md", "Semantic tokens", "Component inventory", "Readable by other DESIGN.md tools"],
   "Exporting a portable design system doc."),
  ("design-system-map", "Design System Map", "workflow",
   "pick design system, material vs polaris vs shadcn, system mapping",
   ["Inherit repo system first", "Map brief → Material/Fluent/Carbon/Polaris/Primer/GOV/Radix/shadcn/native", "Don’t mix three systems", "Document choice in DESIGN.md"],
   "Choosing or justifying a component system."),
  ("dark-mode-protocol", "Dark Mode Protocol", "workflow",
   "dark mode design, dual theme parity, theme tokens",
   ["Dual-mode by default when product themes", "Hierarchy parity; not inverted greys only", "Tint surfaces; avoid pure #000/#fff", "Test both before ship"],
   "Light/dark theme quality."),
  ("block-library", "Block Library Schema", "workflow",
   "block library, page blocks, section components contract",
   ["Name blocks; props contract", "Composition rules", "Keep library coherent across additions", "No one-off snowflake sections"],
   "Growing a landing/page block library."),
  ("gpt-strict-taste", "Strict Taste (GPT/Codex)", "workflow",
   "strict taste for GPT, Codex frontend rules, stronger anti-slop",
   ["Stronger layout variance required", "Ban ghost-cards + over-rounding", "Force brief inference written aloud", "Pre-flight cannot be skipped"],
   "When using GPT/Codex-class models that drift to templates."),
  ("hero-discipline", "Hero Discipline", "workflow",
   "hero section rules, landing first viewport, brand hero",
   ["Brand + one headline + one support + one CTA + one visual", "Full-bleed; no overlays", "No stats in first viewport", "Brand test without nav"],
   "Marketing heroes and first viewports."),
  ("landing-persuade", "Landing Persuade Mode", "workflow",
   "landing page design, marketing site, persuade mode UI",
   ["Surface mode = Persuade", "Story sections with one job each", "Real imagery", "CTA specificity"],
   "Marketing/landing builds."),
  ("dashboard-operate", "Dashboard Operate Mode", "workflow",
   "dashboard design, operate mode, dense app shell",
   ["Surface mode = Operate", "Scanability; tables; filters", "Quiet chrome", "Status sparingly"],
   "App shells and dashboards."),
  ("form-ux", "Form UX Craft", "workflow",
   "form design, checkout forms, input UX",
   ["Labels visible; errors inline", "Minimize fields", "Group decisions", "Keyboard + autofill friendly"],
   "Forms, checkout, settings."),
  ("nav-ia", "Navigation & IA", "workflow",
   "navigation design, information architecture, app nav",
   ["Clear current location", "Depth limits", "Mobile nav patterns", "Don’t hide primary actions"],
   "Nav and information architecture."),
  ("pricing-page", "Pricing Page Craft", "workflow",
   "pricing page design, plans comparison UI",
   ["Clear recommended plan", "Comparable columns", "Honest footnotes", "No dark patterns"],
   "Pricing and plan comparison."),
  ("marketing-sections", "Marketing Sections", "workflow",
   "marketing sections, features benefits social proof",
   ["One job per section", "Social proof credible", "Avoid icon-tile feature grids as default", "Alternate rhythm"],
   "Below-fold marketing composition."),
  ("accessible-ui", "Accessible UI Craft", "workflow",
   "accessible UI design, WCAG frontend, inclusive interface",
   ["Keyboard, SR, contrast, names", "Don’t rely on color alone", "Focus visible", "Pair references/accessibility-checklist.md"],
   "a11y-first visual work."),
  ("performance-ui", "Performance-Aware UI", "workflow",
   "performance UI, CLS free layout, fast frontend design",
   ["Reserve media space", "Avoid layout-animating props", "Lazy below-fold", "Pair performance checklist"],
   "Visual work that must stay fast."),
  ("design-tokens", "Token Engineering", "workflow",
   "design tokens, CSS variables theme, token architecture",
   ["Semantic tokens > raw hex in components", "Space/type/radius scales", "Theme maps", "Document in DESIGN.md"],
   "Creating or fixing token architecture."),
  ("component-gallery", "Component Gallery", "workflow",
   "component gallery, storybook UI inventory, primitive review",
   ["Inventory primitives/variants", "Gaps + inconsistencies", "Normalize before new features", "Export notes"],
   "Auditing a component library visually."),
  ("competitive-teardown", "Competitive Visual Teardown", "workflow",
   "competitor UI teardown, visual analysis, design research",
   ["Screenshot → patterns table", "What to steal / avoid", "Map to our PRODUCT.md", "No cloning trademarked assets"],
   "Learning from competitors before designing."),
  ("worlds-commit", "Direction Worlds / Commit", "workflow",
   "design worlds, commit to direction, dice creative directions",
   ["Propose 3 law-bound worlds", "Score vs PRODUCT.md", "Commit one; sandbox-delete losers only", "Update DESIGN.md"],
   "Escaping the model’s default aesthetic."),
  ("content-first-ui", "Content-First UI", "workflow",
   "content first design, real copy layouts, no lorem",
   ["Real/realistic copy from start", "Layouts that survive long German/labels", "No fake metrics", "ship-complete-ui gate"],
   "Preventing placeholder-driven layout lies."),
  ("iconography", "Iconography System", "workflow",
   "icon system, consistent icons, SVG iconography UI",
   ["One icon set; optical alignment", "No emoji as primary icons", "Drop rounded-square icon tiles above every H2", "Accessible titles"],
   "Icons and pictograms."),
  ("social-proof", "Social Proof Craft", "workflow",
   "testimonials design, logos cloud, social proof section",
   ["Credible quotes; real names/roles when allowed", "Logo walls quiet", "No fake star spam", "One proof job per section"],
   "Trust and proof sections."),
  ("error-pages", "Error & Empty Pages", "workflow",
   "404 page design, error pages, empty product states",
   ["Human, on-brand, useful next step", "No meme slop unless brand is meme", "Preserve nav", "Accessible"],
   "404/500/empty product pages."),
  ("settings-ux", "Settings UX", "workflow",
   "settings page design, preferences UI, account settings",
   ["Group by task", "Destructive actions isolated", "Immediate save vs explicit save — pick one", "Search when large"],
   "Settings and preferences."),
]

def write_skill(a: dict) -> None:
    name, title, family, triggers, bullets, when = (
        a[0], a[1], a[2], a[3], a[4], a[5]
    )
    d = OUT / name
    d.mkdir(parents=True, exist_ok=True)
    bullet_md = "\n".join(f"- {b}" for b in bullets)
    body = f"""---
name: {name}
description: >-
  {title} design approach. Use when the user wants {triggers}, or when
  using-design-skills routes to this approach.
---

# {title}

## Family
`{family}` · part of the ai-dev-guardrails design approach pack.

## Overview
Apply this approach on top of `anti-slop-frontend` + `safe-file-ops`. Do not invent a second design system when the repo already has tokens.

## When to use
{when}

## Direction rules
{bullet_md}

## Process
1. Load `PRODUCT.md` / `DESIGN.md` if present; else run `design-context` briefly.
2. State this approach name and one direction sentence.
3. Implement the slice; prefer inherit-over-invent.
4. Run `design/references/slop-catalog.md` (or `references/design-slop-catalog.md`).
5. Close with `ship-complete-ui` checks for the touched surface.

## Safety
Follow `safe-file-ops`. “Remove” means edit styles/structure in scoped files — never wipe the repo or delete unrelated directories.

## Verification
- [ ] Approach named in session
- [ ] Slop catalog clean on touched UI
- [ ] No destructive file ops
"""
    (d / "SKILL.md").write_text(body)


def write_index(names: list[tuple[str, str, str]]) -> None:
    by_fam: dict[str, list[tuple[str, str]]] = {}
    for name, title, fam in names:
        by_fam.setdefault(fam, []).append((name, title))
    lines = [
        "# Design approaches index",
        "",
        f"Generated library: **{len(names)}** installable approaches under `design/approaches/`.",
        "",
        "Router: [`../using-design-skills/SKILL.md`](../using-design-skills/SKILL.md) · Safety: [`../safe-file-ops/SKILL.md`](../safe-file-ops/SKILL.md) · [`../SAFETY.md`](../SAFETY.md)",
        "",
    ]
    for fam in ("style", "steer", "motion", "workflow"):
        lines.append(f"## {fam}")
        lines.append("")
        lines.append("| Skill | Title |")
        lines.append("|-------|-------|")
        for name, title in by_fam.get(fam, []):
            lines.append(f"| `{name}` | {title} |")
        lines.append("")
    (OUT / "README.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    meta = []
    for row in APPROACHES:
        write_skill(row)
        meta.append((row[0], row[1], row[2]))
    write_index(meta)
    print(f"Wrote {len(meta)} approaches → {OUT}")


if __name__ == "__main__":
    main()
