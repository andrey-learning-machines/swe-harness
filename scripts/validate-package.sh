#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python3 scripts/validate-package.py

if command -v claude >/dev/null 2>&1; then
  claude plugin validate . || {
    echo "[WARN] Claude marketplace validation failed"
    exit 1
  }
  claude plugin validate ./plugins/swe-harness || {
    echo "[WARN] Claude plugin validation failed"
    exit 1
  }
else
  echo "[WARN] Claude Code CLI not found; skipped claude plugin validate"
fi

echo "[OK] SWE Harness package validation complete"
