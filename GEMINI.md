# Project Overview: Mind

This repository contains an **Obsidian vault** located in the `Mind/` directory. It is used for personal knowledge management, daily journaling, and documentation. The project is a **Non-Code Project** focused on Markdown-based note-taking and utilizes the Obsidian ecosystem for organization and visualization.

## Directory Structure

- `Mind/`: The core Obsidian vault.
    - `daily/`: Contains daily notes following the `YYYY-MM-DD.md` naming convention.
    - `.obsidian/`: Internal Obsidian configuration (plugins, appearance, workspace state).
    - `Welcome.md`: The vault's landing page.
- `AGENTS.md`: Comprehensive guidelines for project structure, conventions, and manual testing.
- `.claude/skills/obsidian_cli.md`: Documentation for the specialized `obsidian_cli` tool, which enables programmatic interaction with the vault when the Obsidian desktop app is running.

## Key Features & Tools

- **Obsidian Integration**: Designed to be opened and managed primarily through the [Obsidian](https://obsidian.md/) desktop application.
- **Obsidian CLI**: A specialized CLI tool is available for automating note operations (create, read, search, etc.). Use `obsidian help` to verify availability.
- **Wikilinks**: Uses standard `[[Note Name]]` syntax for internal linking.

## Usage & Development Conventions

### Note Management
- **Conhecimento**: Antes de criar ou modificar qualquer nota na pasta `Mind/Conhecimento/`, você **DEVE** ler e seguir rigorosamente as diretrizes em `Mind/REGRAS_CONHECIMENTO.md`. Isso garante a integridade dos links, o encoding correto e o padrão de hashtags.
- **Daily Notes**: Create in `Mind/daily/` using the format `YYYY-MM-DD.md`.
- **Permanent Notes**: Create in `Mind/` root with descriptive names (e.g., `Topic Name.md`).
- **Formatting**: Use Markdown with clear headings and sentence-case titles.

### Tooling & Commands
- **Inspection**:
  - `Get-ChildItem Mind`: List vault contents.
  - `rg --files Mind`: Quickly list all tracked files.
  - `rg "\[\[.*\]\]" Mind`: Find internal wikilinks.
- **Obsidian CLI (App must be running)**:
  - `obsidian daily:append content="- New entry"`: Add to today's log.
  - `obsidian search query="keyword"`: Search across the vault.
  - `obsidian read file="Note Name"`: Read a specific note.

### Testing
- Testing is manual: Open the vault in the Obsidian app to verify links, embeds, and workspace behavior after any automated or manual file changes.

## Security Note
- Avoid committing personal or sensitive data.
- Be cautious when committing `.obsidian/workspace.json`, as it often contains local machine-specific state.
