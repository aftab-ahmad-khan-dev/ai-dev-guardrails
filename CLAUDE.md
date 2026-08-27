# CLAUDE.md

**Repo:** aftab-ahmad-khan-dev/ai-dev-guardrails

## How Claude Code loads this file

Claude Code auto-reads `CLAUDE.md` at the repo root on every session — no setup needed.

---

# 🛡️ PRIORITY #1 — SECURITY-FIRST (MANDATORY)

**Security is the highest priority and must be checked before any action.**

Before implementing a feature, fixing an issue, installing/updating a dependency, executing unfamiliar code, or making any project changes:

1. Perform the required security pre-scan.
2. Only after the scan is clean (or issues are reported and addressed) may work begin.

## Session-Start Mandatory Security Scan

On **every new session**, before asking for a task or touching the tracker:

1. Run a project-wide security pre-scan (proportional but non-empty):

   * Inspect top-level structure (skip `node_modules`, `.git`, build artifacts).
   * Search for secrets / credentials patterns (`.env*`, hardcoded keys, API tokens).
   * Inspect `package.json` / lockfiles.
   * Run available SCA tools (see below).
   * Flag install scripts, suspicious packages, or obvious SAST issues in entry points.
2. Output a short **Security Status** paragraph (Clean / Issues found + brief list).
3. Only then:

   * If a concrete task was already given → extract it, add to tracker, implement.
   * If no task yet → show Security Status and ask what to work on.

Never skip the security gate. Never treat “no task yet” as permission to explore first.

---

# 🛡️ PRE-INSTALL SECURITY GATE (CRITICAL)

**Goal: never let untrusted dependency code execute before it has been reviewed.**

Claude must follow this order for **any dependency-related work**.

## Phase 1 — Inspect Before Installation

1. Inspect `package.json` and all relevant lockfiles first.
2. Identify:

   * New packages
   * Version changes
   * Dependency ranges
   * Direct dependencies
   * Transitive dependencies
   * Optional dependencies
   * Peer dependencies
   * Lifecycle scripts
   * Git/tarball dependencies
   * Unusual registries
3. Check whether the requested package has a safer established alternative.

## Phase 2 — Static Review

Before installing an unfamiliar or replacement dependency:

* Review known metadata/source where available.
* Check lifecycle scripts.
* Check suspicious install behavior.
* Check unnecessary filesystem access.
* Check unexpected network activity.
* Check obfuscation.
* Check package provenance where available.
* Check known vulnerability information.

**Do not execute the package during this review.**

## Phase 3 — Safe Installation

When installation is eventually approved:

1. Prefer:

```bash
npm ci --ignore-scripts
```

or:

```bash
npm install --ignore-scripts
```

2. Immediately run available dependency/security checks.
3. Only enable lifecycle scripts if explicitly required and the dependency has been reviewed.
4. Never run a normal installation of an unfamiliar package before its lifecycle scripts and dependency information have been reviewed.

## Critical Rule

If a package looks suspicious because of:

* typosquatting
* dependency confusion
* unexpected lifecycle scripts
* unexpected network access
* unexpected filesystem access
* heavy obfuscation
* credential/environment access
* cryptocurrency-mining behavior
* unrelated functionality
* suspicious binaries
* unexpected remote downloads

then:

**STOP → REPORT → DO NOT INSTALL → RECOMMEND A SAFE ALTERNATIVE.**

Do not continue automatically.

### Important

Never use:

```bash
npm install
```

as the first step when investigating an unfamiliar dependency.

Never use:

```bash
npm audit fix
```

as a substitute for dependency review.

Never execute:

```bash
npx <unknown-package>
```

because `npx` may download and execute a package.

---

# 🛡️ DEPENDENCY & VULNERABILITY SCANNERS (SCA)

These tools may be used when relevant and available:

### npm audit

Built-in npm dependency vulnerability scanner.

Prefer:

```bash
npm audit --audit-level=moderate
```

### @nodesecure/scanner

