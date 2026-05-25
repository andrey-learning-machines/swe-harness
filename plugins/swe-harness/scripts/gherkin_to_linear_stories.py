#!/usr/bin/env python3
"""Generate Linear story drafts from Gherkin feature files."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


SCENARIO_PREFIXES = ("Scenario:", "Scenario Outline:", "Example:")
STEP_PREFIXES = ("Given ", "When ", "Then ", "And ", "But ", "* ")


@dataclass
class Scenario:
    feature_file: Path
    feature: str
    rule: str | None
    title: str
    kind: str
    line: int
    tags: list[str] = field(default_factory=list)
    background: list[str] = field(default_factory=list)
    steps: list[str] = field(default_factory=list)
    examples: list[str] = field(default_factory=list)


def is_feature_file(path: Path) -> bool:
    return path.name.endswith(".feature") or path.name.endswith(".feature.example")


def iter_feature_files(paths: Iterable[Path]) -> Iterable[Path]:
    for path in paths:
        if path.is_dir():
            yield from sorted(candidate for candidate in path.rglob("*") if is_feature_file(candidate))
        elif is_feature_file(path):
            yield path


def parse_feature_file(path: Path) -> list[Scenario]:
    scenarios: list[Scenario] = []
    feature = path.stem.replace("-", " ").replace("_", " ").title()
    feature_tags: list[str] = []
    feature_background: list[str] = []
    rule: str | None = None
    rule_tags: list[str] = []
    rule_background: list[str] = []
    pending_tags: list[str] = []
    current: Scenario | None = None
    background_scope: str | None = None
    in_examples = False

    for line_number, raw_line in enumerate(path.read_text().splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("@"):
            pending_tags.extend(line.split())
            continue
        if line.startswith("Feature:"):
            feature = line.split(":", 1)[1].strip()
            feature_tags = pending_tags
            feature_background = []
            rule = None
            rule_tags = []
            rule_background = []
            pending_tags.clear()
            current = None
            background_scope = None
            in_examples = False
            continue
        if line.startswith("Rule:"):
            rule = line.split(":", 1)[1].strip()
            rule_tags = pending_tags
            rule_background = []
            pending_tags.clear()
            current = None
            background_scope = None
            in_examples = False
            continue
        if line.startswith("Background:"):
            current = None
            background_scope = "rule" if rule else "feature"
            in_examples = False
            continue
        if line.startswith(SCENARIO_PREFIXES):
            kind, title = line.split(":", 1)
            tags = list(dict.fromkeys([*feature_tags, *rule_tags, *pending_tags]))
            current = Scenario(
                feature_file=path,
                feature=feature,
                rule=rule,
                title=title.strip(),
                kind=kind,
                line=line_number,
                tags=tags,
                background=[*feature_background, *rule_background],
            )
            scenarios.append(current)
            pending_tags = []
            background_scope = None
            in_examples = False
            continue
        if background_scope and line.startswith(STEP_PREFIXES):
            if background_scope == "rule":
                rule_background.append(line)
            else:
                feature_background.append(line)
            continue
        if current is None:
            continue
        if line.startswith("Examples:"):
            in_examples = True
            current.examples.append(line)
            continue
        if in_examples:
            current.examples.append(line)
            continue
        if line.startswith(STEP_PREFIXES):
            current.steps.append(line)

    return scenarios


def acceptance_criteria(steps: list[str]) -> list[str]:
    criteria: list[str] = []
    collecting = False
    for step in steps:
        if step.startswith("Then "):
            collecting = True
            criteria.append(step.removeprefix("Then ").strip())
            continue
        if collecting and step.startswith(("And ", "But ", "* ")):
            criteria.append(re.sub(r"^(And|But|\*)\s+", "", step).strip())
        elif step.startswith(("Given ", "When ")):
            collecting = False
    return criteria


def marker_for(scenario: Scenario, root: Path) -> str:
    relative = scenario.feature_file.relative_to(root).as_posix()
    raw = f"{relative}:{scenario.line}:{scenario.feature}:{scenario.rule}:{scenario.title}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def story_statement(scenario: Scenario) -> str:
    return (
        f"As a product user, I want `{scenario.title}` to behave as specified "
        "so the expected outcome is captured and verified."
    )


def build_story(scenario: Scenario, root: Path, project: str, team: str, labels: list[str]) -> dict:
    marker = marker_for(scenario, root)
    relative = scenario.feature_file.relative_to(root).as_posix()
    criteria = acceptance_criteria(scenario.steps)
    title = f"{scenario.feature}: {scenario.title}"
    body_lines = [
        story_statement(scenario),
        "",
        "## Source",
        f"- Feature file: `{relative}`",
        f"- Line: {scenario.line}",
        f"- Feature: {scenario.feature}",
    ]
    if scenario.rule:
        body_lines.append(f"- Rule: {scenario.rule}")
    if scenario.tags:
        body_lines.append(f"- Tags: {' '.join(scenario.tags)}")
    body_lines.extend(["", "## Acceptance Criteria"])
    if criteria:
        body_lines.extend(f"- {item}" for item in criteria)
    else:
        body_lines.append("- Scenario outcome is observable and testable.")
    body_lines.extend(["", "## Gherkin", "```gherkin"])
    if scenario.background:
        body_lines.append("Background:")
        body_lines.extend(f"  {step}" for step in scenario.background)
        body_lines.append("")
    body_lines.append(f"{scenario.kind}: {scenario.title}")
    body_lines.extend(f"  {step}" for step in scenario.steps)
    if scenario.examples:
        body_lines.extend(f"  {line}" for line in scenario.examples)
    body_lines.extend(["```", "", f"<!-- swe-harness:gherkin-story:{marker} -->"])

    return {
        "idempotency_marker": f"swe-harness:gherkin-story:{marker}",
        "source": {
            "feature_file": relative,
            "line": scenario.line,
            "feature": scenario.feature,
            "rule": scenario.rule,
            "scenario": scenario.title,
            "kind": scenario.kind,
            "tags": scenario.tags,
            "background": scenario.background,
        },
        "linear": {
            "team": team,
            "project": project,
            "title": title,
            "labels": labels,
            "description": "\n".join(body_lines),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("features", nargs="+", type=Path)
    parser.add_argument("--project", required=True, help="Target Linear project name")
    parser.add_argument("--team", required=True, help="Target Linear team key or name")
    parser.add_argument("--label", action="append", default=[], help="Linear label to attach")
    parser.add_argument("--output", type=Path, help="Write story drafts to this JSON file")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root")
    args = parser.parse_args()

    root = args.root.resolve()
    scenarios = [
        scenario
        for feature_file in iter_feature_files(path.resolve() for path in args.features)
        for scenario in parse_feature_file(feature_file)
    ]
    stories = [
        build_story(scenario, root, args.project, args.team, args.label)
        for scenario in scenarios
    ]
    payload = {
        "schema": "swe-harness.linear_story_drafts.v1",
        "count": len(stories),
        "stories": stories,
    }
    text = json.dumps(payload, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n")
    else:
        print(text)


if __name__ == "__main__":
    main()
