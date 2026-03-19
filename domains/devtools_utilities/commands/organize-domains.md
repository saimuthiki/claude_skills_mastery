# Organize Domains Command

Organize all extracted entities into domain-organized folder structure.

1. Load all entities from `sources/extracted/` and `sources/web_data/`
2. Deduplicate by name
3. Classify into domains
4. Write entity files (JSON + Markdown) to domain folders
5. Generate domain READMEs
6. Build master registry.json

Run: `python scripts/organize_domains.py`
