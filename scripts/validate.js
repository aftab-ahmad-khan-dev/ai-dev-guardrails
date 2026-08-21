#!/usr/bin/env node
/**
 * Self-lint for this pack: YAML rule-pack schema + SKILL.md frontmatter/category
 * placement. Does not touch consuming projects — only checks this repo's own
 * content stays internally consistent. Writes VALIDATION-REPORT.md and exits
 * non-zero on any FAIL so it can sit in a pre-push gate.
 */
"use strict";

const fs = require("fs");
const path = require("path");
const yaml = require("js-yaml");

const REPO = path.resolve(__dirname, "..");

const YAML_PACKS = [
  "client/client-side-rules.yaml",
  "server/server-side-rules.yaml",
  "security/security-rules.yaml",
  "devops/devops-rules.yaml",
];

const RULE_REQUIRED_FIELDS = [
  "id", "title", "status", "severity", "summary", "rules", "do", "dont", "ai_directive",
];
const VALID_SEVERITIES = new Set(["critical", "high", "medium", "low"]);
const VALID_CATEGORIES = new Set([
  "meta", "define", "plan", "build", "design", "verify", "review", "ship",
]);

function walkSkillFiles(base) {
  const out = [];
  (function walk(dir) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) walk(full);
      else if (entry.name === "SKILL.md") out.push(full);
    }
  })(base);
  return out;
}

function parseFrontmatter(text) {
  const m = /^---\n([\s\S]*?)\n---\n/.exec(text);
  if (!m) return null;
  let name = "";
  let hasDescription = false;
  for (const line of m[1].split("\n")) {
    if (line.startsWith("name:")) name = line.slice(5).trim();
    if (line.startsWith("description:")) hasDescription = true;
  }
  return { name, hasDescription };
}

function checkYamlPacks() {
  const results = [];
  const allIds = new Map(); // id -> pack file (cross-pack uniqueness)

  for (const rel of YAML_PACKS) {
    const full = path.join(REPO, rel);
    const packName = path.basename(rel);
    if (!fs.existsSync(full)) {
      results.push({ pack: rel, status: "FAIL", note: "file missing" });
      continue;
    }

    let doc;
    try {
      doc = yaml.load(fs.readFileSync(full, "utf8"));
    } catch (err) {
      results.push({ pack: rel, status: "FAIL", note: `YAML parse error: ${err.message}` });
      continue;
    }

    if (!doc || !Array.isArray(doc.rules)) {
      results.push({ pack: rel, status: "FAIL", note: "no top-level `rules` list" });
      continue;
    }

    const seenInPack = new Set();
    const problems = [];
    for (const [i, rule] of doc.rules.entries()) {
      const where = `rule #${i + 1}${rule && rule.id ? ` (${rule.id})` : ""}`;
      if (!rule || typeof rule !== "object") {
        problems.push(`${where}: not an object`);
        continue;
      }
      for (const field of RULE_REQUIRED_FIELDS) {
        if (!(field in rule) || rule[field] === null || rule[field] === "") {
          problems.push(`${where}: missing \`${field}\``);
        }
      }
      if (rule.severity && !VALID_SEVERITIES.has(rule.severity)) {
        problems.push(`${where}: invalid severity \`${rule.severity}\``);
      }
      if (rule.id) {
        if (seenInPack.has(rule.id)) problems.push(`${where}: duplicate id within pack`);
        seenInPack.add(rule.id);
        if (allIds.has(rule.id)) {
          problems.push(`${where}: id also used in ${allIds.get(rule.id)}`);
        } else {
          allIds.set(rule.id, rel);
        }
      }
    }

    results.push({
      pack: rel,
      status: problems.length ? "FAIL" : "PASS",
      count: doc.rules.length,
      problems,
    });
  }
  return results;
}

