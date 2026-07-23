# AGENTS.md

Guidance for AI coding agents working in **ai-dev-guardrails** or any project that consumes this pack.

This repo combines three layers:

| Layer | Location | Role |
|-------|----------|------|
| **SRS** | [`SRS.md`](SRS.md) | Project description + living task board (read first; mark tasks done) |
| **Rules** | [`Rules.md`](Rules.md), `client_side/`, `server_side/`, `security/`, `devops/` | Quality, security, DevOps standards — apply only what fits the project |
| **Lifecycle skills** | [`skills/`](skills/) | Production workflows (spec → ship) in this pack |

## Mandatory loop

1. **Read `SRS.md`** — pick an open task; set it `in_progress`.
2. **Pick skills** — if a lifecycle skill applies, follow it (`skills/<name>/SKILL.md`). Start with `using-agent-skills` when unsure.
3. **Apply rules** — only CS/SS/SEC/OPS sections that match the project type; mark others `N/A`.
4. **Complete** — mark the task `done` in `SRS.md` (date + notes); emit the compliance report from the README.

## Intent → skill mapping

- Underspecified ask → `interview-me` / `idea-refine` / `spec-driven-development`
- Planning → `planning-and-task-breakdown`
- Implementation → `incremental-implementation` + `test-driven-development`
- UI → `frontend-ui-engineering`
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

See [`docs/getting-started.md`](docs/getting-started.md) and [`AGENTS.md`](../AGENTS.md).

## Cursor

```bash
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails
# or from a local clone:
mkdir -p .cursor/skills && rsync -a skills/ .cursor/skills/
```

See [`docs/cursor-setup.md`](docs/cursor-setup.md). Keep short policies in `.cursor/rules/*.mdc` — do not paste full `SKILL.md` bodies into rules.

## Anti-patterns

- Skipping `SRS.md` when it exists
- Implementing when a Define/Plan skill clearly applies
- Forcing every rule pack on a frontend-only or library project
- Marking compliance `PASS` without checking
