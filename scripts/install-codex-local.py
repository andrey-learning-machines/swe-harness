#!/usr/bin/env python3
"""Install the SWE Harness plugin into the local Codex personal marketplace."""

from __future__ import annotations

import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path


PLUGIN_NAME = "swe-harness"

CODEX_AGENT_SKILLS = {
    "ui_frontend_builder": ["ui-ux-pro-max", "frontend-skill"],
    "ui_ux_designer": ["ui-ux-pro-max", "frontend-skill"],
    "unicorn_architect": [
        "spec-acceptance-harness",
        "unicorn-code-reading",
        "unicorn-pattern-transfer",
        "unicorn-technical-debt",
    ],
    "unicorn_developer": [
        "spec-acceptance-harness",
        "unicorn-self-verification",
        "unicorn-testing",
        "unicorn-python",
        "unicorn-javascript",
    ],
    "unicorn_devops": ["unicorn-domain-devops", "unicorn-security"],
    "unicorn_polyglot": [
        "unicorn-language-learning",
        "unicorn-pattern-transfer",
        "unicorn-code-reading",
    ],
    "unicorn_qa_security": [
        "spec-acceptance-harness",
        "unicorn-security",
        "unicorn-testing",
    ],
    "ux_auditor": ["ui-ux-pro-max", "frontend-skill"],
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    if not path.exists():
        return {
            "name": "personal",
            "interface": {"displayName": "Personal"},
            "plugins": [],
        }
    return json.loads(path.read_text())


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n")


def install_plugin() -> Path:
    root = repo_root()
    source = root / "plugins" / PLUGIN_NAME
    target_parent = Path(os.environ.get("SWE_HARNESS_CODEX_PLUGIN_HOME", "~/plugins")).expanduser()
    target = target_parent / PLUGIN_NAME

    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(
        source,
        target,
        ignore=shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc"),
    )
    return target


def resolve_skill(skill_name: str, plugin_path: Path) -> Path | None:
    candidates = [
        Path("~/.codex/skills").expanduser() / skill_name / "SKILL.md",
        Path("~/.agents/skills").expanduser() / skill_name / "SKILL.md",
        plugin_path / "skills" / skill_name / "SKILL.md",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def skill_config_sections(agent_name: str, plugin_path: Path) -> str:
    sections: list[str] = []
    for skill_name in CODEX_AGENT_SKILLS.get(agent_name, []):
        skill_path = resolve_skill(skill_name, plugin_path)
        if not skill_path:
            continue
        sections.extend(
            [
                "[[skills.config]]",
                f"path = {json.dumps(str(skill_path))}",
                "enabled = true",
                "",
            ]
        )
    return "\n".join(sections)


def install_codex_agents(plugin_path: Path) -> tuple[Path, int]:
    target_dir = Path(os.environ.get("SWE_HARNESS_CODEX_AGENTS_HOME", "~/.codex/agents")).expanduser()
    template_dir = repo_root() / "templates" / "codex" / "agents"
    target_dir.mkdir(parents=True, exist_ok=True)

    if os.environ.get("SWE_HARNESS_SKIP_CODEX_AGENTS") == "1":
        return target_dir, 0

    installed = 0
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    for template in sorted(template_dir.glob("*.toml")):
        agent_name = template.stem
        text = template.read_text()
        skills = skill_config_sections(agent_name, plugin_path)
        if skills:
            text = text.rstrip() + "\n\n" + skills
        else:
            text = text.rstrip() + "\n"

        target = target_dir / template.name
        if target.exists() and target.read_text() != text:
            backup = target.with_name(f"{target.stem}.pre-swe-harness-{timestamp}.toml.bak")
            shutil.copy2(target, backup)
        target.write_text(text)
        installed += 1
    return target_dir, installed


def update_marketplace() -> Path:
    marketplace = Path(os.environ.get("SWE_HARNESS_CODEX_MARKETPLACE", "~/.agents/plugins/marketplace.json")).expanduser()
    payload = load_json(marketplace)
    payload.setdefault("name", "personal")
    payload.setdefault("interface", {"displayName": "Personal"})
    payload.setdefault("plugins", [])

    entry = {
        "name": PLUGIN_NAME,
        "source": {"source": "local", "path": f"./plugins/{PLUGIN_NAME}"},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Development",
    }

    plugins = [p for p in payload["plugins"] if p.get("name") != PLUGIN_NAME]
    plugins.append(entry)
    payload["plugins"] = plugins
    write_json(marketplace, payload)
    return marketplace


def main() -> None:
    plugin_path = install_plugin()
    agents_path, agent_count = install_codex_agents(plugin_path)
    marketplace_path = update_marketplace()
    print(f"Installed {PLUGIN_NAME} to {plugin_path}")
    if agent_count:
        print(f"Installed {agent_count} Codex agents to {agents_path}")
    else:
        print(f"Skipped Codex agent install at {agents_path}")
    print(f"Updated Codex marketplace at {marketplace_path}")


if __name__ == "__main__":
    main()
