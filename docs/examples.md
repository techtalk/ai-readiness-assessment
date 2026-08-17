# Example: the plugin assessed against itself — and progressing

The clearest way to see what `/ai-readiness-assess` produces is to read
real reports. We ran it against **this plugin's own repository** —
dogfooding the instrument on itself — and then again after acting on its
own top recommendation. The two reports together show **progression**.

Each report opens with two lines — the level and the next step — then an
**AI Readiness Score** broken down across five readiness dimensions
(Context · Conventions · Architectural guidance · Guardrails · Agent
readiness) and a **Prioritised Improvement Plan**.

## The progression at a glance

| | Baseline | After enforcing spec-first | After multi-repo + v1.0.0 |
| --- | --- | --- | --- |
| **AI Readiness — Habitat Maturity** | Level 3 (Regulating) | Level 3 (Regulating) | **Level 4 (Orchestrating)** |
| **Next Step / Gap** | +1.2 to Level 4 (Orchestrating) | +1.1 to Level 4 (Orchestrating) | +1.4 to Level 5 (Supervising) |
| 14-dimension mean | L2.7 | L2.93 | **L3.64** |
| Architectural guidance (readiness dim.) | L3 | **L4** | L4 |
| Cognitive read | L3 — Habitat design | **L4 — Specification-led** | L4 — Specification-led |
| Habitat/Workflow Gap (coherence, secondary) | +0.2 — **Coherent** | +1.07 — **Ambition outpaces enablement** | **+0.36 — Coherent** |
| Date | 2026-06-03 | 2026-06-03 | 2026-08-16 |
| Report | [HTML](examples/self-assessment.html) · [markdown](https://github.com/techtalk/ai-readiness-assessment/blob/main/assessments/2026-06-03-assessment.md) | [HTML](examples/self-assessment-2.html) · [markdown](https://github.com/techtalk/ai-readiness-assessment/blob/main/assessments/2026-06-03-assessment-2.md) | [HTML](examples/self-assessment-3.html) · [markdown](https://github.com/techtalk/ai-readiness-assessment/blob/main/assessments/2026-08-16-assessment.md) |

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

### The third reading — and the uncomfortable part

Seventy-four days later the habitat did catch up. The mean rose **L2.93 →
L3.64**, the headline crossed to **Level 4 (Orchestrating)**, and the gap
closed to **+0.36 — Coherent**.

But read *how* it closed. Of the three dimensions the second report named
as the ceiling — Testing, Observability, Agent composition — **only
Testing moved.** Coherence was restored by everything *else* rising: the
behavioural read climbed six levels across five dimensions as the way of
working shifted to supervising whole slices, and two more dimensions
gained a level from the specifications work.

Agent composition and Observability are still L2. They were the ceiling
in June and they are the ceiling now, and the third report says so rather
than leading with the number that improved.

That arc — *coherent L3 → L4 with a new positive gap → coherent L4* — is
the instrument working as designed: it tracks not just the level but the
[coherence between thinking and habitat](explanation/coherence-not-level.md),
and it stays honest in both directions — naming the habitat debt when the
discipline jumped ahead, and naming the unmoved dimensions when the
number recovered. See the
[assessment output structure](reference/assessment-output.md) for a
section-by-section guide.

## Multi-repo portfolio examples

These show what `/ai-readiness-rollup` produces across several
repositories. All three are **synthetic** — constructed to illustrate the
report shape, not readings of any real estate. Each is a single
self-contained HTML file that works opened straight from disk.

| Example | Shape | Report |
| --- | --- | --- |
| **Parent repo with submodules** | One harness at the root, three submodules, all bound. Narrow spread. | [HTML](examples/parent-repo-submodules.html) · [markdown](examples/parent-repo-submodules.md) |
| **Separate harness, partially bound** | Four services on one platform harness — two bound, one stale-pinned, one not bound at all. Spread of 1.79. | [HTML](examples/separate-harness-partially-bound.html) · [markdown](examples/separate-harness-partially-bound.md) |
| **Fragmented estate** | Five services carrying diverged copies of a common ancestor, plus a legacy repo at `posture: maintenance`. | [HTML](examples/fragmented-estate.html) · [markdown](examples/fragmented-estate.md) |

None of them contains an overall score, grade or percentage. The
portfolio headline is a distribution and a split ceiling — see
[why there is no portfolio score](explanation/why-no-portfolio-score.md).

### The real one

**[The Habitat-Thinking estate](examples/habitat-thinking-estate.md)** is
an actual roll-up across the repositories that build this instrument. It
does not produce a spread — one subject is comparable, one was measured
by a different instrument, and one could not be found. It is published as
it came out, and running it changed the tool: the `incompatible` coverage
status and the two-comparable-subjects rule for the spread both exist
because of it.

