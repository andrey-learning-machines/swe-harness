#!/usr/bin/env python3
"""Install the SWE Harness plugin into the local Codex personal marketplace."""

from __future__ import annotations

import json
import os
import shutil
from pathlib import Path


PLUGIN_NAME = "swe-harness"


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
    marketplace_path = update_marketplace()
    print(f"Installed {PLUGIN_NAME} to {plugin_path}")
    print(f"Updated Codex marketplace at {marketplace_path}")


if __name__ == "__main__":
    main()
