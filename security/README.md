# security — Security Rule Pack

![Security — shield, vault, and leak prevention for code and secrets](banner.jpg)

Rules for keeping code, credentials, and dependencies safe. Covers dependency
scanning, secrets hygiene, **confidential code & IP theft prevention**,
**AI-assistant mistake prevention**, injection, authn/authz, and deployment hardening.

Paste [`security-rules.yaml`](security-rules.yaml) into your AI tool for any project.

**Source:** AI Dev Rules Master Prompt Pack — Part 3 (v2.1.0)

## Index (20 rules · prefix `SEC`)

| ID | Rule | Severity |
|----|------|----------|
| SEC-01 | npm / dependency scanning | critical |
| SEC-02 | Secrets & credentials management | critical |
| SEC-03 | Environment variable rules | critical |
| SEC-04 | Never commit AI-workspace & assistant artifacts | critical |
| SEC-05 | Confidential code, IP theft & leak prevention | critical |
| SEC-06 | AI-assisted development — confidentiality & mistake prevention | critical |
| SEC-07 | Authentication & authorization | critical |
| SEC-08 | Input validation & sanitization | critical |
| SEC-09 | SQL / NoSQL injection prevention | critical |
| SEC-10 | Cross-site scripting (XSS) prevention | critical |
| SEC-11 | CSRF protection | high |
| SEC-12 | Rate limiting & DDoS protection | high |
| SEC-13 | CORS configuration | high |
| SEC-14 | Logging & audit trail | high |
| SEC-15 | Encryption & data at rest | critical |
| SEC-16 | Third-party API & integration security | high |
| SEC-17 | CI/CD pipeline security | critical |
| SEC-18 | Docker & container security | high |
| SEC-19 | Deployment security (multi-platform) | critical |
| SEC-20 | Incident response & security monitoring | high |

### Confidentiality & AI focus (start here)

| ID | What it stops |
|----|----------------|
| **SEC-04** | Committing `.cursor/`, `.claude/`, session logs, AI caches |
| **SEC-05** | Proprietary code leaks, IP theft, public repos, client-bundle exposure |
| **SEC-06** | Pasting secrets/code into AI chats, unreviewed AI output, mistaken AI commits |

### Mandatory local pre-push gate

Before every push, run tests, lint/typecheck, dependency auditing, secret scanning, client-exposure scanning, and the build where configured. Failed tests and high/critical findings block push; fix and rerun locally. Do not bypass with `--no-verify` except under documented emergency approval. Remote CI repeats—not replaces—this gate.

### Public client configuration is still exposed

`VITE_*` and `NEXT_PUBLIC_*` values are embedded in browser bundles. Analytics/project IDs may be public identifiers rather than credentials, but they must not be labeled “secured” or shipped as hardcoded production literals/fallback arrays. Use validated client-safe deployment env vars with placeholder-only examples; keep tokens, webhook secrets, and privileged vendor operations server-side.

> **Status:** All 20 rules are fully written (`status: complete`).
