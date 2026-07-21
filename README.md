# Ai-dev-guardrails — AI Development Rules & Skills

Reusable **rules** and **skills** for **Cursor**, **Claude**, **Copilot**, and any AI coding assistant.  
Keep code clean, modular, secure, and consistent — without forcing rules that do not apply to your project.

**Repository:** https://github.com/aftab-ahmad-khan-dev/ai-dev-guardrails  
**Version:** 2.2.0

---

## Quick start

| Goal | Use this |
|------|----------|
| **Project description & tasks** | [`SRS.md`](SRS.md) — living requirements + version/date task board (AI reads & updates this) |
| **Everything in one file** | [`Rules.md`](Rules.md) — rules + SRS skills + naming + security scans |
| **Category YAML packs** | `client_side/`, `server_side/`, `security/`, `devops/` |
| **Deploy workflow starters** | [`devops/pipelines/`](devops/pipelines/) |

**Paste into your AI system prompt:**

```text
This pack is rules AND skills.
1. Read SRS.md first for project description and open tasks.
2. Follow Rules.md (applicable sections only — see README matrix).
3. After each task is done, mark it complete in SRS.md and refresh status / Last updated.
4. Extend SRS.md tasks by version and/or date when scope grows.
5. At the end, output the Compliance Report template from the README.
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
ai-dev-guardrails/
├── SRS.md                   # ← Project description + version/date task board (template)
├── Rules.md                 # ← Rules + SRS skills + all standards in one file
├── README.md                # ← This file (how to apply + report template)
├── client_side/             # CS-01…CS-20 (YAML)
├── server_side/             # SS-01…SS-20 (YAML)
├── security/                # SEC-01…SEC-20 (YAML)
└── devops/                  # OPS-01…OPS-20 (YAML) + pipelines/
```

YAML packs and `Rules.md` stay in sync. Prefer **`Rules.md`** for a single paste; use **folder YAML** when you only need one layer.  
Copy **`SRS.md`** into each consuming project and fill description + tasks — that file is the living backlog the AI must maintain.

---

## Rules vs skills

| | **Rules** | **Skills** |
|---|-----------|------------|
| **What** | Quality / security / delivery standards (CS-*, SS-*, SEC-*, OPS-*) | How the AI must run a project day-to-day |
| **Where** | `Rules.md` §§1–6 + YAML packs | `Rules.md` §0 (SRS-01, SRS-02) + this README |
| **Example** | “No file over 400 LOC” | “Read `SRS.md`, finish `T-003`, mark `done`” |

---

## SRS-driven delivery (mandatory skill)

**Source of truth for product detail and tasks:** [`SRS.md`](SRS.md)

1. **Read `SRS.md`** — project description, roadmap, and open tasks (by version and/or date).
2. **Pick a task** — prefer current-version `todo` / continue `in_progress`; announce the task ID.
3. **Apply rules** — only sections that match project type (matrix below).
4. **Mark complete** — set status `done`, fill **Completed** date + **Notes**, bump **Last updated**.
5. **Extend when needed** — add rows under a version section or a dated backlog; update roadmap when versions change.
6. **Report** — emit the compliance report after a reviewable slice.

Do not delete task history; use `cancelled` with a reason. If `SRS.md` is missing, scaffold from this template before large work.

---

## How AI should follow rules effectively

1. **Read `SRS.md`** — description, current version, open tasks.
2. **Read applicability** — Confirm project type (frontend / backend / full-stack / deploy target).
3. **Load relevant sections** — From `Rules.md` or merged YAML packs.
4. **Respect existing conventions** — Server rules extend the boilerplate; naming mirrors the codebase.
5. **Refuse violations** — No secrets in code, no `.cursor/` in commits, no proprietary logic in client bundles.
6. **Estimate file size** — Split before 400 LOC (CS-01 / SS-01).
7. **Update `SRS.md`** — mark finished tasks `done`; extend by version/date if scope grew.
8. **Run applicable scans** — See Rules §6 and report results.
9. **Emit compliance report** — After implementation or review (template below); include SRS task IDs in **Scope**.

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
║  SRS     : <task IDs e.g. T-002, T-003 — statuses updated in SRS.md> ║
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
- Confirm `SRS.md` was updated for every completed task ID listed under **SRS**.
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

## Rule & skill index

| Pack | File | Count | Focus |
|------|------|-------|-------|
| SRS board | [SRS.md](SRS.md) | template | Project description + version/date tasks |
| All | [Rules.md](Rules.md) | SRS skills + 80 + naming + scans | Rules & skills in one file |
| [client_side](client_side/README.md) | `CS` | 20 | Modularity, UX, a11y, SEO, Tailwind |
| [server_side](server_side/README.md) | `SS` | 20 | Layers, REST, auth, jobs, migrations |
| [security](security/README.md) | `SEC` | 20 | Confidentiality, AI safety, injection |
| [devops](devops/README.md) | `OPS` | 20 | CI/CD, platforms, pipelines |
| [pipelines](devops/pipelines/README.md) | Actions | 6 starters | Platform deploy workflow templates |

Each category folder README includes a thematic `banner.jpg` for GitHub browsing.

---

## License

This project is licensed under the [MIT License](LICENSE).  
Copyright (c) 2026 Aftab Ahmad Khan.

---

## Contributing

- Keep `Rules.md` in sync when YAML packs change.
- Keep `SRS.md` current when this pack’s own roadmap/tasks change.
- One rule = one testable directive; skills document mandatory workflows.
- Never commit real secrets, `.env`, or AI-workspace files (SEC-04, SEC-06).
