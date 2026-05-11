# Model Routing

How the team picks between models per task type. Reviewed quarterly.

## Routing rules

| Task type | Default model | Why | Cost ceiling per run |
|---|---|---|---|
| Implementation (`/spec-implement` body) | Sonnet 4.6 | Cheap, fast, accurate enough on small specs | $0.50 |
| Adversarial review | Sonnet 4.6 | Adversarial pass benefits from a different model than the one that drafted | $0.30 |
| Plan drafting (orchestrator step 2) | Opus 4.7 | Plan quality compounds; worth the cost | $1.50 |
| Skill review (`wordcount-style`) | Haiku 4.5 | Pattern match against rules; cheap and consistent | $0.05 |
| Long-running code refactor | Opus 4.7 (1M context) | Needs whole-repo context | $5.00 |

Exceptions require an entry in `CHOICES.md`.

## Quarterly spend history

| Quarter | Total spend | Notes |
|---|---|---|
| 2025-Q4 | $342 | Baseline. |
| 2026-Q1 | $401 | Adversarial-review runs over budget by 22% — see REFLECTION_LOG.md 2026-05-02 and CHOICES.md C-005. |

## Capture cadence

Costs are captured quarterly via `scripts/cost-capture.sh`. The
governance audit (quarterly) checks for routing-rule drift.
