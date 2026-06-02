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

## Running tests

The suite is two halves, run differently.

### A-tier (structural) — automated

```
python3 tests/run.py                          # all 6 fixtures
python3 tests/run.py --fixture level-3-habitat   # one fixture
```

The runner reads each fixture's most recent
`assessments/*-assessment.md` and checks the structural assertions
encoded in `tests/run.py` (level line, discovery-section ordering,
required absences enumerated, discipline-score bounds, reading-path
content, single CTA, Leanpub link present, CTA gap-language, the four
headline Operational Axes, the Habitat Build Gap regime, and the full
fourteen-dimension Habitat Maturity Profile). It
writes a fresh report to `tests/auto-results.md` and exits non-zero
if any assertion fails — suitable for a CI gate.

To produce a new assessment for a fixture (so the runner has
something fresh to check):

1. Open a Claude Code session with the plugin installed.
2. `cd tests/fixtures/<fixture>`
3. Run `/ai-readiness-assess`. The skill writes
   `assessments/YYYY-MM-DD-assessment.md`.
4. Back in the repo root, run `python3 tests/run.py`.

### B-tier (behavioural) and C-tier (semantic) — manual or LLM-judged

The runner does **not** cover B-tier (scan-first sequencing,
questions one-at-a-time, the 3–5 question count) or C-tier
(rationale fits the evidence, recommendations are gap-anchored, CTA
reads as advice). To verify those:

1. Run the skill interactively against the fixture (as above).
2. Open the produced assessment alongside `expected.md`.
3. Walk through the B and C assertions and mark each PASS / FAIL.
4. Record findings in a new
   `tests/fixtures/<fixture>/test-report-YYYY-MM-DD.md`.

For each FAIL, decide whether the fix lives in the skill prose
(usually) or in the assertion (sometimes the expectation was wrong).
When the skill prose changes, run the automated A-tier sweep first
to catch regressions.

## What's here

- `fixtures/level-0-blank/` — minimal repo with no AI-instruction
  files, no CI, no constraints, no specs. Expected outcome: L0
  assessment, gap in all three disciplines, CTA pointing to a
  habitat-document bootcamp.

Future fixtures should cover L1 (thin AI-instruction file only), L2
(verification discipline but no habitat), L3 (rich habitat), L4
(specs-first), and L5 (sovereign / portfolio practice).

## Promotion path for these tests

| Tier | Today | Next | Eventually |
|---|---|---|---|
| **A** — structural | **deterministic** (`tests/run.py`) | wire into CI as a required check | — |
| **B** — behavioural | manual, interactive Claude session | agent-judged transcript review | deterministic where falsifiable (e.g. count `?` characters in skill output) |
| **C** — semantic | manual review | agent judge that returns PASS/FAIL with reasons | hybrid: deterministic regex + agent for genuinely fuzzy properties |

The A-tier promotion happened in commit history — see
`tests/run.py`. B and C are still ahead.
