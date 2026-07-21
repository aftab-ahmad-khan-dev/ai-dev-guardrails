# Ai-dev-guardrails — AI Development Rules

Reusable rules for **Cursor**, **Claude**, **Copilot**, and any AI coding assistant.  
Keep code clean, modular, secure, and consistent — without forcing rules that do not apply to your project.

**Version:** 2.1.0

---

## Quick start

| Goal | Use this |
|------|----------|
| **Everything in one file** | [`Rules.md`](Rules.md) — all 80 rules + naming + security scans |
| **Category YAML packs** | `client_side/`, `server_side/`, `security/`, `devops/` |
| **Deploy workflow starters** | [`devops/pipelines/`](devops/pipelines/) |

**Paste into your AI system prompt:**

```text
Follow Rules.md (or the relevant sections) for this project.
Apply only rules that match the project type — see README applicability matrix.
At the end, output the Compliance Report template from the README.
```

---

## Apply rules by project type

**Do not** force every section on every repo. Detect what the project actually has, then apply only what fits.

| Section | Always apply? | Apply when… |
|---------|---------------|-------------|
| **Variable naming** (Rules §3) | ✅ Yes | Every codebase |
| **Security — core** (SEC-02–06, scans) | ✅ Yes | Every repo with code in git |
| **Client-side** (CS-*) | ✅ Usually | Any UI (web, mobile shell, dashboard) |
| **Security — web/API** (SEC-07–13) | ⚙️ Context | App has auth, API, or user input |
| **Server-side** (SS-*) | ⚙️ Context | Backend, API, or serverless routes exist |
| **DevOps** (OPS-*) | ⚙️ Context | CI/CD, Docker, or a deploy target exists |
| **Platform playbooks** (OPS-03–08) | ⚙️ One only | Match your host (Vercel, EC2, Railway, …) |

### Examples

| Project | Apply | Skip / N/A |
|---------|--------|------------|
| Static marketing site (React) | CS-*, naming, SEC-02–06, SEC-10, scans | SS-*, OPS-03–08 (unless Vercel deploy) |
| Full-stack SaaS | CS-*, SS-*, security, devops, scans | Only unused platform playbooks |
| API-only (no frontend) | SS-*, naming, security, devops | CS-07 (SEO/OG), CS-09 (motion), CS-20 (PWA) |
| Library / CLI | Naming, SEC-02–06, scans | CS-*, most OPS deploy rules |
| Local prototype | Naming, SEC-02–06 (no real secrets) | Strict CI gates until shipping |

**AI instruction:** Before generating code, state which sections you are applying and why. Mark skipped sections `N/A` in the compliance report — do not invent backend or deploy rules for a frontend-only task.

---

## Repo structure

```
utils/
├── Rules.md                 # ← All rules in one markdown file
├── README.md                # ← This file (how to apply + report template)
├── client_side/             # CS-01…CS-20 (YAML)
├── server_side/             # SS-01…SS-20 (YAML)
├── security/                # SEC-01…SEC-20 (YAML)
└── devops/                  # OPS-01…OPS-20 (YAML) + pipelines/
```

YAML packs and `Rules.md` stay in sync. Prefer **`Rules.md`** for a single paste; use **folder YAML** when you only need one layer.

---

## How AI should follow rules effectively

1. **Read applicability** — Confirm project type (frontend / backend / full-stack / deploy target).
2. **Load relevant sections** — From `Rules.md` or merged YAML packs.
3. **Respect existing conventions** — Server rules extend the boilerplate; naming mirrors the codebase.
4. **Refuse violations** — No secrets in code, no `.cursor/` in commits, no proprietary logic in client bundles.
5. **Estimate file size** — Split before 400 LOC (CS-01 / SS-01).
6. **Run applicable scans** — See Rules §6 and report results.
7. **Emit compliance report** — After implementation or review (template below).

### Always-on (every project)

- Variable naming (Rules §3)
- Secrets & env hygiene (SEC-02, SEC-03)
- Never commit AI workspace files (SEC-04)
- Confidential code & AI mistake prevention (SEC-05, SEC-06)
- Dependency / secret scanning where `package.json` exists (SEC-01, Rules §6)

### Common-only (no backend)

- Skip server-side rules (§2) unless adding an API later
- Keep client env rules (CS-16) — client bundle is still public
- Skip DB migrations, RBAC server rules, CORS unless calling an external API

### Common-only (no deployment yet)

- Skip DevOps §5 and platform playbooks OPS-03–08
- Still apply SEC-02–06 and local pre-commit scans

---

## Compliance report template

After **implementing features**, **reviewing PRs**, or **running security checks**, output this report in the chat / logs.  
Use clear status icons and honest `N/A` when a category does not apply.