function checkSkills() {
  const skillsRoot = path.join(REPO, "skills");
  const files = walkSkillFiles(skillsRoot);
  const results = [];

  for (const full of files) {
    const rel = path.relative(REPO, full);
    const parts = path.relative(skillsRoot, full).split(path.sep);
    // expects: skills/<category>/<name>/SKILL.md
    const category = parts[0];
    const dirName = parts[1];
    const problems = [];

    if (parts.length !== 3) {
      problems.push(`unexpected depth (expected skills/<category>/<name>/SKILL.md, got skills/${parts.join("/")})`);
    } else if (!VALID_CATEGORIES.has(category)) {
      problems.push(`category \`${category}\` is not one of: ${[...VALID_CATEGORIES].join(", ")}`);
    }

    const text = fs.readFileSync(full, "utf8");
    const fm = parseFrontmatter(text);
    if (!fm) {
      problems.push("missing or malformed frontmatter block");
    } else {
      if (!fm.name) problems.push("frontmatter missing `name`");
      else if (dirName && fm.name !== dirName) {
        problems.push(`frontmatter name \`${fm.name}\` does not match folder \`${dirName}\``);
      }
      if (!fm.hasDescription) problems.push("frontmatter missing `description`");
    }
    if (!/^## ⚡ Command\s*$/m.test(text)) {
      problems.push("missing `## ⚡ Command` section");
    }

    results.push({ file: rel, status: problems.length ? "FAIL" : "PASS", problems });
  }
  return results;
}

function render(yamlResults, skillResults) {
  const lines = [];
  lines.push("# VALIDATION-REPORT — Self-lint");
  lines.push("");
  lines.push(`> Generated by \`node scripts/validate.js\` · ${new Date().toISOString().replace("T", " ").slice(0, 16)} UTC`);
  lines.push("");
  lines.push("Checks this pack's own content only (YAML rule-pack schema + SKILL.md frontmatter/category placement). Does not scan consuming projects — see `project-functionality-scan` for that.");
  lines.push("");

  lines.push("## YAML rule packs");
  lines.push("");
  lines.push("| Pack | Rules | Status | Notes |");
  lines.push("|------|------:|--------|-------|");
  let yamlFail = 0;
  for (const r of yamlResults) {
    if (r.status === "FAIL") yamlFail++;
    const notes = r.problems && r.problems.length ? r.problems.join("; ") : (r.note || "all required fields present, ids unique");
    lines.push(`| \`${r.pack}\` | ${r.count ?? "—"} | ${r.status} | ${notes} |`);
  }
  lines.push("");

  lines.push("## Skills");
  lines.push("");
  const skillFails = skillResults.filter((r) => r.status === "FAIL");
  lines.push(`**${skillResults.length} SKILL.md checked** — ${skillResults.length - skillFails.length} PASS, ${skillFails.length} FAIL.`);
  lines.push("");
  if (skillFails.length) {
    lines.push("| File | Notes |");
    lines.push("|------|-------|");
    for (const r of skillFails) {
      lines.push(`| \`${r.file}\` | ${r.problems.join("; ")} |`);
    }
    lines.push("");
  }

  const totalFail = yamlFail + skillFails.length;
  lines.push("## Summary");
  lines.push("");
  lines.push(`- YAML packs: ${yamlResults.length} checked, ${yamlFail} FAIL`);
  lines.push(`- Skills: ${skillResults.length} checked, ${skillFails.length} FAIL`);
  lines.push(`- **Verdict:** ${totalFail === 0 ? "✅ Clean — safe to proceed" : "❌ Fix failures before pushing"}`);
  lines.push("");

  return { text: lines.join("\n"), totalFail };
}

function main() {
  const yamlResults = checkYamlPacks();
  const skillResults = checkSkills();
  const { text, totalFail } = render(yamlResults, skillResults);

  fs.writeFileSync(path.join(REPO, "VALIDATION-REPORT.md"), text, "utf8");
  console.log(text);

  if (totalFail > 0) {
    console.error(`\n${totalFail} check(s) failed. See VALIDATION-REPORT.md.`);
    process.exit(1);
  }
}

main();
