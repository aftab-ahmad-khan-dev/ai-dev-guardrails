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
  # Point relative reference links at design/references from skills/design/<name>/ (3 levels deep)
  sed 's|](../references/|](../../../design/references/|g; s|\[`../references/|[`../../../design/references/|g; s|](../SAFETY.md)|](../../../design/SAFETY.md)|g; s|](../safe-file-ops/|](../../../skills/design/safe-file-ops/|g; s|](../approaches/|](../../../design/approaches/|g' \
    "$src" > "$dest"
}

for skill in "${core[@]}"; do
  mkdir -p "$root/skills/design/$skill"
  rewrite_refs "$root/design/$skill/SKILL.md" "$root/skills/design/$skill/SKILL.md"
done

# Approaches library
if [ -d "$root/design/approaches" ]; then
  count=0
  for skill_md in "$root/design/approaches"/*/SKILL.md; do
    [ -f "$skill_md" ] || continue
    name="$(basename "$(dirname "$skill_md")")"
    mkdir -p "$root/skills/design/$name"
    # Approaches rarely link to ../references — copy as-is with safety note path fix
    sed 's|design/references/slop-catalog.md|../../../design/references/slop-catalog.md|g; s|references/design-slop-catalog.md|../../../references/design-slop-catalog.md|g' \
      "$skill_md" > "$root/skills/design/$name/SKILL.md"
    count=$((count + 1))
  done
  echo "Synced $count approach skills"
fi

cp "$root/design/references/slop-catalog.md" "$root/references/design-slop-catalog.md"
cp "$root/design/references/context-templates.md" "$root/references/design-context-templates.md"
# command-vocabulary.md / motion-standards.md link to design/ siblings one level shallower
# than their root references/ copy, and command-vocabulary.md self-links slop-catalog.md
# under its renamed sibling — rewrite both on copy instead of a plain cp.
sed 's|](../design-steer/|](../design/design-steer/|g; s|](slop-catalog.md)|](design-slop-catalog.md)|g' \
  "$root/design/references/command-vocabulary.md" > "$root/references/design-command-vocabulary.md"
sed 's|](../motion-craft/|](../design/motion-craft/|g; s|](../review-motion/|](../design/review-motion/|g' \
  "$root/design/references/motion-standards.md" > "$root/references/design-motion-standards.md"

echo "Synced ${#core[@]} core design skills → skills/design/"
echo "push-report lives under skills/ship/push-report (not mirrored from design/)"
