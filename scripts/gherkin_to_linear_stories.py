#!/usr/bin/env python3
"""Run the packaged Gherkin-to-Linear story draft generator."""

from __future__ import annotations

import runpy
from pathlib import Path

SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "plugins"
    / "swe-harness"
    / "scripts"
    / "gherkin_to_linear_stories.py"
)

runpy.run_path(str(SCRIPT), run_name="__main__")
