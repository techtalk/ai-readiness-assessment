# Spec 0011: Multi-repo scope — subject, habitat, team

- **Status**: accepted
- **Date**: 2026-08-14
- **Issues**: #63, #64, #65, #66, #67, #68, #69

This is an **umbrella spec**. It records the design once; each of the six
slices is a separate issue and a separate PR, and each slice PR ticks its
line in [Acceptance](#acceptance) rather than opening a spec of its own.
The invariants below are the citable part — they are what later slices
are checked against.

## Intent

The instrument currently assumes the repo it is invoked in *is* the
habitat under examination. That holds in the single-repo case and
nowhere else. Teams that own six services governed by one platform
harness, or a monorepo with three different habitats inside it, cannot
be assessed today without pretending each repo is an island.

Splitting the assumption into its three real parts makes every
multi-repo shape expressible, and — more importantly — produces a signal
the single-repo instrument structurally cannot produce.

## Design

### The three things currently conflated

| Concept | What it is | Natural scope |
| --- | --- | --- |
| **Subject** | The code artefacts the habitat governs | A repo, a submodule, a directory in a monorepo |
| **Habitat** | The harness, control surfaces and agentic artefacts governing it | May live in the subject, a sibling repo, a parent, a package, or an org |
| **Team** | Whose behaviour produces the cognitive read | People — never a repo |

Which yields one primitive covering every shape:

> **Assessment unit = subject × governing habitat**, with the cognitive
> read scoped to the *team* and reused across units unless explicitly
> overridden.

### Why the spread is the finding

The payoff is not "it now works across repos". One cognitive read
against *N* habitat means produces *N* gaps, and **the spread of those
gaps is the headline**. A team can sit Coherent in the greenfield
service and deep in Ambition-outpaces-enablement in the legacy one. The
enablement work implied by those two facts is completely different, and
a single-repo run can never surface the difference because it only ever
has one reading to look at.

This is also why there is no portfolio score (I4). Averaging the gaps
destroys the exact signal the multi-repo unit exists to expose.

### Invariants

These hold at the end of every slice.

| # | Invariant | Why |
| --- | --- | --- |
| **I1** | **Self-contained.** No network calls, no language runtime, no external plugin, skill or service at assessment time. Model, schemas and heuristics stay embedded in the command and skill files. | The instrument's core promise. `tests/` is contributor-only and does not count. |
| **I2** | **Backwards compatible.** With no scope manifest present, `/ai-readiness-assess` behaves exactly as today. | Opt-in extension, not a migration. |
| **I3** | **Command/skill parity.** Framework content stays identical across `commands/ai-readiness-assess.md` and `skills/ai-readiness-assessment/SKILL.md`. | Both entry points must produce the same assessment. |
| **I4** | **No portfolio score.** The roll-up never averages gaps, maturity means or levels into a single number, grade or percentage. The headline is a distribution and a ceiling. | Averaging destroys the spread signal and reintroduces the score theatre the instrument exists to avoid. |
| **I5** | **Honesty flags survive aggregation.** Every placement carries its `confidence` (`observed`/`inferred`/`asked`) and, from Slice 2, its `provenance`. | A roll-up must not launder an `inferred` placement into a confident portfolio claim. |
| **I6** | **Reused cognitive reads are always declared** — in the body, not a footnote. | Silent reuse is a lie about evidence. |
| **I7** | **Reports live with their subject.** Per-unit reports go to `<subject>/assessments/`; only the roll-up goes to the scope root. | Each team keeps its own report; consultancies can assemble without owning the repos. |
| **I8** | **Weakest-as-ceiling holds at both levels**, and the portfolio ceiling is reported *split* into common-weak and locally-weak. | Preserves the model's core heuristic while separating the enablement backlog from team backlogs. |

### Terminology

The build spec proposed renaming "Habitat Build Gap" to
"Habitat/Workflow Gap" as part of Slice 1. **That rename already
shipped** in spec 0009 (issue #57), so no rename work is carried here.
The five surviving "Habitat Build Gap" strings are historical records —
CHANGELOG entries, the reflection log, and spec 0003's title — and stay
frozen.

### Scope manifest — `.habitat/scope.yml`

Absent ⇒ single-repo behaviour (I2). Present ⇒ scope-aware behaviour.
Fields are tagged with the slice that introduces them; the full schema
lives in `docs/reference/scope-manifest.md`.

```yaml
version: 1                     # S1
team: payments-tribe           # S1 — the cognitive read is scoped to this

habitats:                      # S2
  - id: platform-harness
    kind: repo                 # S2: repo | submodule | self · S5 adds: package | org | upstream
    path: ../platform-harness
    provides: [HARNESS.md, AGENTS.md, hooks, skills, agents, ci]

subjects:                      # S1
  - id: orders-api
    path: ../orders-api
    habitat: platform-harness  # S2 — omit ⇒ self-governed
    posture: active            # S3: active | maintenance | archived
  - id: legacy-batch
    path: ../legacy-batch
    posture: maintenance
    justified_variance:        # S4
      - dimension: testing
        reason: COBOL batch; harness test tooling does not apply

report:                        # S1
  output: assessments/
```

Validation: `subjects` non-empty, each with `id` and exactly one of
`path`/`paths`; `id` unique across both lists; a `habitat` reference
naming no declared habitat is a hard error. Unreadable paths are **not**
errors — they land in the coverage ledger as `unreachable`. Unknown keys
warn, never fail: forward compatibility matters more than strictness
when six slices will extend this schema.

### Assessment summary block

Appended as the **last** element of every per-unit report, in a fenced
`yaml assessment-summary` block. This is the highest-leverage change in
the whole design: it makes reports machine-readable, and so decouples
*running* an assessment from *rolling one up*. Slice 1 exists at all
because of this block.

It carries all fourteen dimensions with their level, confidence and
(from S2) provenance, plus the maturity mean, cognitive level, signed
gap, regime, ceiling dimensions and weakest discipline. Full schema in
`docs/reference/assessment-summary-block.md`.

The block is generated from the same placements the prose reports, never
computed separately, and a test asserts prose/block agreement on
`habitat_maturity_level`, `cognitive_level` and `regime`. `provenance`
is omitted entirely in Slice 1 rather than faked as `local`.

### Slices

Elephant Carpaccio — six thin vertical slices, each shippable and
independently demonstrable. Docs and examples sit *inside* each slice,
never as a trailing phase.

| Slice | Whole value | Blocked by | Issue |
| --- | --- | --- | --- |
| 1 | A portfolio report from assessments you already have | — | #63 |
| 2 | Subjects governed by a shared harness, with binding truthfully reported | 1 | #64 |
| 3 | One session, one set of behavioural questions, whole estate | 1, 2 | #65 |
| 4 | The estate's regime named, with the structural move that fits it | 1, 2 | #66 |
| 5 | Habitat outside the checkout handled honestly | 2 | #67 |
| 6 | The matrix becomes shareable | 1 | #68 |

Slices 4 and 5 are independent; either may follow 3. Slice 6 may be
pulled forward if an engagement needs the artefact sooner.

### Why Slice 1 is first

Roll-up-over-artefacts is the cheapest whole value in the set, and it
removes the ergonomic blocker that would otherwise sink every later
slice. Twelve repos × ten minutes, with the behavioural questions asked
twelve times, is not a session anyone sits through — and a single-session
scan of twelve repos exhausts context long before it finishes. It also
decouples *who runs the assessment* from *who reads the summary*, which
is what a client engagement actually needs.

## Alternatives considered

- **A `scope:` key inside the existing report front matter** rather than
  a separate manifest. Rejected — the manifest has to be readable from a
  parent directory that may contain no assessment at all, which is
  precisely the consultancy case.
- **Assessing all subjects in one pass and holding the evidence.**
  Rejected on context grounds; the sequential per-subject discipline in
  Slice 3 exists for this reason.
- **A portfolio score.** Rejected as I4 — see above. This is the
  alternative that will keep being proposed, which is why
  `docs/explanation/why-no-portfolio-score.md` exists: so the position
  can be cited rather than re-argued each time.
- **pytest for the new tests.** Rejected — `tests/run.py` is stdlib-only
  and `requirements.txt` is documentation-only. New assertions extend
  the existing TDAB runner and the zero-dependency property survives.
- **One spec per slice.** Rejected — six documents restating the same
  eight invariants drift apart. One umbrella, six issues, six PRs.

## Risks / what could go wrong

- **The portfolio average creeps back in.** Every stakeholder shown a
  matrix asks for "the one number". *Mitigated* by making I4 a tested
  invariant rather than a convention: an assertion checks that no
  generated report contains an averaged gap or grade.
- **Manifests rot.** Repos get added, renamed and archived; the manifest
  silently narrows the scope. *Mitigated* — the coverage ledger is
  mandatory and appears first in every roll-up, reports over 90 days are
  `stale`, and a ceiling is never claimed as estate-wide under partial
  coverage.
- **Framework drift between command and skill.** Two files, near-identical
  content, six slices of edits. *This is the sharpest risk in the set*,
  and today I3 has no test behind it at all. Slice 1 adds the parity
  assertion; the bodies are currently byte-identical from `## The model
  (embedded)` to EOF except two deliberate words, so the boundary is
  unambiguous.
- **Binding detection produces false negatives** (S2) — a team binds the
  harness in a way the checklist does not recognise and the report
  accuses them of a discipline failure they do not have. *Mitigated* —
  binding findings are always evidence-bearing, and where the checklist
  is *silent* rather than negative the dimension is placed `inferred`,
  not `inherited-unbound`, with an `asked` fallback before asserting
  unbound.
- **Context exhaustion on large estates.** *Mitigated* by sequential
  processing with evidence released between subjects, an explicit
  statement of run size before starting, and roll-up-over-artefacts
  remaining the recommended path at scale.
- **Slice 1's value depends on report parseability**, and every existing
  report predates the summary block. *Mitigated* by the three-tier
  fallback — block, then prose (marked `degraded`), then `unparseable`
  with a re-run instruction in the ledger.
- **The estate becomes the unit of blame.** A matrix across teams invites
  league-table use. *Mitigated* by I8's split ceiling, which exists
  precisely to separate what enablement owes the estate from what a team
  owes itself, and by writing portfolio steers to the estate rather than
  to named teams.

## Adversarial review

**Objection**: Six slices of edits to two files that must stay identical
is a drift machine, and the repo has been running that rule on trust.
*Disposition*: Accepted, and it is the reason the parity assertion is
pulled into Slice 1 rather than left implicit. The measurement was taken
before committing to this: the shared bodies differ by two words today,
so the test is cheap to write and will fail loudly the first time a
slice touches one file and not the other.

**Objection**: The instrument's promise is that it works in one repo with
no setup. A YAML manifest is setup, and it is the thin end of a
configuration wedge.
*Disposition*: Accepted as a real tension, bounded by I2 — with no
manifest, nothing changes for existing users, and the manifest is only
ever required for the multi-repo case it enables. The forward-compatible
validation rule (unknown keys warn, never fail) is there so later slices
extend the schema without breaking manifests written today.

**Objection**: Deferring Example 1 means Slice 1 ships without the real
demonstration the design leans on for credibility.
*Disposition*: Accepted as a genuine cost, tracked as #69. Substituting
a synthetic example was considered and rejected — a tidy fake on the docs
site is worth less than an honest gap, and the whole argument for
Example 1 is that it is real.

**Objection**: `inherited-unbound` (S2) risks telling teams their
governance does not work on the strength of a checklist that cannot see
every binding mechanism.
*Disposition*: Deferred to Slice 2, where it is the central risk; the
silent-versus-negative distinction above is the agreed mitigation and
must be implemented with the feature, not after it.

**Disposition**: Proceed, slice by slice, Slice 1 first.

## Acceptance

Ticked per slice as each PR merges.

- [x] **S1** (#63) — Roll-up produces a portfolio report from existing
      assessments. Summary block emitted by both surfaces. Parity
      assertion live in CI. Coverage ledger, dimension matrix, gap
      table, spread, split ceiling, confidence summary, one steer. No
      averaged gap, grade or percentage anywhere in the output.
      Docs: 1 tutorial, 1 how-to, 3 reference, 1 explanation, nav.
      *Landed: 90 assertions green (72 before). Two spec assumptions
      proved stale on contact and were dropped rather than worked
      around — the terminology rename (already shipped in 0009) and
      registering the new surfaces in `plugin.json` (Claude Code
      auto-discovers `commands/` and `skills/`; there is nothing to
      register). Example 1 deferred to #69.*
- [x] **S2** (#64) — Effective habitat merge with `local` /
      `inherited` / `inherited-unbound` provenance; binding checklist;
      `habitats:` support; `.gitmodules` autodetection that offers a
      manifest and assesses unchanged if declined.
      *Landed: 94 assertions green. The silent-versus-negative
      mitigation is implemented with the feature as the adversarial
      review required, and asserted by R9. Examples 2 and 3 shipped
      synthetic and banner-marked, with R11 asserting the banner.
      Portfolio regime names are deliberately absent from both — they
      are Slice 4, and the examples describe the shape without
      claiming the label.*
- [x] **S3** (#65) — Behavioural questions asked once per team;
      per-subject difference question; reuse declared in the body;
      `posture` excluding archived subjects from the ceiling;
      sequential per-subject context discipline.
      *Landed: 99 assertions green. One addition beyond the slice's
      declared scope — an internal documentation link check — added
      after a mistyped relative link was written and caught by hand.
      mkdocs is not in strict mode here, so that class of bug ships
      silently; the check was verified against the real broken link
      before being kept.*
- [x] **S4** (#66) — Federated / Distributed / Fragmented / Islanded
      named with their evidence; near-duplicate detection reported as
      fragmented-with-lineage; `justified_variance` listed as declared,
      never as drift.
      *Landed: 102 assertions green. Near-duplicate detection requires
      all three signals together — name, overlap and divergence —
      because any two without the third is a coincidence, and a
      consolidation programme started against unrelated files is worse
      than no finding. Where the four inputs disagree the report names
      both regimes rather than forcing a label. R11 was generalised to
      check every example page declares itself synthetic or real,
      which also protects Example 1 (#69) from acquiring the synthetic
      banner.*
- [x] **S5** (#67) — `package`, `org` and `upstream` habitats; org
      habitat never raises a dimension and is listed as declared and
      unverifiable with the action that would make it verifiable;
      partial scope reported as "n of m".
      *Landed: 105 assertions green. The org rule is `inherited-unbound`
      one layer up, with higher stakes: a sibling harness at least has
      an artefact to read, so an unbound rule can be caught. An org
      habitat has none, which is precisely why it must never raise a
      dimension. Coverage is now reported against **named** subjects
      rather than readable ones — the denominator is the claim.*
- [ ] **S6** (#68) — Self-contained HTML portfolio, matrix as
      centrepiece, spread as a distribution, coverage ledger above the
      fold, no gauge or grade.
- [ ] **Example 1** (#69) — the real Habitat-Thinking estate roll-up,
      published whatever it says.

`python3 tests/run.py` passes at the end of every slice.
