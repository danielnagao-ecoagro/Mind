# Repository Guidelines

## Project Structure & Module Organization
This repository currently contains a single Obsidian vault in `Mind/`.

- `Mind/*.md`: vault notes. Example: `Mind/Welcome.md`, `Mind/2026-04-17.md`.
- `Mind/.obsidian/`: local vault configuration such as `app.json`, `appearance.json`, and `workspace.json`.

Keep content notes at the vault root unless a clear folder structure emerges. Treat `.obsidian/` changes carefully because they can be user-specific.

## Build, Test, and Development Commands
There is no build pipeline or automated test suite in the current repository. Useful local commands are:

- `Get-ChildItem Mind`: inspect vault contents.
- `rg --files Mind`: list tracked note and config files quickly.
- `Get-Content Mind\\Welcome.md`: read a note from the terminal.

Use Obsidian to edit and validate note links, embeds, and workspace behavior.

## Coding Style & Naming Conventions
Write notes in Markdown with clear headings and short paragraphs. Prefer descriptive filenames:

- Daily notes: `YYYY-MM-DD.md`
- Permanent notes: `Topic Name.md`

Use sentence case for headings, standard Obsidian wikilinks like `[[Note Name]]`, and fenced code blocks for commands or snippets. Keep JSON files in `.obsidian/` formatted consistently if edited manually.

## Testing Guidelines
Testing is manual for now.

- Open the vault in Obsidian after changes.
- Verify new or renamed notes resolve through `[[wikilinks]]`.
- Confirm `.obsidian/` edits do not break the workspace or core plugins.

If automation is added later, place tests beside the tooling they cover and document the command here.

## Commit & Pull Request Guidelines
No Git history is available in this workspace, so no established commit convention can be inferred. Use short imperative commit messages such as `Add daily note template` or `Clean up Obsidian config`.

Pull requests should include:

- a brief summary of changed notes or config
- any renamed or moved files
- screenshots only when UI or workspace behavior changed

## Security & Configuration Tips
Avoid committing secrets, personal data, or machine-specific workspace state unless it is intentionally shared. Review `.obsidian/workspace.json` before committing because it often reflects a local editor session.
