# Cursor.md

**Repo:** https://github.com/aftab-ahmad-khan-dev/ai-dev-guardrails

## How Cursor loads this file

Cursor does not auto-read `CURSOR.md` by filename. Point it here with one thin rule:

Create `.cursor/rules/cursor-md.mdc`:

```markdown
---
description: Follow Cursor.md rules, security requirements, and feature tracker
alwaysApply: true
---

Before any work:
1. Read `CURSOR.md` at the repo root.
2. Follow its Rules section.
3. Perform the required security checks.
4. Read the User Prompt / Features section.
5. Work only on the next unchecked task unless the user explicitly provides a different task.
```

---

# 🛡️ PRIORITY #1 — SECURITY-FIRST

**Security is the highest priority and must be checked before any action.**

Before:

* implementing a feature
* fixing an issue
* changing dependencies
* installing/updating packages
* executing unfamiliar code
* modifying configuration
* modifying project files

Cursor must perform the appropriate security pre-check first.

Never skip the security gate.

---

# 🔍 SESSION-START SECURITY CHECK

At the beginning of every new Cursor session:

1. Inspect the project structure.

   * Skip `node_modules`
   * Skip `.git`
   * Skip build artifacts
2. Inspect:

   * `package.json`
   * lockfiles
   * relevant configuration
3. Check for obvious:

   * secrets
   * API keys
   * credentials
   * suspicious scripts
   * suspicious dependencies
   * unexpected executables
4. Perform available security checks that do not require installing untrusted dependencies.
5. Provide a short:

**Security Status: Clean**

or:

**Security Status: Issues Found — <brief description>**

6. Only then proceed with the requested task.

Security checks must be proportional to the task.

---

# 🛡️ DEPENDENCY SECURITY GATE

Dependency changes require additional protection.

## Before Installing Any Dependency

First inspect:

* `package.json`
* `package-lock.json`
* `npm-shrinkwrap.json`
* `yarn.lock`
* `pnpm-lock.yaml`
* `.npmrc`
* workspace configuration

Determine:

* package name
* requested version
* version range
* dependency source
* direct/transitive relationship
* lifecycle scripts
* existing alternatives
* known security concerns

Do **not** install the dependency during this inspection.

---

# 🚨 NEVER INSTALL FIRST AND INVESTIGATE LATER

Do not blindly execute:

```bash
npm install
```

```bash
npm ci
```

```bash
npm update
```

```bash
npm audit fix
```

```bash
npx <unknown-package>
```

when investigating an unfamiliar dependency.

Never execute unknown package code merely to determine whether it is safe.

---

# 🔒 SAFE DEPENDENCY INSTALLATION

When dependency installation is explicitly required and approved:

Prefer:

```bash
npm ci --ignore-scripts
```

or:

```bash
npm install --ignore-scripts
```

Then perform the appropriate security checks.

Do not automatically enable lifecycle scripts.

Only enable `preinstall`, `install`, `postinstall`, or `prepare` behavior when:

1. It is genuinely required.
2. The package has been reviewed.
3. The user has explicitly approved continuing where appropriate.

---

# 🔎 SUSPICIOUS DEPENDENCY RULE

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
* crypto-mining behavior
* unrelated functionality

then:

**STOP → REPORT → DO NOT INSTALL → RECOMMEND A SAFE ALTERNATIVE.**

Do not automatically continue.

---

# 🔬 MALICIOUS CODE REVIEW

When reviewing an unfamiliar dependency or script, pay attention to:

* `preinstall`
* `install`
* `postinstall`
* `prepare`
* shell execution
* remote downloads
* unexpected HTTP requests
* filesystem manipulation
* environment-variable harvesting
* credential access
* SSH key access
* browser data access
* encoded/obfuscated JavaScript
* suspicious binaries
* persistence mechanisms
* command execution
* behavior unrelated to the package's stated purpose

Do not execute suspicious code.

---

# 🧪 SECURITY / SCA TOOLS

Use existing, already-available security tools when relevant.

Possible tools:

### npm audit

```bash
npm audit --audit-level=moderate
```

### NodeSecure

`@nodesecure/scanner`

### Retire.js

For known vulnerable JavaScript libraries.

### SAST

When available:

* nodejsscan
* Semgrep
* ESLint security plugins
* eslint-plugin-security

Do not install a security scanner solely to perform a scan if doing so would violate the dependency security gate.

---

# 🔍 SOURCE-CODE SECURITY REVIEW

When relevant, inspect source code for:

