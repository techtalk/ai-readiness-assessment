---
name: wordcount-style
description: Review a diff for style drift in the wordcount codebase. Checks for pathlib vs os.path, bare except clauses, missing type hints on public functions, and print in library code. Use during PR review or after generating code that touches src/wordcount/.
---

# wordcount-style

Project-local skill. Reviews a diff against the conventions in
`CLAUDE.md` and the constraints in `HARNESS.md`.

## Checks

- Any use of `os.path` → flag, suggest `pathlib.Path` equivalent.
- Any bare `except:` (no exception type) → flag.
- Any public function (top-level `def name(...)` in `src/wordcount/`)
  without a return-type annotation → flag.
- Any `print(...)` in `src/wordcount/` files (excluding the `if
  __name__ == "__main__":` block) → flag.
- Any `Union[X, Y]` or `Optional[X]` annotation → flag, suggest
  `X | Y` or `X | None`.

## Output

For each finding: file path, line number, the offending snippet, the
suggested replacement, and the convention it violates (cite
`CLAUDE.md` or the `HARNESS.md` constraint by name).
