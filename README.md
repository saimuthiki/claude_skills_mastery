# Claude Skills Mastery

The most comprehensive Claude Code ecosystem repository. Every skill, agent, command, hook, plugin, MCP, and setting is semantically classified into one of 38 domain folders.

## Repository Structure

```
claude_skills_mastery/
├── .claude/                → Claude Code runtime (20 core skills + settings)
│   ├── settings.json       → Root config (agent teams enabled)
│   └── skills/             → 20 core registered skills (brainstorming, docx, pdf, etc.)
│
├── domains/                → ALL content organized by domain (39 domains)
│   └── {domain_name}/
│       ├── skills/         → Skill directories, each with SKILL.md
│       ├── agents/         → Agent definition .md files
│       ├── commands/       → Slash command .md files
│       ├── hooks/          → Hook config .json files
│       ├── plugins/        → Plugin config .json files
│       ├── mcps/           → MCP server config .json files (10 domains)
│       ├── settings/       → Settings template .json files (7 domains)
│       ├── templates/      → Language scaffold files (3 domains)
│       └── README.md       → Domain overview with entity counts
│
├── registry/               → registry.json (master entity index)
├── scripts/                → Pipeline tools (rebuild_registry.py)
├── sources/                → Raw data (15 repos + 10 websites)
├── CLAUDE.md               → Claude Code project instructions
└── README.md               → This file
```

### Entity Type Reference

| Entity | Format | Location | Purpose |
|--------|--------|----------|---------|
| **Skills** | `SKILL.md` in directory | `domains/{d}/skills/{name}/` | Specialized knowledge + workflows |
| **Agents** | `.md` file | `domains/{d}/agents/` | AI agent definitions with tools/model |
| **Commands** | `.md` file | `domains/{d}/commands/` | Slash commands for Claude Code |
| **Hooks** | `.json` file | `domains/{d}/hooks/` | Pre/post tool event triggers |
| **Plugins** | `.json` file | `domains/{d}/plugins/` | Plugin configurations |
| **MCPs** | `.json` file | `domains/{d}/mcps/` | Model Context Protocol server configs |
| **Settings** | `.json` file | `domains/{d}/settings/` | Claude Code settings templates |
| **Templates** | various | `domains/{d}/templates/` | Language-specific project scaffolds |

---

## Quick Stats

| Entity Type | Count |
|-------------|------:|
| Skills | 20,064 |
| Agents | 1,068 |
| Commands | 1,024 |
| Hooks | 187 |
| MCPs | 67 |
| Settings | 59 |
| Plugins | 43 |
| Templates | 42 |
| **Total** | **22,554** |
| **Domains** | **38** |
| **Core Skills (.claude/)** | **20** |

---

## Complete Domain Breakdown

