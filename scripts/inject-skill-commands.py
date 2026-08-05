#!/usr/bin/env python3
"""Inject ## ⚡ Command blocks into every SKILL.md and write folder COMMANDS.md catalogs."""
from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

COMMAND_RE = re.compile(r"^## ⚡ Command\s*$", re.M)
FRONT_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def parse_name_desc(text: str) -> tuple[str, str]:
    m = FRONT_RE.match(text)
    name, desc = "", ""
    if m:
        for line in m.group(1).splitlines():
            if line.startswith("name:"):
                name = line.split(":", 1)[1].strip()
            if line.startswith("description:"):
                desc = line.split(":", 1)[1].strip().strip(">").strip()
            elif desc.startswith("") and line.startswith("  ") and "description" in m.group(1):
                # folded description lines
                if not line.strip().startswith("name:") and line.strip():
                    if desc and not desc.endswith(" "):
                        pass
        # better parse description block
        dm = re.search(r"description:\s*>-?\s*\n((?:  .*\n)+)", m.group(1))
        if dm:
            desc = " ".join(x.strip() for x in dm.group(1).splitlines())
        elif "description:" in m.group(1):
            for line in m.group(1).splitlines():
                if line.startswith("description:"):
                    desc = line.split(":", 1)[1].strip()
    return name, desc


def command_block(name: str) -> str:
    slash = name.replace("_", "-")
    return f"""## ⚡ Command

```text
/{slash}
# or ask the agent:
use skill {name}
```

"""


