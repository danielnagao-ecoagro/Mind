# obsidian_cli

Use this skill when working with the full Obsidian CLI while the desktop app is running. Handle any supported CLI task the user requests, including note and folder operations, search, links, aliases, properties, tags, tasks, daily notes, templates, bases, bookmarks, tabs, workspace inspection, plugins, themes, snippets, sync, history, recovery, commands, hotkeys, and developer/devtools commands.

## Goals

- Operate safely on Markdown notes inside the vault.
- Preserve Obsidian conventions such as `[[wikilinks]]`, note filenames, and `.obsidian` settings.
- Prefer fast terminal inspection before editing.

## CLI Prerequisite

- Run `obsidian help` to confirm the CLI is reachable.
- If the command returns `The CLI is unable to find Obsidian. Please make sure Obsidian is running and try again.`, start the Obsidian desktop app first.
- Treat Obsidian CLI commands as unavailable until the app is running.
- The CLI is interactive: running `obsidian` opens a prompt, and `help` inside that prompt shows available commands.

## CLI Basics

- Syntax: `obsidian <command> [options]`
- Global option: `vault=<name>` targets a specific vault by name.
- `file=<name>` resolves by note name like a wikilink.
- `path=<path>` uses the exact vault-relative path such as `Projects/Plan.md`.
- Most commands default to the active file when `file` and `path` are omitted.
- Quote values with spaces: `name="Project Roadmap"`.
- Use `\n` and `\t` inside content values when needed.
- Use `obsidian help <command>` to inspect a specific command before using it when arguments are unclear.

## Workflow

1. Identify the vault root and inspect its contents with `rg --files` or `Get-ChildItem`.
2. Check whether the native CLI is available with `obsidian help` before depending on it.
3. If the CLI is unavailable, fall back to direct file operations in the vault.
4. Prefer native Obsidian CLI commands whenever they cover the requested operation.
5. Use `obsidian help <command>` for exact flags and behavior when working outside the common flows.
6. Read relevant notes or inspect current state before mutating content, config, plugins, sync state, or workspace state.
7. Use backlinks, links, history, or search before renaming, moving, deleting, restoring, or bulk-changing notes.
8. Re-scan or re-read results after changes to verify the operation completed as intended.

## Decision Rules

- Use the Obsidian CLI first when the requested action maps cleanly to an existing command.
- Use direct file editing when the CLI cannot express the requested text transformation cleanly, such as replacing sections, rewriting paragraphs, or applying coordinated edits across several notes.
- Use `obsidian help <command>` before execution when a command is unfamiliar or the arguments are ambiguous.
- Read current state before any operation that changes plugins, themes, snippets, sync, history, tabs, workspace state, or developer tooling.
- Prefer machine-readable formats such as `json`, `csv`, or `tsv` when the output will be analyzed or summarized.
- Re-verify after every mutation with a read, search, list, backlink, unresolved-link, or state-inspection command.

## Confirmation Threshold

Proceed directly for normal note work such as create, read, append, prepend, search, list, backlinks, tags, tasks, and non-destructive inspection.

Use extra caution for stateful or destructive operations:

- Destructive note changes: `delete`, especially `delete permanent`
- Recovery changes: `history:restore`, `sync:restore`
- App-state changes: `plugin:*`, `theme:*`, `snippet:*`, `plugins:restrict`, `sync on|off`, `reload`, `restart`
- Developer commands: `eval`, `dev:*`, `devtools`

For these operations, inspect current state first and make the scope explicit in the command being run.

## Command Coverage

The skill should be ready to use all CLI commands shown by `obsidian help`, including:

- Vault and navigation: `vault`, `vaults`, `workspace`, `tabs`, `tab:open`, `open`, `random`, `random:read`, `recents`
- Files and folders: `file`, `files`, `folder`, `folders`, `create`, `read`, `append`, `prepend`, `rename`, `move`, `delete`
- Links and structure: `backlinks`, `links`, `orphans`, `deadends`, `unresolved`, `outline`, `wordcount`
- Search and discovery: `search`, `search:context`, `search:open`, `aliases`, `tags`, `tag`, `properties`, `property:read`
- Metadata mutation: `property:set`, `property:remove`, `bookmark`, `bookmarks`
- Daily notes and templates: `daily`, `daily:path`, `daily:read`, `daily:append`, `daily:prepend`, `templates`, `template:read`, `template:insert`
- Tasks and commands: `tasks`, `task`, `command`, `commands`, `hotkey`, `hotkeys`
- Bases: `bases`, `base:views`, `base:query`, `base:create`
- Plugins, themes, snippets: `plugin`, `plugins`, `plugins:enabled`, `plugin:enable`, `plugin:disable`, `plugin:install`, `plugin:uninstall`, `plugin:reload`, `theme`, `themes`, `theme:install`, `theme:set`, `theme:uninstall`, `snippets`, `snippets:enabled`, `snippet:enable`, `snippet:disable`
- History and sync: `history`, `history:list`, `history:open`, `history:read`, `history:restore`, `diff`, `sync`, `sync:status`, `sync:deleted`, `sync:history`, `sync:open`, `sync:read`, `sync:restore`
- Application and diagnostics: `reload`, `restart`, `version`
- Developer tooling: `devtools`, `dev:debug`, `dev:console`, `dev:errors`, `dev:css`, `dev:dom`, `dev:mobile`, `dev:screenshot`, `dev:cdp`, `eval`

