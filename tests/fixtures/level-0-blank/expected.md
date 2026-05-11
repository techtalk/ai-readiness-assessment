# Expected behaviour — fixture `level-0-blank`

This fixture is a small Python utility with **no AI-literacy artefacts
at all**: no `CLAUDE.md`, no `.github/copilot-instructions.md`, no
`.cursorrules`, no `.windsurfrules`, no `HARNESS.md`, no `specs/`, no
`REFLECTION_LOG.md`, no `.github/workflows/`, no test suite, no
pre-commit hooks. A `README.md`, a `.gitignore`, a `pyproject.toml`,
and a five-line Python module — that's the whole repo.

When `/ai-readiness-assess` runs against this fixture, the output
**must** satisfy every assertion below.

---

## A. Structural assertions (falsifiable from output alone)

A1. **Assessment file is written.** A file at
`assessments/YYYY-MM-DD-assessment.md` exists after the run, where
`YYYY-MM-DD` is today's date. The file is non-empty.

A2. **The assessed level is L0.** The assessment file contains the
line:

```
**Assessed level**: Level 0 — Aware of the landscape
```

No level range. No hedging ("between L0 and L1"). One integer.

A3. **Discovery report comes first.** In the assessment file, the
section `## Habitat Document Discovery` appears **before** any
section that names a level or makes a maturity claim.

A4. **Discovery report enumerates absences.** The discovery section
explicitly records "not found" (or equivalent) for each of:

- `CLAUDE.md`
- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.cursorrules`
- `.windsurfrules`
- `HARNESS.md`
- `CONSTRAINTS.md`
- `specs/` or `docs/specs/`
- `REFLECTION_LOG.md`
- `.github/workflows/`

A5. **No fabricated citations.** Every file path the assessment
mentions exists in the fixture. Specifically: the only paths that
should appear are `README.md`, `.gitignore`, `pyproject.toml`,
`src/wordcount/__init__.py`, `src/wordcount/main.py`. Any other path
is a fabrication and fails the test.

A6. **Discipline Maturity table is present.** The assessment contains
a table with three rows — Context Engineering, Architectural
Constraints, Guardrail Design — and a numeric strength column. The
strength for each discipline is 0 or 1. A score of 2+ on any
discipline fails the test.

A7. **Reading Path is L0-matched.** The Reading Path section names
**Act I** of *The Sovereign Engineer* as the recommended reading. It
does **not** point to a later-act chapter.

A8. **Leanpub link is present.** The string
`https://leanpub.com/thesovereignengineer` appears in the Reading
Path section.

A9. **Single CTA.** The Next Steps / TechTalk section contains
**exactly one** specific engagement recommendation. The word "or" in
the recommendation paragraph is a failure signal — count occurrences;
if any join two engagement options, fail. A bulleted menu of options
is a fail.

A10. **CTA names the weakest discipline.** The recommendation
explicitly anchors itself in **Context Engineering** as the weakest
discipline (since this fixture has zero context artefacts). It must
not anchor in Architectural Constraints or Guardrail Design instead.

A11. **CTA engagement type matches the engagement map.** For weakest
discipline = Context Engineering, the recommendation is a
habitat-document bootcamp (or equivalent name) focused on building
`CLAUDE.md` / `AGENTS.md` / `HARNESS.md` for the team's own
codebase.

---

## B. Behavioural assertions (procedural — observed during the run)

B1. **Scan first, ask second.** The skill produces the discovery
report **before** asking any clarifying questions. The first
clarifying question must not appear in the conversation before the
discovery report is shown.

B2. **Questions asked one at a time.** Clarifying questions are
asked one per turn. A single message containing multiple numbered
questions is a fail.

B3. **3–5 clarifying questions.** The total count of clarifying
questions asked across the run is at least 3 and at most 5.

B4. **No silent canonical picks.** Since this fixture has zero
AI-instruction files, the "two-or-more candidates → stop and ask"
rule cannot fire. Verify negatively: no question of the form "which
of these files is canonical?" is asked.

---

## C. Semantic assertions (agent-judged — needs human or LLM review)

C1. **Rationale fits the evidence.** The one-line rationale in the
assessment names the absence of any AI-instruction file or
guardrail as the reason for L0. It does **not** cite the missing
test suite alone (that would be a justification for L1 → L2 demotion,
not L0).

C2. **Recommendations are gap-anchored.** Each item in the top-3
Recommendations list closes a specific gap named in the Gaps section
above it. A recommendation that floats free of a stated gap fails.

C3. **CTA reads like advice, not marketing.** The recommendation
paragraph reads as a specific next step a person would take, not as
a list of services. Test: would a senior engineer reading this know
exactly what to do next? Yes → pass. "Consider exploring our
offerings…" → fail.

---

## Test outcome

If any of A1–A11, B1–B4, or C1–C3 fails:

1. Record the failing assertion ID in a `actual-YYYY-MM-DD.md` file
   next to this one, with the offending output excerpt.
2. Decide whether the fix lives in the skill prose
   (`skills/ai-readiness-assessment/SKILL.md` AND
   `commands/ai-readiness-assess.md` — dual-surface sync) or in the
   expectation itself.
3. Apply the fix, re-run, and confirm the assertion now passes
   without regressing any other assertion.
