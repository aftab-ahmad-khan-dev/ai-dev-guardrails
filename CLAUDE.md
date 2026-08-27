# CLAUDE.md

**Repo:** https://github.com/aftab-ahmad-khan-dev/ai-dev-guardrails

## How Claude Code loads this file

Claude Code auto-reads `CLAUDE.md` at the repo root on every session — no setup needed.

---

# 🛡️ PRIORITY #1 — SECURITY-FIRST (MANDATORY)

**Security is the highest priority and must be checked before any action.**

Before implementing a feature, fixing an issue, installing/updating a dependency, executing unfamiliar code, or making any project changes:

1. Perform the required security pre-scan.
2. Only after the scan is clean, or issues are reported and addressed, may work begin.

Never skip the security gate.

---

# 🔍 SESSION-START MANDATORY SECURITY SCAN

On **every new session**, before asking for a task or touching the tracker:

1. Inspect top-level project structure.

   * Skip `node_modules`.
   * Skip `.git`.
   * Skip build artifacts.
2. Search for:

   * secrets
   * credentials
   * API keys
   * access tokens
   * suspicious environment variables
3. Inspect:

   * `package.json`
   * lockfiles
   * relevant configuration
4. Run available security scanners when already installed/available.
5. Review:

   * dependency lifecycle scripts
   * suspicious packages
   * obvious SAST issues
   * suspicious entry-point behavior
6. Output a short:

**Security Status: Clean**

or:

**Security Status: Issues Found — <brief list>**

7. Only then:

   * If a concrete task was already provided → extract it, add it to the tracker, and implement it.
   * If no task was provided → show Security Status and ask what to work on.

Never treat "no task yet" as permission to explore unrelated project areas.

---

# 🛡️ PRE-INSTALL SECURITY GATE

**Goal: never allow untrusted dependency code to execute before it has been reviewed.**

Claude must follow this process for **all dependency-related work**.

## Phase 1 — Inspect Before Installation

Inspect:

* `package.json`
* `package-lock.json`
* `npm-shrinkwrap.json`
* `yarn.lock`
* `pnpm-lock.yaml`
* `.npmrc`
* workspace configuration

Determine:

* direct dependencies
* transitive dependencies
* version ranges
* requested versions
* package sources
* Git dependencies
* tarball dependencies
* registry configuration
* optional dependencies
* peer dependencies
* lifecycle scripts

Do not install anything during this phase.

---

## Phase 2 — Static Review

Before installing an unfamiliar dependency:

* Review package metadata.
* Review lifecycle scripts.
* Review known security information.
* Review package provenance where available.
* Look for suspicious filesystem access.
* Look for unexpected network activity.
* Look for obfuscation.
* Look for unexpected binaries.
* Look for behavior unrelated to the package's stated purpose.
* Check whether an established alternative already exists.

Do not execute the dependency during review.

---

## Phase 3 — Safe Installation

When installation is explicitly approved:

Prefer:

```bash
npm ci --ignore-scripts
```

or:

```bash
npm install --ignore-scripts
```

Then perform the appropriate security checks.

Only enable lifecycle scripts when:

1. They are genuinely required.
2. The dependency has been reviewed.
3. Their behavior is understood.
4. Continuing is appropriate for the task.

Never blindly execute dependency lifecycle scripts.

---

## Critical Rule

If a dependency appears suspicious because of:

* typosquatting
* dependency confusion
* unexpected lifecycle scripts
* unexpected network access
* unexpected filesystem access
* heavy obfuscation
* credential/environment access
* remote downloads
* suspicious binaries
* cryptocurrency-mining behavior
* unrelated functionality

then:

**STOP → REPORT → DO NOT INSTALL → RECOMMEND A SAFE ALTERNATIVE.**

---

# 🛡️ DEPENDENCY & VULNERABILITY SCANNERS

Use available scanners when relevant.

## npm audit

Prefer:

```bash
npm audit --audit-level=moderate
```

## NodeSecure

Use `@nodesecure/scanner` when already available and appropriate.

## Retire.js

Use Retire.js when already available and relevant.

## SAST

When already available:

* nodejsscan
* Semgrep
* ESLint security plugins
* `eslint-plugin-security`

