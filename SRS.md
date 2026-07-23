# SRS.md — Software Requirements & Task Board

> AI assistants **must read this file first** for project context and work only from the open tasks below.  
> After finishing a task, **mark it complete here** and refresh status / version notes.  
> Extend tasks by **version** and/or **date** — do not invent scope outside this board unless the human asks.  
> Consuming projects: copy this file and replace description + tasks with your product’s board.

| Field | Value |
|-------|--------|
| **Project** | Ai-dev-guardrails |
| **Repository** | https://github.com/aftab-ahmad-khan-dev/ai-dev-guardrails |
| **Current version** | `2.3.1` |
| **Last updated** | `2026-07-23` |
| **Owner** | aftab-ahmad-khan-dev |

---

## Status legend

| Status | Meaning |
|--------|---------|
| `todo` | Not started |
| `in_progress` | Actively being worked |
| `blocked` | Waiting on dependency / decision |
| `done` | Completed — include completion date |
| `cancelled` | Won't do — note why |

---

## 1. Project description

**One-liner:** Reusable AI development **rules** and **skills** for Cursor, Claude, Copilot, and similar assistants.

**Problem:** Teams paste inconsistent AI instructions; projects need standards plus a living task board the AI must follow and update.

**Goals**
- Ship one-file (`Rules.md`) and category YAML packs for client, server, security, and DevOps.
- Treat delivery as a skill: read `SRS.md`, execute tasks, mark complete, extend by version/date.
- Bundle lifecycle skills (spec → ship) under `skills/` as part of this pack.
- Keep applicability matrix so unused layers are honestly `N/A`.

**Out of scope**
- Application business logic for end-user products (this repo is the guardrails pack itself).
- Hosting a SaaS dashboard for rule management (docs + files only).

**Stack (if known)**
- Frontend: N/A (documentation / rule packs)
- Backend: N/A
- Deploy: GitHub repo distribution

**Constraints**
- Keep `Rules.md` in sync with YAML packs.
- Preserve required upstream notice in `LICENSE` for adapted skill material.
- No secrets or AI workspace caches in git.

**Success criteria**
- AI system prompts can point at `SRS.md` + `Rules.md` + `skills/` and follow the board end-to-end.
- Each finished task leaves an updated status row in `SRS.md`.

---

## 2. Version roadmap

| Version | Target date | Theme | Status |
|---------|-------------|-------|--------|
| `2.1.0` | `2026-07-21` | Rules pack + repo URL | `done` |
| `2.2.0` | `2026-07-21` | Rules & skills + SRS-driven workflow | `done` |
| `2.3.0` | `2026-07-23` | Lifecycle skills pack (`skills/` + agents/commands/docs) | `done` |
| `2.3.1` | `2026-07-23` | README + Rules sync for installable skills pack | `done` |
| `2.4.0` | `TBD` | Optional Cursor rule/skill export helpers | `todo` |

---

## 3. Task board

### Rules for AI (mandatory)

1. **Read this file** before planning or coding.
2. Prefer the highest-priority open task in the **current version** section.
3. Set a task to `in_progress` when starting it (only one primary task at a time unless parallel work is requested).
4. When the task is finished: set status to `done`, fill **Completed**, add a short **Notes** line, and bump **Last updated** (and version notes if the version ships).
5. **Extend** this board when the human adds scope — new rows under the right **version** and/or a new **dated** section. Do not delete history; mark `cancelled` instead.
6. If `SRS.md` is missing in a consuming project, create it from this template before large work, then confirm with the human.

---

### Version `2.2.0` · started `2026-07-21`

| ID | Task | Priority | Status | Completed | Notes |
|----|------|----------|--------|-----------|-------|
| T-001 | Frame pack as rules **and** skills in Rules.md + README | high | `done` | 2026-07-21 | §0 SRS-01/SRS-02 added |
| T-002 | Add `SRS.md` template with description + version/date boards | high | `done` | 2026-07-21 | Template + this repo board |
| T-003 | Mandate: read SRS → complete task → update status | high | `done` | 2026-07-21 | Prompt + workflow in README |
| T-004 | Allow task extension by version and/or date | medium | `done` | 2026-07-21 | SRS-02 + dated backlog section |

