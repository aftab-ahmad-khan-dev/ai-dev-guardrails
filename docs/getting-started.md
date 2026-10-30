# Getting Started — Ai-dev-guardrails

Install this pack as **skills** in any AI coding agent. Works with Cursor, Claude Code, Codex, Gemini CLI, Copilot, OpenCode, Windsurf, and anything that accepts Agent Skills (`SKILL.md`) or Markdown instructions.

## One-command install (recommended)

The open [skills CLI](https://github.com/vercel-labs/skills) detects your agent and installs into the right directory:

```bash
# Install all skills from this pack
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails

# Browse first
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails --list

# Install only the meta skill + essentials
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails --skill ai-dev-guardrails
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails --skill using-agent-skills
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails --skill test-driven-development
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails --skill code-review-and-quality
```

After install, also copy (or keep) at the **project root**:

- [`SRS.md`](../SRS.md) — project description + task board  
- [`Rules.md`](../Rules.md) — standards (or the YAML packs you need)

## How it works

```
SRS.md (what)  +  Rules.md (standards)  +  skills/* (how)
```

1. Agent reads **`SRS.md`** and picks an open task.  
2. Agent follows matching **lifecycle skills** under `skills/`.  
3. Agent enforces applicable **rules** only.  
4. Agent marks the task **done** in `SRS.md` and reports compliance.

Entrypoint skill: [`ai-dev-guardrails`](../skills/meta/ai-dev-guardrails/SKILL.md).

## Manual install (any agent)

### Option A — Paste

1. Clone or download this repo.  
2. Paste [`skills/meta/ai-dev-guardrails/SKILL.md`](../skills/meta/ai-dev-guardrails/SKILL.md) into the agent system prompt or rules.  
3. Add `SRS.md` + `Rules.md` to the project.  
4. Load other `skills/<name>/SKILL.md` files as needed for the task.

### Option B — Skills directory

Copy folders into your agent’s skills path:

| Agent | Typical path |
|-------|----------------|
| Cursor | `.cursor/skills/<name>/SKILL.md` |
| Claude Code | `.claude/skills/<name>/SKILL.md` |
| Codex / many | `.agents/skills/<name>/SKILL.md` |

```bash
# Example: Cursor from a local clone
mkdir -p .cursor/skills
rsync -a /path/to/ai-dev-guardrails/skills/ .cursor/skills/
```

## Tool-specific guides

| Tool | Guide |
|------|-------|
| Cursor | [cursor-setup.md](cursor-setup.md) |
| Claude / marketplace | [getting-started.md](getting-started.md) + Claude plugin docs |
| Copilot | [copilot-setup.md](copilot-setup.md) |
| Gemini CLI | [gemini-cli-setup.md](gemini-cli-setup.md) |
| Codex | [codex-setup.md](codex-setup.md) |
| OpenCode | [opencode-setup.md](opencode-setup.md) |
| Antigravity | [antigravity-setup.md](antigravity-setup.md) |
| Windsurf | [windsurf-setup.md](windsurf-setup.md) |

## Minimal vs full

**Minimal:** `ai-dev-guardrails` + `spec-driven-development` + `test-driven-development` + `code-review-and-quality`

**Full lifecycle:** install all skills; load only the ones matching the current phase (don’t dump every skill into context at once).

## Next

- [Adoption guide](adoption-guide.md) for team rollout  
- [Skill anatomy](skill-anatomy.md) if you author new skills  
- [AGENTS.md](../AGENTS.md) for the combined rules + skills loop
