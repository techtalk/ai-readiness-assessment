# Spec 0012: Scope manifest path resolution — one anchor, named

- **Status**: accepted
- **Date**: 2026-08-17
- **PR**: [#84](https://github.com/techtalk/ai-readiness-assessment/pull/84)

## Intent

Every path in `.habitat/scope.yml` is documented as "relative to the
manifest", but the surfaces disagree about what that means, and two of
them are only correct under *different* readings. Nothing in the
instrument names the directory that paths resolve from. A reader — human
or agent — who picks one reading consistently gets a wrong answer
somewhere: either the subjects cannot be found, or the portfolio report
lands inside a dot-directory.

This spec names the anchor once, applies it to all three path-bearing
fields, and fixes the worked examples that currently depend on the
ambiguity being resolved correctly by intuition.

## The defect

Three fields carry paths. They are described with three different
phrases, none of which identifies a directory:

| Field | Current wording | Where |
|---|---|---|
| `subjects[].path` | "relative to the manifest" | `docs/reference/scope-manifest.md:35` |
| `habitats[].path` | "relative to the manifest" | `docs/reference/scope-manifest.md:103` |
| `report.output` | "relative to the manifest" | `docs/reference/scope-manifest.md:36`; `commands/ai-readiness-rollup.md:101`; `skills/ai-readiness-rollup/SKILL.md:105` |
| `subject_path` (summary block) | "relative to the **report**" | `docs/reference/assessment-summary-block.md:55` |

And the write destination is specified with a fourth phrase:

> Write to `<manifest directory>/<report.output>/YYYY-MM-DD-portfolio.md`
> — `commands/ai-readiness-rollup.md:192`, `skills/ai-readiness-rollup/SKILL.md:196`,
> `docs/reference/portfolio-report.md:4`

"The manifest" is a file at `<root>/.habitat/scope.yml`. "The manifest
directory" most naturally reads as the directory *containing* that file
— `.habitat/`. Under that reading `report.output: assessments/` resolves
to `<root>/.habitat/assessments/`.

But the how-to states the opposite outcome:

> The report lands in `estate/assessments/YYYY-MM-DD-portfolio.md`.
> — `docs/how-to/write-a-scope-manifest.md`

…while the same document's worked example only functions under the
*first* reading:

```text
estate/
├── .habitat/scope.yml     ← contains  path: ../orders-api
├── orders-api/
└── billing/
```

`../orders-api` reaches `estate/orders-api` **only** if subject paths
resolve from `.habitat/`. So the two fields, both documented with the
identical phrase "relative to the manifest", resolve from **different
directories**, and every published example silently depends on that.

`subject_path` compounds it with a third anchor. Read literally,
"relative to the report" makes `subject_path: .` denote the
`assessments/` directory rather than the subject root — since reports
live at `<subject>/assessments/<date>-assessment.md`. Every emitted
report today writes `.` meaning the subject root, which is the useful
value and not the documented one.

### The evidence is the text

The defect needs no run to demonstrate it. The four quotations above are
the evidence, they are all on `main`, and they contradict each other on
the page: the same phrase anchors two fields at two directories, and the
worked example in `write-a-scope-manifest.md` only functions if a reader
splits them. Any reviewer can check that in a minute, and it stays
checkable after this spec ships, because the quotations carry file and
line.

### Why it matters more than a wording defect

The failure mode is quiet. A subject whose path does not resolve is
recorded as `unreachable` in the coverage ledger and **the run
continues** — by design, because an unreadable repository across a client
boundary is an ordinary fact and not an error. So a path-anchor
disagreement is indistinguishable, in the output, from a repository
nobody has access to. The instrument will produce a well-formed portfolio
report covering half the named estate, and its coverage ledger will
correctly say "assessed 1 of 2" while attributing the miss to the wrong
cause. Acceptance criterion 7 exists to close exactly this.

### Corroborating run

A two-subject scope run on 2026-08-17 over `ai-readiness-assessment` and
`ai-literacy-superpowers` completed cleanly, with subject paths resolved
from `.habitat/` and `report.output` from its parent — the split reading.
It produced correct output, but only because the operator inferred the
split from the worked examples rather than from any statement of the
rule; an agent applying the reference table uniformly would have missed
every subject by one level.

**That run's artefacts were deliberately discarded** — it was a trial of
the multi-repo entry point, and its branches and reports were abandoned
without committing. It is recorded here as corroboration only, and
nothing in this spec rests on it. The published three-subject roll-up in
`docs/examples/habitat-thinking-estate.md` (2026-08-15) is a **different,
earlier run** and is not evidence for this defect either way.

## Design

### The rule

> **The scope root is the directory containing `.habitat/`.**
> Every path in the manifest resolves from the scope root. There is no
> second anchor.

`.habitat/` is a container for scope configuration, not a base for path
arithmetic. Naming the *estate directory* as the anchor matches how the
docs already describe where a manifest goes ("a directory *above* the
repositories it names — usually the directory you clone into") and makes
the existing `report.output: assessments/` default correct as written.

### Consequences

| Field | Anchor after this spec | Example |
|---|---|---|
| `subjects[].path` / `subjects[].paths[]` | scope root | `./orders-api` |
| `habitats[].path` | scope root | `./platform-harness` |
| `report.output` | scope root | `assessments/` → `<scope root>/assessments/` |
| `subject_path` (summary block) | scope root, or `.` in a standalone run | `./orders-api` |

The published examples change from `../orders-api` to `./orders-api`.
That is the *visible* cost. It is not the whole cost, and an earlier
draft of this spec claimed it was:

**`subject_path` forces an instrument edit, not only a documentation
one.** Both assess surfaces hardcode `subject_path: .` in the
summary-block template. Under a scope-root anchor that literal is wrong
for every subject in a scope run — only a standalone run, where the
subject *is* the working directory, can honestly emit `.`. Left alone,
the instrument would keep writing a value that the reference page this
spec fixes says is invalid. So the template becomes a placeholder
naming the manifest path, and the change reaches `commands/` and
`skills/`, which brings the *Dual-surface sync* constraint into play.

The Risks row below is right that nothing *consumes* `subject_path`, and
that remains verified. It was wrong to infer from that that the field has
no reach into the instrument: the emitting template is instrument text.
"Nothing reads it" bounds the blast radius downstream; it says nothing
about what has to be edited upstream.

### Manifest lookup, also underspecified

> Look for `.habitat/scope.yml` in the working directory, then upward at
> most three levels. — `commands/ai-readiness-rollup.md:137`

"Three levels" of what is not stated, and the ambiguity matters more once
the anchor is fixed, because the located manifest now determines the
scope root. Specify it as:

> Check `<dir>/.habitat/scope.yml` for `dir` = the working directory,
> then each of its first three parent directories, stopping at the first
> hit. Four directories are tested in total. The scope root is the `dir`
> that produced the hit — never the working directory.

The last clause is the load-bearing one: running the roll-up from inside
`estate/orders-api/` must resolve paths from `estate/`, not from
`orders-api/`.

### Surfaces to change

Command/skill parity (I3 of spec 0011) applies — the framework content
must stay identical across both pairs:

**Fifteen surfaces, not the nine an earlier draft of this table listed.**
Anchor wording lives in four places; `../` example manifests are
scattered across eleven more. Acceptance criterion 4 says *every* example
manifest across `docs/`, and that criterion — not this table — is the
authority where the two disagree.

**Instrument** — *Dual-surface sync* applies (I3 of spec 0011); every
edit is mirrored in the paired file:

| Surface | Change |
|---|---|
| `commands/ai-readiness-rollup.md` ≡ `skills/ai-readiness-rollup/SKILL.md` | Define the scope root with a worked tree; re-anchor the example manifest; `<manifest directory>` → `<scope root>`; rewrite the lookup rule; add the stop-when-nothing-resolves paragraph (criterion 7) |
| `commands/ai-readiness-assess.md` ≡ `skills/ai-readiness-assessment/SKILL.md` | Scope-root reference in scope-run step 1; `subject_path` paragraph; replace the hardcoded `subject_path: .` in the summary-block template |

**Reference** — where the anchor is defined:

| Surface | Change |
|---|---|
| `docs/reference/scope-manifest.md` | New **Path resolution** section: anchor table for all five fields, worked layout, the run-from-inside-a-subject case, the recorded trade-off; three field cells rewritten; lookup rewritten |
| `docs/reference/assessment-summary-block.md` | `subject_path` no longer "relative to the report" |
| `docs/reference/portfolio-report.md` | `<manifest directory>` → `<scope root>` |
| `docs/reference/portfolio-regimes.md` | Example path re-anchored |

**How-to and examples** — where the `../` manifests actually live. These
are the seven the earlier table missed:

| Surface | Change |
|---|---|
| `docs/how-to/write-a-scope-manifest.md` | Example paths, anchor sentence, lookup wording, monorepo case; its `estate/assessments/` claim becomes true rather than accidentally true |
| `docs/how-to/assess-with-an-org-level-habitat.md` | Example paths |
| `docs/how-to/assess-repos-with-a-shared-harness.md` | Example paths |
| `docs/how-to/assess-across-a-client-boundary.md` | Example paths |
| `docs/examples/fragmented-estate.md` | Example paths |
| `docs/examples/separate-harness-partially-bound.md` | Example paths |
| `docs/examples/habitat-thinking-estate.md` | Example paths, plus a note that the manifest is shown re-anchored — the page records a real run and must not appear to have been re-run |
| `docs/tutorials/assess-a-team-across-repositories.md` | **No change** — already uses `./orders-api`; verify only |

38 example paths were re-anchored across `docs/` alone.

The tutorial already wrote `./orders-api` while the how-to wrote
`../orders-api` for the same shape. That the two disagreed before this
change is further evidence the anchor was never fixed.

## Alternatives considered

**Anchor everything at `.habitat/`.** Keeps every published
`subjects[].path` example working untouched, so the migration cost is
zero. Rejected because `report.output: assessments/` would then mean
`.habitat/assessments/`, burying portfolio reports in a dot-directory —
so the default would have to become `../assessments/`, which is a worse
thing to explain than a one-time example fix. It also anchors user-facing
paths to an implementation detail: move the manifest to `scope.yml` at
the root later and every path breaks.

**Resolve paths relative to the repository root (git-discovered).**
Rejected: the scope root is frequently *not* a repository — the
documented layout is a plain directory holding several clones. It would
also make the manifest's meaning depend on whether someone had run
`git init` in the parent.

**Try both anchors and use whichever exists.** Rejected on the
instrument's own stated principle — "Do not guess a scope. Inferring the
estate from sibling directories produces a portfolio report whose
coverage nobody can check" (`commands/ai-readiness-rollup.md:141`). A
path that resolves differently depending on what happens to be on disk is
the same defect wearing a helpful face, and it would make the
`unreachable` ledger status unreadable: a reader could no longer tell a
missing repo from a mis-anchored path.

**Require absolute paths.** Unambiguous and unusable — manifests are
committed and shared across machines.

## Risks / what could go wrong

| Risk | Assessment |
|---|---|
| **Breaks manifests already in the wild.** | Low. Spec 0011 was accepted 2026-08-14, three days before this spec; the scope feature has no known external users. The cost of this change rises with every week it waits — this is the cheapest it will ever be. |
| **A manifest written under the old reading fails silently.** | Real, and the worst failure mode here. A subject whose path no longer resolves is recorded `unreachable` and the run *continues*. Mitigation: when **every** subject is unreachable, stop rather than emit a zero-coverage portfolio report, and say that a path-anchor mismatch is the likely cause. |
| **The rule is stated and the surfaces still drift apart.** | The convention-parity problem this repo already has elsewhere. Nothing deterministic checks that four documents agree about path semantics. Mitigation is the fixture below, not prose. |
| **`subject_path` change ripples into the roll-up's report discovery.** | Checked: nothing consumes the field. `grep -rn subject_path commands/ skills/ docs/ tests/` returns only the two emitting templates and the six fixture reports, all writing the literal `.`. The roll-up locates reports via `<subject path>/assessments/` from the manifest, never via `subject_path`, so this is a documentation fix with no behavioural reach. |
| **The chosen anchor is simply the wrong one.** | The strongest argument against: `.habitat/` is where the file lives, and "relative to the file" is the more conventional convention (`.gitmodules`, `docker-compose.yml`, `tsconfig.json` all resolve relative to themselves). This spec trades that convention for a correct `report.output` default and a movable manifest. A reviewer who weighs the conventions differently should say so — the alternative is fully worked above and switching to it is cheap while this is still a draft. |

## Adversarial review

- **Reviewer**: Russ Miles (anchor decision) · _remaining rows pending PR reviewer_
- **Disposition**: **accepted** — for the anchor decision only
- **Notes**: The Risks row "the chosen anchor is simply the wrong one"
  was adjudicated on 2026-08-17 by the repo owner, with both options
  presented and worked. **Disposition: the scope root — the directory
  containing `.habitat/` — is the anchor**, accepting the two stated
  costs: the published `subjects[].path` examples change from
  `../orders-api` to `./orders-api`, and the instrument departs from the
  self-relative convention that `.gitmodules`, `docker-compose.yml` and
  `tsconfig.json` follow. Accepted because it makes the existing
  `report.output: assessments/` default correct as written and keeps the
  manifest movable. The alternative stays documented under
  *Alternatives considered* so a later reviewer can see what was traded
  away rather than having to reconstruct it.
  The remaining Risks rows are unadjudicated and belong to the PR
  reviewer — in particular the silent-`unreachable` failure mode, which
  Acceptance criterion 7 exists to close.

## Acceptance

**Not all eight are the same kind of claim, and an earlier draft
presented them as peers.** The instrument is markdown instructions, not
code: nothing here resolves a manifest, so no assertion can execute a
path lookup. Each criterion is tagged with what can actually verify it:

- **A** — deterministic. A grep, a diff or a test asserts it, and CI
  fails without it.
- **B** — behavioural. Only an agent run can demonstrate it. Recorded as
  a B-tier expectation in the fixture; a green suite is *not* evidence
  that it holds.

Tagging matters because a B criterion whose prose exists is easy to
mistake for a B criterion that has been observed to work. Criterion 7 is
the trap: that its paragraph is present is an A fact; that a real run
stops as instructed is not.

1. **(A)** `docs/reference/scope-manifest.md` contains a **Path resolution**
   section that defines the scope root as the directory containing
   `.habitat/`, and no field description in the repo says "relative to
   the manifest" without naming that directory.
2. **(A)** `grep -rn "manifest directory" commands/ skills/ docs/` returns
   nothing — the phrase is replaced by "scope root" everywhere.
3. **(A)** The rollup command and skill state the four-directory lookup rule and
   that the scope root is the directory that produced the hit.
4. **(A)** Every example manifest across `docs/` uses paths consistent with the
   rule, and the how-to and the tutorial agree with each other.
5. **(A)** Command/skill parity holds: framework text is byte-identical across
   `commands/ai-readiness-rollup.md` ≡ `skills/ai-readiness-rollup/SKILL.md`
   and `commands/ai-readiness-assess.md` ≡
   `skills/ai-readiness-assessment/SKILL.md` (constraint: *Dual-surface
   sync*).
6. **(B)** A roll-up over the documented `estate/` layout, run from **inside a
   subject directory**, resolves all subjects and writes to
   `estate/assessments/` — the case that is wrong under either uniform
   reading of the current text. No assertion can cover this; it needs a
   session against the fixture, and it is the criterion most worth
   exercising by hand before release.
7. **(A for the prose · B for the behaviour)** A run in which no subject path
   resolves stops with a message naming a path-anchor mismatch as the likely
   cause, instead of emitting a zero-coverage portfolio report. That the
   instruction is present is deterministically checkable; that an agent obeys
   it is not.
8. **(A)** A `tests/fixtures/` case covers a two-subject scope manifest, so the
   TDAB suite fails if the anchor regresses. `tests/run.py` asserts
   against committed sample assessments and currently has no scope-run
   fixture at all — without this, nothing in CI can catch a
   reintroduction. The fixture's `expected.md` carries the B-tier
   expectations for 6 and 7 so they are recorded rather than lost.