## Note Mutation Playbook

Use this sequence whenever the user asks to create, change, move, rename, or delete notes.

1. Resolve the target vault and note identity with `vault`, `files`, `file`, `read`, or `search`.
2. Prefer Obsidian CLI mutations over raw filesystem edits when the app is available.
3. For creation, use `create` with `name=`, optional `path=`, and optional `content=` or `template=`.
4. For content updates, prefer `append`, `prepend`, `daily:append`, or `daily:prepend` when the request is additive.
5. For targeted rewrites, read the note first, then update the file contents carefully. If the CLI has no direct replace operation, edit the Markdown file directly.
6. For renames or moves, inspect backlinks first, then use `rename` or `move`.
7. For deletion, inspect backlinks and unresolved-link risk first, then use `delete`. Only use `permanent` when explicitly requested.
8. After every mutation, verify with `read`, `backlinks`, `unresolved`, `files`, or `search`.

## Mutation Patterns

- Create a note: `obsidian create name="Inbox" content="# Inbox"`
- Create in a folder: `obsidian create path="Projects/Roadmap.md" content="# Roadmap"`
- Create from template: `obsidian create name="Meeting Notes" template="Meeting"`
- Append content: `obsidian append file="Inbox" content="- Follow up with team"`
- Prepend content: `obsidian prepend file="Inbox" content="## Triage"`
- Update today's note: `obsidian daily:append content="- Journal entry"`
- Rename note: `obsidian rename file="Welcome" name="Inbox"`
- Move note: `obsidian move file="Inbox" to="Archive/Inbox.md"`
- Delete note to trash: `obsidian delete file="Inbox"`
- Delete permanently: `obsidian delete file="Inbox" permanent`

## When to Use File Editing

Use direct Markdown file edits only when:

- the Obsidian CLI is unavailable because the app is closed
- the change requires replacing or restructuring existing text beyond simple append/prepend operations
- the task requires bulk link rewrites or coordinated content edits across multiple notes

When editing files directly, preserve frontmatter, headings, wikilinks, and line endings where practical.

## Operating Patterns

- For note creation requests, prefer `create` or `daily:*` commands.
- For additive updates, prefer `append` or `prepend`.
- For structural updates to existing prose, read first and then edit the Markdown file directly if needed.
- For rename or move requests, inspect backlinks before running `rename` or `move`.
- For delete requests, inspect backlinks and unresolved-link impact, then default to trash rather than permanent deletion.
- For audits and reports, prefer list and query commands with structured output.
- For plugin, theme, snippet, sync, history, or workspace tasks, capture the current state before and after the change.

## Core Commands

- Vault and discovery: `vault`, `vaults`, `files`, `folders`, `file`, `folder`, `search`, `search:context`, `workspace`, `recents`
- Note operations: `create`, `read`, `append`, `prepend`, `open`, `move`, `rename`, `delete`
- Link analysis: `backlinks`, `links`, `orphans`, `deadends`, `unresolved`
- Daily notes and templates: `daily`, `daily:path`, `daily:read`, `daily:append`, `daily:prepend`, `templates`, `template:read`, `template:insert`
- Metadata and structure: `properties`, `property:read`, `property:set`, `property:remove`, `outline`, `tags`, `tag`, `aliases`
- Tasks: `tasks`, `task`
- Plugins and themes: `plugins`, `plugins:enabled`, `plugin`, `plugin:enable`, `plugin:disable`, `plugin:install`, `themes`, `theme`, `theme:set`
- History and sync: `history`, `history:read`, `history:restore`, `diff`, `sync:status`, `sync:history`, `sync:read`, `sync:restore`

