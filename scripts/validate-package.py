#!/usr/bin/env python3
"""Validate the SWE Harness public package before release."""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "swe-harness"

SECRET_PATTERNS = [
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"gho_[A-Za-z0-9_]{20,}"),
    re.compile(r"ghu_[A-Za-z0-9_]{20,}"),
    re.compile(r"ghs_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"AIza[0-9A-Za-z_-]{20,}"),
    re.compile(r"lin_api_[A-Za-z0-9]{20,}", re.IGNORECASE),
    re.compile(
        r"LINEAR_API_KEY[^\S\r\n]*=[^\S\r\n]*(?!$|<|\{env:|\$\{)[^\s\"']+",
        re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        r"Authorization\"?\s*:\s*\"Bearer\s+(?!\{env:|<|\$\{)[^\"]+\"",
        re.IGNORECASE,
    ),
    re.compile(r"refresh[_-]?token\"?\s*[:=]\s*\"?[A-Za-z0-9._~+/=-]{20,}", re.IGNORECASE),
    re.compile(r"access[_-]?token\"?\s*[:=]\s*\"?[A-Za-z0-9._~+/=-]{20,}", re.IGNORECASE),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
]

PRIVATE_PATTERNS = [
    re.compile(r"/Users/"),
    re.compile(r"openai-bundled"),
    re.compile(r"openai-curated"),
    re.compile(r"openai-primary-runtime"),
]

FORBIDDEN_PATH_PARTS = {
    ".mcp-auth",
    ".linear",
}

PRIVATE_PATTERNS.extend(
    re.compile(re.escape(term.strip()), re.IGNORECASE)
    for term in os.environ.get("SWE_HARNESS_PRIVATE_TERMS", "").split(",")
    if term.strip()
)

TEXT_SUFFIXES = {
    ".json",
    ".md",
    ".py",
    ".sh",
    ".txt",
    ".toml",
    ".yaml",
    ".yml",
    ".csv",
    ".env",
    ".example",
}

PRIVATE_SCAN_ALLOWLIST = {
    "ATTRIBUTION.md",
    "scripts/validate-package.py",
}


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def ok(message: str) -> None:
    print(f"[OK] {message}")


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in {path}: {exc}")


def validate_json_files() -> None:
    for path in [
        ROOT / ".agents/plugins/marketplace.json",
        ROOT / ".claude-plugin/marketplace.json",
        PLUGIN / ".codex-plugin/plugin.json",
        PLUGIN / ".claude-plugin/plugin.json",
        ROOT / "catalog/package.meta.json",
    ]:
        read_json(path)
    ok("JSON files parse")


def validate_manifests() -> None:
    codex = read_json(PLUGIN / ".codex-plugin/plugin.json")
    claude = read_json(PLUGIN / ".claude-plugin/plugin.json")
    for manifest in [codex, claude]:
        for key in ["name", "version", "description", "author", "license"]:
            if key not in manifest:
                fail(f"{manifest.get('name', '<unknown>')} missing {key}")
        if manifest["name"] != "swe-harness":
            fail("Plugin manifest name must be swe-harness")
    if codex.get("skills") != "./skills/":
        fail("Codex manifest must point skills to ./skills/")
    ok("Plugin manifests have required fields")


def validate_marketplaces() -> None:
    codex = read_json(ROOT / ".agents/plugins/marketplace.json")
    claude = read_json(ROOT / ".claude-plugin/marketplace.json")
    if not any(p.get("name") == "swe-harness" for p in codex.get("plugins", [])):
        fail("Codex marketplace missing swe-harness")
    if not any(p.get("name") == "swe-harness" for p in claude.get("plugins", [])):
        fail("Claude marketplace missing swe-harness")
    ok("Marketplace files include swe-harness")


def validate_skills() -> None:
    skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    if len(skills) < 22:
        fail(f"Expected at least 22 skills, found {len(skills)}")
    for skill in skills:
        text = skill.read_text()
        if not text.startswith("---"):
            fail(f"{skill} missing frontmatter")
        if "description:" not in text.split("---", 2)[1]:
            fail(f"{skill} missing description in frontmatter")
    ok(f"Validated {len(skills)} skills")


def validate_agents() -> None:
    agents = sorted((PLUGIN / "agents").glob("*.md"))
    if len(agents) < 8:
        fail(f"Expected at least 8 agents, found {len(agents)}")
    for agent in agents:
        text = agent.read_text()
        if not text.startswith("---"):
            fail(f"{agent} missing frontmatter")
        header = text.split("---", 2)[1]
        for key in ["name:", "description:"]:
            if key not in header:
                fail(f"{agent} missing {key}")
    ok(f"Validated {len(agents)} agents")


def is_text_candidate(path: Path) -> bool:
    if path.name in {".DS_Store"}:
        return False
    if path.suffix in TEXT_SUFFIXES:
        return True
    if ".example" in path.name:
        return True
    return False


def scan_patterns(patterns: list[re.Pattern[str]], label: str, allowlist: set[str] | None = None) -> None:
    findings: list[str] = []
    allowlist = allowlist or set()
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or not is_text_candidate(path):
            continue
        relative = path.relative_to(ROOT).as_posix()
        if relative in allowlist:
            continue
        text = path.read_text(errors="ignore")
        for pattern in patterns:
            if pattern.search(text):
                findings.append(f"{relative} :: {pattern.pattern}")
    if findings:
        print(f"[FAIL] {label} scan found:")
        for finding in findings:
            print(f"  - {finding}")
        raise SystemExit(1)
    ok(f"{label} scan clean")


def validate_forbidden_paths() -> None:
    findings = [
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if ".git" not in path.parts and any(part in FORBIDDEN_PATH_PARTS for part in path.parts)
    ]
    if findings:
        print("[FAIL] forbidden local state paths found:")
        for finding in findings:
            print(f"  - {finding}")
        raise SystemExit(1)
    ok("forbidden local state path scan clean")


def main() -> None:
    validate_json_files()
    validate_manifests()
    validate_marketplaces()
    validate_skills()
    validate_agents()
    scan_patterns(SECRET_PATTERNS, "secret")
    scan_patterns(PRIVATE_PATTERNS, "private path/cache", PRIVATE_SCAN_ALLOWLIST)
    validate_forbidden_paths()


if __name__ == "__main__":
    main()