---

### Version `2.3.0` · started `2026-07-23`

| ID | Task | Priority | Status | Completed | Notes |
|----|------|----------|--------|-----------|-------|
| T-020 | Add lifecycle skills: `skills/`, `agents/`, `references/`, `commands/`, `hooks/`, `docs/` | high | `done` | 2026-07-23 | Part of this pack under LICENSE |
| T-021 | Wire README / Rules / AGENTS / SRS to lifecycle skills | high | `done` | 2026-07-23 | LIFECYCLE-01 + Cursor sync docs |
| T-023 | Banners + READMEs for skills/agents/references/commands/hooks/docs | medium | `done` | 2026-07-23 | Match pack banner style |
| T-024 | Universal install: `npx skills add` + meta skill `ai-dev-guardrails` | high | `done` | 2026-07-23 | 25 skills discoverable locally |
| T-025 | Sync README + Rules.md for v2.3.1 enhancements | high | `done` | 2026-07-23 | Install section, lifecycle map, LIFECYCLE-02 |

---

### Version `2.4.0` · planned

| ID | Task | Priority | Status | Completed | Notes |
|----|------|----------|--------|-----------|-------|
| T-010 | Optional: export `.cursor/rules` / skill stubs from Rules.md | medium | `todo` | — | |
| T-011 | Optional: sample consuming-app SRS filled for a demo app | low | `todo` | — | |

---

### Ad-hoc / dated backlog (optional)

#### `2026-07-21`

| ID | Task | Priority | Status | Completed | Notes |
|----|------|----------|--------|-----------|-------|
| D-001 | Publish repo URL on Rules.md and README | high | `done` | 2026-07-21 | github.com/aftab-ahmad-khan-dev/ai-dev-guardrails |
| D-002 | Update LICENSE with project + repo attribution | medium | `done` | 2026-07-21 | MIT · Aftab Ahmad Khan · 2026 |
| D-003 | Add thematic banners to each folder README | medium | `done` | 2026-07-21 | client/server/security/devops/pipelines |
| D-004 | Require local test/security scans before push; flag exposed client tracking IDs | high | `done` | 2026-07-21 | Rules, README, client/server/security packs; YAML validated |
| D-005 | Require stats-section bottom border and credible, sourced metrics | medium | `done` | 2026-07-21 | Rules, root/client README, and client YAML updated |

---

## 4. Decisions & open questions

| Date | Decision / question | Status | Outcome |
|------|---------------------|--------|---------|
| `2026-07-21` | SRS is mandatory source of truth for tasks in consuming projects | `decided` | Documented in Rules §0 + README |
| `2026-07-23` | Lifecycle skills are part of this pack under project LICENSE | `decided` | `skills/` + related trees; upstream notice retained in LICENSE |

---

## 5. Change log (SRS only)

| Date | Version | Change |
|------|---------|--------|
| `2026-07-23` | `2.3.1` | README + Rules.md updated for installable skills, lifecycle map, LIFECYCLE-02 |
| `2026-07-23` | `2.3.0` | Folder banners; universal `npx skills` install; meta skill `ai-dev-guardrails` |
| `2026-07-23` | `2.3.0` | Added lifecycle skills pack (`skills/`, agents, references, commands, hooks, docs) |
| `2026-07-21` | `2.2.0` | Stats sections require bottom borders and credible, sourced metrics |
| `2026-07-21` | `2.2.0` | Mandatory local pre-push gate; public client tracking/config exposure rules |
| `2026-07-21` | `2.2.0` | LICENSE attribution; folder README banners |
| `2026-07-21` | `2.2.0` | SRS introduced; rules & skills workflow; v2.2.0 tasks completed |
| `2026-07-21` | `2.1.0` | Repo URL added to Rules.md and README |