Dependency-tree and AST-oriented security analysis.

### Retire.js

Detects known vulnerable JavaScript libraries.

### Coverage

When relevant, review:

* Direct dependencies
* Transitive dependencies
* `package.json`
* Lockfiles
* Existing `node_modules`
* New / updated packages
* Installation scripts
* `preinstall`
* `install`
* `postinstall`
* `prepare`

Do not install a scanner solely for the purpose of running the scanner if doing so would violate the Pre-Install Security Gate.

---

# 🔍 STATIC APPLICATION SECURITY TESTING (SAST)

Scan actual application source code when relevant.

Possible tools include:

* `nodejsscan`
* Semgrep
* ESLint security plugins
* `eslint-plugin-security`

Look for:

* Injection vulnerabilities
* Insecure authentication
* Authorization problems
* Unsafe command execution
* Unsafe filesystem operations
* Hardcoded secrets
* Unsafe deserialization
* RCE risks
* Dynamic code execution
* Insecure configuration
* Dangerous dependency usage
* Exposed credentials
* Sensitive data leakage

Security checks must remain proportional to the task.

---

# 🔎 MALICIOUS CODE & PACKAGE REVIEW

Before installing, executing, or trusting unfamiliar packages/modules/scripts, inspect for:

* Lifecycle scripts
* Obfuscated code
* Encoded payloads
* Unexpected shell execution
* Unexpected network requests
* Hidden downloads
* Data exfiltration
* Credential access
* Environment-variable harvesting
* SSH key access
* Browser credential access
* Suspicious filesystem operations
* Cryptocurrency mining
* Dependency confusion
* Typosquatting
* Unexpected binaries
* Persistence mechanisms
* Behavior unrelated to the package's stated purpose

If a serious issue is found:

1. Stop.
2. Report the finding.
3. Do not execute the suspicious code.
4. Recommend removal, replacement, or a verified version.
5. Continue only after the concern has been addressed.

> **Security principle: Scan first. Trust later. Implement only after relevant checks are complete.**

---

# 📋 GENERAL WORKING RULES

* Never commit yourself. Do not run `git commit`, `git push`, or any commit-related commands unless the user explicitly asks.
* Never add yourself as an author, co-author, or contributor in commits, PRs, changelogs, or file headers.
* Never add `Co-authored-by: Claude`.
* Never add `Generated by Claude`.
* Never add Claude, ChatGPT, AI, assistant, or any AI identity as an author.
* Focus strictly on the user-provided functionality.
* Extract the exact feature/task and implement only that.
* Do not invent extra features.
* Do not perform unsolicited refactoring.
* Do not expand scope.
* Minimize token usage.
* Avoid unnecessary comments.
* Avoid verbose summaries.
* Prefer concise, direct action.
* Prefer surgical, minimal changes.
* Touch only files required for the current task.
* If a task is ambiguous, ask a short clarifying question instead of assuming.
* Do not add tests, documentation, or configuration changes unless explicitly requested as part of the current task.
* Stay silent on process when possible; just do the work and update the tracker.
* Never break or regress previously completed features.

---

# 👤 UNIVERSAL TASK AUTHOR RULE

The `Author` field must **always contain the verified GitHub username responsible for the task.**

## Mandatory Rules

* `Author` = GitHub username only.
* Never use Claude, ChatGPT, AI, assistant, system, or any AI identity as the author.
* Never use a person's real name unless that is also their verified GitHub username.
* Never use an email address.
* Never invent a GitHub username.
* If the task explicitly provides a GitHub username, use it.
* If the GitHub username can be safely verified from the repository/GitHub context, use it.
* If the GitHub username cannot be determined safely, use:
  `Author: <GitHub username required>`
* Do not assume the repository owner is automatically the author unless the username is verified.
* Claude must never add itself as an author, co-author, contributor, or credit.

## Correct Format

```md
> *Author: github-username*
```

## Invalid Formats

Never use:

```md
> *Author: Claude*
```

```md
> *Author: ChatGPT*
```