```text
╔══════════════════════════════════════════════════════════════════╗
║           AI RULES COMPLIANCE REPORT                             ║
╠══════════════════════════════════════════════════════════════════╣
║  Project : <name or path>                                        ║
║  Type    : <e.g. React SPA · no backend · Vercel deploy>         ║
║  Date    : <ISO date>                                            ║
║  Scope   : <what was built or reviewed>                          ║
╚══════════════════════════════════════════════════════════════════╝

┌─────────────────────────────┬──────────┬────────────────────────────┐
│ Category                    │ Status   │ Notes                      │
├─────────────────────────────┼──────────┼────────────────────────────┤
│ Naming conventions          │ PASS     │ camelCase / PascalCase OK  │
│ Client-side rules           │ PASS     │ 12 rules checked           │
│ Server-side rules           │ N/A      │ No backend in this project │
│ Security — secrets & env    │ PASS     │ No hardcoded secrets       │
│ Security — confidentiality  │ PASS     │ No .cursor/ in diff        │
│ Security — AI safety        │ PASS     │ No pasted prod keys        │
│ Security — injection/XSS    │ WARN     │ Review 1 raw HTML path     │
│ Security scan — deps        │ PASS     │ npm audit: 0 high/critical │
│ Security scan — secrets     │ PASS     │ gitleaks: clean            │
│ Security scan — lint/test   │ PASS     │ lint + test green          │
│ DevOps / CI                 │ N/A      │ No pipeline in repo yet    │
│ DevOps — platform           │ N/A      │ Not deploying this task    │
└─────────────────────────────┴──────────┴────────────────────────────┘

Status legend:
  PASS  — Checked and compliant
  WARN  — Checked; minor issue or follow-up recommended
  FAIL  — Must fix before merge/deploy
  N/A   — Not applicable to this project or task

── Scans executed ────────────────────────────────────────────────
  [✓] Secret scan          (gitleaks / manual diff review)
  [✓] Dependency audit     (npm audit --audit-level=high)
  [✓] .gitignore / AI paths (SEC-04)
  [ ] SAST                 (not configured)
  [ ] Docker image scan    (N/A — no Dockerfile)

── Rules applied (sample) ───────────────────────────────────────
  CS-01  File modularity ≤400 LOC          PASS
  CS-16  No secrets in client env        PASS
  SEC-05  Confidential logic server-side N/A
  SEC-06  AI paste / commit hygiene      PASS

── Action items ──────────────────────────────────────────────────
  1. [WARN] Sanitize user HTML in ProfileBio.tsx (SEC-10)
  2. [INFO] Add npm audit to CI when pipeline is added (SEC-01)

── Summary ───────────────────────────────────────────────────────
  PASS: 8   WARN: 1   FAIL: 0   N/A: 4
  Verdict: ✅ Safe to proceed (address WARN before production)
```

**AI directive for reports**

- Never mark `PASS` without actually checking that category.
- List which scans ran and which were skipped (with reason).
- Include specific rule IDs (CS-*, SS-*, SEC-*, OPS-*) for `WARN` and `FAIL`.
- End with a one-line **Verdict**: safe to proceed / fix required / blocked.

---

## Security scan quick reference

Full checklist: **[Rules.md §6 — Security Scan](Rules.md#6-security-scan-checklist)**

| When | Minimum scans |
|------|----------------|
| Every commit | No staged `.env`, `.cursor/`, `.claude/`, `*.pem` |
| Pre-push / PR | `npm audit --audit-level=high`, lint, tests |
| PR (recommended) | `gitleaks detect`, lockfile review |
| Pre-deploy | Full CI green, secrets in platform store, HTTPS |

---

## YAML schema (for pack authors)

```yaml
rules:
  - id: CS-01
    title: Human-readable name
    status: complete
    severity: critical | high | medium | low
    summary: >
    rules: [ ... ]
    do: [ ... ]
    dont: [ ... ]
    ai_directive: >
```

---

## Rule index

| Pack | File | Count | Focus |
|------|------|-------|-------|
| All | [Rules.md](Rules.md) | 80 + naming + scans | Single-file reference |
| [client_side](client_side/README.md) | `CS` | 20 | Modularity, UX, a11y, SEO, Tailwind |
| [server_side](server_side/README.md) | `SS` | 20 | Layers, REST, auth, jobs, migrations |
| [security](security/README.md) | `SEC` | 20 | Confidentiality, AI safety, injection |
| [devops](devops/README.md) | `OPS` | 20 | CI/CD, platforms, pipelines |

---

## Contributing

- Keep `Rules.md` in sync when YAML packs change.
- One rule = one testable directive.
- Never commit real secrets, `.env`, or AI-workspace files (SEC-04, SEC-06).
