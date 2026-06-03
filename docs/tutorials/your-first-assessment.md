# Your first assessment

This tutorial takes you from nothing to a finished, interpreted AI
readiness assessment. By the end you'll have a report committed under
`assessments/` and you'll understand what every part of it means.

It should take about fifteen minutes.

## Before you start

You need one supported AI tool with an account, and a repository to
assess. See [Prerequisites](../index.md) if you're unsure. This tutorial
uses **GitHub Copilot CLI**; the
[Claude Code path](../how-to/install-claude-code.md) is identical in
spirit.

We'll assess a real repository — open your terminal in the root of one
you know well, so you can sanity-check the findings.

## Step 1 — Install the plugin

Install and sign in to the Copilot CLI, then add this marketplace and
install the plugin:

```shell
npm install -g @github/copilot
copilot
```

Inside the `copilot` session:

```text
/plugin marketplace add techtalk/ai-readiness-assessment
/plugin install ai-readiness-assessment@techtalkai
```

Confirm it's there:

```text
/skills list
```

You should see `ai-readiness-assessment` in the list.

## Step 2 — Run the assessment

From the same session, with your repository as the working directory:

```text
/ai-readiness-assess
```

The assessment runs in four visible movements:

1. **Discovery.** It reports the habitat documents it found — things
   like `CLAUDE.md`, `HARNESS.md`, CI workflows, a `specs/` directory —
   each with the path and the markers that confirmed the match. It also
   lists what's *absent*. Read this: absences matter as much as
   presences.
2. **Questions.** It asks **3–5 clarifying questions, one at a time** —
   the things the filesystem can't tell it, like how the team actually
   works with the agent. Answer honestly; an inflated answer just
   produces a confidently-wrong score.
3. **Assessment.** It places all fourteen
   [model dimensions](../reference/habitat-maturity-model.md), reads your
   [cognitive level](../reference/cognitive-ladder.md), and computes the
   [Habitat Build Gap](../reference/habitat-build-gap.md).
4. **Report.** It writes `assessments/YYYY-MM-DD-assessment.md` and
   prints a short summary in the chat.

## Step 3 — Read the result

Open `assessments/YYYY-MM-DD-assessment.md`. Work through it top to
bottom:

- **Habitat Maturity Profile** — your placement on all fourteen
  dimensions, each reported with the model's verb (e.g. *Testing: L3 —
  Verifying*). The headline **Habitat Maturity Level** is the rounded
  mean, with the weakest dimensions named as the ceiling.
- **Level Assessment** — your cognitive level (L0–L5) and the one
  discipline holding you back.
- **Habitat Build Gap** — the signed gap and its
  [regime](../reference/habitat-build-gap.md#interpretation-regimes).
  This is the headline signal: are your habitat and your thinking *in
  step*?

See [Read the Habitat Build Gap](../how-to/read-the-habitat-build-gap.md)
for how to act on each regime.

## Step 4 — Act on one thing

The report ends with **three recommendations** and **one** TechTalk
engagement suggestion — deliberately one, not a menu. Pick the single
recommendation tied to your weakest dimension or discipline and do it
this week. Re-run the assessment next month; the gap should move.

## Optional — share it

Ask the assessment:

> Render this as a shareable HTML page.

You'll get a single-file, print-friendly report you can hand to a lead
or a stakeholder. See
[Render the HTML report](../how-to/render-the-html-report.md).

## Where to go next

- Want a rigorous, survey-scored profile instead of the evidence-first
  default? See [Run the precise survey](../how-to/run-the-precise-survey.md).
- Curious *why* there are two maps rather than one score? Read
  [Two reads, one habitat](../explanation/two-reads.md).