```md
> *Author: AI*
```

```md
> *Author: Aftab Ahmad Khan*
```

unless `Aftab Ahmad Khan` is verified to be the GitHub username.

---

# 📝 UNIVERSAL TASK COMMENT / TRACKER RULE

Every tracked task **must have a concise comment directly below the corresponding task entry.**

This applies to:

* `feat`
* `fix`
* `security`
* `update`
* `issue`
* `feat/fix`
* Any other tracked work

The comment must:

* Be directly below the task entry.
* Explain what was done or what needs to be done.
* Mention important implementation details when relevant.
* Reflect the actual current status.
* Remain concise and factual.
* Never contain invented information.
* Never contain unrelated commentary.

## When Adding a Task

```md
### New / Uncompleted

- [ ] **feat(N)**: short description of the requested work
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Author: github-username*
  > *Comment: Briefly describe what needs to be done.*
```

## When Completing a Task

```md
### Completed

- [x] **feat(N)**: short description of the requested work
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Completed: YYYY-MM-DD HH:MM PKT*
  > *Author: github-username*
  > *Comment: Brief summary of what was implemented and the final result.*
  > *Token Usage: <usage if available>*
```

## When a Task Is Blocked

```md
- [ ] **issue(N)**: short description
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Author: github-username*
  > *Comment: Blocked because <specific reason>. Remaining work: <specific action>.*
```

## Tracker Rules

1. Create the task entry first.
2. Immediately place the comment directly underneath it.
3. Keep the comment synchronized with actual work.
4. When work progresses, update the comment accordingly.
5. When work is completed, mark the task `[x]`.
6. Update the comment with the final result.
7. Never leave a tracked task without a comment.
8. Never create a separate comments section for individual task comments.
9. Do not write lengthy explanations inside comments.
10. Do not claim something was completed unless it was actually completed.
11. Do not claim a security scan was clean if issues were found.
12. If security issues prevent implementation, record that fact in the task comment.
13. The author must always be the verified GitHub username.

---

# 📊 TRACKER WORKFLOW

When receiving new work, Claude must:

1. Parse the request.
2. Determine the type:

   * `feat`
   * `fix`
   * `security`
   * `update`
   * `issue`
   * `feat/fix`
3. Normalize the request.
4. Assign the next sequential number `N`.
5. Add the task as unchecked.
6. Immediately add its Task Comment.
7. Perform the required security checks.
8. Complete only the requested work.
9. Update the Task Comment during completion when necessary.
10. Mark the task `[x]` when successfully completed.
11. Add:

* completion date
* completion time
* notes
* verified GitHub author
* token usage

12. Update `Last updated`.
13. Update the daily token total.

---

# 📌 STANDARD TRACKER ENTRY FORMAT

## New / Uncompleted

```md
### New / Uncompleted

- [ ] **type(N)**: short description of the requested work
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Author: github-username*
  > *Comment: Briefly describe what needs to be done.*
```

## Completed

```md
### Completed

- [x] **type(N)**: short description of the requested work
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Completed: YYYY-MM-DD HH:MM PKT*
  > *Author: github-username*
  > *Comment: Brief summary of the implementation and final result.*
  > *Token Usage: <usage if available>*
```

---

# 📁 PROJECT STRUCTURE

Root folders:

```text
api.domainname.com/
web.domainname.com/
```

### Backend

`api.domainname.com`

Contains backend/API functionality.

### Frontend

`web.domainname.com`

Contains frontend/client functionality.

Maintain proper separation between API and client code.

---

# 🧹 CODE QUALITY

* No source file should exceed approximately 400 lines.
* Maintain a clean and professional folder structure.
* Use meaningful variable names.
* Use meaningful function names.
* Use meaningful class names.
* Avoid funky, cryptic, or abbreviated naming.
* Maintain proper separation of concerns.
* Keep API and client responsibilities separated.
* Prefer reusable code over unnecessary duplication.
* Avoid unnecessary abstraction.
* Do not refactor unrelated code.

