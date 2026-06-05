# Spec 0006: Align HTML report design with the TechTalk marketing site

**Status**: Accepted
**Date**: 2026-06-05

## Intent

Update the HTML rendering step (step 7) in the assessment command and
skill so that generated reports are visually consistent with the TechTalk
marketing site at `techtalk.at`. The instrument, scoring model, and
markdown report output are unchanged — only the optional HTML rendering
is affected.

## Changes

1. **All-sans-serif typography** — drop Georgia serif body; use the
   system sans-serif stack throughout.
2. **Dark header band** — a `#0b2b3c` (TechTalk navy) header containing
   the TechTalk wordmark, project name, date, the two headline lines in a
   semi-transparent card, and a five-level progress strip showing all five
   levels with the current level highlighted and the target level dashed.
3. **TechTalk navy section headings** — `h2` uses `#0b2b3c` text and a
   2 px navy bottom border; overridden to white/borderless inside the CTA
   block.
4. **TechTalk GmbH footer branding** — "© TechTalk GmbH · Vienna,
   Austria" and a `techtalk.at` link in the footer.
5. **Fix existing example HTML reports** — update `techtalk.ai` CTA links
   to `techtalk.at`.

## Risks / what could go wrong

- The HTML output is cosmetic and not CI-gated; regressions affect only
  the rendered report, not the assessment instrument or scores.
- The five-level progress strip uses the **habitat maturity level** as
  "you are here", not the cognitive level. This must be documented
  clearly in the strip (to avoid confusion when the two levels differ,
  as in the re-assessment example).

## Adversarial review

**Objection 1**: Changing the HTML spec in the command/skill without a
corresponding change to the example reports creates a documentation gap.
*Disposition*: Mitigated — the example reports are being rewritten in the
same PR.

**Objection 2**: The dark header may render poorly in print.
*Disposition*: Mitigated — `print-color-adjust: exact` preserves the
dark background; a print `@media` rule falls back the CTA block to white.

**Disposition**: Proceed.
