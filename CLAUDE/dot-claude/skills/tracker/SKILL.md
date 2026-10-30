---
name: tracker
description: Use for tracker and feature work — logging a task, numbering it, adding a comment, and marking it done after verification. The tracker lives in the project's own root CLAUDE.md, never in the global one.
---
# Tracker / feature work

- Tracker lives in the **project's own root CLAUDE.md** (create if missing). Never log tasks in the global ~/.claude/CLAUDE.md.
- Sequential numbering only. Every task gets a Comment. Mark `[x]` only after real completion + verification.
- Scope = exactly what was asked.

**New**
```
- [ ] **type(N)**: short description
> *Added: YYYY-MM-DD HH:MM PKT*
> *Author: github-username*
> *Comment: what needs to be done*
```

**Completed**
```
- [x] **type(N)**: short description
> *Added: ...*
> *Completed: YYYY-MM-DD HH:MM PKT*
> *Author: github-username*
> *Comment: what was done*
> *Token Usage: <number>*
```
