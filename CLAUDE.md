# Claude Skills Mastery

The most comprehensive Claude Code ecosystem repository. Every skill, agent, command, hook, and plugin is semantically classified and physically placed in its domain folder.

## How This Repo Works

Everything lives inside `domains/`. Each domain folder has up to 8 entity subfolders:

```
domains/{domain_name}/
├── skills/       # Skill directories, each with SKILL.md
├── agents/       # Agent definition .md files
├── commands/     # Command/slash-command .md files
├── hooks/        # Hook config .json files
├── plugins/      # Plugin config .json files
├── mcps/         # MCP server config .json files (10 domains)
├── settings/     # Settings template .json files (7 domains)
├── templates/    # Language project scaffolds (3 domains)
└── README.md     # Domain overview with entity counts
```

The `.claude/` folder holds the Claude Code agent team infrastructure — settings, agent definitions, slash commands, hooks, and 20 core skills that agent teams use directly.

## Quick Stats

| Type | Count |
|------|------:|
| Skills | 20,637 |
| Agents | 1,122 |
| Commands | 1,026 |
| Hooks | 187 |
| MCPs | 67 |
| Settings | 69 |
| Plugins | 43 |
| Templates | 42 |
| **Total** | **23,193** |
| **Domains** | **39** |
| **Core Skills** | **20** |
| Templates | 64 | 6 |
| **Total** | **~6,600** | **~128** |

## Domains

| Domain | What's In It |
|--------|-------------|
| **ai_ml_llm** | LLM agents, RAG, prompt engineering, MCP, Langchain |
| **composio_integrations** | 794 third-party service automation skills |
| **devops_cicd** | Docker, Kubernetes, GitHub Actions, deploys, pipelines |
| **testing_qa** | TDD, E2E, Playwright, Jest, coverage, QA automation |
| **frontend** | React, Vue, Next.js, Astro, Vite, web components |
| **database** | Postgres, MongoDB, Prisma, Supabase, Redis, migrations |
| **security** | Pentest, OWASP, auth, encryption, SOC2, compliance |
| **ui_ux_design** | Figma, Tailwind, design systems, themes, branding |
| **marketing_seo** | SEO, CRO, content strategy, ads, social media |
| **code_quality** | Linting, code review, refactoring, best practices |
| **api_integration** | REST, GraphQL, webhooks, API design |
| **automation_scripting** | CLI tools, bots, cron, scraping, n8n workflows |
| **scientific_research** | Bioinformatics, papers, lab tools, genomics |
| **performance_optimization** | Caching, profiling, bundle size, web vitals |
| **project_management** | Agile, sprints, Jira, OKRs, roadmaps |
| **documentation** | Docs generation, Docusaurus, diagrams |
| **game_development** | Unity, Godot, Roblox, Blender, shaders |
| **legal_compliance** | GDPR, SOC2, ISO, contracts, privacy |
| **communication_collaboration** | Slack, Discord, email, notifications |
| **ecommerce** | Shopify, payments, carts, inventory |
| **backend** | Express, FastAPI, Django, Laravel, Spring |
| **cloud_infrastructure** | AWS, Azure, GCP, Cloudflare, serverless |
| **mobile_development** | iOS, Android, React Native, Flutter, Expo |
| **devtools_utilities** | CLI utilities, converters, parsers |
| **content_creation** | Blog writing, video, podcasts, social media |
| **monitoring_observability** | Logging, Sentry, Datadog, Grafana |
| **productivity_workflow** | Git workflow, Notion, Obsidian, planning |
| **healthcare_medical** | FDA, HIPAA, clinical, pharma, MedTech |
| **finance_accounting** | Invoicing, Stripe, bookkeeping, fintech |
| **networking_protocols** | TCP, DNS, SSL, WebSocket, proxies |
| **office_documents** | PDF, DOCX, XLSX, PPTX processing |
| **data_analytics** | ETL, BigQuery, Snowflake, dbt, pandas |
| **hr_recruiting** | Hiring, onboarding, resumes, interviews |
| **education_learning** | Tutorials, courses, LMS |
| **accessibility** | WCAG, ARIA, screen readers, a11y |
| **sap_enterprise** | SAP, Salesforce, enterprise CRM/ERP |
| **blockchain_web3** | Solidity, Ethereum, DeFi, smart contracts |
| **miscellaneous** | Anything that doesn't fit elsewhere |