Do not install a security scanner merely to perform a scan if doing so would violate the dependency security gate.

---

# 🔎 MALICIOUS CODE & PACKAGE REVIEW

Before trusting unfamiliar packages, scripts, or modules, inspect for:

* `preinstall`
* `install`
* `postinstall`
* `prepare`
* shell execution
* remote downloads
* unexpected network requests
* data exfiltration
* credential access
* environment-variable harvesting
* SSH key access
* browser data access
* filesystem manipulation
* encoded/obfuscated JavaScript
* suspicious binaries
* persistence mechanisms
* crypto-mining behavior
* dependency confusion
* typosquatting

If a serious issue is found:

1. Stop.
2. Report the finding.
3. Do not execute the suspicious code.
4. Recommend removal/replacement.
5. Continue only after the concern is addressed.

> **Security principle: Scan first. Trust later. Implement only after relevant checks are complete.**

---

# 📋 GENERAL WORKING RULES

* Never commit yourself.
* Do not run `git commit`, `git push`, or commit-related commands unless the user explicitly asks.
* Never add Claude, ChatGPT, AI, assistant, or any AI identity as an author.
* Never add `Co-authored-by: Claude`.
* Never add `Generated by Claude`.
* Never add self-attribution.
* Focus strictly on the user's requested functionality.
* Do not invent features.
* Do not add unsolicited polish.
* Do not perform unrelated refactoring.
* Do not expand scope.
* Prefer surgical, minimal changes.
* Touch only files required for the current task.
* If a task is ambiguous, ask a short clarifying question.
* Do not add tests unless explicitly requested.
* Do not add documentation unless explicitly requested.
* Do not add configuration unless required by the task.
* Never break or regress previously completed features.
* Minimize token usage.
* Avoid unnecessary comments.
* Avoid verbose summaries.
* Stay silent on process when possible.

---

# 👤 GITHUB AUTHOR RULE

The `Author` field must **always contain the verified GitHub username responsible for the task.**

## Mandatory Rules

* `Author` = GitHub username only.
* Never use a person's real name unless it is also their verified GitHub username.
* Never use an email address.
* Never use Claude.
* Never use Cursor.
* Never use ChatGPT.
* Never use AI.
* Never invent a GitHub username.
* If the task explicitly provides a GitHub username, use it.
* If the GitHub username can be safely verified from repository/GitHub context, use it.
* If it cannot be verified, use:

```text
Author: <GitHub username required>
```

Do not assume the repository owner is automatically the author without verification.

---

# 📝 UNIVERSAL TASK COMMENT / TRACKER RULE

Every tracked task must have a concise **Comment** directly below the task entry.

This applies to:

* `feat`
* `fix`
* `security`
* `update`
* `issue`
* `feat/fix`
* any other tracked work

The comment must:

* appear directly below the task
* explain what was done or needs to be done
* reflect the actual status
* remain concise
* contain factual information only
* never claim work that was not performed

## New Task

```md
- [ ] **feat(N)**: short description of the requested work
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Author: github-username*
  > *Comment: Briefly describe what needs to be done.*
```

## Completed Task

