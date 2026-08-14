# Subject, habitat, team

The single-repo instrument assumes the repository it runs in *is* the
habitat under examination. That assumption holds in exactly one case,
and quietly conflates three different things everywhere else.

| Concept | What it is | Natural scope |
|---|---|---|
| **Subject** | The code artefacts the habitat governs | A repo, a submodule, a directory in a monorepo |
| **Habitat** | The harness and control surfaces governing it | May live in the subject, a sibling repo, a parent, a package, or an org |
| **Team** | Whose behaviour produces the cognitive read | People — never a repo |

Separating them gives one primitive that covers every shape:

> **Assessment unit = subject × governing habitat**, with the cognitive
> read scoped to the *team*.

## Why the team is not a repository

The cognitive read measures what people can think and do — how
directive their relationship to the agent is, what they actually inspect
before accepting work, how much of a unit of work they hand over. None
of that is a property of a directory.

A team of six that owns four services does not become four teams. They
carry the same habits into all four. What changes between the four is
the *environment* those habits meet.

Which is why the [scope run](../tutorials/assess-a-team-across-repositories.md)
asks the behavioural questions **once**. Asking them per repository does
not produce four readings; it produces four copies of one reading, at
four times the cost, with four opportunities to answer slightly
differently out of fatigue.

## Why the spread is the finding

One cognitive read measured against four habitats produces four gaps.
Their **spread** is a signal the single-repo instrument cannot produce,
because a single assessment has only one reading to compare.

A team can be Coherent in the greenfield service and a full level and a
half ahead of its environment in the legacy one. Both facts are true at
once, and the work they imply is opposite: hold the first, invest in
habitat for the second. Average them and you get a number describing
neither — which is
[why there is no portfolio score](why-no-portfolio-score.md).

## When practice genuinely does differ

Sometimes it does. A team really can work one way in the service they
deploy daily and another in the batch job they touch twice a year.

So each subject gets exactly one cheap question — *is your way of
working here materially different?* — and if the answer is yes, the six
behavioural dimensions are asked again for that subject. Its report
records `cognitive_source: subject`, and the portfolio shows its gap
separately from the team's general pattern.

One question is the right price. Asking nothing assumes uniformity that
may not hold; asking everything again assumes difference that usually
does not.

## Reuse is always declared

Where the team read is applied to a subject, the report **says so in its
body** — not in a footnote.

This matters more than it first appears. A reader picking up the report
for one repository has no way to tell a placement gathered there from
one carried in from a conversation about a different repository. Both
render as "L3". Silent reuse is not a shortcut; it is a false claim
about where the evidence came from.

## What this does not change

The model is untouched. Fourteen dimensions, the same verbs, the same
six-level ladder, the same three disciplines, the same gap formula and
the same three regimes. This is a change of *unit*, not of measure — and
with no scope manifest present, nothing about a single-repo assessment
is different at all.
