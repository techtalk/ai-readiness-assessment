---
name: spec-implement
description: Take a spec under specs/ and produce an implementation plan, then pause for human-approved adversarial review before writing code. Used as the entry point for spec-first work in this repo.
---

# /spec-implement

Project-local command. Orchestrates the spec-first workflow.

## Usage

```
/spec-implement specs/NNNN-<slug>.md
```

## Process

1. **Read the spec.** Identify the "what", the "why", the acceptance
   criteria, and the explicit "out of scope" boundaries.
2. **Draft the plan.** Write a plan under
   `specs/plans/NNNN-<slug>-plan.md` covering: approach, steps,
   risks, verification.
3. **Pause for adversarial review.** Tell the human: "Plan is at
   `specs/plans/NNNN-<slug>-plan.md`. Walk through the adversarial
   review and record dispositions under
   `docs/objections/NNNN-<slug>.md`. Return here when all
   dispositions are resolved."
4. **Wait for human confirmation** that objections are resolved.
5. **Write the failing test** described in the acceptance criteria.
6. **Confirm the test is red** for the right reason.
7. **Write the minimal production code** to make the test pass.
8. **Run the full test suite** and the linter. Confirm green.
9. **Open the PR**, referencing the spec by path in the PR body.

Do not proceed past step 3 until the human confirms the objection
dispositions are resolved.
