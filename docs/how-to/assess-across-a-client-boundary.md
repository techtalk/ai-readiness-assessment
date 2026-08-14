# Assess across a client boundary

Consultancy work, cross-business-unit reviews and partner estates all
share a condition: you are asked about repositories you cannot read.

The instrument handles this by **naming what it could not see**, rather
than quietly assessing whatever happened to be reachable.

## Name every subject, including the unreadable ones

Put all fourteen in the manifest even if six are readable:

```yaml
version: 1
team: client-payments-tribe

subjects:
  - id: orders-api
    path: ../orders-api
  - id: billing
    path: ../billing
  # ... four more you can read ...
  - id: settlement
    path: ../settlement          # no access
  - id: partner-gateway
    path: ../partner-gateway     # different business unit
  # ... six more you cannot ...
```

The manifest is the *claim about scope*. Leaving the unreadable ones out
would make the report say "6 of 6" — which is true about the manifest
and false about the estate.

## What the report does

The coverage ledger reports against the **named** subjects:

```text
| Subject         | Status      | Report date | Note                    |
| orders-api      | assessed    | 2026-08-02  | —                       |
| settlement      | unreachable | —           | no access               |
| partner-gateway | unreachable | —           | different business unit |

Assessed 6 of 14 named subjects; 8 unreachable.
```

The denominator is the claim. "Assessed 6 subjects" and "assessed 6 of
14 named subjects" are different statements, and only the second one is
honest about what was left out.

Under partial coverage the report also **never describes the ceiling as
estate-wide**. It is the ceiling of the six that were read, and the
report says so — because a common-weak dimension across six repositories
is much weaker evidence about fourteen than about six.

## Why not just assess what you can see

Because the result gets quoted without its caveats.

A portfolio report is a persuasive artefact — the matrix in particular
travels well and travels alone. If it does not carry its own coverage on
its face, "our estate is Distributed with an observability ceiling"
becomes a sentence about fourteen repositories on the strength of six.
The coverage ledger sits first in the report, above the matrix, for
exactly this reason.

## The engagement pattern

Where teams can run the assessment but you cannot read their code, the
roll-up is designed to work from artefacts:

1. Each team runs `/ai-readiness-assess` in their own repository.
2. Each team keeps their own report — it stays in their
   `assessments/` directory, and you never need access to their code.
3. They share only the report, or only its
   [summary block](../reference/assessment-summary-block.md).
4. You roll up what you have received.

This separates *who runs the assessment* from *who reads the summary*,
which is usually what makes a cross-boundary engagement possible at all.
Teams that will not grant repository access will often happily share a
report they generated and can read themselves first.

## Reassessing later

Subjects that were unreachable stay in the manifest. When access
arrives, or a team sends their report, they move from `unreachable` to
`assessed` and the coverage sentence improves on its own.

An estate that goes from "6 of 14" to "11 of 14" between reviews has
made real progress in *visibility*, and that is worth reporting
alongside any change in the levels themselves.

## Next

- [Assess with an org-level habitat](assess-with-an-org-level-habitat.md)
- [Roll up existing assessments](../tutorials/roll-up-existing-assessments.md)
- [Portfolio report structure](../reference/portfolio-report.md)
