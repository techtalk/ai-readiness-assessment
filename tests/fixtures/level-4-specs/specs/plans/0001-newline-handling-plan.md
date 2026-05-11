---
spec: specs/0001-newline-handling.md
status: complete
---

# Plan — Newline handling

## Approach

`str.split()` with no argument already splits on any whitespace and
collapses consecutive whitespace. The current implementation
(`text.split()`) already satisfies the spec for the simple cases. The
plan: write the failing tests to confirm the behaviour, then verify
no implementation change is needed.

## Steps

1. Add `test_count_words_newlines_count_as_separators` to
   `tests/test_main.py`. Expect it to pass on first run.
2. Add `test_count_words_handles_carriage_returns_and_tabs`. Expect
   it to pass on first run.
3. Add `test_count_words_collapses_consecutive_whitespace`. Expect
   it to pass on first run.
4. If any test fails, switch to `re.split(r'\s+', text)` and re-run.

## Risk

`str.split()` returns an empty list for the empty string. This
collides with Spec 0002 — that spec demands a raise, not zero. Make
sure Spec 0002 lands first.

## Verification

`pytest tests/test_main.py -v` shows all four word-count tests
passing.
