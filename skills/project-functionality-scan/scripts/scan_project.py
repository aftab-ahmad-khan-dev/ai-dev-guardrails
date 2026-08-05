#!/usr/bin/env python3
"""Project functionality scanner — findings → SCAN-REPORT.md + SCAN-REPORT.svg."""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

SKIP_DIRS = {
    ".git", "node_modules", "dist", "build", ".next", "coverage",
    ".turbo", ".vercel", "vendor", "__pycache__", ".cache",
    ".claude", ".cursor", ".agents", "pods", ".venv", "venv",
}
CODE_EXT = {
    ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
    ".vue", ".svelte", ".py", ".go", ".rb", ".php",
    ".java", ".kt", ".swift", ".cs",
}
ROUTE_EXT = CODE_EXT | {".mdx"}

@dataclass
class Finding:
    category: str
    severity: str  # critical | high | medium | low | info
    file: str
    line: int
    snippet: str
    message: str
    rule: str


RULES: list[tuple[str, str, str, re.Pattern[str]]] = [
    # category, severity, rule_id, pattern
    ("broken_cta", "high", "href-hash", re.compile(r"""href\s*=\s*['"]#['"]""")),
    ("broken_cta", "high", "href-empty", re.compile(r"""href\s*=\s*['"]['"]""")),
    ("broken_cta", "high", "onclick-empty", re.compile(r"""onClick\s*=\s*\{\s*\(\)\s*=>\s*\{\s*\}\s*\}""")),
    ("broken_cta", "medium", "todo-wire", re.compile(r"""(?i)(TODO|FIXME).{0,40}(wire|button|cta|handler|click)""")),
    ("broken_cta", "medium", "coming-soon-btn", re.compile(r"""(?i)(coming soon|not wired|placeholder click)""")),
    ("broken_workflow", "high", "not-implemented", re.compile(r"""(?i)not[\s_-]?implemented|throw new Error\(\s*['"]TODO""")),
    ("broken_workflow", "medium", "fixme-hack", re.compile(r"""\b(FIXME|HACK|XXX)\b""")),
    ("broken_workflow", "medium", "todo-feature", re.compile(r"""(?i)//\s*TODO[:\s].{0,80}""")),
    ("crash_risk", "critical", "throw-error", re.compile(r"""throw new Error\(""")),
    ("crash_risk", "high", "non-null-assert", re.compile(r"""\w+!\.(map|length|id|data)\b""")),
    ("crash_risk", "medium", "empty-catch", re.compile(r"""catch\s*\([^)]*\)\s*\{\s*\}""")),
    ("crash_risk", "medium", "as-any", re.compile(r"""\bas any\b""")),
    ("api_client", "info", "fetch-call", re.compile(r"""\bfetch\s*\(\s*[`'"][^`'"]+[`'"]""")),
    ("api_client", "info", "axios-call", re.compile(r"""\baxios\.(get|post|put|patch|delete)\s*\(""")),
    ("api_client", "medium", "localhost-hardcode", re.compile(r"""https?://localhost(:\d+)?/""")),
    ("abandoned_stub", "high", "stub-service", re.compile(r"""(?i)(stub|fake|mock)[\s_]*(api|service|client|endpoint)""")),
    ("abandoned_stub", "high", "return-null-todo", re.compile(r"""return null;\s*//\s*(TODO|temp|hack)""", re.I)),
    ("not_integrated", "high", "feature-flag-false", re.compile(r"""(?i)(FEATURE_|ENABLE_|FLAG_).{0,40}(false|0)\b""")),
    ("not_integrated", "medium", "console-log-debug", re.compile(r"""console\.(log|debug|warn)\(""")),
    ("forms", "high", "prevent-default-only", re.compile(r"""preventDefault\(\)\s*;?\s*(\}|//\s*TODO)""")),
    ("tables", "medium", "empty-tbody", re.compile(r"""<tbody>\s*</tbody>""")),
    ("tables", "low", "table-lorem", re.compile(r"""(?i)<t[dh][^>]*>\s*(lorem|placeholder|test)\b""")),
    ("routes", "medium", "link-todo", re.compile(r"""(?i)(Link|href).{0,40}(TODO|coming soon)""")),
    ("crash_risk", "critical", "process-exit", re.compile(r"""process\.exit\([1-9]""")),
]


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def iter_files(root: Path) -> list[Path]:
    out: list[Path] = []
    for p in root.rglob("*"):
        if not p.is_file() or should_skip(p.relative_to(root)):
            continue
        if p.suffix.lower() in CODE_EXT:
            out.append(p)
    return out


