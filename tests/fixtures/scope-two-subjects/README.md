# Fixture — `scope-two-subjects`

Unlike the six `level-*` fixtures, this is **not** a toy repository. It
is a toy *estate*: a scope root holding a manifest and two subjects,
each with a committed assessment, plus the portfolio report a roll-up
over them produces.

```text
scope-two-subjects/          ← the scope root
├── .habitat/scope.yml       ← two subjects: ./orders-api, ./billing
├── orders-api/
│   └── assessments/2026-08-17-assessment.md
├── billing/
│   └── assessments/2026-08-17-assessment.md
└── assessments/             ← report.output: assessments/
    └── 2026-08-17-portfolio.md
```

It exists to hold the path anchor still. Spec 0012 fixed one anchor —
the scope root, the directory containing `.habitat/` — after the
surfaces had drifted into describing two. Prose alone cannot stop that
happening again, so the anchor is asserted here instead: the manifest's
paths resolve from the scope root and demonstrably *fail* to resolve
from `.habitat/`, so a regression to the self-relative reading turns a
check red rather than turning a portfolio report quietly empty.

The numbers in the three reports are invented. They are shaped to give
the estate a real spread (one Coherent subject, one where ambition
outpaces enablement) so the portfolio report has something to say, and
to exercise a reused cognitive read — `billing` records
`cognitive_source: team`.

See `expected.md` for what is asserted and what is deliberately not.