| Domain | Skills | Agents | Commands | Hooks | Plugins | MCPs | Settings | Templates | Total |
|--------|-------:|-------:|---------:|------:|--------:|-----:|---------:|----------:|------:|
| **ai_ml_llm** | 3,171 | 198 | 90 | 4 | 7 | 5 | 6 | 0 | **3,481** |
| **ui_ux_design** | 1,498 | 45 | 21 | 3 | 3 | 0 | 0 | 0 | **1,570** |
| **monitoring_observability** | 1,468 | 6 | 15 | 7 | 0 | 0 | 4 | 0 | **1,500** |
| **devops_cicd** | 1,043 | 107 | 154 | 14 | 4 | 0 | 6 | 0 | **1,328** |
| **code_quality** | 1,207 | 71 | 24 | 20 | 0 | 0 | 0 | 0 | **1,322** |
| **testing_qa** | 1,114 | 66 | 78 | 21 | 1 | 0 | 0 | 0 | **1,280** |
| **security** | 1,074 | 38 | 47 | 15 | 0 | 0 | 9 | 0 | **1,183** |
| **scientific_research** | 1,133 | 21 | 13 | 0 | 2 | 0 | 0 | 0 | **1,169** |
| **database** | 981 | 49 | 48 | 2 | 1 | 5 | 0 | 0 | **1,086** |
| **composio_integrations** | 888 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | **889** |
| **miscellaneous** | 673 | 5 | 57 | 2 | 0 | 0 | 6 | 2 | **745** |
| **office_documents** | 685 | 8 | 0 | 0 | 1 | 0 | 0 | 0 | **694** |
| **marketing_seo** | 545 | 65 | 9 | 0 | 4 | 2 | 0 | 0 | **625** |
| **automation_scripting** | 485 | 17 | 54 | 44 | 1 | 6 | 0 | 0 | **607** |
| **cloud_infrastructure** | 475 | 7 | 8 | 0 | 0 | 0 | 4 | 0 | **494** |
| **frontend** | 357 | 48 | 60 | 4 | 2 | 4 | 0 | 17 | **492** |
| **api_integration** | 359 | 17 | 29 | 0 | 0 | 3 | 0 | 0 | **408** |
| **productivity_workflow** | 250 | 25 | 113 | 2 | 0 | 2 | 0 | 0 | **392** |
| **legal_compliance** | 325 | 11 | 7 | 0 | 1 | 0 | 0 | 0 | **344** |
| **backend** | 245 | 58 | 8 | 0 | 1 | 0 | 0 | 23 | **335** |
| **data_analytics** | 278 | 40 | 6 | 0 | 0 | 1 | 0 | 0 | **325** |
| **devtools_utilities** | 139 | 21 | 42 | 22 | 0 | 38 | 24 | 0 | **286** |
| **performance_optimization** | 180 | 27 | 20 | 4 | 0 | 0 | 0 | 0 | **231** |
| **content_creation** | 192 | 24 | 3 | 0 | 0 | 1 | 0 | 0 | **220** |
| **communication_collaboration** | 188 | 1 | 2 | 18 | 0 | 0 | 0 | 0 | **209** |
| **project_management** | 118 | 13 | 47 | 0 | 1 | 0 | 0 | 0 | **179** |
| **documentation** | 103 | 14 | 29 | 0 | 2 | 0 | 0 | 0 | **148** |
| **blockchain_web3** | 130 | 7 | 6 | 0 | 0 | 0 | 0 | 0 | **143** |
| **healthcare_medical** | 129 | 0 | 3 | 0 | 2 | 0 | 0 | 0 | **134** |
| **sap_enterprise** | 124 | 0 | 1 | 3 | 0 | 0 | 0 | 0 | **128** |
| **game_development** | 69 | 24 | 5 | 0 | 0 | 0 | 0 | 0 | **98** |
| **mobile_development** | 88 | 8 | 2 | 0 | 0 | 0 | 0 | 0 | **98** |
| **finance_accounting** | 86 | 7 | 2 | 0 | 1 | 0 | 0 | 0 | **96** |
| **hr_recruiting** | 68 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | **75** |
| **networking_protocols** | 59 | 4 | 8 | 2 | 2 | 0 | 0 | 0 | **75** |
| **ecommerce** | 56 | 7 | 0 | 0 | 6 | 0 | 0 | 0 | **69** |
| **accessibility** | 48 | 4 | 3 | 0 | 0 | 0 | 0 | 0 | **55** |
| **education_learning** | 33 | 3 | 4 | 0 | 1 | 0 | 0 | 0 | **41** |

---

## Core Skills (.claude/skills/)

These 20 skills are **registered in Claude Code's runtime** and available as slash commands:

| Skill | Domain Affiliation | Description |
|-------|-------------------|-------------|
| `brainstorming` | productivity_workflow | Requirements gathering, ideation |
| `code-review` | code_quality | Engineering code review practices |
| `deep-research` | ai_ml_llm | Multi-source research with citations |
| `docx` | office_documents | Word document creation/editing |
| `e2e-testing` | testing_qa | Playwright E2E testing |
| `executing-plans` | productivity_workflow | Execute implementation plans |
| `frontend-design` | frontend | Production-grade frontend UIs |
| `mcp-builder` | ai_ml_llm | Build MCP servers (Python/Node) |
| `pdf` | office_documents | PDF read/merge/split/OCR |
| `pptx` | office_documents | PowerPoint creation/editing |
| `security-review` | security | Security auditing |
| `skill-creator` | devtools_utilities | Guide for creating new skills |
| `subagent-driven-development` | code_quality | Multi-agent dev workflows |
| `systematic-debugging` | code_quality | Debugging methodology |
| `test-driven-development` | testing_qa | TDD workflow |
| `ui-ux-pro-max` | ui_ux_design | UI/UX design (50+ styles, 161 palettes) |
| `verification-before-completion` | testing_qa | Pre-completion verification |
| `webapp-testing` | testing_qa | Test web apps with Playwright |
| `writing-plans` | productivity_workflow | Plan multi-step tasks |
| `xlsx` | office_documents | Excel creation/editing |

