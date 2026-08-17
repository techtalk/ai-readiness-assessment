# Expected behaviour — fixture `scope-two-subjects`

This fixture is an estate, not a repository: a scope root holding
`.habitat/scope.yml`, two subjects with committed assessments, and the
portfolio report over them. See `README.md` for the layout.

It exists for one property — **the path anchor of spec 0012**:

> The scope root is the directory containing `.habitat/`. Every path in
> the manifest resolves from the scope root. There is no second anchor.

The fixture is built so the discarded reading cannot pass. `./orders-api`
and `./billing` exist at the scope root and do not exist under
`.habitat/`, and the portfolio report sits at `<scope root>/assessments/`
and not at `<scope root>/.habitat/assessments/`. Anchor the rule on
`.habitat/` again and the A-tier checks below go red instead of a
roll-up quietly reporting an empty estate.

---

## A. Structural assertions — automated in `tests/run.py`

These run as repo-level checks (the `instrument (repo-level)` group), not
as per-fixture checks, because the fixture is read as an estate rather
than as a report.

**R30 — the manifest resolves from the scope root.** The manifest exists
at `<fixture>/.habitat/scope.yml`; it names at least two subjects; every
`path` resolves to an existing directory **from the scope root**; each
resolved subject holds a `assessments/*-assessment.md` carrying an
`assessment-summary` block; and no subject path resolves from
`.habitat/`. `report.output` resolves to `<fixture>/assessments/`, which
exists and holds a portfolio report, while `<fixture>/.habitat/assessments/`
does not exist.

**R31 — the anchor is named, not implied.** No file under `commands/`,
`skills/` or `docs/` contains the phrase `manifest directory`, and no
line says `relative to the manifest` without naming the scope root. Both
roll-up surfaces and `docs/reference/scope-manifest.md` define the scope
root, the reference under a `## Path resolution` heading.

**R32 — the lookup rule is stated.** Both roll-up surfaces state that
four directories are tested and that the scope root is the directory
that produced the hit.

**R33 — a zero-coverage run stops.** Both roll-up surfaces instruct the
agent to stop, rather than write a portfolio report, when no subject path
resolves, and to name a path-anchor mismatch as the likely cause.

**R34 — every example manifest agrees.** No manifest example under
`docs/`, `commands/` or `skills/` anchors a path on `../`, which is what
a `.habitat/`-relative manifest looks like.

---

## B. Behavioural assertions — manual or LLM-judged

B1. **A roll-up run from inside a subject directory resolves both
subjects.** `cd tests/fixtures/scope-two-subjects/orders-api` and run
`/ai-readiness-rollup`. The manifest is found one level up, the scope
root is the fixture root, both subjects are `assessed`, and the report is
offered at `<fixture>/assessments/`. This is acceptance criterion 6 of
spec 0012, and it is the case that was wrong under either uniform reading
of the pre-0012 text. **Not automatable here** — the instrument is
markdown instructions, so only a real agent run exercises it.

B2. **A mis-anchored manifest stops the run.** Rewrite the manifest's
paths to `../orders-api` and `../billing` (do not commit), and run
`/ai-readiness-rollup` from the fixture root. Expected: the run stops,
says no subject path resolved, and names a path-anchor mismatch as the
likely cause. It must **not** write a portfolio report claiming 0 of 2.
Acceptance criterion 7.

B3. **The reused cognitive read is declared.** `billing`'s report records
`cognitive_source: team` and says so in its body; the portfolio report
repeats it in the ledger.

---

## C. Semantic assertions — manual

C1. The spread is presented as the headline finding, with both extremes
named and one line on what differs — not buried under the matrix.

C2. No single portfolio number appears anywhere: no average gap, no
overall grade, no percentage.

C3. The split ceiling separates what the estate owes (agent composition,
observability) from what one subject owes (testing).
