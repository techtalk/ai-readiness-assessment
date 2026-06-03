# Run an assessment

## Prerequisites

- The plugin installed in
  [Copilot CLI](install-github-copilot.md) or
  [Claude Code](install-claude-code.md).
- Your terminal / tool open with the **target repository as the working
  directory**, so the scan can see its files.

## Run it

Use the slash command:

```text
/ai-readiness-assess
```

Or trigger it by natural language — the skill responds to phrases like:

> assess our AI readiness · where are we on the framework? · check our
> habitat maturity · score our AI maturity

## What happens

1. **Discovery** — a report of the habitat documents and signals found
   (with paths) and the ones absent.
2. **Questions** — 3–5 clarifying questions, asked one at a time, to
   place the behavioural dimensions the filesystem can't show. Answer
   each before the next is asked.
3. **Assessment** — all fourteen
   [model dimensions](../reference/habitat-maturity-model.md) placed
   L1–L5, the [cognitive level](../reference/cognitive-ladder.md), and
   the [Habitat Build Gap](../reference/habitat-build-gap.md).
4. **Report** — written to `assessments/YYYY-MM-DD-assessment.md`, with
   a short summary in the chat.

See the full [assessment output structure](../reference/assessment-output.md)
for a section-by-section breakdown.

## Tips

- **Run it from the repo root.** Running from a subdirectory hides
  habitat documents and skews the result.
- **If two files seem to fill the same role** (say two candidate
  instruction files), the assessment will stop and ask which is
  canonical rather than guess. Answer it — silent picks produce
  confidently-wrong assessments.
- **Commit the report.** `assessments/YYYY-MM-DD-assessment.md` is a
  durable record; committing it lets you track movement over time.

## Next

- [Read the Habitat Build Gap](read-the-habitat-build-gap.md) to act on the result.
- [Render the HTML report](render-the-html-report.md) to share it.
- Want rigorous per-dimension scoring? [Run the precise survey](run-the-precise-survey.md).
