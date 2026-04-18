# Repository Guidelines

This repository contains a structured digital knowledge base (Obsidian vault) focused on financial management, agribusiness, and investment funds. All agents should refer to this file for guidelines on project structure, conventions, and operations.

## Project Overview

The `Mind/` directory is the core Obsidian vault, supplemented by guidelines, AI agent rules, and specialized CLI skills.

**Key Areas Covered:**
- Financial Markets (interest rates, spreads, derivatives, valuation)
- Investment Funds (FIDC, FIAGRO, FII, ETF, FIP)
- Agribusiness (supply chains, financing, CPR)
- Credit & Risk (default, recovery, guarantees)
- Accounting & Control (fund accounting, cost calculations)
- Quantitative Methods (statistics, rates, regression, time value of money)
- Economics (micro, macro, SFN, policy, FX)
- Portfolio Management (allocation, IPS, performance, benchmarking)
- Corporate & Financial Analysis (capital structure, governance, statements)
- Financial Technology (crowdfunding, CVM 88, innovation)
- Legal & Regulatory (laws, compliance, CVM rules)
- Structuring & Operations (origination, custody, servicing)

## Directory Structure & Module Organization

```text
Mind/
├── Conhecimento/
│   ├── Mercado_Financeiro/
│   ├── Fundos_Investimento/
│   │   ├── FIDC/
│   │   ├── FIAGRO/
│   │   ├── FII/
│   │   ├── FIP/
│   │   └── ETF/
│   ├── Agronegocio/
│   ├── Credito_e_Risco/
│   ├── Contabilidade_e_Controle/
│   ├── Metodos_Quantitativos/
│   ├── Economia/
│   ├── Analise_Financeira_e_Corporativa/
│   ├── Gestao_de_Carteiras/
│   ├── Tecnologia_e_Inovacao_Financeira/
│   ├── Portfolio/
│   ├── Juridico_e_Regulatorio/
│   ├── Estruturacao_e_Operacoes/
│   ├── Glossario/
│   ├── indice.md
│   └── Indice_*.md
├── daily/
├── .obsidian/
└── Welcome.md

REGRAS_CONHECIMENTO.md
.claude/skills/
├── conhecimento.md
└── obsidian_cli.md
```

Keep content notes organized in the `Conhecimento/` folder structure. Treat `.obsidian/` changes carefully because they can be user-specific.

## Content Creation Rules

All knowledge notes must follow the mandatory rules in `Mind/REGRAS_CONHECIMENTO.md`.

### Encoding & Language
- Encoding: UTF-8, preferably without BOM.
- Language: Portuguese (Brazil).
- After large writing batches, reopen a sample of files in terminal and Obsidian to confirm accents were preserved.
- Legacy notes may already contain mojibake. Do not use a corrupted terminal rendering alone as proof that a newly written file is wrong.

### File Naming & Structure
- File names: use `Snake_Case.md` or `PascalCase.md`.
- Daily notes: `YYYY-MM-DD.md`.
- Title: use `# Friendly Title`.

Every technical note should include:
1. Main title (`#`)
2. Context or summary paragraph
3. Content organized by subtitles (`##`, `###`)
4. `## Referências e Links`
5. Navigation footer linking to the category index and master index
6. Hashtags at the end

Default linking minimum for new notes:
- 1 link to the category index
- 1 link to `Mind/Conhecimento/indice`
- 3 semantic links to related notes when the topic is broad enough

### Wikilink Strategy
- Use `[[Caminho/Relativo/Nota|Display Text]]` for internal links.
- Link technical terms to their own notes or to `[[Glossario/Glossario|Glossário]]`.
- Cross-link related concepts across domains.
- When creating a new concept cluster, update backlinks in relevant existing notes instead of only linking forward from the new notes.
- If a topic becomes too broad, create a hub note plus smaller child notes by concept.

