# utils — AI Development Rule Packs

Reusable rule packs (YAML + README) you paste into **Cursor / Claude / Copilot**
before generating code. Each pack encodes conventions, security concerns, and
specifications so AI-generated code stays clean, modular, secure, and consistent.

> Think of these as *linting rules for the AI*, expressed in plain language.

**Version:** 2.0.0 — aligned with the **AI Dev Rules Master Prompt Pack**
(Parts 1–4).

---

## Structure

```
utils/
├── client_side/          # Part 1 — Frontend (CS-01…CS-20)
│   ├── README.md
│   └── client-side-rules.yaml
├── server_side/          # Part 2 — Backend (SS-01…SS-20)
│   ├── README.md
│   └── server-side-rules.yaml
├── security/             # Part 3 — Security (SEC-01…SEC-20)
│   ├── README.md
│   └── security-rules.yaml
└── devops/               # Part 4 — CI/CD & deploy (OPS-01…OPS-20)
    ├── README.md
    ├── devops-rules.yaml
    └── pipelines/        # GitHub Actions starters (EC2, DO, Vercel, …)
```

Each category folder holds **one combined YAML** with all 20 rules, plus a
README index. DevOps also ships copy-pasteable workflow templates.

---

## How to use

1. Open the folder for the layer you're working on (e.g. `client_side/`).
2. Copy the whole YAML, or just the rule blocks you need, into your AI chat /
   Cursor rules / project system prompt.
3. Prefix with: *"Follow every rule in the YAML below while generating code."*

Merge packs as needed (e.g. `client_side` + `security` + `devops`).

For deploys, copy a file from [`devops/pipelines/`](devops/pipelines/) into your
app's `.github/workflows/` and fill in CI secrets.

---

## YAML schema

```yaml
meta:
  category: client_side
  title: Client-Side Rules
  version: 2.0.0
  updated: 2026-07-21
  rule_id_prefix: CS
  purpose: >
  usage: >
  stack: [React, Tailwind CSS]   # optional

rules:
  - id: CS-01
    title: Human-readable name
    status: complete
    severity: critical | high | medium | low
    summary: >
    rules: [ ... ]
    do: [ ... ]
    dont: [ ... ]
    example:
      bad: |
      good: |
    ai_directive: >
```

All four packs ship with every rule at `status: complete` (v2.0.0).

---

## Rule index

| Pack | Prefix | Count | Focus |
|------|--------|-------|-------|
| [client_side](client_side/README.md) | `CS` | 20 | Modularity, state, API, a11y, SEO/OG, motion, Tailwind, i18n, PWA |
| [server_side](server_side/README.md) | `SS` | 20 | Layers, REST, migrations, auth, jobs, caching, transactions |
| [security](security/README.md)       | `SEC` | 20 | Deps, secrets, injection, XSS/CSRF, CORS, containers, incidents |
| [devops](devops/README.md)           | `OPS` | 20 | CI/CD, EC2, DO, Vercel, cPanel, Railway, Render + templates |

---

## Contributing

- One rule = one entry under `rules:` in the category YAML.
- Keep each rule **atomic and testable** — an AI should be able to obey or
  violate it unambiguously.
- Fill `do` / `dont` with concrete, copy-pasteable guidance.
- Never commit real secrets, `.env`, or AI-workspace files (see `security/`).