def scan_file(root: Path, path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return findings
    rel = str(path.relative_to(root))
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        for category, severity, rule, pat in RULES:
            if pat.search(line):
                findings.append(
                    Finding(
                        category=category,
                        severity=severity,
                        file=rel,
                        line=i,
                        snippet=line.strip()[:160],
                        message=rule.replace("-", " "),
                        rule=rule,
                    )
                )
    return findings


def collect_api_surface(root: Path, files: list[Path]) -> tuple[set[str], set[str]]:
    """Best-effort: client fetch paths vs server route-ish paths."""
    client: set[str] = set()
    server: set[str] = set()
    fetch_re = re.compile(r"""(?:fetch|axios\.(?:get|post|put|patch|delete))\(\s*[`'"]([^`'"]+)[`'"]""")
    route_re = re.compile(r"""(?:app|pages)/(api/.+?)(?:/route\.(?:ts|js)|\.(?:ts|js|tsx|jsx))$""")
    express_re = re.compile(r"""\.(?:get|post|put|patch|delete)\(\s*[`'"](/[^`'"]+)[`'"]""")

    for path in files:
        rel = str(path.relative_to(root)).replace("\\", "/")
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for m in fetch_re.finditer(text):
            url = m.group(1)
            if url.startswith(("/", "http")):
                client.add(url.split("?")[0])
        m = route_re.search(rel)
        if m:
            server.add("/" + m.group(1).replace("/route", ""))
        # Next.js app router: app/api/foo/route.ts → /api/foo
        if "/api/" in rel and rel.endswith(("route.ts", "route.js")):
            idx = rel.find("/api/")
            api_path = "/" + rel[idx + 1 :].rsplit("/", 1)[0]
            server.add(api_path)
        for m in express_re.finditer(text):
            server.add(m.group(1))
    return client, server


def abandoned_api_findings(client: set[str], server: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    # Normalize simple /api/* paths
    def norm(u: str) -> str:
        if u.startswith("http"):
            # keep path only
            from urllib.parse import urlparse
            return urlparse(u).path or u
        return u

    c_paths = {norm(u) for u in client if "/api" in u or u.startswith("/")}
    s_paths = {norm(u) for u in server}

    for c in sorted(c_paths):
        if c.startswith("http"):
            continue
        # if looks like API and no exact server match
        if c.startswith("/api") and c not in s_paths and not any(c.startswith(s) for s in s_paths):
            findings.append(
                Finding(
                    category="abandoned_api",
                    severity="high",
                    file="(client calls)",
                    line=0,
                    snippet=c,
                    message=f"Client calls `{c}` but no matching API route was found",
                    rule="client-without-server",
                )
            )
    for s in sorted(s_paths):
        if s.startswith("/api") and s not in c_paths and not any(c.startswith(s) for c in c_paths):
            findings.append(
                Finding(
                    category="abandoned_api",
                    severity="medium",
                    file="(server routes)",
                    line=0,
                    snippet=s,
                    message=f"API route `{s}` has no detected client caller",
                    rule="server-without-client",
                )
            )
    return findings


def severity_rank(s: str) -> int:
    return {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}.get(s, 9)


def write_markdown(root: Path, findings: list[Finding], meta: dict) -> Path:
    out = root / "SCAN-REPORT.md"
    counts = Counter(f.severity for f in findings)
    by_cat = Counter(f.category for f in findings)
    ts = meta["timestamp"]
    lines = [
        "# SCAN-REPORT — Project Functionality Scan",
        "",
        f"> Generated by skill `project-functionality-scan` · `{ts}`",
        "",
        "## Latest",
        "",
        f"| Field | Value |",
        f"|-------|-------|",
        f"| Root | `{meta['root']}` |",
        f"| Files scanned | {meta['files_scanned']} |",
        f"| Findings | {len(findings)} |",
        f"| Visual | [`SCAN-REPORT.svg`](SCAN-REPORT.svg) |",
        "",
        "### Severity",
        "",
        "| Severity | Count |",
        "|----------|------:|",
    ]
    for sev in ("critical", "high", "medium", "low", "info"):
        lines.append(f"| {sev} | {counts.get(sev, 0)} |")
    lines += ["", "### By category", "", "| Category | Count |", "|----------|------:|"]
    for cat, n in by_cat.most_common():
        lines.append(f"| {cat} | {n} |")

    lines += ["", "### Findings", ""]
    if not findings:
        lines.append("_No heuristic findings. Still run a manual workflow pass._")
    else:
        lines += [
            "| Sev | Category | File | Line | Rule | Detail |",
            "|-----|----------|------|-----:|------|--------|",
        ]
        for f in sorted(findings, key=lambda x: (severity_rank(x.severity), x.category, x.file, x.line)):
            snip = f.snippet.replace("|", "\\|")[:100]
            msg = f.message.replace("|", "\\|")[:80]
            loc = f"`{f.file}`" if f.line == 0 else f"`{f.file}:{f.line}`"
            lines.append(
                f"| {f.severity} | {f.category} | {loc} | {f.line or '—'} | `{f.rule}` | {msg} — `{snip}` |"
            )

    lines += [
        "",
        "### Agent checklist",
        "",
        "- [ ] Review every **critical** / **high** finding (confirm or mark false-positive)",
        "- [ ] Click through primary user workflows manually or via browser tools",
        "- [ ] Verify CTAs hit real handlers / routes",
        "- [ ] Verify API client paths match live handlers",
        "- [ ] Fix or ticket top issues before ship",
        "",
        "### Verdict",
        "",
    ]
    crit = counts.get("critical", 0) + counts.get("high", 0)
    if crit:
        lines.append(f"**NEEDS WORK** — {crit} critical/high findings. See table above.")
    elif findings:
        lines.append("**WATCH** — medium/low findings only; still do a manual pass.")
    else:
        lines.append("**CLEAN (heuristics)** — no pattern hits; runtime QA still recommended.")

    lines += ["", "---", "", "## Machine JSON", "", "```json", json.dumps({
        "meta": meta,
        "counts": dict(counts),
        "by_category": dict(by_cat),
        "findings": [asdict(f) for f in findings[:500]],
    }, indent=2), "```", ""]

    # Preserve prior Latest as history if file exists
    history = ""
    if out.exists():
        old = out.read_text(encoding="utf-8", errors="replace")
        if "## Latest" in old:
            history = "\n## History\n\n<details><summary>Previous scan</summary>\n\n" + old + "\n</details>\n"
    out.write_text("\n".join(lines) + history, encoding="utf-8")
    return out


def write_svg(root: Path, findings: list[Finding], meta: dict) -> Path:
    out = root / "SCAN-REPORT.svg"
    counts = Counter(f.severity for f in findings)
    by_cat = Counter(f.category for f in findings)
    top = sorted(findings, key=lambda x: (severity_rank(x.severity), x.category))[:12]

    colors = {
        "critical": "#E11D48",
        "high": "#F97316",
        "medium": "#EAB308",
        "low": "#38BDF8",
        "info": "#94A3B8",
    }
    total = max(len(findings), 1)
    bar_max_w = 420

    def esc(s: str) -> str:
        return html.escape(s, quote=True)

    # Bars
    y = 210
    bars = []
    for sev in ("critical", "high", "medium", "low", "info"):
        n = counts.get(sev, 0)
        w = int(bar_max_w * (n / total)) if findings else 0
        bars.append(
            f'<text x="48" y="{y + 14}" fill="#E2E8F0" font-size="14" font-family="ui-sans-serif,system-ui">{sev}</text>'
            f'<rect x="130" y="{y}" width="{max(w, 2) if n else 2}" height="18" rx="4" fill="{colors[sev]}" opacity="{0.95 if n else 0.25}"/>'
            f'<text x="{140 + max(w, 2)}" y="{y + 14}" fill="#F8FAFC" font-size="13" font-family="ui-monospace,monospace">{n}</text>'
        )
        y += 32

    # Category chips
    cx, cy = 48, 400
    chips = []
    for cat, n in by_cat.most_common(10):
        label = f"{cat} {n}"
        chips.append(
            f'<rect x="{cx}" y="{cy}" width="{min(20 + len(label) * 7, 200)}" height="26" rx="13" fill="#1E293B" stroke="#334155"/>'
            f'<text x="{cx + 12}" y="{cy + 17}" fill="#F1F5F9" font-size="12" font-family="ui-sans-serif,system-ui">{esc(label)}</text>'
        )
        cx += min(28 + len(label) * 7, 208)
        if cx > 900:
            cx = 48
            cy += 36

    # Top issues
    issue_lines = []
    iy = 520
    for i, f in enumerate(top, 1):
        loc = f.file if f.line == 0 else f"{f.file}:{f.line}"
        text = f"{i}. [{f.severity}] {f.category} — {loc}"
        issue_lines.append(
            f'<text x="48" y="{iy}" fill="#F8FAFC" font-size="13" font-family="ui-monospace,monospace">{esc(text[:110])}</text>'
        )
        iy += 22

    crit_high = counts.get("critical", 0) + counts.get("high", 0)
    verdict = "NEEDS WORK" if crit_high else ("WATCH" if findings else "CLEAN*")
    verdict_color = "#E11D48" if crit_high else ("#EAB308" if findings else "#22C55E")

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="780" viewBox="0 0 1000 780">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0B1220"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
  </defs>
  <rect width="1000" height="780" fill="url(#bg)"/>
  <circle cx="920" cy="80" r="120" fill="#1D4ED8" opacity="0.15"/>
  <circle cx="80" cy="700" r="140" fill="#E11D48" opacity="0.10"/>

  <text x="48" y="64" fill="#F8FAFC" font-size="32" font-weight="700" font-family="ui-sans-serif,system-ui">Project Functionality Scan</text>
  <text x="48" y="92" fill="#94A3B8" font-size="14" font-family="ui-sans-serif,system-ui">ai-dev-guardrails · project-functionality-scan</text>

  <rect x="700" y="40" width="252" height="64" rx="12" fill="#0F172A" stroke="{verdict_color}" stroke-width="2"/>
  <text x="826" y="68" text-anchor="middle" fill="{verdict_color}" font-size="18" font-weight="700" font-family="ui-sans-serif,system-ui">{esc(verdict)}</text>
  <text x="826" y="90" text-anchor="middle" fill="#94A3B8" font-size="12" font-family="ui-sans-serif,system-ui">{len(findings)} findings · {meta["files_scanned"]} files</text>

  <text x="48" y="140" fill="#CBD5E1" font-size="12" font-family="ui-monospace,monospace">{esc(meta["timestamp"])}</text>
  <text x="48" y="160" fill="#64748B" font-size="12" font-family="ui-monospace,monospace">{esc(str(meta["root"])[:90])}</text>

  <text x="48" y="196" fill="#F8FAFC" font-size="18" font-weight="600" font-family="ui-sans-serif,system-ui">Severity mix</text>
  {''.join(bars)}

  <text x="48" y="380" fill="#F8FAFC" font-size="18" font-weight="600" font-family="ui-sans-serif,system-ui">Categories</text>
  {''.join(chips) if chips else '<text x="48" y="420" fill="#64748B" font-size="14">No categories</text>'}

  <text x="48" y="500" fill="#F8FAFC" font-size="18" font-weight="600" font-family="ui-sans-serif,system-ui">Top issues</text>
  {''.join(issue_lines) if issue_lines else '<text x="48" y="530" fill="#64748B" font-size="14">No heuristic hits — still do a manual workflow pass.</text>'}

  <text x="48" y="760" fill="#475569" font-size="11" font-family="ui-sans-serif,system-ui">Open SCAN-REPORT.md for the full table · *CLEAN means heuristics only</text>
</svg>
'''
    out.write_text(svg, encoding="utf-8")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Project functionality scan")
    ap.add_argument("--root", default=".", help="Project root to scan")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 1

    files = iter_files(root)
    findings: list[Finding] = []
    for f in files:
        findings.extend(scan_file(root, f))

    client, server = collect_api_surface(root, files)
    findings.extend(abandoned_api_findings(client, server))

    # Dedupe identical rule+file+line
    seen = set()
    uniq: list[Finding] = []
    for f in findings:
        key = (f.rule, f.file, f.line, f.snippet)
        if key in seen:
            continue
        seen.add(key)
        uniq.append(f)
    findings = uniq

    meta = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "root": str(root),
        "files_scanned": len(files),
        "client_api_samples": sorted(client)[:40],
        "server_api_samples": sorted(server)[:40],
    }
    md = write_markdown(root, findings, meta)
    svg = write_svg(root, findings, meta)
    print(f"Wrote {md}")
    print(f"Wrote {svg}")
    print(f"Findings: {len(findings)} (critical+high={sum(1 for f in findings if f.severity in ('critical','high'))})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
