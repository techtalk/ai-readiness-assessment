# word-count

A small utility that counts words in a text file.

## Install

Clone the repo. Requires Python 3.10+.

## Use

```bash
python -m wordcount path/to/file.txt
```

## Development

- Linting: `ruff check .` (also runs in CI on every PR).
- Tests: `pytest` (CI requires ≥ 80% coverage to merge).
- Pre-commit: `pre-commit install` once; ruff runs on every commit.
- PR checklist: see `.github/PULL_REQUEST_TEMPLATE.md`.

The team uses Cursor; see `.cursorrules` for the agent's coding
preferences. The team has CI verification but no project-wide
agent-collaboration document yet — adding `CLAUDE.md` is on the
roadmap.
