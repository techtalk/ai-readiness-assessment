---
id: 0001
title: Newline handling in count_words
status: implemented
created: 2026-03-04
---

# Spec 0001 — Newline handling

(Same as L4 fixture — see specs/0001-newline-handling.md there for
the full text. Kept in this fixture as part of the L4 habitat
inheritance.)

## What

`count_words(text: str) -> int` treats any whitespace character as
a word separator.

## Why

The library is used for prose; whitespace-collapsing matches user
intuition.

## Acceptance

- `count_words("one\ntwo\nthree") == 3`
- `count_words("a\tb\tc") == 3`
- `count_words("hello world\r\nhow are you") == 5`

## Plan / Objections

See `specs/plans/0001-newline-handling-plan.md` and
`docs/objections/0001-newline-handling.md`.
