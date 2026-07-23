# Skill installation guide

Install **ai-dev-guardrails** as Agent Skills in Cursor, Claude Code, Codex, Gemini CLI, Copilot, OpenCode, Windsurf, and any tool that supports `SKILL.md`.

**Version:** 2.3.1  
**Repo:** https://github.com/aftab-ahmad-khan-dev/ai-dev-guardrails

---

## 1. One-command install (recommended)

Uses the open [skills CLI](https://github.com/vercel-labs/skills) — detects your agent and installs into the correct directory:

```bash
# All 25 skills
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails

# List skills without installing
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails --list

# Meta skill only (SRS + Rules + lifecycle entrypoint)
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails --skill ai-dev-guardrails

# Essentials
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails --skill using-agent-skills
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails --skill test-driven-development
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails --skill code-review-and-quality
```

Useful flags:

```bash
# Global (user-level) instead of project
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails -g

# Target a specific agent
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails -a cursor
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails -a claude-code

# Non-interactive
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails -y --all
```

---

## 2. After install — project files

Copy (or keep) these at the **root of the consuming app**:

| File | Purpose |
|------|---------|
| [`SRS.md`](SRS.md) | Project description + living task board |
| [`Rules.md`](Rules.md) | Standards in one file (or use YAML packs below) |

Optional YAML packs: `client_side/`, `server_side/`, `security/`, `devops/`.

---

## 3. Cursor (local sync)

If you cloned this repo:

```bash
git clone https://github.com/aftab-ahmad-khan-dev/ai-dev-guardrails.git
cd your-app
mkdir -p .cursor/skills
rsync -a ../ai-dev-guardrails/skills/ .cursor/skills/
```

Or from the pack itself:

```bash
mkdir -p .cursor/skills && rsync -a skills/ .cursor/skills/
```

Details: [`docs/cursor-setup.md`](docs/cursor-setup.md)

---

## 4. Manual paste (any AI)

1. Open [`skills/ai-dev-guardrails/SKILL.md`](skills/ai-dev-guardrails/SKILL.md).
2. Paste into the agent system prompt / custom instructions.
3. Add `SRS.md` + `Rules.md` to the project.
4. Load other `skills/<name>/SKILL.md` files when the phase matches (spec, TDD, review, ship).

Typical skill directories:

| Agent | Path |
|-------|------|
| Cursor | `.cursor/skills/<name>/SKILL.md` |
| Claude Code | `.claude/skills/<name>/SKILL.md` |
| Codex / many | `.agents/skills/<name>/SKILL.md` |

---

## 5. What you get

| Piece | Count | Role |
|-------|-------|------|
| Lifecycle skills | 25 | Spec → plan → build → verify → review → ship |
| Meta skill | `ai-dev-guardrails` | Pack entrypoint |
| Agents | 4 | Reviewer, test, security, webperf |
| Commands | 8 | `/spec` `/plan` `/build` `/test` `/review` `/ship` … |
| Rules | CS / SS / SEC / OPS | Quality & security standards |
| SRS | template | Task board the AI must update |

---

## 6. Verify install

```bash
npx skills add aftab-ahmad-khan-dev/ai-dev-guardrails --list
```

You should see `ai-dev-guardrails`, `using-agent-skills`, `test-driven-development`, and the rest of the lifecycle skills.

In the agent session, ask:

> Follow the ai-dev-guardrails skill. Read SRS.md and list open tasks.

---

## 7. More guides

| Guide | Tool |
|-------|------|
| [docs/getting-started.md](docs/getting-started.md) | Universal overview |
| [docs/cursor-setup.md](docs/cursor-setup.md) | Cursor |
| [docs/copilot-setup.md](docs/copilot-setup.md) | GitHub Copilot |
| [docs/gemini-cli-setup.md](docs/gemini-cli-setup.md) | Gemini CLI |
| [docs/codex-setup.md](docs/codex-setup.md) | Codex |
| [docs/opencode-setup.md](docs/opencode-setup.md) | OpenCode |
| [docs/antigravity-setup.md](docs/antigravity-setup.md) | Antigravity |
| [docs/windsurf-setup.md](docs/windsurf-setup.md) | Windsurf |
| [AGENTS.md](AGENTS.md) | Combined rules + skills loop |

---

## License

MIT — Copyright (c) 2026 Aftab Ahmad Khan. See [LICENSE](LICENSE).
