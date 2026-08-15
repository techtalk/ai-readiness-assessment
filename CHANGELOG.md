# Changelog

All notable changes to the `ai-readiness-assessment` plugin are documented in
this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the plugin adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The version lives in `.claude-plugin/plugin.json`. **Every version bump must add
a matching `## [x.y.z]` section below** — the release workflow
(`.github/workflows/release.yml`) reads this file for the GitHub Release notes
and fails the release if the entry is missing. Record day-to-day changes under
`Unreleased` and rename it to the new version when you bump.

## [Unreleased]

## [1.0.0] - 2026-08-15

First stable release.

The instrument has been single-repository since 0.1.0. This release adds
**multi-repo scope**: the assessment unit becomes *subject × governing
habitat*, with the cognitive read scoped to the **team** rather than to a
repository, and the **spread** of gaps across an estate as the headline
finding a single-repository assessment structurally cannot produce.

With no `.habitat/scope.yml` present, `/ai-readiness-assess` behaves as
it did before — the one difference in a single-repo run is the
machine-readable `assessment-summary` block appended to every report.

Deliberately absent: any portfolio score, grade, percentage or averaged
gap. Averaging destroys the spread, which is the only thing a portfolio
view adds.

This release also accumulates specs 0008–0010, which had not been cut
into a version: the Assessment Review section, the Habitat/Workflow Gap
rename, and book links in reports.

### Changed