---

# 🎨 FRONTEND — web.domainname.com

* Use reusable components.
* Extract reusable components cleanly.
* Use Tailwind CSS.
* Maintain proper theme variables.
* Define reusable:

  * colors
  * spacing
  * radii
  * typography
  * component tokens

## Dark / Light Mode

The frontend must support:

* System preference detection.
* Manual theme toggle.
* Persistent user preference.
* No flash of incorrect theme during initial load.

Do not introduce a theme system change unless required by the current task.

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
* database access
* file uploads
* command execution
* filesystem access
* deployment
* environment variables
* external services

must receive an appropriate security review before implementation.

Do not weaken an existing security control merely to make a feature work.

If a requested implementation creates a significant security concern:

**STOP → REPORT → ASK FOR DIRECTION.**

---

# 🚫 DANGEROUS COMMAND RULE

Claude must not execute commands that can cause destructive or system-wide changes unless explicitly required and explicitly approved by the user.

Examples include:

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

If a destructive command appears necessary:

1. Stop.
2. Explain exactly what it would do.
3. Ask for explicit approval.
4. Never assume approval.

---

# 🌐 NETWORK / EXTERNAL RESOURCE RULE

Do not download or execute unknown external content.

Before using:

* remote scripts
* curl-piped scripts
* wget-piped scripts
* unknown binaries
* unverified installers
* unknown npm packages
* external executables

perform appropriate review first.

Never blindly execute:

```bash
curl <url> | bash
```

or:

```bash
wget <url> | sh
```

---

# 📦 DEPENDENCY CHANGE RULE

Any dependency change requires:

1. Identify why the dependency is needed.
2. Inspect the existing dependency configuration.
3. Check for an existing package that already provides the functionality.
4. Review the proposed package.
5. Review its version and dependency requirements.
6. Review lifecycle scripts.
7. Review known security issues.
8. Prefer established alternatives.
9. Install with scripts disabled initially where practical.
10. Scan after installation.
11. Only enable lifecycle scripts when necessary and explicitly justified.

Never add a dependency simply because it is convenient.

---

# 🧪 TESTING RULE

Do not add tests unless explicitly requested.

When testing is already available in the project:

* Prefer existing tests.
* Do not modify unrelated tests.
* Do not disable tests merely to make the task pass.
* Do not hide failures.
* Report failures honestly.

For dependency/security work, never execute potentially unsafe dependency code merely to obtain a test result.

---

# 🔄 REGRESSION RULE

Before completing a task:

* Verify the requested functionality.
* Ensure existing functionality was not intentionally removed.
* Review changed files.
* Check for accidental changes.
* Confirm security requirements remain intact.

Do not expand scope merely to improve unrelated areas.

---

# 📌 TASK SCOPE RULE

The user's current request defines the scope.

Claude must not automatically:

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

unless explicitly requested.

---

# 🛑 STOP CONDITIONS

Claude must stop and report instead of continuing if:

* A serious security issue is discovered.
* A dependency appears malicious or highly suspicious.
* A command could damage the operating system.
* A command could delete significant project data.
* Credentials are discovered.
* A required dependency cannot be safely reviewed.
* The requested change conflicts with an existing security control.
* The requested behavior is ambiguous and implementation would require guessing.
* The task requires access outside the repository without explicit authorization.

When stopped:

1. Explain the issue concisely.
2. State what was discovered.
3. State what was not changed.
4. State what decision or approval is required.

---

# 📅 TRACKER DATE / TIME

Use Pakistan Standard Time (PKT / UTC+05:00) for tracker timestamps.

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

Update the daily token total when the project's tracker supports it.

---

# 🔒 FINAL SECURITY PRINCIPLE

> **Scan first. Trust later. Change minimally. Execute only what is necessary.**

Security checks are mandatory before relevant actions.

Never bypass the security gate merely because a task appears simple.

Never trade security for convenience.

Never install first and investigate later.

Never execute unknown code to determine whether it is safe.

**Security comes before implementation.**
