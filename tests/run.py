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
    """Count blockquote-CTA paragraphs in the Next Steps section.

    A CTA paragraph is a contiguous run of '> ' lines. Each contiguous
    run counts as one CTA.
    """
    body = section(text, "## Next Steps")
    if body is None:
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
    """Habitat Build Gap present — the scannable header line, the section,
    and the expected interpretation regime for this fixture."""

    def check(text: str, fixture: Path) -> Result:
        if "## Habitat Build Gap" not in text:
            return failing("A13", "no Habitat Build Gap section")
        if "**Habitat Build Gap**:" not in text:
            return failing("A13", "no scannable **Habitat Build Gap** header line")
        if regime not in text:
            return failing("A13", f"expected regime not found: {regime!r}")
        return passing("A13", f"Habitat Build Gap present with regime {regime!r}")

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
    for _aid, fn in CHECKERS[name]():
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

    _p, f = print_summary(all_results)
    write_report(all_results)
    print(f"\n  Report written to {REPORT_PATH.relative_to(ROOT)}")

    return 0 if f == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
