# Spec 0007: TechTalk CTA is the primary answer; the book is secondary

**Status**: Accepted
**Date**: 2026-06-05

## Intent

Make the TechTalk engagement (Next Steps) the most prominent answer in
the assessment results and reports, with *The Sovereign Engineer* reading
path demoted to a secondary, self-guided alternative. The book remains a
resource in every report — it is reframed, not removed.

Previously the reading path (book) appeared **before** the TechTalk CTA in
both the markdown report and the rendered HTML, so the book was the first
recommendation a reader met. This inverts that.

## Changes

1. **Report section order** — `## Next Steps` (the TechTalk CTA) now
   precedes `## Reading Path` in the markdown report skeleton (step 4)
   and in the rendered HTML.
2. **Next Steps reframed as the primary recommendation** (step 6); the
   single-CTA structure is unchanged (still exactly one CTA blockquote,
   so the A9 structural assertion still holds).
3. **Reading Path reframed as the secondary, self-guided option**
   (step 5) — "prefer to explore on your own first?". It still names the
   matched chapter and carries the Leanpub link (A7/A8 hold).
4. **HTML**: the `.cta` block is rendered first and prominent (navy, gold
   button), with a secondary "Want to read more?" link to the matched
   chapter directly below the button; the `.reading` block follows as a
   lighter resource.
5. **Chat summary (step 9)** leads with the TechTalk engagement as the
   one recommendation; the book chapter follows as the secondary line.
6. Both dogfood example reports (markdown + HTML) updated to match, and
   their stale `techtalk.ai` CTA links fixed to the booking link (missed
   in #50, which touched only the command, skill, and example HTML).

## Risks / what could go wrong

- **Single-CTA convention**: the HARNESS "Single CTA" convention forbids
  *multiple TechTalk engagements*. The book is not a TechTalk engagement,
  so a secondary book link does not violate it. *Mitigated.*
- **A9 structural test** counts CTA blockquote runs in `## Next Steps`;
  the secondary book pointer lives in `## Reading Path` (markdown) or
  below the button (HTML), never as a second blockquote run in Next
  Steps. *Mitigated.*
- **Fixture-order drift**: the six `tests/fixtures/*/assessments/*.md`
  retain the prior Reading-Path-before-Next-Steps order. No A-tier
  assertion checks the order of these two sections (A3 only checks
  discovery-before-level-assessment), so the suite stays green. The
  fixtures will adopt the new order the next time they are regenerated.
  *Accepted.*

## Adversarial review

**Objection**: Reordering the markdown template without regenerating the
fixtures leaves the template and the test fixtures inconsistent.
*Disposition*: Accepted as low-cost drift — the inconsistency is cosmetic
(section order of two adjacent end-of-report sections), no assertion
depends on it, and the user-facing dogfood examples *are* updated.

**Disposition**: Proceed.
