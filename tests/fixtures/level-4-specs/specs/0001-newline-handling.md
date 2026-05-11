---
id: 0001
title: Newline handling in count_words
status: implemented
created: 2026-03-04
---

# Spec 0001 — Newline handling in `count_words`

## What

`count_words(text: str) -> int` treats any whitespace character —
including newlines, tabs, and carriage returns — as a word separator.

## Why

The library is used to count words across multi-line plain-text
files (essays, prose drafts). Treating only spaces as separators
under-counts heavily for typical input. The behaviour should match
the user's intuition: "if I see N words on the page, count_words
returns N."

## Acceptance

- `count_words("one\ntwo\nthree") == 3`
- `count_words("a\tb\tc") == 3`
- `count_words("hello world\r\nhow are you") == 5`
- Mixed whitespace (any combination of `\n`, `\r`, `\t`, ` `) is
  treated as one separator boundary.

## Out of scope

- Locale-specific word boundaries (CJK languages, etc.).
- Stripping of punctuation.

## Plan

See `specs/plans/0001-newline-handling-plan.md`.

## Objections

See `docs/objections/0001-newline-handling.md`.
