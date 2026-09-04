# CLAUDE.md

**Repo:** https://github.com/aftab-ahmad-khan-dev/ai-dev-guardrails

## How Claude Code loads this file

Claude Code auto-reads `CLAUDE.md` at the repo root on every session — no setup needed.

---

# 🗂️ TABLE OF CONTENTS

| Part | Section | Type |
|---|---|---|
| 0 | Session-Start Menu | runs every session |
| A | Compulsory Baseline (Security, Project Structure, Code Quality, Clarification Loop, General Rules) | **always applied — never asked** |
| B | Group 1 — Tracker / Feature Work | asked |
| C | Group 2 — Dependency / Package Work | asked |
| D | Group 3 — Design / Frontend Work | asked (+ design-type sub-question) |
| E | Group 4 — Tool / Skill Installation | asked |
| F | Group 5 — SRS / Requirements Documentation Work | asked (+ requirement-gathering loop) |
| G | Tracker Entry Templates | reference |

---

# 0️⃣ SESSION-START MENU

**Every session runs Part A silently first — no exceptions, no asking.** It is not optional and it is not a menu item.

1. Run the Part A security scan (§A2). Output `Security Status: Clean` or `Security Status: Issues Found — <brief list>`.
2. If a concrete task was already given in the user's message, skip the menu — identify which Group(s) below it belongs to, apply the Part A15 clarification loop if anything is underspecified, log it in the tracker, then apply that Group's bundled rules.
3. If no concrete task was given, show the Security Status and present:

```text
Security Status: <Clean | Issues Found — brief list>

What are we working on?

  1) Tracker work (Group 1 — Part B)
     → Logs a feat/fix/security/update/issue in the tracker, numbers it,
       implements only that, marks it complete with a Comment.

  2) Dependency / package work (Group 2 — Part C)
     → Reviews the package before touching it (metadata, lifecycle scripts,
       source), installs with scripts disabled first, then runs security
       scans. Nothing gets installed blind.

  3) Design / frontend work (Group 3 — Part D)
     → Asks what kind of design task it is first, then builds/edits UI
       following the design standard (hierarchy, typography, spacing,
       accessibility) and verifies it in-browser afterward.

  4) Tool / skill install (Group 4 — Part E)
     → Reviews the tool's source, install method, and permissions, then
       stops and reports back for your explicit approval before installing.

  5) SRS / requirements documentation (Group 5 — Part F)
     → Asks a series of short question rounds to understand the project
       fully, then drafts a structured SRS document and tracks it.
```

Each option's description is what actually happens once picked — not just a label. Rules:

* Whichever Group is picked, **all of its bundled sub-rules apply together** — the user doesn't need to separately approve each sub-rule once a Group is chosen. Same logic for every group.
* Part A (baseline) applies underneath every group, always, with no exception and no re-confirmation needed.
* A request can span more than one Group (e.g. "spec out and then build a new dashboard" = Group 5 then Group 3, or "add a new UI library and build a component with it" = Group 2 then Group 3) — call that out and sequence them.
* Picking **Group 3 (Design/Frontend)** triggers the design-type sub-question in §D0 first.
* Picking **Group 5 (SRS)** triggers the requirement-gathering question loop in §F0 first — this is the same engine as §A15, applied specifically to full requirements capture.

---

# 🛡️ PART A — COMPULSORY BASELINE

**Everything in Part A is always active. It is never a menu choice, never skipped, and applies regardless of which Group is selected.**

## A1. Security-First Priority

Security is the highest priority and must be checked before any action: before implementing a feature, fixing an issue, installing/updating a dependency, executing unfamiliar code, or making any project change. Never skip the security gate.

## A2. Session-Start Security Scan

On every new session, before touching the tracker:

1. Inspect top-level project structure (skip `node_modules`, `.git`, build artifacts).
2. Search for secrets, credentials, API keys, access tokens, suspicious environment variables.
3. Inspect `package.json`, lockfiles, relevant configuration.
4. Run available security scanners when already installed/available.
5. Review dependency lifecycle scripts, suspicious packages, obvious SAST issues, suspicious entry-point behavior.
6. Output `Security Status: Clean` or `Security Status: Issues Found — <brief list>`.

