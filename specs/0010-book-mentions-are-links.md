# Spec 0010: Every book mention in a report is a link

- **Status**: accepted
- **Date**: 2026-07-30
- **Issue**: #58

## Intent

Wherever a generated report names *The Sovereign Engineer* in its body
copy, the title itself should be a link to the book, so a reader can
always get from the name to the thing. Today some mentions are linked
and some are bare prose — the Assessment Review credit line, the closing
pointer, and the Reading Path prose all name the book without offering a
way to reach it, even though a Leanpub button sits a few lines below.

## Design

### One URL: the campaign link

The repo was using two Leanpub URLs roughly evenly — the bare product
page and `/c/ai-readiness`. Every book link in the report, the docs, and
the README now uses:

```text
https://leanpub.com/thesovereignengineer/c/ai-readiness
```

That is the AI-readiness campaign URL, added deliberately in 0.4.0 for
exactly this audience. Issue #58 as written asked for the bare product
page; standardising on it would have silently reverted that decision and
dropped the reader's discount, so the campaign URL was chosen instead —
it satisfies the intent ("every mention reaches the book") without
costing the reader anything.

### What becomes a link

In the generated report's body copy:

- the Reading Path prose naming the book;
- the Assessment Review credit line ("Author of *The Sovereign
  Engineer*");
- the Assessment Review closing pointer ("…names your matched chapter of
  *The Sovereign Engineer*");
- the step 5 recommendation-phrasing example.

### What stays unlinked

Two places where the phrase is a **label**, not body copy:

- the "Cognitive read (Sovereign Engineer)" badge — a metric label;
- the provenance note naming the framework's sources.

### HTML

Body-copy links inside the dark `.review` box are styled `.review p a`
— inheriting the surrounding colour with an underline. The rule is
scoped to paragraphs deliberately: an unscoped `.review a` also caught
the CTA button and underlined it.

### Surfaces changed

Both instrument surfaces (dual-surface sync), both dogfood examples and
their markdown sources, the six fixture assessments, and `README.md`.

## Alternatives considered

- **The bare product page everywhere**, as #58 was written. Rejected —
  see above; it would have reverted 0.4.0 without saying so.
- **Plain URL for new inline links, campaign URL for the existing
  buttons.** Rejected — the report would then carry two different links
  to the same book, which is the inconsistency the issue set out to
  remove.

## Risks / what could go wrong

- **Link density.** The credit line, the closing pointer, the Reading
  Path prose, and the Leanpub button now sit within about fifteen lines
  of each other, all pointing at the same destination. *Accepted, with
  the mitigation that three of the four are inline title links inside
  sentences rather than buttons, so they read as citation rather than as
  repeated calls to action.* Worth revisiting if the tail starts to feel
  like an advert.
- **Campaign URL churn.** If the coupon is ever retired, every report
  link breaks at once rather than degrading to the product page.
  *Accepted* — it is a single find-and-replace, and the coupon's
  lifetime is the author's to manage.
- **`plugin.json` homepage still points at the bare product page.**
  Deliberate: repo metadata should carry the canonical URL, not a
  campaign-tracked one.
- **A8 is unaffected** — it matches the substring
  `https://leanpub.com/thesovereignengineer`, which the campaign URL
  contains, so it passes for either form.

## Adversarial review

**Objection**: Turning every mention of the author's own book into a
link, inside a report that recommends that book, reads as
self-promotion.
*Disposition*: Accepted as a real tension, mitigated by what was left
alone. The book stays the *secondary* option behind the review, the
Reading Path keeps its "prefer to explore on your own first?" framing,
and no new mentions were added — only existing ones made reachable.

**Objection**: Choosing the campaign URL contradicts the issue text.
*Disposition*: The issue's stated goal is that every mention reaches the
book; the specific URL was flagged as an open question on #58 before any
work started, and the campaign URL was chosen with the 0.4.0 context in
hand.

**Disposition**: Proceed.

## Acceptance

- No body-copy mention of *The Sovereign Engineer* in any report is
  unlinked; the two label exceptions are documented above.
- Every book link in the reports, docs, and README uses the campaign
  URL — no bare product-page links remain outside `plugin.json` and the
  test assertions.
- The CTA button in `.review` is not underlined.
- `python3 tests/run.py` passes.
