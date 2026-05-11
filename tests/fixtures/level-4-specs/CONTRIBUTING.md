# Contributing — wordcount

## Spec-first ordering

Every PR that touches `src/` must either:

- Reference an existing spec under `specs/` in the PR body, **or**
- Introduce a new spec file in the same PR.

PRs labelled `bug` or with a branch prefix `fix/` are exempt. CI
enforces this via `scripts/check-spec-first.sh`.

## Adversarial review

Every non-exempt PR carries an objection record under
`docs/objections/<spec-slug>.md`. All dispositions must be resolved
(accepted, deferred with reason, or refuted with reason) before
merge.

## PR checklist

- [ ] Spec referenced or introduced.
- [ ] Plan under `specs/plans/` updated if material changes.
- [ ] Objection record dispositions resolved.
- [ ] Failing test was written before production code.
- [ ] CI green.
