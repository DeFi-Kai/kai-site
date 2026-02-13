# Agent Guide for kai-site

This repository is a Hugo site using the PaperMod theme. Use this guide to run the site, validate changes, and follow the established content conventions.

## Quick Start
- Primary config lives in `hugo.yaml`.
- Content lives in `content/` as Markdown files with TOML front matter.
- Theme lives in `themes/PaperMod` (vendor/theme content; avoid editing unless requested).

## Daily DeFi Brief
- The latest brief is published as static HTML at `static/briefs/latest/index.html`.
- The Brief Bot pipeline writes this file directly; do not replace it with a Markdown page.
- The live URL is `/briefs/latest/` and is linked from the homepage.

## Build, Lint, Test Commands
This repo does not include Node/Go tooling or test suites beyond Hugo itself.

### Build the Site
- Production build: `hugo --minify`
- Draft-inclusive build: `hugo --buildDrafts --minify`

### Local Development Server
- Live preview: `hugo server`
- Include drafts: `hugo server --buildDrafts`
- Use local baseURL: `hugo server --config hugo.yaml,hugo.dev.yaml`
- Bind all interfaces: `hugo server --bind 0.0.0.0`

### Single Test / Targeted Checks
There are no unit tests or lint tasks configured. For a focused check:
- Build a single draft for review: `hugo --buildDrafts --minify`
- Render only one section: `hugo --minify --renderToDisk --printPathWarnings`

### Clean/Artifacts
Hugo outputs to `public/` by default. If you need a clean build:
- Remove output: `rm -rf public/` (run manually only when needed).

## Code Style and Content Guidelines
These are conventions observed in the current content and Hugo setup.

### Front Matter
- Use TOML front matter with `+++` delimiters.
- Required fields: `date`, `draft`, `title`.
- Use lowercase keys; keep single quotes for string values.
- Prefer explicit `draft = true/false` for clarity.
- Date format follows RFC 3339 with timezone offset.

Example:
```
+++
date = '2025-12-18T14:51:02-05:00'
draft = false
title = 'About'
+++
```

### Markdown Style
- Use ATX headings (`##`, `###`) with a blank line before headings.
- Prefer sentence case for headings.
- Use blank lines between sections and lists.
- Favor short paragraphs; keep lines readable but do not hard-wrap unless it improves clarity.
- Use `**bold**` and `*italic*` for emphasis; avoid excessive formatting.
- Lists should use `-` for bullets with a single space after the dash.

### Content Organization
- Place long-form essays in `content/essays/`.
- Single pages (about, CV) live directly in `content/`.
- Keep file names lowercase and hyphenated (kebab-case).
- Keep titles in Title Case unless the content explicitly calls for stylization.

### Imports and Dependencies
- This project does not use application code imports.
- Do not add JavaScript/CSS dependencies unless explicitly requested.
- If you must reference assets, place them under `static/` and link using absolute site paths (e.g., `/images/foo.png`).

### Formatting and Linting
- No automated formatter is configured.
- Follow existing whitespace conventions in Markdown and YAML.
- Do not introduce tabs in Markdown; use spaces.

### Types and Naming Conventions
- There is no typed language in use; follow filename and title conventions:
  - Filenames: lowercase kebab-case
  - Titles: Title Case
  - Section directories: lowercase plural (`essays`, `research`, etc.)

### Error Handling and Diagnostics
- Use `hugo --printPathWarnings` when diagnosing broken links or missing resources.
- Use `hugo --debug` for verbose logs when troubleshooting builds.
- If a build fails, check `hugo.yaml` for syntax issues first.

## Theme Notes (PaperMod)
- Theme configuration is driven by `hugo.yaml` under `params`.
- Avoid direct edits in `themes/PaperMod` unless specifically requested.
- Refer to the PaperMod wiki for feature flags and supported params.

## Repository Hygiene
- Keep `public/` out of version control unless the repository explicitly expects built assets.
- Do not reformat existing Markdown unless necessary for the task.
- Prefer small, focused edits to content files.

## Cursor and Copilot Rules
- No `.cursor/rules/`, `.cursorrules`, or `.github/copilot-instructions.md` files are present in this repository.

## Content Operations

### Add a New Page
- Create a new Markdown file under `content/` (single pages) or `content/<section>/` (section pages).
- Use TOML front matter with `+++`, required fields `date`, `draft`, `title`.
- Keep filenames lowercase and kebab-case; use Title Case for `title`.
- If the page should appear in navigation, add it to the `menu.main` list in `hugo.yaml`.

Example:
```
+++
date = '2026-01-23T09:00:00-05:00'
draft = true
title = 'New Page'
+++

## Section heading

Body text.
```

### Add a New Section
- Create a new directory under `content/` with a lowercase plural name (e.g., `content/research/`).
- Add at least one Markdown file in the new directory with valid front matter.
- Add the section to `menu.main` in `hugo.yaml` if it should show in nav.

### Delete a Page
- Remove the Markdown file from `content/` or the relevant section directory.
- If it was in navigation, remove its entry from `hugo.yaml`.

### Delete a Section
- Remove the section directory from `content/` once it is empty.
- Remove any matching menu entry from `hugo.yaml`.
- Consider running `hugo --minify --printPathWarnings` to check for broken links.

## Suggested Workflow
1. Edit or add content under `content/`.
2. Run `hugo server --buildDrafts` to preview locally.
3. Run `hugo --minify` for a production build check.

## Notes for Agents
- Treat `themes/PaperMod` as vendor code.
- Keep changes consistent with the existing tone: concise, research-oriented, and professional.
- When adding new pages, ensure they appear in navigation by updating `hugo.yaml` if needed.