Never treat "no task yet" as permission to explore unrelated project areas.

## A3. Security Change Rule

Any task involving authentication, authorization, credentials, tokens, cookies, sessions, APIs, dependencies, packages, databases, file uploads, command execution, filesystem access, deployment, environment variables, or external services requires a security review. Never weaken an existing security control merely to make a feature work. If a significant concern appears: **STOP → REPORT → ASK FOR DIRECTION.**

## A4. Dangerous Command Rule

Do not execute destructive or system-wide commands unless explicitly required and explicitly approved: `sudo`, `rm -rf`, `mkfs`, `dd`, `diskutil eraseDisk`, `git reset --hard`, `git clean -fd`, `git push --force`. If one appears necessary: stop, explain what it does, ask for explicit approval, never assume approval.

## A5. Network / External Resource Rule

Never blindly execute `curl <url> | bash` or `wget <url> | sh`. This also covers `npm install` pointed directly at a GitHub release tarball URL instead of the registry — review contents first before installing, regardless of source popularity. Review any external resource before execution.

## A6. Malicious Code Vigilance

Regardless of which Group is active, if at any point you encounter a suspicious `preinstall`/`install`/`postinstall`/`prepare` script, shell execution, remote downloads, data exfiltration, credential/env harvesting, SSH key or browser data access, filesystem manipulation, obfuscated code, suspicious binaries, persistence mechanisms, crypto-mining behavior, dependency confusion, or typosquatting: **stop, report the finding, do not execute it, recommend removal/replacement, continue only after the concern is addressed.**

## A7. Tool / Skill Trust Rule

External skills, plugins, CLIs, scripts, and dev tools (including everything listed in §D1) are never automatically trusted, regardless of star count or popularity. Before installing anything: identify the official source, review install method/dependencies/lifecycle scripts, check for file modification / remote code execution / elevated permissions / credential access, prefer official docs. **STOP → REVIEW → REPORT → WAIT FOR APPROVAL** unless the user has explicitly approved that specific installation. Being mentioned in this file is never itself authorization to install.

## A8. Project Structure

Expected root folders:

```text
api.domainname.com/   — backend/API functionality
web.domainname.com/   — frontend/client functionality
docs/                 — SRS and other requirements documentation (see Part F)
```

Maintain clear separation between API, client, and docs.

## A9. Code Quality

* No source file should exceed ~400 lines.
* Maintain a clean folder structure; meaningful variable/function/class names; avoid cryptic abbreviations.
* Maintain separation of concerns; prefer reusable components; avoid unnecessary abstraction; avoid unrelated refactoring.

## A10. General Working Rules

* Never commit yourself — no `git commit`/`git push` unless explicitly asked.
* Never add Claude/ChatGPT/AI/assistant as an author, `Co-authored-by: Claude`, `Generated by Claude`, or any self-attribution.
* Focus strictly on the requested functionality — no invented features, unsolicited polish, unrelated refactoring, or scope expansion.
* Prefer surgical, minimal changes; touch only files required for the task.
* No tests, documentation, or configuration added unless explicitly requested (an explicitly requested SRS under Group 5 counts as requested documentation).
* Never break or regress previously completed features.
* Minimize token usage; avoid unnecessary comments; avoid verbose summaries; stay silent on process when possible.

## A11. GitHub Author Rule

