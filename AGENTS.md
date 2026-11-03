# Repository Guidelines

## Project Structure & Module Organization

This repository is a Chinese-language paper-reading site built with MkDocs Material. Read `STRUCTURE.md` before adding content; it defines the target layout and note template. Currently, `docs/index.md` is the only site page. Create planned directories as real content becomes available:

- `docs/papers/<year>-<short-name>/index.md`: one canonical note per paper, with publication year in the path.
- `docs/papers/<year>-<short-name>/assets/`: paper-specific images and figures.
- `docs/topics/`: topic overviews, reading routes, and comparisons linking to canonical notes.
- `docs/reading-list.md`, `docs/papers/index.md`, and `docs/templates/paper-note.md`: reading progress, note index, and reusable template.

`mkdocs.yml` controls navigation and theme; `requirements.txt` declares dependencies. `.github/workflows/deploy.yml` deploys pushes to `main`. There is no application source tree or test directory.

## Build, Test, and Development Commands

Use Python 3.12 to match CI. From the repository root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve                 # Preview locally with live reload
mkdocs build --strict        # Validate and generate site/
git diff --check             # Check patch whitespace
```

Keep `.venv/` and generated `site/` output out of commits. Publishing normally happens through GitHub Actions.

## Coding Style & Naming Conventions

Write site content in Chinese, retaining original paper titles and technical terms where useful. Use descriptive Markdown headings, fenced code blocks, and relative links to Markdown files and assets. Use two-space YAML indentation and no tabs. No formatter or linter is currently configured.

Use lowercase English filenames with hyphens, such as `2026-paper-short-name`. Keep paths stable across rereads. Store each paper once and link it from multiple topics. Follow the note template in `STRUCTURE.md`; distinguish authors’ claims from personal interpretation. Update relevant indexes and reading status when adding notes.

## Testing Guidelines

There is no automated test framework or coverage target. For content, navigation, or configuration changes, run `mkdocs build --strict` and resolve reported problems. Preview affected pages to check navigation, links, images, tables, and formulas. Add navigation entries only after their pages exist.

## Commit & Pull Request Guidelines

The initial commit uses `chore: initialize MkDocs paper notes site`. Follow the `type: short imperative summary` format, using suitable prefixes such as `docs:`, `fix:`, or `chore:`.

Keep changes focused. Pull requests should explain the purpose, list affected pages, report validation performed, and link related issues when applicable. Include screenshots for layout or theme changes. Update `STRUCTURE.md` alongside structural changes.

## End-of-Response Commit Check

Before finishing every response, check `git status --short` and assess whether changes need committing. If so, include a suggested commit message in the final response using the convention above, with a brief description of the intended changes. Otherwise, state that no commit is needed. Suggesting a commit does not authorize creating one.
