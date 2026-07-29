# Spec 0008: Next Steps as its own box; a dedicated Assessment Review section

- **Status**: accepted
- **Date**: 2026-07-29
- **Issue**: #55

## Intent

Bridge the gap between *receiving* a report and *booking* a review. Today
the report's tail jumps straight from the improvement plan into a TechTalk
consulting pitch, so the reader meets a sales block before they have been
told what a review would actually do for them. This change gives the
generated explanation its own quiet container, adds a fixed transition
paragraph that names the purpose of a review, and replaces the consulting
CTA with an **Assessment Review** section that positions the review as the
natural continuation of the assessment rather than an upsell.

The generated content stays generated: the first Next Steps paragraph is
still written by the assessment from the gap. Everything added here is
fixed copy.

## Design

### Report structure (markdown)

```text
## Next Steps          <- generated gap paragraph + fixed transition paragraph
## Assessment Review   <- the single CTA (fixed copy)
## Reading Path        <- unchanged
```

`## Next Steps` keeps the dynamic paragraph and gains one fixed paragraph:

> Your assessment shows where your repository is today. A review helps you
> understand why these findings matter, which improvements will have the
> biggest impact, and what should come next.

`## Assessment Review` is new and carries the report's one call to action
as a single blockquote run: headline ("Not sure what these results
mean?"), intro, the reviewer subheadline (Russell Miles — *Creator of the
AI Readiness Assessment | Author of The Sovereign Engineer*), the
one-hour framing, a four-item "After 60 minutes you'll leave knowing"
list, and the **Book your AI Readiness Review** link. The quiet pointer
to the Reading Path stays as the closing line.

`## Reading Path` is untouched.

### Rendered HTML

Two containers replace the single `.cta` block:

- `.nextsteps` — background `#f0eeeb`, navy heading, the two paragraphs.
- `.review` — background `#162e40`, light text; inside it a highlighted
  outcomes box on `#dcdbdd` with teal check marks, and a centred CTA
  button on `#00b2a2` with white text. The reviewer credit line is teal
  italic. The secondary reading pointer sits below the button in small
  teal text.

The `.reading` block keeps its existing styling and position.

### Surfaces changed

- `commands/ai-readiness-assess.md` and
  `skills/ai-readiness-assessment/SKILL.md` — dual-surface sync; step 4
  skeleton, step 5 lead-in, step 6 (split into 6a/6b), step 7 HTML rules,
  step 9 chat summary.
- `docs/examples/self-assessment.html` and
  `docs/examples/self-assessment-2.html` — both dogfood examples render
  the new sections.
- `assessments/2026-06-03-assessment*.md` — the markdown sources behind
  those examples.
- `docs/reference/assessment-output.md` — documents the new section.
- `tests/run.py` — A9 looks for the CTA in Assessment Review.

## Alternatives considered

- **HTML-only change.** Cheaper, but the markdown report is the source of
  truth the HTML renders from; leaving them divergent would mean the
  rendered page says something the report does not.
- **Keeping the CTA blockquote inside `## Next Steps`.** Would have kept
  `tests/run.py` untouched, but it defeats the intent: the point is that
  the explanation and the invitation are two separate beats.

## Risks / what could go wrong

- **A9 (single CTA) regression.** A9 counted blockquote runs inside
  `## Next Steps`; the CTA now lives in `## Assessment Review`, so a
  newly generated report would score zero CTAs and fail. *Mitigated* —
  `count_cta_paragraphs` now reads `## Assessment Review` and falls back
  to `## Next Steps`, so both the six legacy fixtures and the new format
  are checked by the same assertion.
- **A10 (CTA mentions the gap) regression.** A10 reads `## Next Steps`,
  which still carries the generated engagement paragraph. *Not affected.*
- **Single-CTA convention (HARNESS).** The section proposes exactly one
  engagement — the AI Readiness Review — so the convention holds more
  cleanly than the previous two-option engagement list did.
- **Fixed copy drifting from the dynamic paragraph.** The transition
  paragraph is deliberately generic ("why these findings matter") so it
  reads correctly against any gap regime, positive or negative.
- **Booking URL.** The button copy names Russell Miles but the interim
  URL is the existing TechTalk booking link, pending a replacement URL.
  *Accepted, tracked in #55* — a one-line swap in four places
  (both surfaces, both examples) plus the two markdown assessments.
- **Fixture drift.** The six `tests/fixtures/*/assessments/*.md` keep the
  old shape until regenerated. No assertion depends on the new sections
  existing, so the suite stays green. *Accepted.*

## Adversarial review

**Objection**: Adding fixed marketing copy to a report whose credibility
rests on being evidence-driven dilutes it.
*Disposition*: Accepted with the structure as the mitigation — the fixed
copy is quarantined in its own section below the generated one, and the
generated paragraph is unchanged. The reader can tell which is which.

**Objection**: The reviewer credit ("Creator of the AI Readiness
Assessment") is a claim the report makes about its own author, inside the
report.
*Disposition*: Accepted as intended — the review is with the instrument's
author, and that is the reason the review is worth an hour.

**Disposition**: Proceed.

## Acceptance

- The markdown skeleton in both surfaces shows `## Next Steps`,
  `## Assessment Review`, `## Reading Path` in that order.
- Both surfaces are byte-identical across the framework sections.
- Both `docs/examples/*.html` render a `#f0eeeb` Next steps box, a
  `#162e40` Assessment Review box with a `#dcdbdd` outcomes box and a
  `#00b2a2` button, and an unchanged Reading Path block.
- `python3 tests/run.py` passes.
