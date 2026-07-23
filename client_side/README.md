# client_side — Frontend Rule Pack

![Client Side — modular React UI, responsive layouts, motion](banner.jpg)

Rules for building **clean, modular, scalable React + Tailwind** frontends with a
non-AI, hand-crafted UI/UX feel. Paste [`client-side-rules.yaml`](client-side-rules.yaml)
into your AI tool before generating UI code.

**Assumed stack:** React · Tailwind CSS · Framer Motion · GSAP · React Helmet

**Source:** AI Dev Rules Master Prompt Pack — Part 1 (v2.0.0)

## Index (20 rules · prefix `CS`)

| ID | Rule | Severity |
|----|------|----------|
| CS-01 | Code organization & componentization (≤400 LOC) | high |
| CS-02 | State management | high |
| CS-03 | API integration & data fetching | high |
| CS-04 | Error handling & logging | high |
| CS-05 | Performance optimization | high |
| CS-06 | Accessibility (a11y) | high |
| CS-07 | SEO, meta tags & OG images | high |
| CS-08 | Responsive design & mobile-first | high |
| CS-09 | Animation & motion (Framer Motion / GSAP) | medium |
| CS-10 | Form handling & validation | medium |
| CS-11 | Testing standards | medium |
| CS-12 | Styling & design system (Tailwind) | high |
| CS-13 | Routing & navigation | medium |
| CS-14 | Internationalization (i18n) | medium |
| CS-15 | Asset & image optimization | medium |
| CS-16 | Environment configuration | critical |
| CS-17 | Code review & git workflow | medium |
| CS-18 | Component library & design tokens | high |
| CS-19 | Analytics & tracking | medium |
| CS-20 | PWA & offline support | medium |

## Required pre-push and client-exposure checks

- Before every push, run the applicable local tests, lint/typecheck, dependency audit, secret scan, client-exposure scan, and build. Fix failures before pushing; CI repeats the gate.
- `VITE_*` and `NEXT_PUBLIC_*` are public browser values—not secured secrets.
- Never hardcode production Meta Pixel, Clarity, GA, Sentry, or similar IDs as literals, fallback strings, or arrays. Use validated client-safe deployment env vars with placeholder-only examples.
- Keep actual credentials and privileged vendor operations server-side; consent-gate all tracking.

## Stats-section visual and content rule

- Add a visible, full-width bottom border/divider to stats sections so they do not merge into the next section.
- Use only realistic metrics supported by product data or an approved source. Never invent inflated claims such as `900+ Integrations`, `99.99% Uptime`, `200+ Currencies`, or `<3 wks Typical go-live`.
- If verified figures are unavailable, use clearly labeled placeholders or remove the stats section.

> **Status:** All 20 rules are fully written (`status: complete`).
