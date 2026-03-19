#!/usr/bin/env python3
"""Rebuild registry.json by scanning all domains/."""

import json
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path("D:/claude_code_mastery_real/claude_skills_mastery")
DOMAINS_DIR = BASE_DIR / "domains"
REGISTRY_DIR = BASE_DIR / "registry"

def main():
    entities = []
    domain_counts = defaultdict(lambda: {"skills": 0, "agents": 0, "commands": 0, "hooks": 0, "plugins": 0})

    for domain_dir in sorted(DOMAINS_DIR.iterdir()):
        if not domain_dir.is_dir():
            continue
        domain = domain_dir.name

        # Skills
        skills_dir = domain_dir / "skills"
        if skills_dir.exists():
            for s in sorted(skills_dir.iterdir()):
                if s.is_dir():
                    domain_counts[domain]["skills"] += 1
                    entities.append({"name": s.name, "type": "skill", "domain": domain, "path": f"domains/{domain}/skills/{s.name}"})

        # Agents
        agents_dir = domain_dir / "agents"
        if agents_dir.exists():
            for a in sorted(agents_dir.glob("*.md")):
                domain_counts[domain]["agents"] += 1
                entities.append({"name": a.stem, "type": "agent", "domain": domain, "path": f"domains/{domain}/agents/{a.name}"})

        # Commands
        cmds_dir = domain_dir / "commands"
        if cmds_dir.exists():
            for c in sorted(cmds_dir.glob("*.md")):
                domain_counts[domain]["commands"] += 1
                entities.append({"name": c.stem, "type": "command", "domain": domain, "path": f"domains/{domain}/commands/{c.name}"})

        # Hooks
        hooks_dir = domain_dir / "hooks"
        if hooks_dir.exists():
            for h in sorted(hooks_dir.glob("*.json")):
                domain_counts[domain]["hooks"] += 1
                entities.append({"name": h.stem, "type": "hook", "domain": domain, "path": f"domains/{domain}/hooks/{h.name}"})

        # Plugins
        plugins_dir = domain_dir / "plugins"
        if plugins_dir.exists():
            for p in sorted(plugins_dir.glob("*.json")):
                domain_counts[domain]["plugins"] += 1
                entities.append({"name": p.stem, "type": "plugin", "domain": domain, "path": f"domains/{domain}/plugins/{p.name}"})

    type_counts = defaultdict(int)
    for e in entities:
        type_counts[e["type"]] += 1

    registry = {
        "version": "3.0.0",
        "name": "claude-skills-mastery",
        "stats": {
            "total": len(entities),
            "by_type": dict(type_counts),
            "domains": len(domain_counts),
            "by_domain": {d: sum(v.values()) for d, v in sorted(domain_counts.items(), key=lambda x: -sum(x[1].values()))},
        },
        "entities": entities,
    }

    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)
    out = REGISTRY_DIR / "registry.json"
    out.write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Registry: {len(entities)} entities, {out.stat().st_size // 1024}KB")
    print(f"Types: {dict(type_counts)}")
    print(f"Domains: {len(domain_counts)}")

if __name__ == "__main__":
    main()