---

## Where Each Entity Type Lives

### MCPs (67 total, across 10 domains)

| Domain | MCPs | Notable Servers |
|--------|-----:|-----------------|
| devtools_utilities | 38 | Sentry, Stripe, Terraform, Grafana, Figma, MongoDB, Postman |
| automation_scripting | 6 | Playwright, BrowserMCP, Browserbase |
| database | 5 | Neon, PostgreSQL, MySQL, Supabase |
| ai_ml_llm | 5 | DeepGraph, NIA research, memory |
| frontend | 4 | Web fetch/search, Zread |
| api_integration | 3 | GitHub, memory, integrations |
| productivity_workflow | 2 | Monday.com, Notion |
| marketing_seo | 2 | Facebook Ads, Google Ads |
| content_creation | 1 | ElevenLabs |
| data_analytics | 1 | Bright Data |

### Settings (69 total, across 7 domains)

| Domain | Settings | Notable Configs |
|--------|--------:|-----------------|
| devtools_utilities | 34 | 32 statusline themes, cleanup, filesystem |
| security | 9 | Auth, permissions, secret protection |
| devops_cicd | 6 | Environment, git flow, bash timeouts |
| ai_ml_llm | 6 | MCP config, model selection, partnerships |
| miscellaneous | 6 | Global settings, announcements |
| cloud_infrastructure | 4 | Bedrock, Vertex, proxy, headers |
| monitoring_observability | 4 | Telemetry, LangSmith tracing |

### Templates (42 total, across 3 domains)

| Domain | Templates | Languages |
|--------|--------:|-----------|
| backend | 23 | Python (22), Go (2), Ruby (7), Rust (2) |
| frontend | 17 | JavaScript/TypeScript (26) |
| miscellaneous | 2 | Common shared templates |

---

## Architecture Decisions

### Why domain-first organization?

Each domain folder (`domains/{name}/`) contains ALL entity types for that domain. This means:
- **One-stop shop**: Looking at `security/`? You get its skills, agents, commands, hooks, MCPs, and settings all in one place
- **Self-contained**: Each domain is a complete unit with its own README showing entity counts
- **Scalable**: New entity types (MCPs, settings, templates) slot in naturally alongside existing ones

### Where things go:

| If you have... | Put it in... | Why |
|----------------|-------------|-----|
| A skill with SKILL.md | `domains/{domain}/skills/{name}/` | Skills are directories with SKILL.md + references |
| An agent definition | `domains/{domain}/agents/{name}.md` | Agents are single .md files |
| A slash command | `domains/{domain}/commands/{name}.md` | Commands are single .md files |
| A hook config | `domains/{domain}/hooks/{name}.json` | Hooks are JSON configs |
| An MCP server config | `domains/{domain}/mcps/{name}.json` | MCP configs live in the domain they serve |
| A settings template | `domains/{domain}/settings/{name}.json` | Settings that configure domain-specific behavior |
| A project template | `domains/{domain}/templates/{lang}/` | Language scaffolds grouped by backend/frontend |
| A Claude Code core skill | `.claude/skills/{name}/` | Only the 20 registered runtime skills |

---

## Sources

**15 GitHub repos**: anthropics/skills, obra/superpowers, davila7/claude-code-templates, alirezarezvani/claude-skills, affaan-m/everything-claude-code, BehiSecc/awesome-claude-skills, msitarzewski/agency-agents, and more.

**10 websites crawled**: claudeskills.info, skills.sh, mcpservers.org, openaitoolshub.org, chat2anyllm.github.io, claudeskills.club, aitmpl.com, and more.

---

## License

MIT
