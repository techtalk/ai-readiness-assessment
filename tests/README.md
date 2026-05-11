# Tests — Test-Driven Agentic Behaviour (TDAB)

This directory holds **behavioural tests** for the
`ai-readiness-assessment` skill. The deliverable of this plugin is a
skill that produces agent behaviour when invoked. A skill without
behavioural tests is an unverified claim — TDAB applies test-driven
development to the prose itself.

## How a test works

Each fixture under `fixtures/` is a small toy repository that exhibits
a known AI-literacy level. Alongside the fixture sits an `expected.md`
file: a checklist of assertable properties the assessment output must
satisfy when the skill is run against that fixture.

The loop is:

1. **Red** — run the skill against the fixture; compare its output to
   `expected.md`; identify the first failing assertion.
2. **Green** — edit `commands/ai-readiness-assess.md` and
   `skills/ai-readiness-assessment/SKILL.md` (dual-surface sync —
   change both) until the assertion passes.
3. **Refactor** — once the assertion passes, look at the change and
   ask whether the surrounding prose can be tightened without
   regression.

## Running a test (manual, today)

There is no automated runner yet. The manual procedure:

1. Open a fresh Claude Code session with the plugin installed.
2. `cd tests/fixtures/<fixture>`
3. Run `/ai-readiness-assess`
4. Save the produced `assessments/YYYY-MM-DD-assessment.md` next to
   the fixture as `actual-<YYYY-MM-DD>.md`.
5. Walk through `expected.md` and mark each assertion PASS or FAIL.
6. For each FAIL, decide whether the fix lives in the skill prose
   (most common) or in the assertion (sometimes the expectation was
   wrong).

## What's here

- `fixtures/level-0-blank/` — minimal repo with no AI-instruction
  files, no CI, no constraints, no specs. Expected outcome: L0
  assessment, gap in all three disciplines, CTA pointing to a
  habitat-document bootcamp.

Future fixtures should cover L1 (thin AI-instruction file only), L2
(verification discipline but no habitat), L3 (rich habitat), L4
(specs-first), and L5 (sovereign / portfolio practice).

## Promotion path for these tests

Today: manual, advisory. Each test is a checklist a reviewer walks
through after a meaningful change to the skill or command.

Next: agent-verified. A judge agent reads `actual-*.md` against
`expected.md` and returns PASS / FAIL with reasons. This sits behind
`/harness-constrain` once Architectural Constraints are configured in
`HARNESS.md`.

Eventually: deterministic where falsifiable (regex on the "Assessed
level" line, structural parse of the CTA block, link presence) plus
agent for the genuinely fuzzy properties (does the rationale fit the
evidence; is the recommended chapter the one that closes the gap).
