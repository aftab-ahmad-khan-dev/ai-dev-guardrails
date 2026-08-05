---
name: project-functionality-scan
description: >-
  Full project functionality scan for broken workflows, CTAs, buttons, tables,
  crash risks, API endpoints, abandoned APIs, dead routes, and unfinished
  integrations. Writes SCAN-REPORT.md and a visual SCAN-REPORT.svg. Use when
  the user asks for a project scan, functionality audit, broken-path hunt, or
  /scan /project-scan.
---

# Project Functionality Scan

## ⚡ Command

```text
/scan
/project-scan
/project-functionality-scan
# or ask the agent:
use skill project-functionality-scan
# script
bash skills/project-functionality-scan/scripts/run-scan.sh --root .
```

## Overview

Static + heuristic **functionality X-ray** of a codebase. Surfaces what is broken, unfinished, or likely to crash — then ships two artifacts:

| Artifact | Purpose |
|----------|---------|
| `SCAN-REPORT.md` | Full findings table (human + agent readable) |
| `SCAN-REPORT.svg` | Visual poster of severity counts + top issues |

Does **not** delete files. Follow `safe-file-ops`.

## When to use

- “Scan my project for broken stuff”
- Pre-QA / pre-launch functionality audit
- After a large AI-generated feature dump
- Hunting dead CTAs, abandoned APIs, unfinished paths

## What it checks

| Category | Examples |
|----------|----------|
| **Broken CTAs / buttons** | `href="#"`, empty `onClick`, `TODO: wire`, buttons with no handler |
| **Tables** | Tables without keys/rows wiring, placeholder-only tables |
| **Crash risks** | `throw new Error`, non-null asserts on optional data, `as any` on hot paths |
| **API endpoints** | `fetch`/`axios` URLs; mismatch vs route handlers |
| **Abandoned APIs** | Handlers never called; client calls with no matching route |
| **Broken workflows** | `NotImplemented`, `FIXME`, `HACK`, `coming soon` in user paths |
| **Broken paths / routes** | Links to missing pages; orphaned route files |
| **Not integrated** | Feature flags always off; stub services; empty catch blocks |
| **Forms** | Submit with `preventDefault` and no API call |
| **Nav / dead ends** | Menu items pointing nowhere |

## Process

### 1. Scope

Confirm project root (default: git toplevel). State stack if known (Next, Vite, Express, …).

### 2. Run the scanner

```bash
bash skills/project-functionality-scan/scripts/run-scan.sh --root .
```

Or, if the agent cannot run scripts: walk the checklist manually and still write both artifacts using the templates in `scripts/`.

### 3. Agent deep pass (required)

Scripts catch patterns; **you** still verify high-severity hits:

1. Open each `critical` / `high` finding
2. Confirm true positive vs false positive
3. Mark `confirmed` / `false-positive` / `needs-runtime` in the report
4. Add any workflow breaks the regex missed (e.g. button looks wired but API 404)

### 4. Publish artifacts

- Update `SCAN-REPORT.md` (newest scan section first or replace `## Latest` — keep history under `## History`)
- Regenerate `SCAN-REPORT.svg` via the script
- Summarize for the user: counts by severity + top 10 fixes

### 5. Optional follow-ups

| Finding type | Next skill |
|--------------|------------|
| UI broken | `frontend-ui-engineering`, `ship-complete-ui` |
| API gaps | `api-and-interface-design` |
| Crashes | `debugging-and-error-recovery` |
| Before push | `push-report` |

## Safety

- Read-only scan — no mass deletes
- Do not commit secrets found in env samples into the report body; redact values
- Ignore `node_modules`, `.git`, `dist`, `build`, `.next`, coverage

## Verification

- [ ] `SCAN-REPORT.md` written with severity counts
- [ ] `SCAN-REPORT.svg` generated
- [ ] Critical/high items agent-reviewed
- [ ] User given a clear “what’s bad” summary
