# ⌨️ Slash Commands Deck

> Lifecycle stubs for Antigravity (TOML) and Claude (Markdown).

| Command | Files | Phase |
|---------|-------|-------|
| `/spec` | [`spec.toml`](spec.toml) · [`claude/spec.md`](claude/spec.md) | Define |
| `/plan` | [`planning.toml`](planning.toml) · [`claude/plan.md`](claude/plan.md) | Plan |
| `/build` | [`build.toml`](build.toml) · [`claude/build.md`](claude/build.md) | Build |
| `/test` | [`test.toml`](test.toml) · [`claude/test.md`](claude/test.md) | Verify |
| `/scan` | [`scan.toml`](scan.toml) · [`claude/scan.md`](claude/scan.md) | Verify — functionality X-ray |
| `/review` | [`review.toml`](review.toml) · [`claude/review.md`](claude/review.md) | Review |
| `/code-simplify` | [`code-simplify.toml`](code-simplify.toml) · [`claude/code-simplify.md`](claude/code-simplify.md) | Review |
| `/webperf` | [`webperf.toml`](webperf.toml) · [`claude/webperf.md`](claude/webperf.md) | Review |
| `/ship` | [`ship.toml`](ship.toml) · [`claude/ship.md`](claude/ship.md) | Ship |

## Pair with skills

```text
/scan  → skill project-functionality-scan → SCAN-REPORT.md + SCAN-REPORT.svg
/test  → test-driven-development / browser-testing-with-devtools
/ship  → shipping-and-launch + push-report
```

Full skill list: [`../skills/COMMANDS.md`](../skills/COMMANDS.md) · Design: [`../design/COMMANDS.md`](../design/COMMANDS.md)