## Preferred Commands and Examples

- Check CLI availability: `obsidian help`
- Inspect one command: `obsidian help search`
- List vaults: `obsidian vaults verbose`
- Show current vault path: `obsidian vault info=path`
- List markdown files: `obsidian files ext=md`
- Read a note by name: `obsidian read file="Welcome"`
- Create a note: `obsidian create name="Inbox" content="# Inbox"`
- Rename a note: `obsidian rename file="Welcome" name="Inbox"`
- Move a note: `obsidian move file="Inbox" to="Archive/Inbox.md"`
- Append to today's daily note: `obsidian daily:append content="- Captured from CLI"`
- Search text: `obsidian search query="project roadmap" format=json`
- List unresolved links: `obsidian unresolved counts`
- List orphan notes: `obsidian orphans total`
- Show tasks in the daily note: `obsidian tasks daily`
- Set a property: `obsidian property:set file="Inbox" name=status value=active type=text`
- Query a base: `obsidian base:query file="Projects Base" view="Active" format=md`
- List commands: `obsidian commands filter=workspace`
- List hotkeys: `obsidian hotkeys format=json`
- List plugins: `obsidian plugins filter=community versions`
- Enable a plugin: `obsidian plugin:enable id=templater-obsidian filter=community`
- Set theme: `obsidian theme:set name="Minimal"`
- Read history: `obsidian history:read file="Inbox" version=1`
- Show sync status: `obsidian sync:status`
- Inspect DOM in developer mode: `obsidian dev:dom selector=".workspace-tabs"`
- List notes: `rg --files Mind`
- Find wiki links: `rg "\[\[.*\]\]" Mind`
- Find references to a note: `rg "Welcome|\\[\\[Welcome\\]\\]" Mind`
- Read a note: `Get-Content Mind\\Welcome.md`

## Editing Rules

- Keep daily notes in `YYYY-MM-DD.md` format when that pattern already exists.
- Prefer descriptive note names for evergreen content, such as `Project Roadmap.md`.
- Preserve frontmatter if present.
- Avoid unnecessary changes to `.obsidian/workspace.json`; it is often machine-specific.
- When renaming a note, update all matching wikilinks in the vault.
- Prefer `file=<name>` when the note name is unambiguous and `path=<path>` when precision matters.
- Prefer structured output formats like `json`, `csv`, or `tsv` for commands such as `backlinks`, `bookmarks`, `plugins`, `tags`, and `tasks` when the output will be parsed or summarized.
- For destructive note operations, assume trash-first behavior unless the user explicitly asks for permanent deletion.
- When updating note content, preserve existing sections unless the request clearly asks for replacement.
- Prefer reading current state first for plugins, themes, sync, history, tasks, and workspace operations.
- Use machine-readable output when the result will be filtered, transformed, or summarized.

## Safety Checks

- Confirm the target path is inside the vault before moving or renaming files.
- Review backlinks before deleting or replacing a note.
- Treat `.obsidian/app.json`, `appearance.json`, and `core-plugins.json` as shared config; change them only when the task clearly requires it.
- Do not assume Obsidian CLI commands will work in headless mode; verify the desktop app is open first.
- Use `delete permanent` only when the task explicitly requires bypassing trash.
- Be careful with plugin, theme, sync, history restore, and restart commands because they change application state, not just files.
- Before deleting or renaming a note, check `backlinks`, `links`, and `unresolved` when the note appears to be widely referenced.
- After direct file edits, verify the result with `obsidian read` or terminal file reads.
- Treat `history:restore`, `sync:restore`, `plugin:uninstall`, `theme:set`, `snippet:disable`, `plugins:restrict`, `reload`, `restart`, `eval`, and `dev:*` commands as stateful operations that require extra care.
- For developer commands, avoid actions that inspect or modify unrelated private content beyond the requested scope.

## Example Requests

- Create today's daily note and add starter headings.
- Rename `Welcome.md` to `Inbox.md` and update wiki links.
- Find orphan notes in the vault.
- Review `.obsidian` settings and explain what is safe to commit.
- List unresolved links and summarize the most important cleanup items.
- Query tasks tagged for today and mark one as done.
- Create a note called `Ideas` with starter bullet points.
- Update `Projects/Roadmap.md` to add a new milestone section.
- Delete `Scratch.md`, but only after checking whether other notes link to it.
- List all enabled community plugins with versions.
- Query a base view and summarize the rows returned.
- Show recent files and open one in a new tab.
- Inspect available commands related to templates or workspace actions.
