---
name: wordcount-style
description: Review a diff for style drift against CLAUDE.md and HARNESS.md. Checks pathlib vs os.path, bare except, type hints on public functions, print in library code, and old-syntax unions.
---

# wordcount-style

Project-local skill. Reviews a diff against CLAUDE.md / HARNESS.md.

## Checks

- `os.path` use → flag with pathlib equivalent.
- Bare `except:` → flag.
- Public function without return-type annotation → flag.
- `print(...)` in library code → flag.
- `Union[X, Y]` / `Optional[X]` → flag with `X | Y` / `X | None`.

## Output

Per finding: path, line, snippet, suggested replacement, the
convention cited.
