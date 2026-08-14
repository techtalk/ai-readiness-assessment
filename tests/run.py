#!/usr/bin/env python3
"""
TDAB assertion runner for the ai-readiness-assessment plugin.

Reads each fixture's most recent assessment under
tests/fixtures/<fixture>/assessments/ and runs the A-tier
(structural) assertions encoded below.

Behavioural (B) and semantic (C) assertions are *not* run by this
script — those need an interactive Claude session or an LLM judge.

Exit code: 0 if every assertion passes; 1 if any A-tier assertion
fails; 2 on usage / file-not-found errors.

Usage:
    python tests/run.py                      # all fixtures
    python tests/run.py --fixture level-3-habitat
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "tests" / "fixtures"
REPORT_PATH = ROOT / "tests" / "auto-results.md"


# ---------------------------------------------------------------------------
# Result type and assertion helpers
# ---------------------------------------------------------------------------


@dataclass
class Result:
    id: str
    status: str  # "PASS" | "FAIL" | "N/A"
    evidence: str


def passing(aid: str, evidence: str = "") -> Result:
    return Result(aid, "PASS", evidence)


def failing(aid: str, evidence: str) -> Result:
    return Result(aid, "FAIL", evidence)


def na(aid: str, evidence: str) -> Result:
    return Result(aid, "N/A", evidence)


def latest_assessment(fixture: Path) -> Path | None:
    candidates = sorted((fixture / "assessments").glob("*-assessment.md"))
    return candidates[-1] if candidates else None


def section(text: str, heading: str) -> str | None:
    """Return the body of a markdown section by heading, or None."""
    pattern = re.compile(
        rf"^{re.escape(heading)}\s*\n(.*?)(?=^##\s|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(text)
    return m.group(1) if m else None


def discipline_scores(text: str) -> dict[str, int] | None:
    """Parse the Discipline Maturity table. Return {name: score} or None."""
    body = section(text, "## Discipline Maturity")
    if body is None:
        return None
    scores: dict[str, int] = {}
    for row in re.finditer(
        r"\|\s*(Context Engineering|Architectural Constraints|Guardrail Design)"
        r"\s*\|\s*(\d)\s*\|",
        body,
    ):
        scores[row.group(1)] = int(row.group(2))
    return scores if len(scores) == 3 else None


def count_cta_paragraphs(text: str) -> int:
    """Count blockquote-CTA paragraphs in the section that carries the CTA.

    A CTA paragraph is a contiguous run of '> ' lines. Each contiguous
    run counts as one CTA.

    Since spec 0008 the call to action lives in '## Assessment Review'
    and '## Next Steps' explains without selling. Reports written before
    that split carry the CTA inside '## Next Steps', so fall back to it —
    one assertion covers both shapes, and a report that puts a CTA in
    both sections still counts two and fails.
    """
    body = "\n\n".join(
        s or ""
        for s in (
            section(text, "## Assessment Review"),
            section(text, "## Next Steps"),
        )
    )
    if not body:
        return 0
    runs = re.findall(r"(?:^>.*\n)+", body, re.MULTILINE)
    return len(runs)


# ---------------------------------------------------------------------------
# Per-fixture assertion lists
#
# Each entry: a callable that takes (text, fixture_path) and returns a
# Result. Kept as tuples (id, lambda) for readability.
# ---------------------------------------------------------------------------


def common_a1_a8(level_line: str, absences: list[str]):
    """Return assertion callables for the assertions common to every
    fixture (A1, A2, A4, A8). Other A-tier checks vary per fixture."""

    def a1(text: str, fixture: Path) -> Result:
        a = latest_assessment(fixture)
        if a and a.stat().st_size > 0:
            return passing("A1", f"{a.relative_to(ROOT)} present, non-empty")
        return failing("A1", "no assessment file found")

    def a2(text: str, fixture: Path) -> Result:
        if level_line in text:
            return passing("A2", f"found: {level_line!r}")
        return failing("A2", f"expected level line not found: {level_line!r}")

    def a4(text: str, fixture: Path) -> Result:
        body = section(text, "## Habitat Document Discovery") or text
        missing = [a for a in absences if a not in body and a not in text]
        if not missing:
            return passing("A4", f"all {len(absences)} required absences recorded")
        return failing("A4", f"missing from discovery: {missing}")

    def a8(text: str, fixture: Path) -> Result:
        if "https://leanpub.com/thesovereignengineer" in text:
            return passing("A8", "Leanpub link present")
        return failing("A8", "Leanpub link missing")

    return [("A1", a1), ("A2", a2), ("A4", a4), ("A8", a8)]


def a3_discovery_first():
    def check(text: str, fixture: Path) -> Result:
        d = text.find("## Habitat Document Discovery")
        a = text.find("## Level Assessment")
        if d == -1 or a == -1:
            return failing("A3", "discovery or level-assessment section missing")
        if d < a:
            return passing("A3", "discovery precedes level assessment")
        return failing("A3", "discovery does not precede level assessment")

    return ("A3", check)


def a6_discipline_scores(bounds: dict[str, tuple[int, int]]):
    """bounds: {discipline_name: (min_inclusive, max_inclusive)}."""

    def check(text: str, fixture: Path) -> Result:
        scores = discipline_scores(text)
        if scores is None:
            return failing("A6", "could not parse Discipline Maturity table")
        out_of_bounds = []
        for name, (lo, hi) in bounds.items():
            s = scores.get(name)
            if s is None or s < lo or s > hi:
                out_of_bounds.append(f"{name}={s} (want {lo}-{hi})")
        if not out_of_bounds:
            return passing("A6", f"scores within bounds: {scores}")
        return failing("A6", "; ".join(out_of_bounds))

    return ("A6", check)


def a7_reading_path(must_contain: list[str]):
    def check(text: str, fixture: Path) -> Result:
        body = section(text, "## Reading Path")
        if body is None:
            return failing("A7", "no Reading Path section")
        missing = [m for m in must_contain if m not in body]
        if not missing:
            return passing("A7", f"reading path contains {must_contain}")
        return failing("A7", f"missing from reading path: {missing}")

    return ("A7", check)


def a9_single_cta():
    def check(text: str, fixture: Path) -> Result:
        n = count_cta_paragraphs(text)
        if n == 1:
            return passing("A9", "exactly one CTA paragraph")
        return failing("A9", f"found {n} CTA paragraphs (want 1)")

    return ("A9", check)


def a3a_discovery_cites(required: list[str], aid: str = "A3"):
    """Discovery section must name each of the given paths/markers."""

    def check(text: str, fixture: Path) -> Result:
        body = section(text, "## Habitat Document Discovery") or text
        missing = [r for r in required if r not in body and r not in text]
        if not missing:
            return passing(aid, f"discovery cites all {len(required)} required items")
        return failing(aid, f"discovery missing: {missing}")

    return (aid, check)


def a10_cta_mentions(any_of: list[str]):
    def check(text: str, fixture: Path) -> Result:
        body = section(text, "## Next Steps") or text
        hits = [s for s in any_of if s.lower() in body.lower()]
        if hits:
            return passing("A10", f"CTA mentions {hits}")
        return failing("A10", f"CTA mentions none of {any_of}")

    return ("A10", check)


def a12_operational_axes():
    """Operational Axes (Part D) section present and names all four axes."""

    def check(text: str, fixture: Path) -> Result:
        body = section(text, "## Operational Axes (Part D)")
        if body is None:
            return failing("A12", "no Operational Axes (Part D) section")
        axes = ["Composition", "Testing", "Observability", "Governance"]
        missing = [a for a in axes if a not in body]
        if missing:
            return failing("A12", f"axes missing from Operational Axes table: {missing}")
        return passing("A12", "Operational Axes section names all four axes")

    return ("A12", check)


def a13_build_gap(regime: str):
    """Habitat/Workflow Gap present — the scannable header line, the section,
    and the expected interpretation regime for this fixture."""

    def check(text: str, fixture: Path) -> Result:
        if "## Habitat/Workflow Gap" not in text:
            return failing("A13", "no Habitat/Workflow Gap section")
        if "**Habitat/Workflow Gap**:" not in text:
            return failing("A13", "no scannable **Habitat/Workflow Gap** header line")
        if regime not in text:
            return failing("A13", f"expected regime not found: {regime!r}")
        return passing("A13", f"Habitat/Workflow Gap present with regime {regime!r}")

    return ("A13", check)


# The full Agentic Experience 5-Level Habitat Maturity Model profile.
# A12 already covers the four headline axes; A14 confirms the other ten
# model dimensions are present too, so the assessment evaluates against
# the whole model rather than just the headline four.
_PROFILE_DIMENSIONS = [
    "Agent behaviour", "Agent input", "Workflow", "Operating model",
    "Teams provide", "Output role", "Output artefact", "Humans review",
    "Work patterns", "Agents",  # "Agents…" — matched on the prefix to dodge the ellipsis char
]


def a14_maturity_profile():
    """Habitat Maturity Profile section present and naming the full model —
    the ten non-headline dimensions plus a Habitat Maturity Level read."""

    def check(text: str, fixture: Path) -> Result:
        # Locate by heading prefix — the heading carries a parenthetical
        # ("## Habitat Maturity Profile (Agentic Experience ...)"), so an
        # exact-heading match won't do.
        m = re.search(r"^## Habitat Maturity Profile.*?$", text, re.MULTILINE)
        if m is None:
            return failing("A14", "no Habitat Maturity Profile section")
        rest = text[m.end():]
        nxt = re.search(r"^##\s", rest, re.MULTILINE)
        body = rest[: nxt.start()] if nxt else rest
        missing = [d for d in _PROFILE_DIMENSIONS if d not in body]
        if missing:
            return failing("A14", f"profile missing dimensions: {missing}")
        if "Habitat Maturity Level" not in body:
            return failing("A14", "profile has no Habitat Maturity Level read")
        return passing("A14", "full 14-dimension model profile present")

    return ("A14", check)


# ---------------------------------------------------------------------------
# Assessment summary block (spec 0011, Slice 1)
#
# Every per-unit report ends with a machine-readable summary block. It is
# the thing that makes a roll-up possible without re-running an
# assessment, so its structure is asserted rather than trusted — a
# malformed block silently degrades every portfolio report built on it.
# ---------------------------------------------------------------------------

SUMMARY_BLOCK_RE = re.compile(r"```yaml assessment-summary\n(.*?)\n```", re.DOTALL)

# The model's fourteen dimensions in the block's key form, ordered to
# match the Habitat Maturity Profile table rather than alphabetically, so
# a reader can diff block against prose line by line.
SUMMARY_DIMENSIONS = [
    "agent_behaviour", "agent_input", "workflow", "operating_model",
    "teams_provide", "output_role", "output_artefact", "humans_review",
    "work_patterns", "agent_composition", "agents_do", "testing",
    "observability", "governance",
]

SUMMARY_SCALARS = [
    "schema", "subject", "team", "habitat", "posture", "assessed_at",
    "tool_version", "habitat_maturity_mean", "habitat_maturity_level",
    "cognitive_level", "cognitive_source", "gap", "regime",
    "ceiling_dimensions", "weakest_discipline",
]

# Invariant I6: a cognitive read gathered against the team's general
# practice and applied here must say so. `subject` means it was asked
# about this subject specifically.
VALID_COGNITIVE_SOURCE = {"team", "subject"}

# A dead repository must not pin the portfolio ceiling forever.
VALID_POSTURE = {"active", "maintenance", "archived"}

# Invariant I5: every placement carries how it was arrived at, and
# — from Slice 2 — where the evidence for it lives.
VALID_CONFIDENCE = {"observed", "inferred", "asked"}

# `inherited` means the shared habitat supplies it *and* it demonstrably
# reaches this subject. `inherited-unbound` means the shared habitat
# declares it and nothing here executes or enforces it.
VALID_PROVENANCE = {"local", "inherited", "inherited-unbound"}

# Prose regime wording -> block slug.
REGIME_SLUGS = {
    "Coherent": "coherent",
    "Ambition outpaces enablement": "ambition-outpaces-enablement",
    "Inherited habitat": "inherited-habitat",
}


def summary_block(text: str) -> str | None:
    m = SUMMARY_BLOCK_RE.search(text)
    return m.group(1) if m else None


def summary_dimension_rows(block: str) -> dict[str, dict]:
    """Parse `key: { level: N, confidence: c, provenance: p }` rows.

    `provenance` is captured optionally so the parser can report its
    absence as a finding rather than failing to match the row at all —
    a row that silently does not parse looks identical to a missing
    dimension, which is a much less useful failure message.
    """
    rows: dict[str, dict] = {}
    for m in re.finditer(
        r"^\s*(\w+):\s*\{\s*level:\s*(\d)\s*,\s*confidence:\s*([\w-]+)\s*"
        r"(?:,\s*provenance:\s*([\w-]+)\s*)?\}",
        block,
        re.MULTILINE,
    ):
        rows[m.group(1)] = {
            "level": int(m.group(2)),
            "confidence": m.group(3),
            "provenance": m.group(4),
        }
    return rows


def block_scalar(block: str, key: str) -> str | None:
    m = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", block, re.MULTILINE)
    return m.group(1) if m else None


def a15_summary_block():
    """The report ends with a complete summary block.

    'Ends with' is load-bearing: the roll-up reads the block as the last
    element, so anything appended after it means a report the roll-up
    will misparse.
    """

    def check(text: str, fixture: Path) -> Result:
        m = SUMMARY_BLOCK_RE.search(text)
        if m is None:
            return failing("A15", "no ```yaml assessment-summary block")
        if text[m.end():].strip():
            return failing(
                "A15",
                f"summary block is not the last element; "
                f"{len(text[m.end():].strip())} chars follow it",
            )
        block = m.group(1)
        rows = summary_dimension_rows(block)
        missing = [d for d in SUMMARY_DIMENSIONS if d not in rows]
        if missing:
            return failing("A15", f"block missing dimensions: {missing}")
        bad = {
            d: r["confidence"]
            for d, r in rows.items()
            if r["confidence"] not in VALID_CONFIDENCE
        }
        if bad:
            return failing("A15", f"invalid confidence values: {bad}")
        no_prov = sorted(d for d, r in rows.items() if r["provenance"] is None)
        if no_prov:
            return failing("A15", f"dimensions without provenance: {no_prov}")
        bad_prov = {
            d: r["provenance"]
            for d, r in rows.items()
            if r["provenance"] not in VALID_PROVENANCE
        }
        if bad_prov:
            return failing("A15", f"invalid provenance values: {bad_prov}")
        absent = [k for k in SUMMARY_SCALARS if block_scalar(block, k) is None]
        if absent:
            return failing("A15", f"block missing keys: {absent}")
        for key, allowed in (
            ("cognitive_source", VALID_COGNITIVE_SOURCE),
            ("posture", VALID_POSTURE),
        ):
            value = block_scalar(block, key)
            if value not in allowed:
                return failing("A15", f"{key} is {value!r}, expected one of {sorted(allowed)}")
        return passing("A15", f"summary block complete ({len(rows)} dimensions)")

    return ("A15", check)


def a16_block_agrees_with_prose():
    """The block is generated from the placements the prose reports,
    never computed separately. If the two disagree, one of them is lying
    to whoever reads it — and the roll-up only ever sees the block."""

    def check(text: str, fixture: Path) -> Result:
        block = summary_block(text)
        if block is None:
            return failing("A16", "no summary block to compare against prose")
        problems: list[str] = []

        prose_level = re.search(
            r"\*\*Habitat Maturity Level\*\*:\s*Level\s*(\d)", text
        )
        blk_level = block_scalar(block, "habitat_maturity_level")
        if prose_level and blk_level and prose_level.group(1) != blk_level:
            problems.append(
                f"habitat_maturity_level: prose L{prose_level.group(1)} "
                f"vs block {blk_level}"
            )

        prose_cog = re.search(r"Cognitive read \(Parts A–C\):\s*L(\d)", text)
        blk_cog = block_scalar(block, "cognitive_level")
        if prose_cog and blk_cog and prose_cog.group(1) != blk_cog:
            problems.append(
                f"cognitive_level: prose L{prose_cog.group(1)} vs block {blk_cog}"
            )

        # The regime may carry a qualifier — "Inherited habitat (floor
        # baseline)" — so match on the regime prefix, not equality, or
        # the check silently passes on the fixtures that use one.
        prose_regime = re.search(
            r"\*\*Habitat/Workflow Gap\*\*:\s*[-+][\d.]+\s*\((.+)\)", text
        )
        blk_regime = block_scalar(block, "regime")
        if prose_regime and blk_regime:
            stated = prose_regime.group(1).strip()
            named = next((r for r in REGIME_SLUGS if stated.startswith(r)), None)
            if named is None:
                problems.append(f"prose regime {stated!r} names no known regime")
            elif REGIME_SLUGS[named] != blk_regime:
                problems.append(f"regime: prose {stated!r} vs block {blk_regime!r}")

        if problems:
            return failing("A16", "; ".join(problems))
        return passing(
            "A16", "block agrees with prose on maturity level, cognitive read, regime"
        )

    return ("A16", check)


def universal_assertions():
    """Assertions that hold for every fixture regardless of its level.

    Kept separate from the per-fixture sets so a new report-wide rule is
    added once rather than six times.
    """
    return [a15_summary_block(), a16_block_agrees_with_prose()]


# ---------------------------------------------------------------------------
# Per-fixture assertion sets
# ---------------------------------------------------------------------------


def level_0_assertions() -> list:
    common = common_a1_a8(
        level_line="**Assessed level**: Level 0 — Aware of the landscape",
        absences=[
            "CLAUDE.md", "AGENTS.md", ".github/copilot-instructions.md",
            ".cursorrules", ".windsurfrules", "HARNESS.md",
            "CONSTRAINTS.md", "specs/", "REFLECTION_LOG.md",
            ".github/workflows/",
        ],
    )
    return common + [
        a3_discovery_first(),
        a6_discipline_scores({
            "Context Engineering": (0, 1),
            "Architectural Constraints": (0, 1),
            "Guardrail Design": (0, 1),
        }),
        a7_reading_path(["Act I"]),
        a12_operational_axes(),
        a13_build_gap("Inherited habitat"),
        a14_maturity_profile(),
        a9_single_cta(),
        a10_cta_mentions(["Context Engineering", "habitat-document", "CLAUDE.md"]),
    ]


def level_1_assertions() -> list:
    common = common_a1_a8(
        level_line="**Assessed level**: Level 1 — Communicating through prompts",
        absences=[
            "CLAUDE.md", "AGENTS.md", "HARNESS.md", "specs/",
            "REFLECTION_LOG.md", ".github/workflows/",
            ".pre-commit-config.yaml",
        ],
    )
    return common + [
        a3a_discovery_cites([".cursorrules"]),
        a6_discipline_scores({
            "Context Engineering": (1, 1),
            "Architectural Constraints": (0, 1),
            "Guardrail Design": (0, 1),
        }),
        a7_reading_path(["Level 1", "Level 2"]),
        a12_operational_axes(),
        a13_build_gap("Coherent"),
        a14_maturity_profile(),
        a9_single_cta(),
        a10_cta_mentions([
            "Architectural Constraints", "Guardrail Design",
            "harness-engineering", "CI enforcement",
        ]),
    ]


def level_2_assertions() -> list:
    common = common_a1_a8(
        level_line="**Assessed level**: Level 2 — Verification discipline",
        absences=[
            "CLAUDE.md", "AGENTS.md", "HARNESS.md", "specs/",
            "REFLECTION_LOG.md", "docs/adr/",
        ],
    )
    return common + [
        a3a_discovery_cites([
            ".cursorrules", ".github/workflows/ci.yml",
            "tests/test_main.py", ".pre-commit-config.yaml",
        ]),
        a6_discipline_scores({
            "Context Engineering": (0, 1),
            "Architectural Constraints": (2, 4),
            "Guardrail Design": (2, 4),
        }),
        a7_reading_path(["Level 3"]),
        a12_operational_axes(),
        # 14-dim mean (1.86) sits close to L2 cognition → Coherent
        a13_build_gap("Coherent"),
        a14_maturity_profile(),
        a9_single_cta(),
        a10_cta_mentions(["Context Engineering", "habitat-document", "CLAUDE.md"]),
    ]


def level_3_assertions() -> list:
    common = common_a1_a8(
        level_line="**Assessed level**: Level 3 — Habitat design",
        absences=["specs/", "rfcs/"],
    )
    return common + [
        a3a_discovery_cites([
            "CLAUDE.md", "HARNESS.md", "REFLECTION_LOG.md",
            "ONBOARDING.md", "docs/adr/0001-python-3-10-minimum.md",
            "skills/wordcount-style/SKILL.md",
        ]),
        a6_discipline_scores({
            "Context Engineering": (3, 4),
            "Architectural Constraints": (3, 4),
            "Guardrail Design": (3, 4),
        }),
        a7_reading_path(["Level 4"]),
        a12_operational_axes(),
        a13_build_gap("Ambition outpaces enablement"),
        a14_maturity_profile(),
        a9_single_cta(),
        a10_cta_mentions([
            "specification", "spec-first", "specs/", "spec layer",
            "intent first-class",
        ]),
    ]


def level_4_assertions() -> list:
    common = common_a1_a8(
        level_line="**Assessed level**: Level 4 — Specification-led",
        absences=[
            ".claude-plugin/plugin.json", "MODEL_ROUTING.md", "CHOICES.md",
            "audits/", "fitness",
        ],
    )
    return common + [
        a3a_discovery_cites([
            "specs/0001-newline-handling.md", "specs/0002-empty-input.md",
            "specs/plans/0001-newline-handling-plan.md",
            "docs/objections/0001-newline-handling.md",
            "commands/spec-implement.md", "CONTRIBUTING.md",
        ]),
        a6_discipline_scores({
            "Context Engineering": (3, 4),
            "Architectural Constraints": (3, 4),
            "Guardrail Design": (3, 4),
        }),
        a7_reading_path(["Level 5"]),
        a12_operational_axes(),
        # 14-dim mean (3.64) sits close to L4 cognition → Coherent
        a13_build_gap("Coherent"),
        a14_maturity_profile(),
        a9_single_cta(),
        a10_cta_mentions([
            "platform-engineering", "published plugin", "governance audit",
            "fitness functions", "cross-team",
        ]),
    ]


def level_5_assertions() -> list:
    common = common_a1_a8(
        level_line="**Assessed level**: Level 5 — Sovereign engineering",
        absences=[],
    )
    return common + [
        a3a_discovery_cites([
            ".claude-plugin/plugin.json",
            "commands/wordcount-habitat-init.md",
            "MODEL_ROUTING.md", "CHOICES.md", "audits/2026-Q1.md",
        ]),
        a6_discipline_scores({
            "Context Engineering": (4, 5),
            "Architectural Constraints": (4, 5),
            "Guardrail Design": (4, 5),
        }),
        a7_reading_path(["Enchiridion"]),
        a12_operational_axes(),
        a13_build_gap("Ambition outpaces enablement"),
        a14_maturity_profile(),
        a9_single_cta(),
        a10_cta_mentions([
            "sustaining", "portfolio", "cross-team", "maintenance playbook",
            "top of",
        ]),
    ]


CHECKERS = {
    "level-0-blank": level_0_assertions,
    "level-1-thin-rules": level_1_assertions,
    "level-2-verified": level_2_assertions,
    "level-3-habitat": level_3_assertions,
    "level-4-specs": level_4_assertions,
    "level-5-sovereign": level_5_assertions,
}


# ---------------------------------------------------------------------------
# Repo-level (instrument) assertions — spec 0011
#
# These examine the instrument itself rather than a generated report, so
# they run once rather than once per fixture.
# ---------------------------------------------------------------------------

COMMAND_FILE = ROOT / "commands" / "ai-readiness-assess.md"
SKILL_FILE = ROOT / "skills" / "ai-readiness-assessment" / "SKILL.md"
ROLLUP_COMMAND = ROOT / "commands" / "ai-readiness-rollup.md"
ROLLUP_SKILL = ROOT / "skills" / "ai-readiness-rollup" / "SKILL.md"

# Invariant I3: framework content is identical across both surfaces from
# this heading to end of file. Everything above it is surface-specific
# framing (the command's invocation line, the skill's "when to use").
PARITY_ANCHOR = "## The model (embedded)"

# The only sanctioned divergence: each surface names itself. Both
# phrasings fold to a neutral token before comparison, so any *other*
# difference fails. Adding an entry here is a deliberate act — it widens
# the hole in I3 and should be argued for in the PR that does it.
PARITY_VARIANCES = [
    ("This command is fully", "This instrument is fully"),
    ("the standalone command does not create files",
     "the standalone skill does not create files"),
]

# The roll-up pair's shared body is written without self-reference, so
# it needs no variance allowance — the stricter position, chosen while
# the surfaces were new enough to make it free.
ROLLUP_PARITY_ANCHOR = "## What a roll-up is"

# Invariant I4: the roll-up never reduces the estate to one number.
PORTFOLIO_SCORE_SMELLS = [
    "average gap", "averaged gap", "mean gap", "portfolio score",
    "overall score", "portfolio grade", "overall grade",
    "portfolio percentage",
]

MULTI_REPO_DOCS = [
    "docs/reference/scope-manifest.md",
    "docs/reference/assessment-summary-block.md",
    "docs/reference/portfolio-report.md",
    "docs/explanation/why-no-portfolio-score.md",
    "docs/how-to/write-a-scope-manifest.md",
    "docs/tutorials/roll-up-existing-assessments.md",
]

SLICE2_DOCS = [
    "docs/how-to/assess-repos-with-a-shared-harness.md",
    "docs/reference/provenance-and-binding.md",
    "docs/explanation/distribution-is-not-federation.md",
    "docs/examples/parent-repo-submodules.md",
    "docs/examples/separate-harness-partially-bound.md",
]

# The six ways a shared habitat can demonstrably reach a subject. A
# finding of `inherited-unbound` is only answerable if the report can say
# what was looked for, so these must appear in both surfaces verbatim.
BINDING_SIGNALS = [
    "CI configuration",
    "Hook / plugin configuration",
    "Submodule pin",
    "Package/lockfile pin",
    "Convention file references",
    "Shadowing",
]

SLICE3_DOCS = [
    "docs/tutorials/assess-a-team-across-repositories.md",
    "docs/how-to/assess-a-monorepo-with-several-habitats.md",
    "docs/explanation/subject-habitat-team.md",
]

SLICE4_DOCS = [
    "docs/reference/portfolio-regimes.md",
    "docs/explanation/extract-or-bind.md",
    "docs/examples/fragmented-estate.md",
]

SYNTHETIC_BANNER = (
    "Synthetic example — constructed to illustrate the report shape."
)

# A real example states which repositories were read and when. Example 1
# (#69) will use this; it must never wear the synthetic banner.
REAL_EXAMPLE_MARKER = "Real assessment —"

# The four portfolio regimes: a second axis parallel to the gap regimes,
# read the same way — a regime, never a score.
PORTFOLIO_REGIMES = ["Federated", "Distributed", "Fragmented", "Islanded"]

SLICE5_DOCS = [
    "docs/how-to/assess-with-an-org-level-habitat.md",
    "docs/how-to/assess-across-a-client-boundary.md",
]

# Habitat that cannot be read from any subject checkout.
HABITAT_KINDS_BEYOND_CHECKOUT = ["package", "org", "upstream"]

# The exact phrasing an org habitat gets in a report. An org rule that
# silently raised a dimension would be `inherited-unbound`'s failure
# mode one layer up — and unlike a sibling repo, there is nothing to
# read to catch it.
ORG_HONESTY_MARKER = "declared, unverifiable from here"


def parity_body(path: Path, anchor: str, variances: list) -> str | None:
    """The framework half of a surface file, normalised for comparison."""
    if not path.is_file():
        return None
    text = path.read_text()
    i = text.find(anchor)
    if i == -1:
        return None
    body = text[i:]
    for command_phrasing, skill_phrasing in variances:
        body = body.replace(command_phrasing, "<surface>")
        body = body.replace(skill_phrasing, "<surface>")
    return body


def check_parity(
    aid: str, command: Path, skill: Path, anchor: str, variances: list
) -> Result:
    """Compare a command/skill pair, reporting the first divergent line.

    Naming the line matters more than reporting a boolean: the failure a
    contributor sees should point at the edit that broke it.
    """
    a = parity_body(command, anchor, variances)
    b = parity_body(skill, anchor, variances)
    if a is None or b is None:
        which = [p.name for p, v in ((command, a), (skill, b)) if v is None]
        return failing(aid, f"parity anchor {anchor!r} missing from: {which}")
    if a == b:
        return passing(aid, f"framework bodies identical from {anchor!r}")
    al, bl = a.splitlines(), b.splitlines()
    for n, (x, y) in enumerate(zip(al, bl), start=1):
        if x != y:
            return failing(
                aid,
                f"surfaces diverge at framework line {n} — "
                f"command: {x.strip()[:50]!r} / skill: {y.strip()[:50]!r}",
            )
    return failing(
        aid,
        f"framework bodies differ in length: "
        f"command {len(al)} lines, skill {len(bl)} lines",
    )


def r1_command_skill_parity() -> Result:
    """I3 — both entry points must produce the same assessment."""
    return check_parity("R1", COMMAND_FILE, SKILL_FILE, PARITY_ANCHOR, PARITY_VARIANCES)


def r6_rollup_parity() -> Result:
    """I3 applied to the roll-up pair. Its shared body carries no
    self-reference at all, so unlike R1 it tolerates no variance."""
    return check_parity(
        "R6", ROLLUP_COMMAND, ROLLUP_SKILL, ROLLUP_PARITY_ANCHOR, []
    )


def r2_surfaces_specify_summary_block() -> Result:
    """Both surfaces must instruct the agent to emit the summary block,
    or the two entry points produce reports the roll-up treats
    differently — which is I3 failing by another route."""
    missing = [
        label
        for label, path in (("command", COMMAND_FILE), ("skill", SKILL_FILE))
        if not path.is_file() or "assessment-summary" not in path.read_text()
    ]
    if missing:
        return failing("R2", f"surfaces not specifying the summary block: {missing}")
    return passing("R2", "both surfaces specify the assessment-summary block")


def r3_rollup_surfaces_exist() -> Result:
    missing = [
        str(p.relative_to(ROOT))
        for p in (ROLLUP_COMMAND, ROLLUP_SKILL)
        if not p.is_file()
    ]
    if missing:
        return failing("R3", f"missing roll-up surfaces: {missing}")
    return passing("R3", "roll-up command and skill both present")


def r4_no_portfolio_score() -> Result:
    """I4 — the invariant most likely to erode, because every stakeholder
    shown a matrix asks for the one number. Checked two ways: the rule is
    stated, and no score language appears except as a prohibition."""
    if not ROLLUP_SKILL.is_file():
        return failing("R4", "roll-up skill absent; cannot check I4")
    text = ROLLUP_SKILL.read_text().lower()
    if "no portfolio score" not in text:
        return failing("R4", "roll-up skill does not state the no-portfolio-score rule")
    negations = ("never", "no ", "not ", "without", "refuse")
    offenders = [
        line.strip()[:70]
        for line in text.splitlines()
        for smell in PORTFOLIO_SCORE_SMELLS
        if smell in line and not any(neg in line for neg in negations)
    ]
    if offenders:
        return failing(
            "R4", f"score language not framed as prohibition: {offenders[:2]}"
        )
    return passing("R4", "I4 stated; no unguarded portfolio-score language")


def r7_effective_habitat_specified() -> Result:
    """Both surfaces must describe the shared-plus-local merge and all
    three provenance values, or the two entry points disagree about what
    an inherited placement even means."""
    needed = ["effective habitat", *sorted(VALID_PROVENANCE)]
    problems = []
    for label, path in (("command", COMMAND_FILE), ("skill", SKILL_FILE)):
        text = path.read_text().lower() if path.is_file() else ""
        missing = [n for n in needed if n.lower() not in text]
        if missing:
            problems.append(f"{label}: {missing}")
    if problems:
        return failing("R7", f"effective-habitat vocabulary missing — {problems}")
    return passing("R7", "both surfaces specify the merge and all three provenance values")


def r8_binding_checklist_present() -> Result:
    """The binding evidence checklist is what makes an `inherited-unbound`
    finding answerable — it tells a team what was looked for."""
    problems = []
    for label, path in (("command", COMMAND_FILE), ("skill", SKILL_FILE)):
        text = path.read_text() if path.is_file() else ""
        missing = [s for s in BINDING_SIGNALS if s not in text]
        if missing:
            problems.append(f"{label}: {missing}")
    if problems:
        return failing("R8", f"binding signals missing — {problems}")
    return passing("R8", f"all {len(BINDING_SIGNALS)} binding signals in both surfaces")


def r9_silent_is_not_negative() -> Result:
    """The agreed mitigation for the slice's central risk: a checklist
    that is silent about a binding mechanism must not be read as proof
    that none exists. Without this the instrument accuses teams of
    discipline failures they do not have."""
    problems = [
        label
        for label, path in (("command", COMMAND_FILE), ("skill", SKILL_FILE))
        if not path.is_file()
        or "silent rather than negative" not in path.read_text()
    ]
    if problems:
        return failing(
            "R9", f"silent-vs-negative mitigation not stated in: {problems}"
        )
    return passing("R9", "silent-vs-negative mitigation stated in both surfaces")


def r11_examples_declare_provenance() -> Result:
    """Nothing on the docs site should be ambiguous about whether it is a
    real reading.

    Checked over every example page rather than a fixed list, so a new
    example cannot be added without declaring itself. Both directions
    matter: a synthetic example that reads as real overstates the
    instrument, and a real one wearing the synthetic banner throws away
    the credibility that made it worth publishing.
    """
    examples = sorted((ROOT / "docs" / "examples").glob("*.md"))
    if not examples:
        return failing("R11", "no example pages found under docs/examples/")
    undeclared = [
        str(p.relative_to(ROOT))
        for p in examples
        if not any(m in p.read_text() for m in (SYNTHETIC_BANNER, REAL_EXAMPLE_MARKER))
    ]
    if undeclared:
        return failing("R11", f"example pages not declaring synthetic or real: {undeclared}")
    return passing("R11", f"all {len(examples)} example pages declare their provenance")


def r12_scope_run_specified() -> Result:
    """Both surfaces must describe the single-session run identically —
    the invocation, the one cheap difference question, and the two
    cognitive_source values."""
    needed = ["--scope", "cognitive_source", "materially different"]
    problems = []
    for label, path in (("command", COMMAND_FILE), ("skill", SKILL_FILE)):
        text = path.read_text() if path.is_file() else ""
        missing = [n for n in needed if n not in text]
        if missing:
            problems.append(f"{label}: {missing}")
    if problems:
        return failing("R12", f"scope-run vocabulary missing — {problems}")
    return passing("R12", "both surfaces specify the single-session scope run")


def r13_posture_handled() -> Result:
    """A dead repository must not pin the portfolio ceiling forever, so
    the roll-up has to know what each posture means for the ceiling."""
    problems = []
    for label, path in (("command", ROLLUP_COMMAND), ("skill", ROLLUP_SKILL)):
        text = path.read_text() if path.is_file() else ""
        missing = [p for p in sorted(VALID_POSTURE) if p not in text]
        if missing:
            problems.append(f"roll-up {label}: {missing}")
    if problems:
        return failing("R13", f"posture values missing — {problems}")
    return passing("R13", "roll-up surfaces handle all three postures")


def r14_reuse_is_declared() -> Result:
    """I6 — a reused cognitive read is declared in the body, not a
    footnote. Silent reuse is a lie about evidence."""
    marker = "the team's general practice"
    problems = [
        label
        for label, path in (("command", COMMAND_FILE), ("skill", SKILL_FILE))
        if not path.is_file() or marker not in path.read_text()
    ]
    if problems:
        return failing("R14", f"reuse-declaration wording missing from: {problems}")
    return passing("R14", "both surfaces require reuse to be declared in the body")


def r15_context_discipline_stated() -> Result:
    """The scope run must process subjects sequentially and say how many
    it will do, rather than degrading silently on a large estate."""
    problems = [
        label
        for label, path in (("command", COMMAND_FILE), ("skill", SKILL_FILE))
        if not path.is_file()
        or "one subject's raw evidence" not in path.read_text()
    ]
    if problems:
        return failing("R15", f"context-budget discipline not stated in: {problems}")
    return passing("R15", "sequential context discipline stated in both surfaces")


def r17_portfolio_regimes_named() -> Result:
    """All four regimes must be in both roll-up surfaces, or the two
    entry points classify the same estate differently."""
    problems = []
    for label, path in (("command", ROLLUP_COMMAND), ("skill", ROLLUP_SKILL)):
        text = path.read_text() if path.is_file() else ""
        missing = [r for r in PORTFOLIO_REGIMES if r not in text]
        if missing:
            problems.append(f"roll-up {label}: {missing}")
    if problems:
        return failing("R17", f"portfolio regimes missing — {problems}")
    return passing("R17", f"all {len(PORTFOLIO_REGIMES)} portfolio regimes in both surfaces")


def r18_regime_claims_carry_evidence() -> Result:
    """A regime is a claim about an estate, and an unevidenced one is
    indistinguishable from a guess. The report must state the provenance
    counts and the spread that produced the classification."""
    marker = "never assert a regime without"
    problems = [
        label
        for label, path in (("command", ROLLUP_COMMAND), ("skill", ROLLUP_SKILL))
        if not path.is_file() or marker not in path.read_text().lower()
    ]
    if problems:
        return failing("R18", f"regime evidence rule missing from roll-up: {problems}")
    return passing("R18", "regime claims must carry their evidence in both surfaces")


def r19_justified_variance_handled() -> Result:
    """Declared variance is listed as declared — never as drift, and
    never silently dropped. A polyglot estate where testing genuinely
    cannot be uniform must not be nagged toward false convergence."""
    problems = [
        label
        for label, path in (("command", ROLLUP_COMMAND), ("skill", ROLLUP_SKILL))
        if not path.is_file() or "justified_variance" not in path.read_text()
    ]
    if problems:
        return failing("R19", f"justified_variance not handled in roll-up: {problems}")
    return passing("R19", "justified_variance handled in both roll-up surfaces")


def r20_habitat_kinds_beyond_checkout() -> Result:
    """Both assessment surfaces must know the three kinds of habitat that
    cannot be read from a subject checkout."""
    problems = []
    for label, path in (("command", COMMAND_FILE), ("skill", SKILL_FILE)):
        text = path.read_text() if path.is_file() else ""
        missing = [k for k in HABITAT_KINDS_BEYOND_CHECKOUT if f"`{k}`" not in text]
        if missing:
            problems.append(f"{label}: {missing}")
    if problems:
        return failing("R20", f"habitat kinds missing — {problems}")
    return passing("R20", "package, org and upstream kinds in both surfaces")


def r21_org_habitat_never_raises() -> Result:
    """The slice's central honesty requirement.

    An org habitat cannot be read from any subject, so there is nothing
    to check it against — which makes it the easiest thing in the whole
    instrument to silently take credit for. It must be reported as
    declared and unverifiable, with the action that would make it
    verifiable named.
    """
    problems = []
    for label, path in (("command", COMMAND_FILE), ("skill", SKILL_FILE)):
        text = path.read_text() if path.is_file() else ""
        missing = []
        if ORG_HONESTY_MARKER not in text:
            missing.append(f"{ORG_HONESTY_MARKER!r}")
        if "never raise" not in text.lower():
            missing.append("the never-raise rule")
        if missing:
            problems.append(f"{label}: {missing}")
    if problems:
        return failing("R21", f"org honesty rule incomplete — {problems}")
    return passing("R21", "org habitats are declared-and-unverifiable in both surfaces")


def r22_partial_scope_reported() -> Result:
    """Never silently narrow the scope to whatever happened to be
    readable. A client boundary is a normal condition; hiding it turns a
    partial reading into a false claim about an estate."""
    problems = [
        label
        for label, path in (("command", ROLLUP_COMMAND), ("skill", ROLLUP_SKILL))
        if not path.is_file()
        or "named subjects" not in path.read_text()
    ]
    if problems:
        return failing("R22", f"partial-scope reporting missing from roll-up: {problems}")
    return passing("R22", "partial scope reported against named subjects, not readable ones")


def r16_internal_doc_links_resolve() -> Result:
    """Every relative markdown link in docs/ points at a file that exists.

    mkdocs is not run in strict mode, so a mistyped internal link builds
    and deploys silently — the page renders, the link 404s, and nobody
    notices until a reader does. Cheap to check, so checked.
    """
    docs = ROOT / "docs"
    link_re = re.compile(r"\[[^\]]*\]\(([^)#?]+?)(?:#[^)]*)?\)")
    broken: list[str] = []
    for page in sorted(docs.rglob("*.md")):
        for target in link_re.findall(page.read_text()):
            target = target.strip()
            if not target or "://" in target or target.startswith(("mailto:", "/")):
                continue
            if not (page.parent / target).resolve().exists():
                broken.append(f"{page.relative_to(ROOT)} -> {target}")
    if broken:
        return failing("R16", f"broken internal links: {broken[:4]}")
    return passing("R16", "every relative docs link resolves")


def r5_multi_repo_docs_present() -> Result:
    pages = MULTI_REPO_DOCS + SLICE2_DOCS + SLICE3_DOCS + SLICE4_DOCS + SLICE5_DOCS
    missing = [d for d in pages if not (ROOT / d).is_file()]
    if missing:
        return failing("R5", f"missing docs pages: {missing}")
    return passing("R5", f"all {len(pages)} multi-repo docs pages present")


REPO_GROUP = "instrument (repo-level)"

REPO_CHECKS = [
    ("R1", r1_command_skill_parity),
    ("R2", r2_surfaces_specify_summary_block),
    ("R3", r3_rollup_surfaces_exist),
    ("R4", r4_no_portfolio_score),
    ("R5", r5_multi_repo_docs_present),
    ("R6", r6_rollup_parity),
    ("R7", r7_effective_habitat_specified),
    ("R8", r8_binding_checklist_present),
    ("R9", r9_silent_is_not_negative),
    ("R11", r11_examples_declare_provenance),
    ("R12", r12_scope_run_specified),
    ("R13", r13_posture_handled),
    ("R14", r14_reuse_is_declared),
    ("R15", r15_context_discipline_stated),
    ("R16", r16_internal_doc_links_resolve),
    ("R17", r17_portfolio_regimes_named),
    ("R18", r18_regime_claims_carry_evidence),
    ("R19", r19_justified_variance_handled),
    ("R20", r20_habitat_kinds_beyond_checkout),
    ("R21", r21_org_habitat_never_raises),
    ("R22", r22_partial_scope_reported),
]


def run_repo_checks() -> list[Result]:
    results: list[Result] = []
    for rid, fn in REPO_CHECKS:
        try:
            results.append(fn())
        except Exception as exc:  # noqa: BLE001 — test runner must not crash
            results.append(failing(rid, f"assertion raised: {exc!r}"))
    return results


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


def run_fixture(name: str) -> list[Result]:
    fixture = FIXTURES / name
    if not fixture.is_dir():
        return [failing("RUNNER", f"fixture directory not found: {fixture}")]
    asmnt = latest_assessment(fixture)
    if asmnt is None:
        return [failing("A1", "no assessment file under assessments/")]
    text = asmnt.read_text()
    results: list[Result] = []
    for _aid, fn in CHECKERS[name]() + universal_assertions():
        try:
            results.append(fn(text, fixture))
        except Exception as exc:  # noqa: BLE001 — test runner must not crash
            results.append(failing(_aid, f"assertion raised: {exc!r}"))
    return results


def write_report(all_results: dict[str, list[Result]]) -> None:
    lines = ["# Automated A-tier results", ""]
    lines.append(f"Runner: `tests/run.py` (structural assertions only).")
    lines.append("")
    total_p = total_f = 0
    for name, results in all_results.items():
        lines.append(f"## `{name}`")
        lines.append("")
        lines.append("| ID | Status | Evidence |")
        lines.append("|---|---|---|")
        for r in results:
            lines.append(f"| {r.id} | {r.status} | {r.evidence} |")
            if r.status == "PASS":
                total_p += 1
            elif r.status == "FAIL":
                total_f += 1
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"**Total: {total_p} PASS, {total_f} FAIL.**")
    lines.append("")
    lines.append(
        "B-tier (behavioural) and C-tier (semantic) assertions are not "
        "run by this script. See each fixture's `expected.md` and the "
        "manual test-run summary at `tests/test-run-<date>.md`."
    )
    REPORT_PATH.write_text("\n".join(lines) + "\n")


def print_summary(all_results: dict[str, list[Result]]) -> tuple[int, int]:
    total_p = total_f = 0
    for name, results in all_results.items():
        passed = sum(1 for r in results if r.status == "PASS")
        failed = sum(1 for r in results if r.status == "FAIL")
        marker = "✓" if failed == 0 else "✗"
        print(f"  {marker} {name}: {passed} PASS, {failed} FAIL")
        for r in results:
            if r.status == "FAIL":
                print(f"      [{r.id}] {r.evidence}")
        total_p += passed
        total_f += failed
    print()
    print(f"  Total: {total_p} PASS, {total_f} FAIL")
    return total_p, total_f


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fixture",
        choices=sorted(CHECKERS.keys()),
        help="run a single fixture (default: all)",
    )
    args = parser.parse_args()

    targets = [args.fixture] if args.fixture else sorted(CHECKERS.keys())
    print(f"Running {len(targets)} fixture(s)...")
    print()

    all_results: dict[str, list[Result]] = {}
    for name in targets:
        all_results[name] = run_fixture(name)

    # Repo-level checks examine the instrument, not a report, so they run
    # only on a full sweep — a single-fixture run is a debugging aid.
    if not args.fixture:
        all_results[REPO_GROUP] = run_repo_checks()

    _p, f = print_summary(all_results)
    write_report(all_results)
    print(f"\n  Report written to {REPORT_PATH.relative_to(ROOT)}")

    return 0 if f == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
