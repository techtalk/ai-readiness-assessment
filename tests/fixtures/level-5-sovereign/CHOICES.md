# Choices

Decision archaeology. Every load-bearing choice the project has made,
captured as a story: context, choice, why, alternatives considered.

---

## C-001 — Habitat-as-plugin

**Date**: 2026-02-20

**Context**: Sibling teams kept asking how the wordcount team works.
Documentation walkthroughs didn't transfer; the conventions only
stuck when the receiving team had a working copy to edit.

**Choice**: Package the habitat (CLAUDE.md skeleton, HARNESS.md
skeleton, spec-implement command, wordcount-style skill, CI
workflow) as a Claude Code plugin under `.claude-plugin/plugin.json`.
Adopters install once and run `/wordcount-habitat-init`.

**Why**: Working software transfers; PDFs don't. The plugin is the
team's habitat as a portable artefact.

**Alternatives considered**:

- A walkthrough doc — tried and failed.
- A cookiecutter template — works once but no version-bump pipe.
- A git submodule of the wordcount repo — sibling teams couldn't
  diverge.

**Verified by**: REFLECTION_LOG.md 2026-04-10 (sibling adoption ran
in two steps).

---

## C-002 — Quarterly governance audit cadence

**Date**: 2026-03-01

**Context**: HARNESS.md had constraints declared "agent-enforced"
that nobody had verified for months. Constraint drift was hidden.

**Choice**: Quarterly governance audit. Records land under
`audits/<year>-Q<n>.md`. Audit checks every constraint's actual
enforcement state against its declared state.

**Why**: Drift is the default. Without a scheduled audit, the
declared state and the actual state separate silently.

**Alternatives considered**:

- Continuous (PR-time) audit — too expensive, too noisy.
- Annual — too slow; constraints can rot for 9 months.
- Monthly — overhead exceeded benefit on a project this size.

**Verified by**: audits/2026-Q1.md caught a drifted spec-conformance
constraint (REFLECTION_LOG.md 2026-04-28).

---

## C-003 — CHOICES.md, not ADRs alone

**Date**: 2026-03-15

**Context**: `docs/adr/` had two entries after a year. Most
decisions weren't being captured.

**Choice**: Adopt `CHOICES.md` (one file, story-shaped entries,
plus a CI check that every load-bearing decision lands here). ADRs
remain for the formal-record case.

**Why**: ADR overhead was too high. CHOICES.md is light enough that
people actually use it; the story shape captures more reasoning than
the ADR template.

**Alternatives considered**:

- Stick with ADRs — was failing.
- No structured capture — invisible drift.

---

## C-004 — Fitness functions in CI, not on a schedule

**Date**: 2026-03-22

**Context**: Layer-boundary violations and complexity hotspots were
showing up in code review. Catching them post-merge was costing
re-work.

**Choice**: Three fitness-function jobs in the CI workflow (layer
boundary, complexity hotspots, dependency age). Failures block
merge.

**Why**: Faster feedback. The fitness check is cheap (seconds);
catching the violation at PR time is much cheaper than catching it
at refactor time.

---

## C-005 — Model routing exception for adversarial review

**Date**: 2026-05-03

**Context**: Quarterly cost snapshot showed adversarial-review
runs over budget by 22%. The default model was Opus when the routing
table said Sonnet.

**Choice**: Add a model-routing compliance constraint to HARNESS.md
(advisory at PR time, audit monthly). Codify the routing rules in
`MODEL_ROUTING.md`.

**Why**: Routing rules aren't self-enforcing. Without an active
check, the team will reach for the most familiar model.

**Verified by**: REFLECTION_LOG.md 2026-05-02 (the surprise that
triggered this choice).
