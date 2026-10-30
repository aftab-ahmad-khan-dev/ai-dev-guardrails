# AGENTS.md

Guidance for AI coding agents working in **ai-dev-guardrails** or any project that consumes this pack.

This repo combines three layers:

| Layer | Location | Role |
|-------|----------|------|
| **SRS** | [`SRS.md`](SRS.md) | Project description + living task board (read first; mark tasks done) |
| **Rules** | [`Rules.md`](Rules.md), `client/`, `server/`, `security/`, `devops/` | Quality, security, DevOps standards — apply only what fits the project |
| **Lifecycle skills** | [`skills/`](skills/) | Production workflows (spec → ship) in this pack |
| **Design skills** | [`design/`](design/) | 60+ approaches + safe-file-ops (mirrored into `skills/` for install) |
| **Push report** | [`REPORT.md`](REPORT.md) · [`skills/push-report`](skills/ship/push-report/SKILL.md) | Per-push security/quality log |

## Mandatory loop

1. **Read `SRS.md`** — pick an open task; set it `in_progress`.
2. **Pick skills** — if a lifecycle skill applies, follow it (`skills/<name>/SKILL.md`). Start with `using-agent-skills` when unsure.
3. **Apply rules** — only CS/SS/SEC/OPS sections that match the project type; mark others `N/A`.
4. **Complete** — mark the task `done` in `SRS.md` (date + notes); emit the compliance report from the README.

## Intent → skill mapping

- Underspecified ask → `interview-me` / `idea-refine` / `spec-driven-development`
- Planning → `planning-and-task-breakdown`
- Implementation → `incremental-implementation` + `test-driven-development`
- UI → `frontend-ui-engineering` + design pack (`using-design-skills` → `anti-slop-frontend` / `design-steer` / `motion-craft`)
- AI-looking UI / polish / distill → `design/` pack ([`design/README.md`](design/README.md))
- API / boundaries → `api-and-interface-design`
- Bugs → `debugging-and-error-recovery`
- Review → `code-review-and-quality`
- Simplify → `code-simplification`
- Security → `security-and-hardening`
- Ship → `shipping-and-launch` / `ci-cd-and-automation`

Slash-command stubs: [`commands/`](commands/) and [`commands/claude/`](commands/claude/).  
Personas: [`agents/`](agents/). Checklists: [`references/`](references/).

## Install (any AI)

```bash
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails
```

See [`docs/getting-started.md`](docs/getting-started.md).

## Cursor

```bash
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails
# or from a local clone — DESTINATION must be .cursor/skills/ ONLY (never ./ , never --delete):
mkdir -p .cursor/skills && rsync -a skills/ .cursor/skills/
# mandatory in the consuming app — do not commit installed skills:
bash scripts/ensure-skills-gitignore.sh .
```

See [`docs/cursor-setup.md`](docs/cursor-setup.md), [`design/README.md`](design/README.md), and [`design/SAFETY.md`](design/SAFETY.md). Keep short policies in `.cursor/rules/*.mdc` — do not paste full `SKILL.md` bodies into rules.

**Installed skills are gitignored** (`.cursor/skills/`, `.agents/skills/`, `skills-lock.json`, …). The upstream pack repo still commits its source `skills/` tree.

## Safety (critical)

- **Never wipe a consuming repo.** Follow [`design/SAFETY.md`](design/SAFETY.md) and `safe-file-ops`.
- Never `rm -rf` project roots, never `git clean -fdx` / `git reset --hard` unless the user explicitly asked in the current message.
- Never `rsync --delete` into a project root. Install skills only into `.cursor/skills/` / `.agents/skills/` / agent skill dirs.
- “Delete losing variants” = only `prototypes/**` or `*.prototype.*` created this session.
- Before push: run `push-report` and update `REPORT.md`.
- Functionality X-ray: `/scan` → `project-functionality-scan` → `SCAN-REPORT.md` + `SCAN-REPORT.svg`.
- Slash cheat-sheets: [`skills/COMMANDS.md`](skills/COMMANDS.md) · [`design/COMMANDS.md`](design/COMMANDS.md) · [`commands/COMMANDS.md`](commands/COMMANDS.md).

## Anti-patterns

- Skipping `SRS.md` when it exists
- Implementing when a Define/Plan skill clearly applies
- Forcing every rule pack on a frontend-only or library project
- Marking compliance `PASS` without checking
- Deleting unrelated files as “cleanup” after installing skills
