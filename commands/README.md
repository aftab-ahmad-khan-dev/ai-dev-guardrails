# commands — Slash Commands

![Commands — /spec /plan /build /test /scan /review /ship](banner.jpg)

Lifecycle slash-command stubs. Copy into your agent’s command directory (or use the installer for your tool).

**Browse the pretty deck:** [`COMMANDS.md`](COMMANDS.md)

| Command | Phase |
|---------|-------|
| `/spec` | Define |
| `/plan` | Plan |
| `/build` | Build |
| `/test` | Verify |
| `/scan` | Verify — functionality X-ray → `SCAN-REPORT.md` + `.svg` |
| `/review` | Review |
| `/code-simplify` | Review |
| `/webperf` | Review |
| `/ship` | Ship |

- Antigravity / TOML: `*.toml` in this folder  
- Claude Markdown: [`claude/`](claude/)  
- Skill wiring: [`../skills/`](../skills/) · [`../skills/COMMANDS.md`](../skills/COMMANDS.md) · [`../docs/getting-started.md`](../docs/getting-started.md)
