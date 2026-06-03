# Example: the plugin assessed against itself — and progressing

The clearest way to see what `/ai-readiness-assess` produces is to read
real reports. We ran it against **this plugin's own repository** —
dogfooding the instrument on itself — and then again after acting on its
own top recommendation. The two reports together show **progression**.

## The progression at a glance

| | Baseline | After enforcing spec-first |
| --- | --- | --- |
| **Cognitive read** | L3 — Habitat design | **L4 — Specification-led** |
| **Habitat Maturity Level** | L3 (mean 2.79) | L3 (mean 2.93) |
| **Habitat Build Gap** | +0.2 — **Coherent** | +1.1 — **Ambition outpaces enablement** |
| Report | [HTML](examples/self-assessment.html) · [markdown](https://github.com/techtalk/ai-readiness-assessment/blob/main/assessments/2026-06-03-assessment.md) | [HTML](examples/self-assessment-2.html) · [markdown](https://github.com/techtalk/ai-readiness-assessment/blob/main/assessments/2026-06-03-assessment-2.md) |

## The story

The **baseline** read a *coherent* L3: a strong habitat, with the absence
of a specifications layer as the one thing capping the cognitive read.
Its top recommendation was to add a `specs/` layer.

We did exactly that — and made spec-first an *enforced* discipline (a
`specs/` layer, the Spec-first constraint, a required CI gate, and an
adversarial review at the plan-approval gate). The **re-assessment** then
read **L4 — Specification-led**.

But notice the gap. It didn't stay coherent — it flipped to **+1.1,
ambition outpaces enablement**. Lifting the *discipline* to L4 left the
broader operational habitat (Testing, Observability, Agent composition —
still L2) behind. That's not a regression; it's the honest, instructive
consequence of a deliberate jump, and it names the next work: **build the
habitat the L4 thinking now implies**.

That arc — *coherent L3 → L4 with a new positive gap* — is the whole
point of the instrument working as designed: it tracks not just the level
but the [coherence between thinking and habitat](explanation/coherence-not-level.md),
and it stays honest (the repo is L4 in discipline, but the report says
plainly that the habitat must catch up). See the
[assessment output structure](reference/assessment-output.md) for a
section-by-section guide.