`Author` = verified GitHub username only. Never a real name (unless it's also the verified username), never an email, never Claude/Cursor/ChatGPT/AI, never invented. If it can't be verified, use `Author: <GitHub username required>`. Never assume the repo owner is automatically the author.

## A12. Regression Rule

Before completing any task: verify requested functionality, review changed files, check for accidental changes, confirm previously completed functionality and security requirements remain intact.

## A13. Stop Conditions

Stop and report instead of continuing if: a serious security issue is discovered; a dependency appears malicious/highly suspicious; a command could damage the OS or delete significant project data; credentials are discovered; a required dependency can't be safely reviewed; the requested change conflicts with security controls; the task is genuinely ambiguous after the clarification loop in §A15; the task needs access outside the repo without explicit authorization.

When stopped: explain the issue concisely, state what was discovered, state what was not changed, state what decision/approval is required.

## A14. Tracker Date/Time & Token Usage

Use Pakistan Standard Time: `YYYY-MM-DD HH:MM PKT` (actual current date/time). Record token usage in completed tracker entries when available (e.g. `> *Token Usage: 12,450*`) and update the daily total when supported.

## A15. Clarification-Until-Understood Rule (Compulsory)

**Do not start implementing on a guess.** Before real work begins on any Group, Claude must know, concretely:

* what the deliverable is,
* what "done" looks like,
* and which constraints (tech, scope, security, timeline) apply.

If any of that is missing or ambiguous:

1. Ask a short, focused round of clarifying questions — 1 to 3 at a time, not a giant intake form.
2. Use the user's answers to narrow the remaining unknowns.
3. Ask another short round if unknowns remain. Repeat — do not cap this at one round if the task genuinely isn't clear yet.
4. Stop asking once you can state back, in one or two sentences, exactly what will be built/changed/produced and how you'll know it's correct. If the user confirms or doesn't correct that summary, proceed.
5. If the user explicitly says "just use your judgment" or gives a fully-specified request up front, skip straight to work — this rule exists to prevent guessing, not to force ceremony on clear requests.

**Whenever a choice is presented to the user anywhere in this workflow** (the Part 0 menu, §D0 design-type question, or any other selectable options), each option must show a short one-line description of what actually happens if it's picked — not just a bare label. A label like "Dependency work" tells the user nothing; "reviews the package before touching it, installs with scripts disabled first" tells them what they're choosing.

This is the same engine used by §F0 for SRS work, just scoped there to full project/feature requirements instead of a single task.

## A16. Final Security Principle

> **Scan first. Trust later. Change minimally. Execute only what is necessary.**
> Never install first and investigate later. Never execute unknown code to determine whether it's safe. Never sacrifice security for convenience. Never modify unrelated functionality. Never break previously completed work.
> **Security → Scope → Implementation → Verification → Tracker Update**

---

# 📋 PART B — GROUP 1: TRACKER / FEATURE WORK

Selecting this Group bundles the following — all apply together, no separate confirmation needed:

## B1. Universal Task Comment Rule

Every tracked task (`feat`, `fix`, `security`, `update`, `issue`, `feat/fix`, `srs`, or any other tracked work) needs a concise **Comment** directly below it — factual, concise, reflects actual status, never claims unperformed work.

## B2. Tracker Workflow

1. Parse the request; determine type; normalize it.
2. Find the highest existing task number; assign `N + 1`.
3. Add the task unchecked; immediately add its Comment.
4. Confirm which other Group(s) this task also touches (e.g. a feature needing a new package pulls in Group 2 as well; a feature needing a spec first pulls in Group 5) and apply those bundles too.
5. Implement only the requested work.
6. Update the Comment when necessary; mark `[x]` only after successful completion.
7. Add completion date/time, verified GitHub username, and token usage when available.
8. Update `Last updated`.

## B3. Task Numbering

Sequential only. Never reuse, never renumber completed tasks, never delete completed tracker history. New task = highest existing `N + 1`.

## B4. Task Scope

The current request defines the scope. Do not automatically redesign unrelated UI, refactor unrelated code, upgrade unrelated packages, change architecture, rename unrelated files, rewrite working components, add unrelated features/documentation/tests/configuration — unless explicitly requested or strictly required.

(Entry templates are in Part G.)

---

# 📦 PART C — GROUP 2: DEPENDENCY / PACKAGE WORK

Selecting this Group bundles the following — all apply together:

## C1. Pre-Install Security Gate

**Phase 1 — Inspect before installation:** review `package.json`, `package-lock.json`, `npm-shrinkwrap.json`, `yarn.lock`, `pnpm-lock.yaml`, `.npmrc`, workspace config. Determine direct/transitive dependencies, version ranges, sources, Git/tarball dependencies, registry config, optional/peer dependencies, lifecycle scripts. Do not install anything yet.

**Phase 2 — Static review:** review package metadata, lifecycle scripts, known security info, provenance; look for suspicious filesystem/network access, obfuscation, unexpected binaries, behavior unrelated to stated purpose; check if an established alternative exists. Treat installs pointing at GitHub release tarball URLs (rather than the registry) as extra-scrutiny cases, same risk class as `curl | bash`, regardless of star count. A large star/download count or marketing claim is not verification — check whether benchmark/feature-completeness claims are independently corroborated, especially for agentic tooling with broad tool/filesystem/network access.

**Phase 3 — Safe installation:** prefer `npm ci --ignore-scripts` or `npm install --ignore-scripts`, then run security checks. Only enable lifecycle scripts when genuinely required, the dependency has been reviewed, behavior is understood, and it's appropriate for the task.

**Critical rule:** if a dependency shows typosquatting, dependency confusion, unexpected lifecycle scripts/network/filesystem access, obfuscation, credential/env access, remote downloads, suspicious binaries, crypto-mining behavior, unrelated functionality, or direct tarball installs bypassing the registry: **STOP → REPORT → DO NOT INSTALL → RECOMMEND A SAFE ALTERNATIVE.**

## C2. Dependency & Vulnerability Scanners

Use when already available/relevant: `npm audit --audit-level=moderate`, NodeSecure (`@nodesecure/scanner`), Retire.js, SAST tools (nodejsscan, Semgrep, ESLint security plugins / `eslint-plugin-security`). Do not install a scanner merely to perform a scan if that itself would violate the dependency gate.

## C3. Dependency Change Rule

Identify why it's needed → check if an existing package already covers it → review the proposed package's version/requirements/lifecycle scripts/security → prefer established alternatives → install with scripts disabled initially → run security checks → enable lifecycle scripts only when necessary and justified. Never add a dependency simply because it's convenient.

## C4. Testing Rule

Do not add tests unless explicitly requested. Prefer existing tests; don't modify unrelated tests; don't disable tests to hide failures; report failures honestly. Never execute potentially unsafe dependency code merely to obtain a test result.

---

# 🎨 PART D — GROUP 3: DESIGN / FRONTEND WORK

Selecting this Group first asks the design-type sub-question, then bundles the rest — all apply together.

## D0. Design-Type Sub-Question (ask before writing any code)

```text
What kind of design work is this?

  1) New component / page from scratch
     → Builds fresh UI using Taste Skill (anti-generic layout) plus any
       image/design references you provide.

  2) Full redesign or audit of existing UI
     → Audits the current design system first (Impeccable), then applies
       Taste Skill direction only where the audit found real gaps.

  3) Visual polish only — typography, spacing, color, accessibility
     → Impeccable-only pass: tightens existing UI without restructuring
       layout or components.

  4) Animation / motion / micro-interactions
     → Applies Emil Kowalski's design-engineering principles — purposeful,
       performant motion, respecting reduced-motion preferences.

  5) Responsive fix / dark-light mode / theming
     → Applies Frontend Conventions (§D4) plus Impeccable's accessibility/
       contrast checks; no unrelated visual changes.
```

Each option's description is what Claude will actually do, not just a category label. Claude still applies the rest of Part D regardless of the answer, but leads with the matched approach above.

Playwright and/or Reticle verification (§D1.5, §D1.6) apply after implementation no matter which type was picked, when either is already available in the project.

## D1. AI Design & Development Skills (Reference Tools)

These are references and workflow tools, not automatic installation authorization — §A7/§E2 still governs every one of them.

**1. Taste Skill** — https://www.tasteskill.dev/ (docs: /docs, guide: /guide) · GitHub: https://github.com/Leonxlnx/taste-skill. Reduces generic AI-frontend patterns; layout, typography, spacing, motion, design-system thinking. Audit-first on existing projects; don't blindly replace an existing design system.

**2. Impeccable** — https://impeccable.style/. UI audits, visual polish, typography, spacing, color systems, accessibility, responsive design, design-system consistency. On existing interfaces: inspect current system → identify weak areas → preserve working conventions → targeted improvements → verify. Don't redesign unrelated UI.

**3. Emil Kowalski — Design Engineering** — https://emilkowal.ski/skill · GitHub: https://github.com/emilkowalski/skills (`emil-design-eng`, `review-animations`, `improve-animations`, `find-animation-opportunities`, etc). Animation, micro-interactions, transitions, hover states, motion design. Animations must serve a purpose, stay performant, avoid excessive motion, respect reduced-motion preferences, use appropriate easing, avoid unnecessary animation libraries.

**4. ImageToCode** — use image/design references when the user provides them, for layout/spacing/typography/hierarchy/component structure/responsive behavior. Don't blindly reproduce implementation details; preserve the project's architecture.

**5. Playwright CLI** — https://playwright.dev/. Use when already available: open the app, verify pages/navigation, test responsive layouts, capture screenshots, spot visual regressions, inspect console errors, verify interactions/forms/flows. Don't install automatically.

**6. Reticle** — GitHub: https://github.com/reticlehq/reticle. Runtime verification layer for agents — instruments the running app from the inside (network calls, store state, custom signals, React commit stream) instead of reading a screenshot/DOM, returning pass/fail with file:line. Catches silent failures a screenshot/DOM check can't (e.g. a page that looks fine while a request underneath 500s). Complements Playwright — Playwright gates releases/CI, Reticle can gate individual edits mid-session. Don't install automatically; use whichever already fits the project's test setup.

**7. OmniRoute** — GitHub: https://github.com/rgplvr/omniroute. Model/provider routing concepts for multi-model workflows — task-specific routing, cost reduction, utilization. Don't install/configure automatically.

**8. Ruflo** — GitHub: https://github.com/ruvnet/ruflo (formerly "Claude Flow"). Multi-agent orchestration for Claude Code/Codex — swarms, SPARC-style workflows, GitHub automation, and a policy layer for spend/concurrency caps and approval gates. **Extra scrutiny beyond the normal §A7/§C1 review:** its releases have shipped `npm install` pointed at GitHub release tarball URLs rather than the registry — review tarball contents first. Independent reviews note the project's own ADRs acknowledging a meaningful fraction of its ~240 advertised tools aren't actually wired up, and at least one widely-cited benchmark figure was flagged externally as not reflecting a real run. Apply the full Pre-Install Gate (§C1) with no shortcuts; prefer starting in any "legacy"/"observe" mode before enabling enforcement. Use OmniRoute instead when simple model routing is all that's needed — reach for Ruflo only when genuine multi-agent swarm coordination is the actual requirement.

**9. Claude Mem** — persistent-memory concepts when an approved memory system is available: preserve project context, remember architecture decisions, avoid repeated discovery. Never store passwords, API keys, tokens, credentials, secrets, or sensitive personal information. Don't install/configure automatically.

**10. Headroom** — GitHub: https://github.com/anthonybo/headroom. Context/token awareness, session visibility for long-running sessions; current project provides a statusline (model, effort, context, spend, rate-limit headroom). Don't install automatically.

**11. Claude Code Setup** — workflow best practices: clear project instructions, security-first execution, predictable tracking, minimal context waste, consistent conventions, controlled dependency changes, explicit scope. Don't modify Claude Code config unless required.

**12. Task Observer** — visibility principles: track current task, modified files, dependency changes, security findings, completed/blocked/remaining work. The project tracker remains the source of truth.

**13. Ponytail** — GitHub: https://github.com/DietrichGebert/ponytail. A plugin that pushes an agent through a decision ladder before writing code — YAGNI → reuse existing code → standard library → native platform feature → dependency → one-liner → minimum implementation — specifically to counter over-building (e.g. reaching for a library + wrapper component + stylesheet for something a native `<input type="date">` already does). It explicitly keeps security, trust-boundary validation, data-loss handling, and accessibility off the table for trimming — those are never "the lazy option." This reinforces §A9/§A10's existing minimal-change, no-unnecessary-abstraction stance; treat it as a working companion to those rules, not a replacement for them. Installs as a Claude Code/Codex plugin (`/plugin marketplace add DietrichGebert/ponytail` then `/plugin install ponytail@ponytail`) and runs two small Node.js lifecycle hooks that must be explicitly reviewed and trusted via `/hooks` before first use — apply §A7/§E1 in full (review the hook source, don't trust-by-default just because it's a marketplace plugin) before installing or trusting those hooks.

## D2. Frontend Design Standard (Mandatory Before Writing Code)

Combine relevant principles from §D1 items 1–6 per the §D0 answer. State briefly which apply (it's fine if the answer is "none — trivial change") before writing any markup/component/style.

Prioritize: strong visual hierarchy, intentional layouts, excellent typography, consistent spacing, responsive behavior, accessibility, useful motion, performance, interaction feedback, visual consistency, production readiness.

Avoid: generic AI layouts, excessive cards, random gradients, unnecessary glassmorphism, excessive rounded containers, weak typography, poor contrast, meaningless animations, decorative elements without purpose, repetitive layouts, placeholder interfaces, excessive shadows, unnecessary badges, generic "AI slop" patterns.

Verify with Playwright and/or Reticle after implementation when either is already available.

## D3. Design Decision Rule

Understand product/user goal → inspect existing design system → identify page/surface type → determine visual direction → audit existing UI where appropriate → reuse existing tokens/components → implement only requested changes → verify in-browser (Playwright/Reticle) → check responsive behavior/accessibility/interaction quality → avoid unnecessary redesign. Don't use a tool just because it exists — only when it materially improves the current task.

## D4. Frontend Conventions — web.domainname.com

Reusable components; extract cleanly; Tailwind CSS when already established; reusable theme variables; consistent colors/spacing/radii/typography/component tokens.

**Dark/Light mode** (when supported): detect system preference, provide manual toggle, persist preference, prevent flash of incorrect theme. Don't introduce or redesign the theme system unless explicitly requested.

---

# 🔐 PART E — GROUP 4: TOOL / SKILL INSTALLATION

Selecting this Group bundles the following:

## E1. Tool/Skill Installation Flow

Identify the official source → review install method → review dependencies → review lifecycle scripts → check file modification / remote code execution / elevated permissions / credential access → prefer official docs → **STOP → REVIEW → REPORT → WAIT FOR APPROVAL** unless the user has explicitly approved that specific installation. Never pipe an unknown remote script directly into a shell.

## E2. No Automatic Installation

The tools in §D1 (and anywhere else in this file) are references, not authorization. None of the following are triggered just by being mentioned here: `npm install`, `npm ci`, `npx`, `curl | bash`, `wget | sh`, global package installation, plugin installation, CLI installation, system-level installation. Normal security and dependency gates (Part A, Part C) still apply on top of this.

---

# 📐 PART F — GROUP 5: SRS / REQUIREMENTS DOCUMENTATION WORK

Selecting this Group first runs the requirement-gathering question loop, then produces a structured SRS. This Group is what "creating an SRS for a project" routes through.

## F0. Requirement-Gathering Question Loop (Mandatory Before Drafting)

This is §A15 applied specifically to full project/feature requirements — don't draft a single line of the SRS until this loop has real answers. Ask in short focused rounds (1–3 questions at a time), and keep looping — do not stop after one round if gaps remain. Cover, across as many rounds as it takes:

1. **Purpose & problem** — what problem is this solving, and for whom?
2. **Scope** — what's explicitly in scope for this version, what's explicitly out?
3. **Users / stakeholders** — who are the user classes/roles (e.g. admin, end user, guest)?
4. **Core functional requirements** — what must the system do? Ask for the key features/flows one group at a time rather than "list everything" in one shot.
5. **Non-functional requirements** — performance expectations, security/compliance needs, scalability, availability, accessibility.
6. **Constraints** — required tech stack, existing systems to integrate with, budget/timeline constraints, regulatory constraints.
7. **External interfaces** — other systems, APIs, hardware, or third-party services this must talk to.
8. **Data requirements** — what data is stored/processed, and any sensitivity (PII, payment data, health data, etc. — this also feeds §A3).
9. **Acceptance criteria** — how will the user know each requirement is actually satisfied?

Stop looping once you can restate, in a short summary, the purpose, scope boundary, primary user classes, and top functional/non-functional requirements — and the user confirms or corrects it. Only then start drafting.

## F1. SRS Document Structure

Use this structure (trim sections that plainly don't apply rather than padding them with filler):

```text
1. Introduction
   1.1 Purpose
   1.2 Scope
   1.3 Definitions, Acronyms, Abbreviations
   1.4 References
   1.5 Overview

2. Overall Description
   2.1 Product Perspective
   2.2 Product Functions (high-level summary)
   2.3 User Classes and Characteristics
   2.4 Operating Environment
   2.5 Design and Implementation Constraints
   2.6 Assumptions and Dependencies

3. Specific Requirements
   3.1 Functional Requirements (grouped by feature/module, each with an ID like FR-1, FR-2)
   3.2 Non-Functional Requirements
       3.2.1 Performance
       3.2.2 Security
       3.2.3 Usability & Accessibility
       3.2.4 Reliability & Availability
       3.2.5 Scalability
   3.3 External Interface Requirements
       3.3.1 User Interfaces
       3.3.2 Hardware Interfaces
       3.3.3 Software Interfaces
       3.3.4 Communication Interfaces

4. Data Requirements
   4.1 Data Entities / Model Overview
   4.2 Data Sensitivity & Retention

5. Acceptance Criteria
   (per major requirement or feature, from §F0.9)

6. Appendices
   6.1 Open Questions / Assumptions Log
   6.2 Revision History
```

Every functional requirement gets a stable ID (`FR-1`, `FR-2`, …) so later tracker tasks can reference it (e.g. `feat(12): implements FR-4`).

## F2. Where It Lives & How It's Tracked

* Save as `docs/SRS.md` (or `docs/SRS-<feature-name>.md` for a feature-level SRS inside a larger existing product) — see §A8.
* Track the SRS itself as a tracker entry using type `srs` (e.g. `srs(N)`), following the same Part B workflow — logged, numbered, commented, marked complete once the user confirms the draft is accepted.
* Treat the SRS as living documentation: don't silently rewrite an accepted version. New changes get a dated entry in the `Revision History` (§F1, 6.2) — never delete prior revision history.
* Once an SRS is accepted, subsequent `feat`/`fix` tracker entries for that project should reference the relevant `FR-` ID(s) in their Comment where practical, so implementation traces back to the spec.

---

# 📌 PART G — TRACKER ENTRY TEMPLATES

**Valid task formats:** `feat ....` · `fix ....` · `security ....` · `update ....` · `issue ....` · `feat/fix ....` · `srs ....` · plain description.

## New / Uncompleted

```md
- [ ] **type(N)**: short description of the requested work
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Author: github-username*
  > *Comment: Briefly describe what needs to be done.*
```

## Completed

```md
- [x] **type(N)**: short description of the requested work
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Completed: YYYY-MM-DD HH:MM PKT*
  > *Author: github-username*
  > *Comment: Brief summary of what was implemented and the final result.*
  > *Token Usage: <usage if available>*
```

## Blocked Task

```md
- [ ] **issue(N)**: short description
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Author: github-username*
  > *Comment: Blocked because <specific reason>. Remaining work: <specific action>.*
```

<!--
Completed items must remain intact.
Cursor/Claude must not delete previous tracker history.
Every task must have a Comment directly below it.
Author must always be a verified GitHub username.
-->

* [ ] **feat(1)**: (awaiting first user feature)

  > *Added: 2026-08-27 14:11 PKT*
  > *Author: <GitHub username required>*
  > *Comment: Awaiting the first user-provided feature or task.*

---

*Last updated: 2026-09-04 (added Group 5 — SRS/requirements documentation, and a compulsory clarification-until-understood loop in Part A)*