- **Every mention of *The Sovereign Engineer* in a report is now a link** (spec
  [0010](specs/0010-book-mentions-are-links.md), #58) — the Reading Path prose,
  the Assessment Review credit line, and the closing pointer all link the
  book's title. Two labels stay unlinked by design: the "Cognitive read
  (Sovereign Engineer)" badge and the provenance note.
- **One Leanpub URL throughout** — the AI-readiness campaign link
  (`/c/ai-readiness`) is now used by every book link in the reports, the docs,
  and the README, replacing the bare product-page URL that was in use in about
  half of them. `.claude-plugin/plugin.json`'s `homepage` keeps the canonical
  product URL.

- **The Habitat Build Gap is now the Habitat/Workflow Gap** (spec
  [0009](specs/0009-habitat-workflow-gap-rename.md), #57) — renamed across the
  command, the skill, the plugin manifests, every documentation page, both
  dogfood examples, and the test suite. The measure is unchanged: still
  `cognitive level − 14-dimension habitat maturity mean` with the same three
  regimes. Two documentation pages moved with it:
  `reference/habitat-build-gap` → `reference/habitat-workflow-gap` and
  `how-to/read-the-habitat-build-gap` → `how-to/read-the-habitat-workflow-gap`;
  the old URLs no longer resolve. The six `tests/fixtures/*/assessments/`
  reports were rewritten to the new name too, so every report in the repo reads
  the same way and the A13 assertion stays strict. Records that describe past
  decisions — specs 0003 and 0004, released changelog entries, and
  `REFLECTION_LOG.md` — keep the name the instrument used at the time.

### Added

- **The real Habitat-Thinking estate example** (#69) — an actual
  `/ai-readiness-rollup` across the repositories that build this instrument,
  published as it came out. It does **not** produce a spread: one subject is
  comparable, one was measured by a different instrument, and one could not be
  found. Every absent number in it is the machinery declining to invent one.
- **Fixed: the roll-up had no coverage status for a report produced by a
  different instrument.** `Habitat-Thinking/ai-literacy-superpowers` carries a
  well-formed assessment with a cognitive read and discipline scores, but no
  Habitat Maturity Profile and no gap — it is neither `degraded` (which means
  "measured the right things, predates the summary block") nor `unparseable`.
  New status **`incompatible`**, kept deliberately distinct from `degraded`:
  collapsing them would report a subject as nearly-there when it has not been
  assessed against this model at all.
- **Fixed: a single-subject estate could have its one gap reported as a
  spread.** A spread is a range and needs **at least two comparable subjects**;
  with fewer the roll-up now says so and names what would produce one. Reporting
  one gap as a range would manufacture exactly the finding a portfolio view
  exists to produce.
- **Shareable HTML portfolio report** (spec
  [0011](specs/0011-multi-repo-scope.md), #68) — the roll-up can now be rendered
  the way the per-repo report already could: a single self-contained file, all
  CSS inlined, **no network assets**, working opened straight from the
  filesystem. The matrix is the artefact that travels, and it travels badly as
  markdown. Same visual language as the per-repo report — navy header band, the
  same level colours, no emoji, print-friendly. **Coverage renders above the
  fold**, before the matrix: a matrix is persuasive whether or not the data
  behind it is complete, so an incomplete assessment has to *look* incomplete.
  The spread renders as a plotted distribution with the extremes named —
  **never a dial, gauge, grade or percentage**, a rule held strictest here
  because the render is where an estate gets reduced to one number if anywhere
  does.
- **Three portfolio examples published as HTML** alongside their markdown, all
  banner-marked synthetic. Generated from the same figures as the markdown, so
  the two cannot drift.
- **Fixed: four occurrences of the retired "Habitat Build Gap" survived spec
  [0009](specs/0009-habitat-workflow-gap-rename.md)'s rename** — including the
  instrument's own definition of the metric ("The Habitat Build Gap measures
  coherence between the two reads") in both surfaces. All four were **wrapped
  across a line break**, and 0009's acceptance check matched the unwrapped
  string, so it reported success. A new assertion matches the term across
  whitespace in the live surfaces, so a wrap cannot hide it again. Specs, the
  changelog and the reflection log keep the name deliberately — they record
  what the instrument said at the time.
- **Habitat beyond the checkout — org layer, packages and forks** (spec
  [0011](specs/0011-multi-repo-scope.md), #67) — three new habitat kinds for
  governance that exists but cannot be read from any subject.
  **`package`**: the lockfile or plugin manifest gives a resolved version and
  pin age, so the pin is verified but the content is not — dimensions the
  package supplies stay `inferred` unless local evidence corroborates them, and
  the pinned version governs rather than the latest release.
  **`org`** (org `.github` repo, org rulesets, org-wide instructions): **never
  raises a dimension**, and is reported as *declared, unverifiable from here*
  with the action that would make it verifiable — reference it from the subject,
  so it becomes bindable and therefore observable. With a sibling repo there is
  at least an artefact to read; an org habitat has none, which makes it the
  easiest thing in the instrument to take silent credit for.
  **`upstream`**: placed as `inherited`, with divergence choosing the steer —
  contribute back when close to upstream, overlay locally and stop claiming to
  track when heavily diverged.
- **Partial scope is reported against named subjects, not readable ones.** A
  manifest naming fourteen subjects of which six can be read now reports
  "assessed 6 of 14 named subjects" — the denominator is the claim. A client
  boundary, another business unit or a repository nobody has access to is an
  ordinary condition, not a reason to shrink the scope silently, and under
  partial coverage the ceiling is never described as estate-wide.
- **Two new how-to guides** for the consultancy and cross-business-unit cases,
  including the engagement pattern where each team runs its own assessment,
  keeps its own report, and shares only the summary — so a roll-up never needs
  access to anyone's code.
- **Portfolio regimes, duplication and drift** (spec
  [0011](specs/0011-multi-repo-scope.md), #66) — the roll-up now names what
  *kind* of multi-repo situation an estate is in, on a second axis parallel to
  the gap regimes and read the same way: a regime, not a score. **Federated**
  holds and watches the pin ages; **Distributed** binds the harness that
  already exists rather than extending it; **Fragmented** extracts the common
  layer; **Islanded** moves people rather than files. Selection runs on four
  coarse, checkable inputs — whether habitats are declared, the `inherited` vs
  `inherited-unbound` proportion, near-duplicate control surfaces, and the gap
  spread. Where the inputs disagree the report names **both** regimes rather
  than forcing one label onto an estate genuinely in two states at once.
- **A regime never ships without its evidence** — the provenance counts, the
  spread, the declared habitats and the duplicated artefacts that produced the
  classification are stated in the report. An unevidenced claim about somebody's
  estate gets argued with rather than acted on. Asserted by the suite.
- **Near-duplicate detection**, reported as *fragmented with lineage*. Requires
  all three of a shared artefact name, substantially overlapping content, and
  divergent specifics — any two without the third is a coincidence, and acting
  on a coincidence starts a consolidation programme against files that were
  never related. The report names **where** the copies diverged, because that is
  what an extraction has to reconcile.
- **`justified_variance`** in the manifest suppresses drift findings and
  extraction candidates for named dimensions while **listing them as declared**
  with their reason. Listed so a reader can disagree; suppressed so a polyglot
  estate is not nagged toward a convergence that would make it worse.
- **Example 4** on the docs site — a fragmented estate of five services with a
  `HARNESS.md` descended from a common ancestor and diverged, plus a legacy
  repository at `posture: maintenance` that would otherwise set the ceiling on
  eleven of fourteen dimensions.
- **Every example page must now declare itself synthetic or real**, checked
  across the whole examples directory rather than a fixed list — so a new
  example cannot be added without saying which it is, and a real reading can
  never end up wearing the synthetic banner.
- **Single-session scope run with a team-scoped cognitive read** (spec
  [0011](specs/0011-multi-repo-scope.md), #65) — `/ai-readiness-assess --scope`
  assesses every subject in a manifest in one session, asking the behavioural
  questions **once for the team** rather than once per repository. Each subject
  then gets exactly one cheap question — whether the way of working there is
  materially different. No reuses the team read and records
  `cognitive_source: team`; yes re-asks the six behavioural dimensions and
  records `cognitive_source: subject`, with the portfolio showing that
  subject's gap separately from the team pattern. A reused read is **always
  declared in the report body**, never a footnote: a reader cannot otherwise
  tell a placement gathered here from one carried in from a conversation about
  a different repository.
- **The run states its size before it starts** and recommends splitting rather
  than degrading half-way through, processes subjects sequentially, and holds
  no more than one subject's raw evidence at a time — the reports on disk are
  the durable record.
- **`posture` (`active` / `maintenance` / `archived`)** — stops a single dead
  repository pinning the estate's ceiling permanently. `archived` subjects are
  excluded from the ceiling and marked in the matrix; `maintenance` subjects
  are reported but excluded from common-weak detection. Both are still shown:
  hiding them would misstate coverage.
- **Multi-path subjects (`paths:`)** — a contract repo and its implementation
  merge into one placement rather than reporting two half-habitats.
- **Internal documentation links are now checked.** mkdocs does not run in
  strict mode, so a mistyped relative link built and deployed silently. A new
  assertion resolves every relative link in `docs/` — added after exactly that
  bug was introduced and caught by hand during this slice.
- **Shared-habitat inheritance and binding** (spec
  [0011](specs/0011-multi-repo-scope.md), #64) — a subject governed by a harness
  that lives elsewhere is now placed against the **effective habitat**: the
  shared layer merged with the local one, with each dimension recording its
  `provenance` as `local`, `inherited`, or `inherited-unbound`. The third value
  is the point of the slice — it caps the dimension at what the *local*
  evidence supports and names the shared artefact that was expected to bind.
  A harness held centrally is not a harness that governs; recorded is not
  enforced. Comes with a six-signal binding evidence checklist (CI reuse, hook
  and plugin config, submodule pin, lockfile pin, convention-file references,
  shadowing), the rule that a **pinned revision is the governing habitat**
  rather than the shared repo's tip, and `.gitmodules` autodetection that
  *offers* a manifest and leaves the run unchanged if declined. The manifest
  gains `habitats:` with kinds `repo`, `submodule` and `self`; the summary
  block gains `provenance` on every row, a `habitat` key, and an optional
  `binding:` section recording what was found rather than only the conclusion.
- **Silence is not negation.** Where the binding checklist finds no signal but
  no evidence of absence either, the dimension is placed `inferred` and a
  clarifying question is spent before anything is called `inherited-unbound` —
  so a team binding its harness by an unrecognised mechanism is never accused
  of a discipline failure it does not have. Every binding finding names the
  artefact expected to bind and where it was looked for. Asserted by the suite.
- **Two worked examples** on the docs site, both clearly banner-marked as
  synthetic: a parent repo with three bound submodules (narrow spread), and a
  platform harness governing four services where one is stale-pinned and one is
  not bound at all (spread of 1.79 across the same team). A test asserts every
  synthetic example carries its banner — nothing on the docs site should be
  ambiguous about whether it is a real reading.
- **`/ai-readiness-rollup` — portfolio roll-up across repositories** (spec
  [0011](specs/0011-multi-repo-scope.md), #63) — the first slice of multi-repo
  scope. A new command and skill read the machine-readable summary block from
  assessments that already exist and produce one portfolio report: a coverage
  ledger, a matrix of subjects against the fourteen dimensions, the gap
  **spread**, and a ceiling split into what enablement owes the estate and what
  each team owes itself. No re-assessment and no behavioural questions — twelve
  repositories interactively is not a session anyone sits through. Driven by an
  opt-in `.habitat/scope.yml`; with no manifest present `/ai-readiness-assess`
  behaves exactly as before. There is deliberately **no portfolio score**:
  averaging the gaps erases the spread, which is the only thing the portfolio
  view adds.
- **Every report now ends with a machine-readable `assessment-summary` block**
  — all fourteen dimensions with their level and `confidence`
  (`observed` / `asked` / `inferred`), plus the maturity mean, cognitive read,
  signed gap, regime, ceiling dimensions and weakest discipline. This is what
  decouples *running* an assessment from *summarising* one, so a roll-up can
  read a report months later without re-parsing prose. `provenance` is
  deliberately not emitted yet — it arrives with shared-habitat support, and a
  placeholder `local` on every row would make an unbound inherited rule
  indistinguishable from local evidence.
- **Command/skill parity is now asserted, not assumed.** The rule that both
  entry points carry identical framework content had been running on trust; the
  suite now compares the two bodies directly (`R1`, and `R6` for the roll-up
  pair) and names the first divergent line. It caught a real drift during its
  own slice. Also new: `A15`/`A16` assert the summary block is complete, is the
  last element of the file, and agrees with the prose on maturity level,
  cognitive read and regime. 72 → 90 assertions.
- **Multi-repo documentation** — a tutorial (roll up existing assessments), a
  how-to (write a scope manifest), three reference pages (scope manifest schema,
  assessment summary block, portfolio report structure) and an explanation
  (why there is no portfolio score), under a new **Multi-repo** nav section.
- **Assessment Review section** in the generated report (spec
  [0008](specs/0008-assessment-review-section.md), #55) — the report's single
  call to action now lives in its own section that positions a one-hour review
  of the results as the continuation of the assessment: "Not sure what these
  results mean?", the reviewer credit, the four outcomes of the hour, and a
  **Book your AI Readiness Review** button. In HTML it renders as a `#162e40`
  box with a `#dcdbdd` outcomes panel and a `#00b2a2` button.
- A fixed transition paragraph closing `## Next Steps`, introducing the purpose
  of a review and bridging the report to the invitation that follows.

### Changed

- `## Next Steps` now explains without selling — it keeps its fully generated,
  gap-anchored first paragraph and carries no link or button. In HTML it is its
  own light grey (`#f0eeeb`) box rather than the navy CTA block.
- `tests/run.py` A9 (single CTA) reads `## Assessment Review`, falling back to
  `## Next Steps` so reports written before the split are still checked.
- Both dogfood examples in `docs/examples/`, their markdown sources under
  `assessments/`, and the output reference docs updated to the new structure.
  The **Reading Path** section is unchanged.
- The booking link behind the call to action now points at the AI Readiness
  Review calendar (`.../bookwithme/user/f16fa59…@techtalk.at`), replacing the
  previous TechTalk booking link across both surfaces, both examples, and both
  markdown assessments. The `thomas.stangl@techtalk.at` contact line under the
  button is dropped.

### Fixed

- The product page link in `README.md` and `docs/index.md` now points at the
  published `https://techtalk.at/ai-readiness-assessment/` instead of the
  `-draft` URL (#42).
- The two `ai-literacy-superpowers` links in `README.md` now point at the
  canonical `Habitat-Thinking/` org rather than relying on the
  `russmiles/` rename redirect, matching the docs site.

### Removed

- The *Inspired by* pointer to the `ai-literacy-for-software-engineers`
  reference repository in `README.md` — the repository is private, so the
  link was unreachable for public readers.
- The orphaned `assessments/2026-06-03-assessment.html` and
  `assessments/2026-06-03-assessment-2.html` — unreferenced duplicates of
  the maintained example reports under `docs/examples/`, still carrying
  the pre-redesign look and the dead `techtalk.ai` link. The canonical
  rendered examples live in `docs/examples/` (linked from the README and
  docs site).

### Changed

- **Made the TechTalk engagement the primary answer; the book is now
  secondary** (spec 0007): Next Steps (the TechTalk CTA) is rendered
  before the Reading Path in both the markdown report and the HTML; the
  HTML CTA block leads as the prominent answer with a secondary "Want to
  read more?" link to the matched chapter below the button, and the
  Reading Path follows as a lighter self-guided resource. The book stays
  in every report. Updated both example reports, and fixed their stale
  `techtalk.ai` markdown CTA links to the booking link (missed in #50).
- **Updated the TechTalk CTA to a calendar booking link**: the "Get in
  touch" / "Book a call with TechTalk" button in the command, skill, and
  both example reports now points to the Outlook *Book With Me* page;
  `thomas.stangl@techtalk.at` retained as a secondary contact line. (#50)
- **Aligned docs site style with TechTalk branding**: TechTalk navy
  primary colour (`#0b2b3c`) for the nav bar and active links — in both
  light and dark mode (#47, #48); teal accent, lightened to teal-300 for
  links in dark mode for readability (#49); system font stack (drop
  Google Fonts Roboto); copyright footer "© TechTalk GmbH · Vienna,
  Austria" on every page; TechTalk website added to social links.
- **Aligned HTML report design with the TechTalk marketing site** (spec
  0006): all-sans-serif typography (drop Georgia serif body); dark navy
  header band with TechTalk wordmark, headline lines, and a five-level
  progress strip; TechTalk navy `h2` headings and borders; TechTalk GmbH
  footer branding. Updated the two example reports and fixed their
  `techtalk.ai` CTA links to `techtalk.at`.
- **Aligned repo language and links with the TechTalk marketing site**:
  fixed the TechTalk CTA domain (`techtalk.ai`, a parked GoDaddy page →
  `techtalk.at` with `thomas.stangl@techtalk.at`) in the command and
  skill; corrected the command description from "AI literacy" to "AI
  readiness"; added a **Product page** link to the README and a matching
  button to `docs/index.md`; echoed the "scan, score, and a plan"
  framing in the README intro line. (#42)

### Added

- A **No direct pushes to main** harness constraint (HARNESS.md,
  deterministic), enforced by GitHub branch protection with
  `enforce_admins: true` — all changes must arrive via a pull request.
  Constraint count 3/4 → 4/5. (#44)
- An **AI Literacy: Level 4** badge (and an **Agent Harness Enabled**
  badge) in the README, after `/assess` independently confirmed the repo
  reads **Level 4 — Specification-led**. Also corrected the stale harness
  badge (2/3 → 3/4 enforced) after the Spec-first constraint.

### Changed

- The assessment now **leads with two headline lines** — *AI Readiness —
  Habitat Maturity: Level N (Verb)* and *Next Step / Gap: +X to Level N+1
  (NextVerb)* — with the Habitat Build Gap (coherence) kept as a
  secondary line. (Specs 0004–0005.)
- **Report language aligned with the public "AI Readiness" mockup**
  (spec 0005): the headline shows *AI Readiness — Habitat Maturity*; an
  **AI Readiness Score** breakdown across five readiness dimensions
  (Context · Conventions · Architectural guidance · Guardrails · Agent
  readiness) is added; and Recommendations are reframed as a
  **Prioritised Improvement Plan** ordered by what the team must develop
  and the organisation must provide. The two example reports — and the
  narrative example surfaces (the docs `examples` page and the README
  example table) — were aligned to match.

### Added

- An example self-assessment — the plugin run against its own repo —
  committed under `assessments/` (markdown + HTML) and linked from the
  README and the docs site (`/examples/`).
- A `specs/` layer (README + template + the first spec) and a
  **spec-first** convention in HARNESS.md — starting the L3→L4 jump the
  self-assessment recommended.
- An **Onboarding gate** (`.github/workflows/onboarding-gate.yml`) and a
  matching GC rule: a PR that changes the HARNESS body or AGENTS.md must
  refresh ONBOARDING.md, so the onboarding guide can't silently trail its
  sources.
- **Spec-first is now enforced**: promoted from convention to a HARNESS
  constraint, backed by a **Spec-first gate**
  (`.github/workflows/spec-first-gate.yml`) — instrument changes must
  carry a spec. The spec format gained an adjudicated **Adversarial
  review** disposition, and specs 0002–0003 were added (completing the
  L3→L4 specifications discipline).
- A **re-assessment** showing the L3→L4 progression
  (`assessments/2026-06-03-assessment-2.md` + HTML), linked from the
  README and docs as a progression example: cognitive read L3→L4, with
  the Habitat Build Gap flipping +0.2 (Coherent) → +1.1 (Ambition
  outpaces enablement).

## [0.4.1] - 2026-06-03

### Changed

- Reworded the TechTalk call to action in the assessment ("TechTalk
  offers …" → "TechTalk can support …"), kept in sync across the command
  and skill, and the matching engagements line in the README.

## [0.4.0] - 2026-06-02

### Added

- Apache License 2.0 (`LICENSE`), declared as `Apache-2.0` in
  `plugin.json` and `marketplace.json`, with a License badge in the
  README.
- A documentation site (MkDocs Material, Diátaxis-structured) under
  `docs/`, deployed to GitHub Pages via `.github/workflows/pages.yml`,
  covering tutorials, how-to guides, reference, and explanation for the
  whole plugin — especially the assessment.
- `CHANGELOG.md` and a changelog-driven release workflow: every version
  bump publishes a GitHub Release whose notes are the matching CHANGELOG
  section.
- CI for the TDAB structural suite, a PR-time changelog gate, and
  required status checks (`A-tier structural assertions`, `Changelog
  gate`) on a protected `main`.
- `AGENTS.md`, `ONBOARDING.md`, and `REFLECTION_LOG.md` for contributors,
  plus a "Dual-surface sync" harness constraint (command ≡ skill) and
  synced Cursor / Copilot / Windsurf convention files.
- README prerequisites and status / scope badges; repo description,
  topics, and homepage.

### Changed

- The Sovereign Engineer call-to-action now points to the AI-readiness
  campaign URL (`https://leanpub.com/thesovereignengineer/c/ai-readiness`)
  — in the assessment's reading-path CTA (command + skill) and the
  "buy the book" CTAs in the README and the docs.

## [0.3.0] - 2026-06-02

### Changed

- Made the **Agentic Experience 5-Level Habitat Maturity Model** the assessment
  spine — all fourteen dimensions placed L1–L5 with the model's own verbs, with
  the *Sovereign Engineer* six-level cognitive ladder folded in as the cognitive
  read (#5).
- The **Habitat Build Gap** is now measured against the mean of all fourteen
  dimensions, not just the four headline axes (#5).
- README leads with the model; install docs cover GitHub Copilot CLI first, then
  Claude Code, with both interactive and command-line forms (#5).

### Added

- TDAB A-tier structural test suite (`tests/run.py`) wired into CI on every PR,
  including the fourteen-dimension Habitat Maturity Profile assertion (#5).
- Required `A-tier structural assertions` status check on `main`.
- Convention files for Cursor, Copilot, and Windsurf synced from HARNESS.md (#7).
- Release workflow that cuts a GitHub Release on every version bump (#8).

### Maintenance

- Upgraded the harness to template 0.40.0; adopted the *Consistent formatting*
  and *Tests must pass* constraints and the *Template currency* GC rule (#6).

## [0.2.0] - 2026-06-01

### Added

- ALCI Part D operational axes (Composition, Testing, Observability, Governance)
  and the Habitat Build Gap (#4).

## [0.1.0] - 2026-05-11

### Added

- Initial `ai-readiness-assessment` plugin: the self-contained assessment
  instrument (command + skill).
- `techtalkai` marketplace manifest.
- Harness and TDAB scaffolding.

[Unreleased]: https://github.com/techtalk/ai-readiness-assessment/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/techtalk/ai-readiness-assessment/compare/v0.4.1...v1.0.0
[0.4.1]: https://github.com/techtalk/ai-readiness-assessment/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/techtalk/ai-readiness-assessment/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/techtalk/ai-readiness-assessment/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/techtalk/ai-readiness-assessment/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/techtalk/ai-readiness-assessment/releases/tag/v0.1.0