def ensure_command(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    name = path.parent.name
    parsed_name, _ = parse_name_desc(text)
    if parsed_name:
        name = parsed_name
    block = command_block(name)
    if COMMAND_RE.search(text):
        # Refresh existing command block (replace until next ##)
        new_text, n = re.subn(
            r"## ⚡ Command\n\n```text\n.*?```\n\n",
            block,
            text,
            count=1,
            flags=re.S,
        )
        if n:
            if new_text != text:
                path.write_text(new_text, encoding="utf-8")
                return True
            return False
        return False
    # Insert after H1
    m = re.search(r"^# .+$", text, re.M)
    if not m:
        path.write_text(text.rstrip() + "\n\n" + block, encoding="utf-8")
        return True
    insert_at = m.end()
    # skip blank lines after title
    rest = text[insert_at:]
    skip = re.match(r"\n*", rest).end()
    insert_at = insert_at + skip
    new_text = text[:insert_at] + "\n" + block + text[insert_at:].lstrip("\n")
    # ensure single newline after block start
    path.write_text(new_text, encoding="utf-8")
    return True


def collect_skills(base: Path) -> list[tuple[str, str, Path]]:
    rows = []
    for skill_md in sorted(base.glob("**/SKILL.md")):
        # skip nested junk
        if "node_modules" in skill_md.parts:
            continue
        text = skill_md.read_text(encoding="utf-8")
        name, desc = parse_name_desc(text)
        if not name:
            name = skill_md.parent.name
        if not desc:
            # first non-empty non-heading line
            for line in text.splitlines():
                if line.startswith("#") or line.startswith("---") or not line.strip():
                    continue
                if line.startswith("name:") or line.startswith("description:"):
                    continue
                desc = line.strip()
                break
        rows.append((name, desc[:140], skill_md))
    return rows


EMOJI = {
    "meta": "🧭",
    "define": "💡",
    "plan": "🗺️",
    "build": "🔨",
    "design": "🎨",
    "verify": "🧪",
    "review": "🔍",
    "ship": "🚀",
    "style": "✨",
    "steer": "🎛️",
    "motion": "💫",
    "workflow": "🧩",
    "scan": "📡",
    "other": "📦",
}


def classify(name: str) -> str:
    if name in ("ai-dev-guardrails", "using-agent-skills", "using-design-skills", "safe-file-ops"):
        return "meta"
    if name.startswith("style-"):
        return "style"
    if name.startswith("steer-"):
        return "steer"
    if name.startswith("motion-") or name in ("motion-craft", "review-motion", "find-motion"):
        return "motion"
    if name in (
        "anti-slop-frontend", "design-context", "design-steer", "redesign-audit",
        "visual-prototype", "ship-complete-ui", "image-to-code", "brand-kit",
        "stitch-export", "design-system-map", "dark-mode-protocol", "block-library",
        "gpt-strict-taste", "hero-discipline", "landing-persuade", "dashboard-operate",
        "form-ux", "nav-ia", "pricing-page", "marketing-sections", "accessible-ui",
        "performance-ui", "design-tokens", "component-gallery", "competitive-teardown",
        "worlds-commit", "content-first-ui", "iconography", "social-proof",
        "error-pages", "settings-ux",
    ):
        return "design"
    if name in ("interview-me", "idea-refine", "spec-driven-development"):
        return "define"
    if name == "planning-and-task-breakdown":
        return "plan"
    if name in (
        "incremental-implementation", "test-driven-development",
        "frontend-ui-engineering", "api-and-interface-design",
        "context-engineering", "source-driven-development", "doubt-driven-development",
    ):
        return "build"
    if name in ("browser-testing-with-devtools", "debugging-and-error-recovery", "project-functionality-scan"):
        return "verify"
    if name in (
        "code-review-and-quality", "code-simplification",
        "security-and-hardening", "performance-optimization",
    ):
        return "review"
    if name in (
        "git-workflow-and-versioning", "ci-cd-and-automation",
        "deprecation-and-migration", "documentation-and-adrs",
        "observability-and-instrumentation", "shipping-and-launch", "push-report",
    ):
        return "ship"
    if name.startswith(("image-", "brand-", "stitch-", "design-", "dark-", "block-", "gpt-", "hero-", "landing-", "dashboard-", "form-", "nav-", "pricing-", "marketing-", "accessible-", "performance-", "component-", "competitive-", "worlds-", "content-", "iconography", "social-", "error-", "settings-")):
        return "workflow"
    return "other"


def write_catalog(path: Path, title: str, subtitle: str, rows: list[tuple[str, str, Path]], relative_to: Path) -> None:
    by: dict[str, list[tuple[str, str, Path]]] = {}
    for name, desc, p in rows:
        by.setdefault(classify(name), []).append((name, desc, p))

    order = ["meta", "define", "plan", "build", "design", "style", "steer", "motion", "workflow", "verify", "review", "ship", "other"]
    lines = [
        f"# {title}",
        "",
        f"> {subtitle}",
        "",
        f"**{len(rows)} commands** · copy a slash command into chat, or say `use skill <name>`.",
        "",
        "---",
        "",
        "## Quick start",
        "",
        "```text",
        "/using-agent-skills          → pick the right engineering skill",
        "/using-design-skills        → pick the right design approach",
        "/project-functionality-scan → full broken-workflow / CTA / API scan",
        "/push-report                → write REPORT.md before push",
        "/safe-file-ops              → never wipe the repo",
        "```",
        "",
    ]
    for fam in order:
        items = by.get(fam)
        if not items:
            continue
        emoji = EMOJI.get(fam, "📦")
        lines += [f"## {emoji} {fam.title()}", ""]
        lines += [
            "| Command | Skill | What it does |",
            "|---------|-------|--------------|",
        ]
        for name, desc, p in sorted(items, key=lambda x: x[0]):
            rel = p.parent.relative_to(relative_to) if p.is_relative_to(relative_to) else p.parent.name
            lines.append(f"| `/{name}` | [`{name}`]({rel}/SKILL.md) | {desc} |")
        lines.append("")

    lines += [
        "---",
        "",
        "## Tips",
        "",
        "- One skill at a time beats loading everything.",
        "- Design work → start with `/safe-file-ops` + `/using-design-skills`.",
        "- Before push → `/push-report` then check `REPORT.md`.",
        "- Broken product feel → `/project-functionality-scan` then open `SCAN-REPORT.svg`.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    updated = 0
    # All skills under skills/ and design/
    skill_files = list(REPO.glob("skills/*/SKILL.md")) + list(REPO.glob("design/*/SKILL.md")) + list(REPO.glob("design/approaches/*/SKILL.md"))
    for p in skill_files:
        if ensure_command(p):
            updated += 1
    print(f"Updated Command section on {updated} skills")

    skills_rows = collect_skills(REPO / "skills")
    # Prefer skills/ copies for catalog (installable)
    write_catalog(
        REPO / "skills" / "COMMANDS.md",
        "🕹️ Skills Command Deck",
        "Every installable skill in this pack — slash it, don't hunt it.",
        skills_rows,
        REPO / "skills",
    )

    design_rows = collect_skills(REPO / "design")
    write_catalog(
        REPO / "design" / "COMMANDS.md",
        "🎨 Design Command Deck",
        "Taste · steer · style · motion — fun to browse, sharp to run.",
        design_rows,
        REPO / "design",
    )

    # commands/ folder catalog from toml + claude md
    cmd_lines = [
        "# ⌨️ Slash Commands Deck",
        "",
        "> Lifecycle stubs for Antigravity (TOML) and Claude (Markdown).",
        "",
        "| Command | Files | Phase |",
        "|---------|-------|-------|",
        "| `/spec` | [`spec.toml`](spec.toml) · [`claude/spec.md`](claude/spec.md) | Define |",
        "| `/plan` | [`planning.toml`](planning.toml) · [`claude/plan.md`](claude/plan.md) | Plan |",
        "| `/build` | [`build.toml`](build.toml) · [`claude/build.md`](claude/build.md) | Build |",
        "| `/test` | [`test.toml`](test.toml) · [`claude/test.md`](claude/test.md) | Verify |",
        "| `/scan` | [`scan.toml`](scan.toml) · [`claude/scan.md`](claude/scan.md) | Verify — functionality X-ray |",
        "| `/review` | [`review.toml`](review.toml) · [`claude/review.md`](claude/review.md) | Review |",
        "| `/code-simplify` | [`code-simplify.toml`](code-simplify.toml) · [`claude/code-simplify.md`](claude/code-simplify.md) | Review |",
        "| `/webperf` | [`webperf.toml`](webperf.toml) · [`claude/webperf.md`](claude/webperf.md) | Review |",
        "| `/ship` | [`ship.toml`](ship.toml) · [`claude/ship.md`](claude/ship.md) | Ship |",
        "",
        "## Pair with skills",
        "",
        "```text",
        "/scan  → skill project-functionality-scan → SCAN-REPORT.md + SCAN-REPORT.svg",
        "/test  → test-driven-development / browser-testing-with-devtools",
        "/ship  → shipping-and-launch + push-report",
        "```",
        "",
        "Full skill list: [`../skills/COMMANDS.md`](../skills/COMMANDS.md) · Design: [`../design/COMMANDS.md`](../design/COMMANDS.md)",
        "",
    ]
    (REPO / "commands" / "COMMANDS.md").write_text("\n".join(cmd_lines), encoding="utf-8")
    print("Wrote skills/COMMANDS.md, design/COMMANDS.md, commands/COMMANDS.md")


if __name__ == "__main__":
    main()