## .claude/ Structure

The `.claude/` directory follows a **component-type-first, domain-second** organization.
All components are organized by type (agents, commands, hooks, etc.) with domain subfolders within each.

```
.claude/
├── REGISTRY.md              # Master component index (file counts, descriptions)
├── DOMAINS.md               # Cross-reference: domain → all component types
├── settings.json            # Root config (CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1)
│
├── agents/ (27 domains)     # 495 agent definitions (.md)
│   ├── development/         # 52 agents (code review, CI/CD, frontend, backend)
│   ├── expert-advisors/     # 52 agents (domain experts)
│   ├── programming-languages/ # 50 agents (Rust, Go, Python, C++, etc.)
│   ├── data-ai/             # 40 agents (data science, ML)
│   ├── devops-infrastructure/ # 39 agents
│   ├── meta-tools/          # 21 agents (pipeline infrastructure)
│   ├── security/            # 20 agents
│   └── ...                  # 20 more domain folders
│
├── commands/ (23 domains)   # 348 slash commands (.md)
│   ├── google-workspace/    # 107 commands (Gmail, Drive, Sheets, etc.)
│   ├── git/                 # 15 commands (feature, hotfix, PR, worktrees)
│   ├── utilities/           # 21 commands
│   ├── project-management/  # 20 commands
│   └── ...                  # 19 more domain folders
│
├── hooks/ (10 domains)      # 68 hook configs (.json + scripts)
│   ├── automation/          # 20 hooks (notifications, deploy)
│   ├── development/         # 10 hooks (lint, format, debug)
│   ├── git/                 # 8 hooks (commits, branches)
│   ├── security/            # 6 hooks (secret scanner, command blocker)
│   └── ...                  # 6 more domain folders
│
├── mcps/ (12 domains)       # 67 MCP server configs (.json)
│   ├── dev-tools/           # 37 MCPs (Sentry, Stripe, Grafana, Figma, etc.)
│   ├── browser-automation/  # 6 MCPs (Playwright, Browserbase)
│   ├── database/            # 5 MCPs (Neon, PostgreSQL, Supabase)
│   └── ...                  # 9 more domain folders
│
├── settings/ (12 domains)   # 69 settings templates (.json)
│   ├── statusline/          # 32 status bar themes
│   ├── permissions/         # 6 permission configs
│   └── ...                  # 10 more domain folders
│
├── skills/ (43 domains + 20 core)  # 5,490 skill files
│   ├── _CORE_SKILLS.md      # Index of 20 registered top-level skills
│   ├── ai-research/         # 1,512 skills (AI/ML research library)
│   ├── development/         # 1,057 skills (full-stack dev)
│   ├── scientific/          # 1,032 skills (bio, chem, medicine)
│   ├── document-processing/ # 518 skills (OCR, conversion)
│   ├── creative-design/     # 325 skills (design tools, workflows)
│   ├── brainstorming/       # Core skill (registered)
│   ├── docx/                # Core skill (registered)
│   ├── pdf/                 # Core skill (registered)
│   └── ...                  # 54 more skill domains + core skills
│
├── templates/ (6 languages) # 64 project scaffolds
│   ├── javascript-typescript/ # 26 templates
│   ├── python/              # 22 templates
│   └── ...                  # 4 more languages
│
├── sandbox/                 # Cloudflare, Docker, E2B environments
└── .claude-plugin/          # Plugin marketplace config
```

### Organization Principles

1. **Component-type first**: Claude Code expects `agents/`, `commands/`, `skills/` at specific paths
2. **Domain subfolders**: Within each type, files are grouped by domain (security, git, etc.)
3. **Unified domain naming**: Same domain name across all component types (kebab-case)
4. **Core skills stay top-level**: 20 registered skills keep their paths for Claude Code discovery
5. **Cross-references**: `DOMAINS.md` maps domain → all component types; `_CORE_SKILLS.md` maps skills → domains

## Sources

- **aitmpl.com** (github.com/davila7/claude-code-templates) — 6,500+ components
- **15 GitHub repositories** cloned in `sources/repos/`
- **10 websites** crawled, data in `sources/web_data/`
- **registry.json** indexes all entities with domain classification
