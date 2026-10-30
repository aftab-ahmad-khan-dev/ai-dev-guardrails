# Install — the `claude` bundle into your repo

This drops a project-scoped Claude setup into your repo: a tiny `CLAUDE.md` brain, a skills library
(your 8 house skills + 25 lifecycle skills), 4 specialist agents, a repo malware scanner, and a
clone/pull auto-scan hook. Plus `.gitignore` rules so workspace/editor/Reticle state and secrets
never get pushed.

## 1. Place the files (run from your repo root)
```bash
# from inside the unzipped 'claude' folder:
cp CLAUDE.md               /path/to/your/repo/CLAUDE.md
cp -R dot-claude           /path/to/your/repo/.claude      # becomes the repo's .claude/ folder
chmod +x /path/to/your/repo/.claude/hooks/scan-on-clone-pull.sh
chmod +x /path/to/your/repo/.claude/tools/repo-malware-scan.sh
cat gitignore-additions.txt >> /path/to/your/repo/.gitignore
cp ATTRIBUTION.md          /path/to/your/repo/.claude/ATTRIBUTION.md
```
If `.claude/settings.json` already exists in your repo, don't overwrite it — open both and paste the
`"hooks"` block in. Install `jq` if you haven't: `brew install jq`.

## 2. ⚠️ Untrack what's already in the repo (critical)
`.gitignore` only stops NEW files. Anything already committed — most importantly `.vscode/`, which is
how the malware got in — stays tracked until you remove it. Run:
```bash
cd /path/to/your/repo
git rm -r --cached .vscode .idea .reticle 2>/dev/null
git rm --cached .env .env.* 2>/dev/null
git add .gitignore
git commit -m "chore: ignore workspace/editor/local state and secrets; stop tracking them"
```
This removes them from the repo on the next push WITHOUT deleting your local copies.

## 3. Scan the repo once now
```bash
.claude/tools/repo-malware-scan.sh --report-only .
```
Review the report before trusting the repo. To quarantine findings, re-run without `--report-only`.

## How this behaves
- **On every `git clone`/`git pull`** (with the hook installed) the repo is auto-scanned and a short
  report is surfaced. `.gitignore` stops you *pushing* workspace files; the scanner catches workspace
  malware that *arrives* in a pull — two different layers, both needed.
- **Skills load on demand**: only short descriptions are always in context; a skill's full body loads
  only when its task comes up, so simple turns stay cheap.
- **Global vs project**: this is a project (repo) install. To use the same setup everywhere, copy
  `CLAUDE.md` to `~/.claude/CLAUDE.md` and the `dot-claude/` contents into `~/.claude/` instead —
  but do NOT globally install any third-party project's own CLAUDE.md; only this brain + the skills.

## Attribution
The 25 lifecycle skills and 4 agents are from Addy Osmani's MIT-licensed `agent-skills`
(https://github.com/addyosmani/agent-skills). See `ATTRIBUTION.md`.
