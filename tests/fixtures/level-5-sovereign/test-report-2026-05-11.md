# Test report — `level-5-sovereign` — 2026-05-11

Assessment under test: `assessments/2026-05-11-assessment.md`
Expectations: `expected.md`
Runner: Claude (Opus 4.7), batch mode

## A. Structural assertions

| ID | Status | Evidence |
|---|---|---|
| A1 | PASS | Assessment file present, non-empty. |
| A2 | PASS | `**Assessed level**: Level 5 — Sovereign engineering`. |
| A3 | PASS | All 6 required L5 sovereign-layer artefacts named in the discovery section (`.claude-plugin/plugin.json`, `commands/wordcount-habitat-init.md`, `MODEL_ROUTING.md`, `CHOICES.md`, `audits/2026-Q1.md`, fitness-function GC rules in HARNESS.md). |
| A4 | PASS | All cited paths exist in the fixture. The honest "scripts/ referenced but not implemented" note is recorded as a fixture-fidelity gap, not as a fabrication. |
| A5 | PASS | L3 habitat and L4 specs layer both acknowledged as inherited — the assessment explicitly says "The full L0–L4 stack is present" and treats L5 as additive. |
| A6 | PASS | Context 5, Constraints 5, Guardrails 5. At least one ≥ 5 (in fact all three) and none below 4. Within bounds. |
| A7 | PASS | Reading Path: "the Enchiridion chapter ... and the portfolio-scale chapters that follow". Matches the L5 row of the reading map. |
| A8 | PASS | Leanpub link present. |
| A9 | PASS | Single CTA paragraph. |
| A10 | PASS | CTA explicitly says "The question is no longer 'what's next' but 'how is this sustained?'" — frames L5 as a sustained practice, not a step toward L6. Mentions "The aim isn't a sixth level; it's compounding the practice you already have". Anti-L6 framing is explicit. |
| A11 | PASS | "portfolio-sovereignty engagement" — a sustaining / portfolio-level engagement, not a repeat of the L4→L5 platform engagement. Names cross-team governance audit, maintenance playbook for the published plugin, portfolio-level assessment artefact. |

Structural: **11 / 11 PASS**.

## B. Behavioural assertions

| ID | Status | Evidence |
|---|---|---|
| B1 | N/A (batch) | Discovery first; no questions to sequence against. |
| B2 | N/A (batch) | No questions asked. |
| B3 | N/A (batch) | Per updated assertion: interactive-only. |
| B4 | PASS | The fixture has one `.claude-plugin/plugin.json` (the published-plugin manifest) — not duplicated, no canonical-pick question needed. CLAUDE.md and HARNESS.md and CHOICES.md and MODEL_ROUTING.md all coexist with non-overlapping roles. The assessment correctly treats them as complementary. |

Behavioural: **1 PASS, 3 N/A**. No FAILS.

## C. Semantic assertions

| ID | Status | Evidence |
|---|---|---|
| C1 | PASS | Rationale: "every platform-level signal is present and exercised. The team's habitat is published as a Claude Code plugin with a real adoption command, and a sibling team has installed it (REFLECTION_LOG.md 2026-04-10 — verified, not aspirational)". Positions the team as at L5, not "approaching L5". |
| C2 | PASS | Strength 1 names the habitat-as-plugin pattern verified by reflection-log entry. Strength 2 names the governance audit finding real drift. Strength 3 names the CHOICES.md ↔ REFLECTION_LOG.md ↔ HARNESS.md cross-reference triple. All three Strengths name platform-level practice. |
| C3 | PASS | CTA: "Your team is at L5 — the top of the published framework. The question is no longer 'what's next' but 'how is this sustained?'". Names three concrete deliverables (cross-team audit, maintenance playbook, portfolio-level assessment artefact). Explicitly anti-sales-pitch by acknowledging the team is at the top. |

Semantic: **3 / 3 PASS**.

## Verdict

**Structural 11/11 · Behavioural 1/4 (3 N/A, 0 FAIL) · Semantic 3/3.**

Same clean result as L4. The L5 fixture also exercises a subtler
property: the skill correctly recognises that L5 is the top of the
framework and doesn't invent a "Level 6" or recommend reaching for
one. A failure mode I worried about — the CTA producing "next steps
toward L6" — did not occur.
