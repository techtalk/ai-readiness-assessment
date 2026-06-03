# Reflection Log

Post-task reflections captured via `/reflect`. Each entry records what
was done, what surprised the agent, and the signal it carries for future
work. Curators promote durable entries into `AGENTS.md` or `HARNESS.md`
and add a `Promoted` line in the same commit.

---

- **Date**: 2026-06-02
- **Agent**: Claude Code (Opus 4.8)
- **Task**: Hardened the ai-readiness-assessment plugin end to end — made the Agentic Experience 5-Level Habitat Maturity Model the assessment spine (fourteen dimensions; Habitat Build Gap on the fourteen-dimension mean) — and added CI (the TDAB structural suite), required status checks on `main`, GitHub Releases with a changelog-driven release workflow, a PR-time changelog gate, an Apache-2.0 licence, repo metadata (description / topics / homepage), and a Diátaxis MkDocs documentation site on GitHub Pages.
- **Surprise**: The TDAB suite (`tests/run.py`) asserts against the **committed sample assessments** under `tests/fixtures/`, not freshly-generated output — so the model-as-spine rewrite did not break CI until all six fixtures and their `expected.md` were hand-regenerated and `run.py`'s expected gap regimes updated. Two infrastructure gotchas: GitHub blocks required status checks on a **free private** repo (resolved only by making the repo public), and `gh release create --target <short-sha>` returns HTTP 422 for retroactive tags — the robust path is to push real git tags first, then `gh release create --verify-tag`.
- **Proposal**: Add an instrument-change checklist to AGENTS.md — edit `commands/ai-readiness-assess.md` and `skills/ai-readiness-assessment/SKILL.md` identically (dual-surface sync); regenerate the six `tests/fixtures/*/assessments/*.md` and their `expected.md`; update `run.py` expected regimes; then `mkdocs build --strict`. (Human decides; AGENTS.md is human-edited only.)
- **Improvement**: Enforce dual-surface sync in CI so the command and skill cannot silently drift — it was declared as a HARNESS convention but previously unverified.
- **Signal**: workflow
- **Constraint**: Dual-surface sync — command ≡ skill (agent)
- **Promoted**: 2026-06-02 → AGENTS.md WORKFLOWS ("Changing the instrument") + GOTCHAS ("tests assert against committed sample assessments, not live output")
- **Session metadata**:
  - Duration: unknown
  - Model tiers used: unknown
  - Pipeline stages completed: manual (no orchestrator pipeline)
  - Agent delegation: manual

---

- **Date**: 2026-06-03
- **Agent**: Claude Code (Opus 4.8)
- **Task**: Checked whether `HARNESS.md` Context was in step with the repo's actual CI/CD, and updated it.
- **Surprise**: `HARNESS.md` Context > Stack still declared **"Build system: None"** and did not mention CI/CD at all — even though the repo has since grown four GitHub Actions workflows (the TDAB suite, the changelog gate, automated releases, and a MkDocs docs build/deploy), two required status checks, and branch protection on `main`. The harness's own priming had quietly fallen out of step with what CI actually does.
- **Proposal**: none — acted directly (see Promoted).
- **Improvement**: When CI/CD or build tooling changes, update `HARNESS.md` Context > Stack in the same change so the harness's priming never trails the pipeline. A periodic GC check ("Context names the workflows that exist in `.github/workflows/`") could catch this automatically if it recurs.
- **Signal**: context
- **Constraint**: none
- **Promoted**: 2026-06-03 → HARNESS.md Context > Stack: added a CI/CD entry (GitHub Actions pipeline) and clarified the build-system note
- **Session metadata**:
  - Duration: unknown
  - Model tiers used: unknown
  - Pipeline stages completed: manual (no orchestrator pipeline)
  - Agent delegation: manual

---

- **Date**: 2026-06-03
- **Agent**: Claude Code (Opus 4.8)
- **Task**: Acted on the repo's own self-assessment — installed an enforced spec-first discipline (a `specs/` layer, the Spec-first constraint + a required CI gate, an adversarial-review disposition, specs 0001–0003) — then re-assessed and published the L3→L4 progression as an example.
- **Surprise**: Lifting **one** discipline (spec-first) to L4 made the repo *less* coherent, not more. The cognitive read crossed L3→L4, but the Habitat Build Gap flipped from **+0.2 (Coherent)** to **+1.1 (Ambition outpaces enablement)** because the operational habitat (Testing, Observability, Agent composition — still L2) did not move with it. A targeted "level up" created a new, healthy-to-address imbalance — the instrument's own thesis (coherence > level) demonstrated on itself. Separately: the new required gates had to be **scoped to not fire on each other** — the spec-first gate ignores non-instrument PRs, and the onboarding gate compares the HARNESS *body* (not the Status block) so `/harness-sync` PRs pass.
- **Proposal**: Add to AGENTS.md ARCH_DECISIONS that a single-dimension level jump can flip the Habitat Build Gap to "ambition outpaces enablement" — lift the operational habitat *alongside* the discipline, or expect (and name) a temporary positive gap. Also note the multi-gate scoping pattern (gates must exclude Status-only / non-instrument PRs so they don't block sync).
- **Improvement**: When deliberately chasing a level jump, check the projected gap regime first — a discipline-only jump trades coherence for level unless the lagging operational dimensions are lifted too.
- **Signal**: workflow
- **Constraint**: none
- **Session metadata**:
  - Duration: unknown
  - Model tiers used: unknown
  - Pipeline stages completed: manual (no orchestrator pipeline)
  - Agent delegation: manual
