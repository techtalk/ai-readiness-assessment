# Expected behaviour — fixture `level-1-thin-rules`

This fixture is the same Python utility as `level-0-blank`, plus a
thin `.cursorrules` file (style hints + a few do/don't bullets) and a
ruff config in `pyproject.toml` that is **only run locally** — no CI,
no pre-commit hook, no test suite.

The team is communicating with the agent through a prompt file. They
have not yet built any verification discipline. This is the textbook
L1 signal.

When `/ai-readiness-assess` runs against this fixture, the output
**must** satisfy every assertion below.

---

## A. Structural assertions

A1. **Assessment file is written** at
`assessments/YYYY-MM-DD-assessment.md`.

A2. **Assessed level is L1.** The assessment contains:

```
**Assessed level**: Level 1 — Communicating through prompts
```

Not L0, not L2.

A3. **Discovery report cites `.cursorrules`.** The Habitat Document
Discovery section names `.cursorrules` as the AI-instruction file
found, with content markers matching it (e.g. "style rules, do/don't
bullets").

A4. **Discovery report enumerates the missing habitat layer.** The
following are explicitly "not found" in the discovery section:

- `CLAUDE.md`
- `AGENTS.md`
- `HARNESS.md`
- `specs/` or `docs/specs/`
- `REFLECTION_LOG.md`
- `.github/workflows/`
- `.pre-commit-config.yaml`
- test directory

A5. **No fabricated citations.** Only paths that actually exist in the
fixture appear in the assessment. The full file list is: `README.md`,
`.gitignore`, `pyproject.toml`, `.cursorrules`,
`src/wordcount/__init__.py`, `src/wordcount/main.py`.

A6. **Discipline maturity bounds.**

- Context Engineering: strength 1 (.cursorrules present but thin; no
  CLAUDE.md / AGENTS.md / skills).
- Architectural Constraints: strength 0 or 1 (ruff config exists but
  is local-only; no CI enforcement).
- Guardrail Design: strength 0 (no tests, no CI, no hooks).

Any discipline scored ≥ 2 fails the test.

A7. **Reading Path matches L1.** The Reading Path section recommends
the Level 1 chapter of *The Sovereign Engineer* **and** points
forward to the Level 2 verification chapter (per the embedded reading
map). It does **not** stop at the Level 1 chapter alone, and does
**not** jump past Level 2.

A8. **Leanpub link present.** `https://leanpub.com/thesovereignengineer`
appears in the Reading Path section.

A9. **Single CTA.** Exactly one TechTalk engagement is recommended in
the Next Steps section. No "or" joining two options, no bulleted
menu of services.

A10. **CTA names a verification-discipline gap.** The CTA's weakest
discipline must be **Architectural Constraints** or **Guardrail
Design** (the two zero-scored disciplines). Context Engineering as
the weakest discipline fails the test, since `.cursorrules` is
present.

A11. **CTA engagement type matches the engagement map.**

- If weakest = Architectural Constraints → harness-engineering
  consulting (machine-checkable constraint set with CI enforcement).
- If weakest = Guardrail Design → orchestrator and verification
  engagement (adversarial review, plan-approval gates, verification
  loops).

Any other engagement description fails.

---

## B. Behavioural assertions

B1. **Scan first.** Discovery report is produced before any
clarifying question is asked.

B2. **Questions asked one at a time** if the run includes clarifying
questions.

B3. **(Interactive runs only)** 3–5 clarifying questions in total.
**N/A in batch test runs.**

B4. **No silent canonical picks.** Only `.cursorrules` is present, so
no "which file is canonical?" question should be asked.

---

## C. Semantic assertions

C1. **Rationale fits the evidence.** The L1 rationale names the
**absence of verification discipline** (no CI, no tests, no hooks) as
the ceiling on the level. The rationale does **not** cite "thin
.cursorrules" as the only signal — the team is at L1 because they
*have* an instruction file, not because the file is thin.

C2. **Recommendations are gap-anchored.** Top-3 Recommendations close
specific gaps named in the Gaps section above them.

C3. **CTA reads like advice.** The recommendation paragraph names a
concrete first step (e.g. "set up a CI workflow that runs ruff and
pytest on every PR"), not a generic offering.
