# Distribution is not federation

A platform team writes an excellent harness. It sits in
`platform-harness`, governs nothing by accident, and is referenced in
every architecture deck. Twelve service teams are told to adopt it.

Eighteen months later, how many of those twelve are actually governed by
it?

Nobody knows — and that is the problem this distinction exists to
expose.

## Recorded is not enforced

A harness that exists somewhere is not a harness that governs here. The
difference is not paperwork; it is whether anything in the subject
*executes, references, or enforces* the shared rule.

The assessment records three states per dimension:

| Provenance | What it means |
|---|---|
| `local` | The evidence is in the subject itself. |
| `inherited` | The shared habitat supplies it **and** it demonstrably reaches this subject. |
| `inherited-unbound` | The shared habitat declares it; nothing here executes it. |

`inherited-unbound` caps the dimension at whatever the *local* evidence
supports, and names the shared artefact that was expected to bind.

This is the same argument the instrument already makes about
[specifications you cannot verify](coherence-not-level.md): an
unenforceable rule is aspiration, not control. A governance policy that
lives in another repository and reaches this one through nothing but an
architecture diagram is in exactly that category.

## Why this is worth measuring

Because the two situations look identical on a slide and need opposite
responses.

An estate where the shared harness **binds** everywhere has a
maintenance problem: keep the binding current, watch the pins. An estate
where the same harness is declared everywhere and binds nowhere has a
much cheaper opportunity than it thinks — the habitat already exists.
Nobody needs to build anything. Somebody needs to wire it up.

Without the distinction, both estates report "we have a platform
harness" and the second one keeps investing in *more* harness while the
governance gap stays exactly where it was.

## An unbound rule is not a weak team

When a dimension is unbound across several subjects, that is a
**binding** failure, not a capability failure, and it belongs to whoever
provides the habitat. The
[portfolio report](../reference/portfolio-report.md) puts it in the
common-weak column — the enablement backlog — rather than attributing it
to each team in turn.

Getting this wrong would be worse than not measuring it. Telling twelve
teams they each have a governance problem, when what exists is one
unwired harness, produces twelve local workarounds and a fragmented
estate.

## The honest failure mode

Binding detection can be wrong, and the way it is wrong matters.

A team may bind its harness through a mechanism the
[checklist](../reference/provenance-and-binding.md#binding-evidence-checklist)
does not recognise. Reading that silence as "unbound" would accuse them
of a discipline failure they do not have — and an assessment that does
that once is not trusted again.

So the rule is: **silence is not negation.** Where no signal is found
but there is no evidence of absence either, the dimension is `inferred`,
and a clarifying question gets spent before anything is called unbound.
Every binding finding names the artefact expected to bind and where it
was looked for, so a team that binds differently can say so and correct
the record.
