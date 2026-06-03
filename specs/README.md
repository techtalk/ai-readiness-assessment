# Specifications

This directory makes intent **first-class** — the L3→L4 move. A spec
captures the *what and why* of a change, separately from the *how* that
lives in the diff. It was introduced (see
[`0001-introduce-specs-layer.md`](0001-introduce-specs-layer.md)) to start
the jump surfaced by the repo's own self-assessment, where the absence of
a specs layer capped the cognitive read at L3.

## When to write one

Write a spec for **substantive, behaviour-changing work** — the
assessment instrument (command / skill), the model or scoring, or a new
workflow. **Exempt:** docs, chore, surface-sync, dependency, and
pure-fix changes.

## How

- **Start lightweight.** A one-paragraph **Intent** is enough to begin;
  flesh out Design and Risks as the change firms up.
- **Spec-first.** Write or update the spec with the implementation, and
  reference it in the PR.
- **Number sequentially:** `specs/NNNN-slug.md`. Copy
  [`TEMPLATE.md`](TEMPLATE.md).
- Every spec carries a **Risks / what could go wrong** section — a
  lightweight adversarial review embedded in the spec itself, rather than
  a separate gate.

## Status

Spec-first is currently a **convention** (HARNESS.md → Context →
Conventions), not yet an enforced constraint. Promote it to an
agent-enforced constraint via `/harness-constrain` once the habit
settles — that promotion is the step that lifts the cognitive read from
L3 toward L4.