* injection vulnerabilities
* authentication problems
* authorization problems
* unsafe command execution
* unsafe filesystem operations
* hardcoded credentials
* unsafe deserialization
* dynamic code execution
* insecure configuration
* sensitive-data exposure
* dangerous dependency usage

Keep security checks proportional to the requested task.

---

# 📋 GENERAL RULES

* Never commit yourself.
* Do not run `git commit`.
* Do not run `git push`.
* Do not run any commit-related command unless the user explicitly asks.
* Never add Cursor, Claude, ChatGPT, AI, assistant, or any AI identity as an author.
* Never add `Co-authored-by: Cursor`.
* Never add `Generated by Cursor`.
* Never add self-attribution.
* Focus strictly on the user's requested functionality.
* Do not invent features.
* Do not add unsolicited polish.
* Do not refactor unrelated code.
* Do not expand scope.
* Prefer surgical, minimal changes.
* Touch only files required for the current task.
* Do not add tests unless explicitly requested.
* Do not add documentation unless explicitly requested.
* Do not add configuration changes unless required by the requested task.
* Never break or regress previously completed features.
* If a task is ambiguous, ask a short clarifying question.
* Keep explanations concise.
* Avoid unnecessary comments.
* Avoid verbose summaries.
* Stay silent on process when possible.

---

# 👤 GITHUB AUTHOR RULE

The `Author` field must **always contain the verified GitHub username responsible for the task.**

## Mandatory

* Author = GitHub username only.
* Never use a person's real name unless it is also their verified GitHub username.
* Never use an email address.
* Never use Cursor.
* Never use Claude.
* Never use ChatGPT.
* Never use AI.
* Never invent a GitHub username.
* If the GitHub username is explicitly provided, use it.
* If the GitHub username can be safely verified from repository/GitHub context, use it.
* If it cannot be verified, use:

```text
Author: <GitHub username required>
```

Do not assume the repository owner is the author without verification.

---

# 📝 UNIVERSAL TASK COMMENT RULE

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

---

# 📊 TASK TRACKER WORKFLOW

When receiving new work:

1. Parse the request.
2. Determine the task type:

   * `feat`
   * `fix`
   * `security`
   * `update`
   * `issue`
   * `feat/fix`
3. Normalize the request.
4. Find the highest existing task number.
5. Assign the next sequential number `N`.
6. Add the task as unchecked.
7. Immediately add its Comment.
8. Perform the required security checks.
9. Implement only that task.
10. Update the Comment if the status changes.
11. Mark the task `[x]` only after successful completion.
12. Add completion date/time.
13. Add the verified GitHub username.
14. Add token usage when available.
15. Update `Last updated`.
16. Update the daily token total when supported.

---

# 📌 TASK FORMAT

## New / Uncompleted

```md
- [ ] **feat(N)**: short description of the requested work
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Author: github-username*
  > *Comment: Briefly describe what needs to be done.*
```

## Completed

```md
- [x] **feat(N)**: short description of the requested work
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Completed: YYYY-MM-DD HH:MM PKT*
  > *Author: github-username*
  > *Comment: Brief summary of what was implemented and the final result.*
  > *Token Usage: <usage if available>*
```

## Blocked

```md
- [ ] **issue(N)**: short description
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Author: github-username*
  > *Comment: Blocked because <specific reason>. Remaining work: <specific action>.*
```

---

# 🔢 TASK NUMBERING

Task numbers must always be sequential.

Before adding a new task:

1. Read the existing tracker.
2. Find the highest existing `N`.
3. Assign `N + 1`.
4. Never reuse a previous number.
5. Never modify the numbering of completed tasks.

Previous completed tasks must remain intact.

---

# 🎯 NEXT TASK RULE

When the user gives a normal feature request:

* Read the tracker.
* Ignore completed items.
* Work on the next unchecked task.
* Do not skip an earlier unchecked task.
* Do not automatically work on multiple tasks.
* Only work on multiple tasks when the user explicitly requests multiple tasks.

If the user explicitly names a particular task number, follow the user's explicit instruction.

---

# 📁 PROJECT STRUCTURE

The expected project structure is:

```text
api.domainname.com/
web.domainname.com/
```

### Backend

`api.domainname.com`

Contains:

* APIs
* server logic
* routes
* controllers
* services
* middleware
* backend configuration

### Frontend

`web.domainname.com`

Contains:

* UI
* pages
* components
* frontend routing
* client-side logic

Maintain clear separation between backend and frontend.

---

# 🧹 CODE QUALITY

