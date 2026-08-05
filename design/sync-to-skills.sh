#!/usr/bin/env bash
# Sync canonical design/* skills into skills/ for npx skills discovery.
# Run from repo root after editing design/ skills or regenerating approaches.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"

# Core design skills (top-level under design/)
core=(
  using-design-skills
  anti-slop-frontend
  design-context
  design-steer
  redesign-audit
  motion-craft
  review-motion
  find-motion
  visual-prototype
  ship-complete-ui
  safe-file-ops
)

rewrite_refs() {
  local src="$1" dest="$2"
  # Point relative reference links at design/references from skills/
  sed 's|](../references/|](../../design/references/|g; s|\[`../references/|[`../../design/references/|g; s|](../SAFETY.md)|](../../design/SAFETY.md)|g; s|](../safe-file-ops/|](../../design/safe-file-ops/|g' \
    "$src" > "$dest"
}

for skill in "${core[@]}"; do
  mkdir -p "$root/skills/$skill"
  rewrite_refs "$root/design/$skill/SKILL.md" "$root/skills/$skill/SKILL.md"
done

# Approaches library
if [ -d "$root/design/approaches" ]; then
  count=0
  for skill_md in "$root/design/approaches"/*/SKILL.md; do
    [ -f "$skill_md" ] || continue
    name="$(basename "$(dirname "$skill_md")")"
    mkdir -p "$root/skills/$name"
    # Approaches rarely link to ../references — copy as-is with safety note path fix
    sed 's|design/references/slop-catalog.md|../../design/references/slop-catalog.md|g; s|references/design-slop-catalog.md|../../references/design-slop-catalog.md|g' \
      "$skill_md" > "$root/skills/$name/SKILL.md"
    count=$((count + 1))
  done
  echo "Synced $count approach skills"
fi

cp "$root/design/references/slop-catalog.md" "$root/references/design-slop-catalog.md"
cp "$root/design/references/command-vocabulary.md" "$root/references/design-command-vocabulary.md"
cp "$root/design/references/motion-standards.md" "$root/references/design-motion-standards.md"
cp "$root/design/references/context-templates.md" "$root/references/design-context-templates.md"

echo "Synced ${#core[@]} core design skills → skills/"
echo "push-report lives under skills/push-report (not mirrored from design/)"
