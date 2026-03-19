# Validate Registry Command

Validate all entities in the registry for completeness and correctness.

1. Load `registry/registry.json`
2. Check each entity has: name, type, description, source, domain
3. Verify all domains are valid
4. Check for duplicates
5. Report validation results with error/warning counts