```md
- [x] **feat(N)**: short description of the requested work
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

---

# 📊 TRACKER WORKFLOW

When receiving new work:

1. Parse the request.
2. Determine the type:

   * `feat`
   * `fix`
   * `security`
   * `update`
   * `issue`
   * `feat/fix`
3. Normalize the request.
4. Find the highest existing task number.
5. Assign the next sequential number.
6. Add the task as unchecked.
7. Immediately add its Comment.
8. Perform the required security checks.
9. Implement only the requested work.
10. Update the Comment when necessary.
11. Mark the task `[x]` only after successful completion.
12. Add:

* completion date
* completion time
* verified GitHub username
* token usage when available

13. Update `Last updated`.
14. Update the daily token total when supported.

---

# 🔢 TASK NUMBERING

* Task numbers must always be sequential.
* Never reuse a previous number.
* Never renumber completed tasks.
* Never delete completed tracker history.
* Find the highest existing `N` before adding a new task.
* New task = highest existing `N + 1`.

---

# 🎯 TASK SCOPE

The user's current request defines the scope.

Do not automatically:

* redesign unrelated UI
* refactor unrelated code
* upgrade unrelated packages
* change architecture
* rename unrelated files
* rewrite working components
* add unrelated features
* add documentation
* add tests
* change configuration

unless explicitly requested or strictly required.

---

# 🎨 AI DESIGN, UI/UX & DEVELOPMENT SKILLS

These are preferred design and development resources.

They are **references and workflow tools, not automatic installation authorization**.

---

## 1. Taste Skill

Official website:

https://www.tasteskill.dev/

Documentation:

https://www.tasteskill.dev/docs

Prompt guide:

https://www.tasteskill.dev/guide

GitHub:

https://github.com/Leonxlnx/taste-skill

Taste Skill is designed to reduce generic AI-generated frontend patterns and improve layout, typography, spacing, motion, design-system thinking, and frontend quality. Its current documentation lists Cursor and Claude Code among compatible agents.

Use it when relevant for:

* frontend design
* UI/UX
* visual hierarchy
* layout direction
* typography
* spacing
* design systems
* anti-generic design
* redesign audits
* responsive composition
* visual pre-flight checks

For existing projects, prefer an audit-first approach before redesigning.

Do not blindly replace an existing design system.

---

## 2. Impeccable

Official website:

https://impeccable.style/

Use it for:

* UI audits
* visual polish
* typography
* spacing
* color systems
* accessibility
* responsive design
* UI refinement
* design-system consistency
* identifying weak AI-generated design patterns

When improving an existing interface:

1. Inspect the current design system.
2. Identify weak areas.
3. Preserve working conventions.
4. Make targeted improvements.
5. Verify the result.

Do not redesign unrelated UI.

---

## 3. Emil Kowalski — Design Engineering

Official website:

https://emilkowal.ski/skill

Official skills repository:

https://github.com/emilkowalski/skills

Use it for:

* animation
* micro-interactions
* transitions
* hover states
* component polish
* motion design
* interaction quality
* animation review
* UI details

The current repository includes `emil-design-eng`, `review-animations`, `improve-animations`, `find-animation-opportunities`, and other design-engineering skills.

Animations must:

* serve a purpose
* remain performant
* avoid excessive motion
* respect reduced-motion preferences
* avoid distracting users
* use appropriate easing
* avoid unnecessary animation libraries

---

## 4. ImageToCode

Use image/design references when the user provides them.

Use references to understand:

* layout
* spacing
* typography
* hierarchy
* component structure
* visual relationships
* responsive behavior

Do not blindly reproduce implementation details.

Preserve the project's architecture.

---

## 5. Playwright CLI

Official website:

https://playwright.dev/

Use Playwright when it is already available and relevant.

Use it to:

* open the application
* verify pages
* inspect navigation
* test responsive layouts
* capture screenshots
* identify visual regressions
* inspect console errors
* verify interactions
* verify forms
* validate user flows

Do not install Playwright automatically.

If Playwright is unavailable, do not install it unless explicitly requested and the dependency security gate has been completed.

---

## 6. OmniRoute

GitHub:

https://github.com/rgplvr/omniroute

Use OmniRoute concepts when the workflow uses multiple AI models/providers.

Use it for:

* model routing
* model selection
* provider selection
* task-specific routing
* reducing unnecessary model costs
* improving model utilization

Do not install or configure OmniRoute automatically.

Its current documentation includes Claude Code configuration and model-routing support.

---

## 7. Claude Mem

Use persistent-memory concepts when an approved memory system is available.

Goals:

* preserve useful project context
* remember architecture decisions
* avoid repeated discovery
* maintain continuity between sessions

Never store:

* passwords
* API keys
* access tokens
* private credentials
* secrets
* sensitive personal information

Do not install or configure a memory system automatically.

---

## 8. Headroom

GitHub:

https://github.com/anthonybo/headroom

Use Headroom concepts for:

* context management
* token awareness
* session visibility
* context-window monitoring
* long-running AI development sessions

Do not install automatically.

The current Headroom project provides a Claude Code statusline showing model, effort, context, spend, and rate-limit headroom.

---

## 9. Claude Code Setup

Use Claude Code workflow best practices where applicable.

Prioritize:

* clear project instructions
* security-first execution
* predictable task tracking
* minimal context waste
* consistent project conventions
* controlled dependency changes
* explicit scope

Do not modify Claude Code configuration unless required by the user's task.

---

## 10. Task Observer

Use task-observation principles to maintain visibility into agent work.

Track:

* current task
* modified files
* dependency changes
* security findings
* completed work
* blocked work
* remaining work

The project tracker remains the source of truth.

Every tracked task must have a Comment directly below it.

---

# 🖥️ FRONTEND DESIGN STANDARD

For frontend work, combine relevant principles from:

1. Taste Skill
2. Impeccable
3. Emil Kowalski's design-engineering principles
4. Image/design references
5. Playwright browser verification when available

Prioritize:

* strong visual hierarchy
* intentional layouts
* excellent typography
* consistent spacing
* responsive behavior
* accessibility
* useful motion
* performance
* interaction feedback
* visual consistency
* production readiness

Avoid:

* generic AI layouts
* excessive cards
* random gradients
* unnecessary glassmorphism
* excessive rounded containers
* weak typography
* poor contrast
* meaningless animations
* decorative elements without purpose
* repetitive layouts
* placeholder-looking interfaces
* excessive shadows
* unnecessary badges
* generic "AI slop" patterns

---

# 🔐 TOOL / SKILL SECURITY RULE

External skills, plugins, CLIs, scripts, and development tools are **not automatically trusted**.

Before installing any tool:

1. Identify the official source.
2. Review its installation method.
3. Review dependencies.
4. Review lifecycle scripts where applicable.
5. Check whether it modifies project files.
6. Check whether it executes remote code.
7. Check whether it requires elevated permissions.
8. Check whether it requires credentials or sensitive files.
9. Prefer official repositories/documentation.
10. Do not install automatically.

If installation is required:

**STOP → REVIEW → REPORT → WAIT FOR APPROVAL**

unless the user has explicitly approved that specific installation.

Never pipe an unknown remote script directly into a shell.

Never install a tool merely because it is mentioned in this file.

---

# 🚫 NO AUTOMATIC INSTALLATION

The resources listed in this file are **preferred references and workflow capabilities**.

Their presence does NOT authorize:

```bash
npm install
npm ci
npx
curl | bash
wget | sh
```

It also does not authorize:

* global package installation
* plugin installation
* CLI installation
* system-level installation

Normal security and dependency gates still apply.

---

# 🎯 DESIGN DECISION RULE

Before implementing significant frontend design changes:

1. Understand the product and user goal.
2. Inspect the existing design system.
3. Identify the page/surface type.
4. Determine the appropriate visual direction.
5. Audit existing UI where appropriate.
6. Reuse existing tokens/components where possible.
7. Implement only requested changes.
8. Verify in the browser when possible.
9. Check responsive behavior.
10. Check accessibility.
11. Check interaction quality.
12. Avoid unnecessary redesign.

**Do not use a tool just because it exists. Use it only when it materially improves the current task.**

---

# 📁 PROJECT STRUCTURE

Expected root folders:

```text
api.domainname.com/
web.domainname.com/
```

## Backend

`api.domainname.com`

Contains backend/API functionality.

## Frontend

`web.domainname.com`

Contains frontend/client functionality.

Maintain clear separation between API and client code.

---

# 🧹 CODE QUALITY

* No source file should exceed approximately 400 lines.
* Maintain a clean folder structure.
* Use meaningful variable names.
* Use meaningful function names.
* Use meaningful class names.
* Avoid cryptic abbreviations.
* Maintain separation of concerns.
* Prefer reusable components.
* Avoid unnecessary abstraction.
* Avoid unrelated refactoring.

---

# 🎨 FRONTEND — web.domainname.com

* Use reusable components.
* Extract reusable components cleanly.
* Use Tailwind CSS when already established.
* Maintain reusable theme variables.
* Maintain consistent:

  * colors
  * spacing
  * radii
  * typography
  * component tokens

## Dark / Light Mode

When supported by the project:

* Detect system preference.
* Provide manual toggle.
* Persist preference.
* Prevent flash of incorrect theme.

Do not introduce or redesign the theme system unless explicitly requested.

---

# 🔐 SECURITY CHANGE RULE

Any task involving:

* authentication
* authorization
* credentials
* tokens
* cookies
* sessions
* APIs
* dependencies
* packages
* databases
* file uploads
* command execution
* filesystem access
* deployment
* environment variables
* external services

requires an appropriate security review.

Never weaken an existing security control merely to make a feature work.

If a significant security concern appears:

**STOP → REPORT → ASK FOR DIRECTION.**

---

# 🚫 DANGEROUS COMMAND RULE

Do not execute destructive or system-wide commands unless explicitly required and explicitly approved.

Examples:

```bash
sudo
rm -rf
mkfs
dd
diskutil eraseDisk
git reset --hard
git clean -fd
git push --force
```

If such a command appears necessary:

1. Stop.
2. Explain what it does.
3. Ask for explicit approval.
4. Never assume approval.

---

# 🌐 NETWORK / EXTERNAL RESOURCE RULE

Do not blindly download or execute remote content.

Never blindly execute:

```bash
curl <url> | bash
```

or:

```bash
wget <url> | sh
```

Review external resources before execution.

---

# 📦 DEPENDENCY CHANGE RULE

Any dependency change requires:

1. Identify why it is needed.
2. Inspect existing dependency configuration.
3. Check whether an existing package already provides the functionality.
4. Review the proposed package.
5. Review its version and requirements.
6. Review lifecycle scripts.
7. Review security concerns.
8. Prefer established alternatives.
9. Install with scripts disabled initially where practical.
10. Run appropriate security checks.
11. Enable lifecycle scripts only when necessary and justified.

Never add a dependency simply because it is convenient.

---

# 🧪 TESTING RULE

Do not add tests unless explicitly requested.

When existing tests are available:

* Prefer existing tests.
* Do not modify unrelated tests.
* Do not disable tests to hide failures.
* Report failures honestly.

For dependency/security work, never execute potentially unsafe dependency code merely to obtain a test result.

---

# 🔄 REGRESSION RULE

Before completing a task:

* Verify requested functionality.
* Review changed files.
* Check accidental changes.
* Confirm completed functionality remains intact.
* Confirm security requirements remain intact.

---

# 🛑 STOP CONDITIONS

Stop and report instead of continuing if:

* A serious security issue is discovered.
* A dependency appears malicious or highly suspicious.
* A command could damage the operating system.
* A command could delete significant project data.
* Credentials are discovered.
* A required dependency cannot be safely reviewed.
* The requested change conflicts with security controls.
* The task is ambiguous.
* The task requires access outside the repository without explicit authorization.

When stopped:

1. Explain the issue concisely.
2. State what was discovered.
3. State what was not changed.
4. State what decision or approval is required.

---

# 📅 TRACKER DATE / TIME

Use Pakistan Standard Time:

```text
YYYY-MM-DD HH:MM PKT
```

Use the actual current date/time available to the environment.

---

# 📈 TOKEN USAGE

When available, record token usage in completed tracker entries.

Example:

```md
> *Token Usage: 12,450*
```

Update the daily token total when supported.

---

# 🔒 FINAL SECURITY PRINCIPLE

> **Scan first. Trust later. Change minimally. Execute only what is necessary.**

Security comes before implementation.

Never install first and investigate later.

Never execute unknown code to determine whether it is safe.

Never sacrifice security for convenience.

Never modify unrelated functionality.

Never break previously completed work.

**Security → Scope → Implementation → Verification → Tracker Update**

---

# 📋 USER PROMPT / FEATURES

**Valid task formats:**

1. `feat ....`
2. `fix ....`
3. `security ....`
4. `update ....`
5. `issue ....`
6. `feat/fix ....`
7. Plain description

When receiving new work:

1. Parse the request.
2. Determine the type.
3. Normalize it.
4. Find the highest task number.
5. Assign the next sequential number.
6. Add it unchecked.
7. Add the Comment directly below it.
8. Perform security checks.
9. Implement only the requested work.
10. Mark completed only after successful completion.
11. Add completion metadata.
12. Update `Last updated`.

---

# 📌 STANDARD TRACKER ENTRY

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

*Last updated: 2026-08-27 14:11 PKT*
