# Clone Repos Command

Clone all source GitHub repositories for skill extraction.

Clone each repo listed in `registry/registry.json` sources.github_repos into `sources/repos/`.
Use `git clone --depth 1` for speed. Skip repos that already exist.
