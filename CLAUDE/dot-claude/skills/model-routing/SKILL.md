---
name: model-routing
description: Use when deciding how to delegate work to sub-agents and which model to assign. Covers the routing table and delegation flow.
---
# Smart model routing & delegation

- Never do real work yourself — dispatch a sub-agent. One per discrete task. Always pass `model` (cheapest capable).
- Plan first, then dispatch.

| Model       | Use for                                               | Avoid for                 |
|-------------|-------------------------------------------------------|---------------------------|
| **Fable 5.1** | Architecture, hard bugs, deep review, complex reasoning | Simple edits, lookups     |
| **Opus 5.5**  | Edits, tests, docs, refactors, implementation         | Pure lookups / summaries  |
| **Haiku 4.5** | Lookups, summaries, quick facts, extraction           | Any real reasoning or code|

Flow: understand task → map to the right skill → break into smallest tasks → assign lightest capable model →
dispatch one sub-agent with a clear brief + `model` → verify → next task / tracker update.
Exceptions: pure conversation or one-liners → answer directly; user forces a model → honour it.