* Keep source files around 400 lines or less.
* Maintain clean folder structure.
* Use meaningful variable names.
* Use meaningful function names.
* Use meaningful class names.
* Avoid cryptic abbreviations.
* Avoid unnecessary duplication.
* Maintain separation of concerns.
* Prefer reusable components where appropriate.
* Avoid unnecessary abstraction.
* Do not refactor unrelated code.

---

# 🎨 FRONTEND — web.domainname.com

* Use reusable components.
* Keep components properly separated.
* Use Tailwind CSS where already established.
* Maintain reusable theme variables.
* Maintain consistent:

  * colors
  * spacing
  * radii
  * typography
  * component tokens

## Dark / Light Mode

When supported by the project, maintain:

* system preference detection
* manual theme toggle
* persistent preference
* no flash of incorrect theme

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
* filesystem operations
* deployment
* environment variables
* external services

requires an appropriate security review.

Never weaken an existing security control simply to make functionality work.

If the requested implementation creates a significant security concern:

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

Also avoid commands that can modify files outside the repository.

If such a command appears necessary:

1. Stop.
2. Explain what it will do.
3. Ask for explicit approval.
4. Do not assume approval.

---

# 🌐 EXTERNAL NETWORK RULE

Do not blindly download or execute remote content.

Never blindly execute:

```bash
curl <url> | bash
```

or:

```bash
wget <url> | sh
```

Do not execute unknown remote scripts.

Review external resources before execution.

---

# 📦 DEPENDENCY CHANGE RULE

Any dependency change requires:

1. Identify why it is needed.
2. Inspect existing dependency configuration.
3. Check whether an existing package already provides the functionality.
4. Review the proposed package.
5. Review its version and dependency requirements.
6. Review lifecycle scripts.
7. Review known security concerns.
8. Prefer established alternatives.
9. Install with scripts disabled initially where practical.
10. Run appropriate security checks.
11. Only enable lifecycle scripts when necessary and justified.

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

* Verify the requested functionality.
* Review changed files.
* Check for accidental changes.
* Confirm previously completed functionality remains intact.
* Confirm security requirements remain intact.

Do not expand the task scope.

---

# 📌 TASK SCOPE RULE

The user's request defines the scope.

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

unless explicitly requested or strictly required for the requested task.

---

# 🛑 STOP CONDITIONS

Stop and report instead of continuing if:

* A serious security issue is discovered.
* A dependency appears malicious or highly suspicious.
* A command could damage the operating system.
* A command could delete significant project data.
* Credentials are discovered.
* A required dependency cannot be safely reviewed.
* The requested change conflicts with a security control.
* The task is ambiguous and implementation would require guessing.
* The task requires access outside the repository without explicit authorization.

When stopped:

1. Explain the issue concisely.
2. State what was discovered.
3. State what was not changed.
4. State what decision or approval is required.

---

# 📅 TRACKER DATE / TIME

Use Pakistan Standard Time (PKT / UTC+05:00).

Format:

```text
YYYY-MM-DD HH:MM PKT
```

Use the actual current date and time available to the environment.

---

# 📈 TOKEN USAGE

When token usage is available, record it in completed tracker entries.

Example:

```md
> *Token Usage: 12,450*
```

Update the daily token total when the tracker supports it.

---

# 🔒 FINAL PRINCIPLE

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

**How user adds work (any of these are valid):**

1. `feat ....`
2. `fix ....`
3. `security ....`
4. `update ....`
5. `issue ....`
6. `feat/fix ....`
7. Plain description

Cursor must normalize every request into the tracker format.

---

# 📌 STANDARD TRACKER ENTRY

### New / Uncompleted

```md
- [ ] **type(N)**: short description of the requested work
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Author: github-username*
  > *Comment: Briefly describe what needs to be done.*
```

### Completed

```md
- [x] **type(N)**: short description of the requested work
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Completed: YYYY-MM-DD HH:MM PKT*
  > *Author: github-username*
  > *Comment: Brief summary of what was implemented and the final result.*
  > *Token Usage: <usage if available>*
```

<!--
Cursor ignores completed items and works only on the next unchecked item.
Previous completed work must never be deleted, rewritten, or broken.
Every task must have a Comment directly below it.
Author must always be a verified GitHub username.
-->

* [ ] **feat(1)**: (awaiting first user feature)

  > *Added: 2026-08-27 13:10 PKT*
  > *Author: <GitHub username required>*
  > *Comment: Awaiting the first user-provided feature or task.*

---

*Last updated: 2026-08-27 13:10 PKT*
