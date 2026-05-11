---
id: 0002
title: Empty input is an error
status: implemented
created: 2026-04-22
---

# Spec 0002 — Empty input is an error, not zero

## What

`count_words("")` raises `ValueError` with the message "empty input".
It does not return 0.

## Why

Returning 0 is ambiguous — the caller cannot distinguish "the file
was empty" from "the file had no recognisable words." Raising forces
the caller to handle the case deliberately. The CLI catches the
error and prints "empty input" to stderr with exit code 1.

## Acceptance

- `count_words("")` raises `ValueError` with message matching
  `"empty input"`.
- `python -m wordcount /path/to/empty/file` prints "empty input" to
  stderr and exits 1.

## Out of scope

- Files that contain only whitespace (treated as empty after
  `.strip()`).

## Plan

Inline — the change is two lines:

```python
if not text:
    raise ValueError("count_words received empty input")
```

## Objections

See `docs/objections/0002-empty-input.md`.
