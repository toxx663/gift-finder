#!/usr/bin/env python3
"""Check that the skill and the plugin manifests are well formed and in sync.

Run from the repository root:  python3 scripts/validate.py
No third-party packages needed.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
errors = []


def fail(msg):
    errors.append(msg)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^\s*([A-Za-z_-]+):\s*(.*)$", line)
        if km:
            fields[km.group(1)] = km.group(2).strip().strip('"')
    return fields


versions = set()

for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        fail(f"{skill_dir.name}: SKILL.md is missing")
        continue
    text = skill_md.read_text(encoding="utf-8")
    fm = frontmatter(text)
    if fm is None:
        fail(f"{skill_dir.name}: no YAML frontmatter")
        continue
    name = fm.get("name", "")
    desc = fm.get("description", "")
    if name != skill_dir.name:
        fail(f"{skill_dir.name}: name '{name}' must match the folder name")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        fail(f"{skill_dir.name}: name must be lowercase kebab-case, max 64 chars")
    if not desc:
        fail(f"{skill_dir.name}: description is empty")
    if len(desc) > 1024:
        fail(f"{skill_dir.name}: description is {len(desc)} chars (max 1024)")
    if "<" in desc or ">" in desc:
        fail(f"{skill_dir.name}: description must not contain angle brackets")
    lines = text.count("\n") + 1
    if lines > 500:
        fail(f"{skill_dir.name}: SKILL.md has {lines} lines (keep under 500)")
    if fm.get("version"):
        versions.add(fm["version"])

for rel in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
    path = ROOT / rel
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        fail(f"{rel}: {exc}")
        continue
    if rel.endswith("plugin.json"):
        versions.add(data.get("version", ""))
    else:
        for plugin in data.get("plugins", []):
            versions.add(plugin.get("version", ""))

versions.discard("")
if len(versions) > 1:
    fail(f"version mismatch across files: {sorted(versions)}")

if errors:
    print("Validation failed:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print(f"OK (version {next(iter(versions), 'n/a')})")
