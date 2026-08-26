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
   - Inspect top-level structure (skip `node_modules`, `.git`, build artifacts).
   - Search for secrets / credentials patterns (`.env*`, hardcoded keys, API tokens).
   - Inspect `package.json` / lockfiles.
   - Run available SCA tools (see below).
   - Flag install scripts, suspicious packages, or obvious SAST issues in entry points.
2. Output a short **Security Status** paragraph (Clean / Issues found + brief list).
3. Only then:
   - If a concrete task was already given → extract it, add to tracker, implement.
   - If no task yet → show Security Status and ask what to work on.

Never skip the security gate. Never treat “no task yet” as permission to explore first.

## Pre-Install Security Gate (CRITICAL)

**Goal: never let untrusted code land in the working tree before it is scanned.**

Claude must follow this order for any dependency work:

1. Inspect `package.json` / lockfile first (new packages, version ranges, lifecycle scripts).
2. Prefer `npm ci --ignore-scripts` (or `npm install --ignore-scripts`) so no `preinstall` / `install` / `postinstall` scripts run.
3. Immediately run:
   - `npm audit --audit-level=moderate`
   - `@nodesecure/scanner` (when available)
   - Retire.js (when available)
4. Only if the scan is clean (or issues are explicitly accepted by the user) may scripts be enabled (`npm rebuild` or re-install without `--ignore-scripts`).
5. Never run a full `npm install` that executes lifecycle scripts before the audit step.
6. Never commit `node_modules`. Confirm it is gitignored. If present in the repo, stop and report.

If a package looks suspicious (typosquat name, unexpected network/filesystem access, heavy obfuscation, crypto-mining patterns, or unrelated behavior):
- Stop
- Report
- Do not enable scripts
- Prefer a known-safe alternative or pin a verified version

## 🛡️ Dependency & Vulnerability Scanners (SCA)
These tools recursively walk `node_modules` or package manifests for known vulnerabilities (CVEs) and malicious code.

- **npm audit** — Built-in npm scanner.  
  Docs: https://docs.npmjs.com/cli/v10/commands/npm-audit  
  Prefer: `npm audit --audit-level=moderate`

- **@nodesecure/scanner** — Walks dependency trees + AST analysis for suspicious patterns.  
  https://www.npmjs.com/package/@nodesecure/scanner

- **Retire.js** — Finds known vulnerable JavaScript library files.

Cover (when relevant):
- Direct + transitive dependencies
- New / updated packages
- `node_modules`, `package.json`, lock files
- Installation scripts (`preinstall`, `install`, `postinstall`)

## 🔍 Static Application Security Testing (SAST)
Scan actual source code (not just dependencies) for insecure patterns.

- **nodejsscan (njsscan)** — Semgrep-powered Node.js security scanner.  
  https://github.com/ajinabraham/nodejsscan

- **ESLint Security Plugins** — e.g. `eslint-plugin-security` for development-time detection.

Look for:
- Injection vulnerabilities
- Insecure auth / authorization
- Unsafe command / file operations
- Hardcoded secrets
- Unsafe deserialization
- RCE risks
- Insecure configurations
- Dangerous dynamic code execution

## Malicious Code & Package Review
Before installing, executing, or trusting unfamiliar packages/modules/scripts:

Pay special attention to:
- Lifecycle scripts (`preinstall`, `install`, `postinstall`)
- Obfuscated / heavily encoded code
- Unexpected shell execution or network calls
- Hidden downloads / data exfiltration
- Access to credentials, env vars, SSH keys
- Suspicious filesystem operations
- Cryptocurrency mining
- Dependency confusion / typosquatting
- Behavior unrelated to the package’s stated purpose

If a serious issue is found:
1. Stop immediately.
2. Report concisely.
3. Prefer safe alternative / patch / removal.
4. Continue only after the concern is addressed.

> **Security principle: Scan first. Trust later. Implement only after relevant checks are complete.**

Security checks must be proportional. Do not re-run full scans on every tiny change when nothing relevant changed.

---

## General Working Rules
- Never commit yourself. Do not run `git commit`, `git push`, or any commit-related commands unless the user explicitly asks.
- Never add yourself as an author, co-author, or contributor in commits, PRs, changelogs, or file headers (no `Co-authored-by: Claude`, no `Generated by Claude`, no self-attribution).
- Focus strictly on the user-provided functionality. Extract the exact feature/task and implement only that. Do not invent extra features, polish, refactor, or expand scope.
- Minimize token usage: avoid long explanations, unnecessary comments, verbose summaries, or re-stating the prompt. Prefer concise, direct action.
- Do not waste tokens on content the user did not request (marketing copy, extra docs, decorative text, unsolicited improvements).
- Prefer surgical, minimal changes. Touch only the files required for the current feature.
- If a task is ambiguous, ask a short clarifying question instead of assuming and over-building.
- Do not add tests, docs, or config changes unless the user explicitly requested them as part of the current feature.
- Stay silent on process when possible; just do the work and update the tracker.
- Never break or regress previously completed features.

## Project structure
- Root folders named:
  - `api.domainname.com` (backend)
  - `web.domainname.com` (frontend)

## Code quality
- No source file exceeds ~400 lines of code
- Clean, professional folder structure
- Meaningful, professional variable / function / class names (no funky or abbreviated style)
- Proper separation of concerns (API vs client)

## Frontend (web.domainname.com)
- Reusable components extracted cleanly
- Tailwind CSS set up with proper theme variables (colors, spacing, radii, etc.)
- Professional dark / light mode support:
  - System preference detection
  - Manual toggle
  - Persistent preference
  - No flash of wrong theme

---

## User Prompt / Features

**How user adds work (any of these are fine):**
1. `feat ....`
2. `fix ....`
3. `security ....`
4. `update ....`
5. `issue ....`
6. `feat/fix ....`
7. Plain description

**What Claude does when receiving new work:**
1. Parse the request and determine type (`feat` / `fix` / `security` / `update` / `issue`).
2. Normalize into the standard entry below.
3. Assign next sequential number `N`.
4. Add as unchecked.
5. Perform security-first checks (including Pre-Install Security Gate when dependencies are involved).
6. Complete only the requested work.
7. Mark completed with date, time, notes, author, and token usage.
8. Update “Last updated” and daily token total.

**Standard entry format (Claude writes this):**

### New / Uncompleted
```md
- [ ] **type(N)**: short description of the requested work
  > *Added: YYYY-MM-DD HH:MM PKT*
  > *Author: <name if provided>*
