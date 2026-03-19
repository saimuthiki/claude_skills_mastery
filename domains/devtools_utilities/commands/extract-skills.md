# Extract Skills Command

Run the full extraction pipeline on all cloned repositories.

1. Scan `sources/repos/` for all cloned repositories
2. For each repo, extract skills, agents, plugins, commands, and hooks
3. Save extracted entities to `sources/extracted/all_entities.json`
4. Print statistics on extracted entities by type and domain

Run: `python scripts/extract_entities.py`
