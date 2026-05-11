# Reflection log

---

## 2026-04-10 — sibling team adopted the habitat plugin

**Surprise**: The team in `documents-service` installed the
`wordcount-habitat` plugin and ran `/wordcount-habitat-init`. By
hour two they had a CLAUDE.md, HARNESS.md skeleton, the
spec-implement command, and a green CI run.

**Lesson**: Packaging the habitat as a plugin works. The "in two
steps" claim survived a real-world test.

**Action**: Promoted "habitat-as-plugin" to a load-bearing choice
in `CHOICES.md`.

---

## 2026-04-28 — governance audit caught a drifted constraint

**Surprise**: The "Spec conformance" constraint had been declared
agent-enforced for six months but the team realised in audit that
no agent had actually been running the check on PRs. Constraint
drift was hidden because no one was looking.

**Lesson**: Declared-but-unrun constraints rot quietly. The
governance audit is doing real work.

**Action**: Spec-conformance check moved into the
`/spec-implement` workflow so it runs every time, not only when
someone remembers. Recorded as a CHOICES.md entry.

---

## 2026-05-02 — model-routing budget overshot for one task type

**Surprise**: Quarterly cost snapshot showed adversarial-review
runs over budget by 22%. The default model was Opus; the routing
table said adversarial review should use Sonnet.

**Lesson**: Routing rules aren't self-enforcing.

**Action**: Added a `MODEL_ROUTING.md` constraint to `HARNESS.md` —
advisory at PR time, audit monthly. CHOICES.md entry added.
