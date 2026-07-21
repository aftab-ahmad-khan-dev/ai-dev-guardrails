# security — Security Rule Pack

Rules for keeping code, credentials, and dependencies safe. Covers dependency
scanning, secrets hygiene, code-leak prevention, AI-workspace hygiene, injection,
authn/authz, and deployment hardening.

Paste [`security-rules.yaml`](security-rules.yaml) into your AI tool for any project.

**Source:** AI Dev Rules Master Prompt Pack — Part 3 (v2.0.0)

## Index (20 rules · prefix `SEC`)

| ID | Rule | Severity |
|----|------|----------|
| SEC-01 | npm / dependency scanning | critical |
| SEC-02 | Secrets & credentials management | critical |
| SEC-03 | Environment variable rules | critical |
| SEC-04 | .gitignore & never-commit rules | high |
| SEC-05 | Code & data leak prevention | critical |
| SEC-06 | Variable naming conventions | medium |
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

> **Status:** All 20 rules are fully written (`status: complete`).
