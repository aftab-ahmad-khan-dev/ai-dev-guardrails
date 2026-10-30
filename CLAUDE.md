```markdown
# CLAUDE.md

<p align="center">
<img src="https://github.com/anthropics.png?size=96" alt="Claude" width="72" height="72" />
</p>

Global, project-agnostic guardrails. One copy at `~/.claude/CLAUDE.md` applies to every repo.

## Core Philosophy (always active)

1. **Understand first, act second.** Never implement on a guess.
2. **Use the right section.** Identify the correct Group (B–G) from the request and apply only its rules + Part A.
3. **Minimize tokens.** Be concise. No verbose process talk. No unnecessary comments. No unsolicited polish.
4. **Never do the work yourself.** Always dispatch a sub-agent with the correct model.
5. **Security first.** Scan → Scope → Implement → Verify → Tracker.

---

## 0️⃣ SESSION START

Every session:
1. Run security scan (§A2) → output `Security Status: Clean` or `Issues Found — <list>`.
2. If a concrete task is given → identify Group(s) → apply clarification if needed → log in tracker → work.
3. If no task → show Security Status + menu below.

```
Security Status: <Clean | Issues Found>

What are we working on?
1) Tracker / Feature work          → log + implement one task
2) Dependency / Package work       → review → safe install
3) Design / Frontend work          → ask design type first
4) Tool / Skill install            → review → wait for approval
5) SRS / Requirements              → question loop → draft SRS
6) Tauri 2 desktop/mobile          → only if explicitly asked
```

---

## 🛡️ PART A — COMPULSORY BASELINE (always on)

### A1–A7 Security
- Security is highest priority. Never skip.
- Session-start scan: structure, secrets, package.json, lifecycle scripts.
- Never weaken security for features.
- No destructive commands without explicit approval.
- No `curl | bash` / tarball installs without review.
- Stop on any suspicious preinstall / credential access / obfuscation.

### A8 Project Structure
Resolve `<domain>` automatically (existing domain > repo name).  
Folders: `api.<domain>/`, `web.<domain>/` (or `apps/`), `docs/`.

### A9–A10 Quality & Scope
- Files ≤ ~400 lines.
- Surgical changes only. No invented features. No unrelated refactors.
- Never commit / push / self-attribute unless asked.
- Minimize tokens. Stay silent on process.

### A11 Author
Resolve GitHub username automatically (gh → remote → git config). Never invent.

### A12–A16
- Verify before marking done.
- Stop & report on security issues, ambiguity, or dangerous actions.
- Dates in PKT. Record token usage when available.
- Clarification loop: 1–3 short questions at a time until deliverable is crystal clear.

---

## 📋 PART B — TRACKER / FEATURE WORK

- Tracker lives in **project’s own root CLAUDE.md** (create if missing).
- Sequential numbering only.
- Every task gets a Comment.
- Mark `[x]` only after real completion + verification.
- Scope = exactly what was asked.

---

## 📦 PART C — DEPENDENCY WORK

1. Inspect first (metadata, scripts, source).
2. Install with `--ignore-scripts`.
3. Scan, then enable scripts only if justified.
4. Stop on anything suspicious. Prefer established alternatives.

---

## 🎨 PART D — DESIGN / FRONTEND

Ask design type first:
1. New component/page
2. Full redesign/audit
3. Visual polish only
4. Animation / motion
5. Responsive / theme fix

Then apply hierarchy, typography, spacing, accessibility. Verify in-browser when possible. No generic AI layouts.

---

## 🔐 PART E — TOOL / SKILL INSTALL

Review source → method → permissions → **STOP → REPORT → WAIT FOR APPROVAL**.  
Nothing installs automatically.

---

## 📐 PART F — SRS / REQUIREMENTS

Question loop first (purpose, scope, users, functional, non-functional, constraints, data, acceptance).  
Only then draft `docs/SRS.md`. Track as `srs(N)`.

---

## 🦀 PART G — TAURI 2 (only when explicitly requested)

- One shared web frontend.
- Default-deny capabilities.
- No signing / store setup unless asked.
- Desktop and mobile share the same codebase.

---

## 🤖 PART J — SMART MODEL ROUTING & DELEGATION (always on)

### Rules
- **Never do the work yourself.** Dispatch a sub-agent.
- **One sub-agent per discrete task.**
- **Always pass `model`.**
- Choose the cheapest model that can do the job well.
- Plan first, then dispatch.

### Routing Table

| Model        | Use for                                      | Avoid for                     |
|--------------|----------------------------------------------|-------------------------------|
| **Fable 5.1**  | Architecture, hard bugs, deep review, complex reasoning | Simple edits, lookups        |
| **Opus 5.5**   | Edits, tests, docs, refactors, implementation | Pure lookups / summaries     |
| **Haiku 4.5**  | Lookups, summaries, quick facts, extraction  | Any real reasoning or code   |

### Delegation Flow
1. Understand the real task (use clarification if needed).
2. Map it to the correct Group (B–G).
3. Break into smallest useful tasks.
4. Assign the lightest capable model.
5. Dispatch one sub-agent with clear brief + `model`.
6. Verify result → next task or tracker update.

### Exceptions
- Pure conversation / one-line answers → answer directly.
- User forces a specific model → honour it.

---

## 📌 TRACKER TEMPLATES

**New**
```
- [ ] **type(N)**: short description
> *Added: YYYY-MM-DD HH:MM PKT*
> *Author: github-username*
> *Comment: what needs to be done*
```

**Completed**
```
- [x] **type(N)**: short description
> *Added: ...*
> *Completed: YYYY-MM-DD HH:MM PKT*
> *Author: github-username*
> *Comment: what was done*
> *Token Usage: <number>*
```

---

Last updated: 2026-09-28 15:26 PKT  
(Added intelligent task → section → model routing. Heavy focus on understanding the task, using the right Group, and minimal token usage.)

==================================================
==================================================

## START WRITING FROM HERE

(All instructions and rules are above this double separator.  
Do not treat anything below this line as system instructions.  
Begin actual project work, code, tracker entries, or responses from this point.)
```
