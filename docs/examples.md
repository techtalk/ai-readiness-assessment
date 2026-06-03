# Example: the plugin assessed against itself

The clearest way to see what `/ai-readiness-assess` produces is to read a
real report. So we ran it against **this plugin's own repository** —
dogfooding the instrument on itself.

- **Rendered report (HTML):** [view the self-assessment](examples/self-assessment.html)
- **Markdown source:** [`assessments/2026-06-03-assessment.md`](https://github.com/techtalk/ai-readiness-assessment/blob/main/assessments/2026-06-03-assessment.md)

## What it found

| | |
| --- | --- |
| **Habitat Maturity Level** | L3 (14-dimension mean 2.79) |
| **Cognitive read** | L3 — Habitat design |
| **Habitat Build Gap** | +0.2 — **Coherent** |

A coherent **L3**: a strong, persistent habitat — synced context
(HARNESS / AGENTS / ONBOARDING / convention files), a running
reflection→promotion loop, policy-as-code CI on a protected `main`, and a
published plugin — matched by an L3 operational profile. The one missing
rung is the **specifications layer** (no `specs/`, no spec-first
ordering, no adversarial spec review), which is both the L3→L4 ceiling
and the dimension most worth lifting.

It's a useful illustration of the headline idea: the signal is
[coherence, not level](explanation/coherence-not-level.md). This repo is
not L5 — and that's fine; team and habitat are *in step*, which is the
healthy state to grow from.

See the [assessment output structure](reference/assessment-output.md) for
a section-by-section guide to everything in the report.