### Category Folder Purpose
- `Mercado_Financeiro/`: macro, rates, indices, instruments, derivatives, valuation.
- `Fundos_Investimento/`: fund regulation, taxation, and fund families.
- `Agronegocio/`: supply chains, CPR, logistics, sustainability in agro.
- `Credito_e_Risco/`: analysis, guarantees, default, ratings, risk types.
- `Contabilidade_e_Controle/`: accounting, DCF, quotas, expenses, marking.
- `Metodos_Quantitativos/`: statistics, regression, probability, rates, time value.
- `Economia/`: micro, macro, SFN, fiscal/monetary policy, FX.
- `Analise_Financeira_e_Corporativa/`: statements, governance, capital structure, restructuring.
- `Gestao_de_Carteiras/`: IPS, allocation, benchmarks, performance, rebalancing.
- `Tecnologia_e_Inovacao_Financeira/`: fintech, crowdfunding, technology regulation.
- `Portfolio/`: fund-specific information.
- `Juridico_e_Regulatorio/`: laws, compliance, CVM, ANBIMA, ASG.
- `Estruturacao_e_Operacoes/`: origination, custody, servicing, registries, securitization.
- `Glossario/`: technical definitions.

If a new source introduces a recurring domain that does not fit cleanly in the existing tree, expand the taxonomy explicitly instead of forcing the content into an unrelated folder.

## Build, Test, and Development Commands

There is no build pipeline or automated test suite. Useful local commands are:

### Inspection Commands
- `rg --files Mind` — list all vault files quickly
- `rg "\[\[.*\]\]" Mind` — find all wikilinks
- `rg "keyword" Mind` — search content across the vault
- `Get-ChildItem Mind` — inspect vault contents

### Obsidian CLI
- `obsidian daily:append content="- New entry"`
- `obsidian search query="keyword"`
- `obsidian read file="Note Name"`
- `obsidian help`

### Git & Version Control
- `git status`
- `git diff`
- Do not commit `.obsidian/workspace.json` unless changes are intentional.

## Testing Guidelines

Testing is manual and performed in Obsidian:
1. Open the vault in Obsidian desktop app.
2. Check that wikilinks resolve correctly.
3. Verify embeds display properly.
4. Confirm no broken references after file moves or renames.
5. Validate workspace functionality after `.obsidian/` changes.
6. After structural expansions, check for orphan notes, duplicate concepts, and broken navigation between indices and hubs.

## Workflow for Content Updates

1. Prepare: read `Mind/REGRAS_CONHECIMENTO.md`.
2. Create or edit: follow the mandatory structure and linking standards.
3. Index: add new main topics to the appropriate `Indice_*.md`.
4. Link: create forward links and update backlinks in impacted notes.
5. Review: look for orphan notes, duplicate concepts, and missing category links.
6. Validate: check links, hashtags, and encoding in Obsidian.
7. Commit: use short imperative messages.

## Commit & Pull Request Guidelines

Use short imperative commit messages such as:
- `Add daily note 2026-04-18`
- `Add FIDC subordination rules`
- `Update fund indices`
- `Clean up Obsidian config`

Pull requests should include:
- a brief summary of changed notes or config
- any renamed or moved files
- screenshots only when UI or workspace behavior changed

## Security & Configuration Tips

- Do not commit secrets, API keys, or personal sensitive data to the vault.
- Avoid committing machine-specific workspace state unless intentionally shared.
- Review `.obsidian/workspace.json` before committing.
- Verify UTF-8 encoding before committing Portuguese notes to prevent encoding mismatches.

## Specialized Skills & Tools

This repository includes specialized `.claude/skills/` files:
- `conhecimento.md` — guidance for managing technical knowledge notes in `Mind/Conhecimento/`.
- `obsidian_cli.md` — documentation for programmatic vault interaction via Obsidian CLI.

## Delegation Guidance

- Prefer organizing new knowledge by concept, not by the chapter order of a source PDF.
- Before using cheaper subagents, compare likely token cost against the context size required to keep notes coherent.
- Use cheaper subagents only for semantically tight batches with minimal context.
- Keep taxonomy decisions, deduplication, and final cross-link review in the main agent or in a dedicated final link-review pass.
