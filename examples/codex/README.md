# Codex Example

Use this example when testing the Codex adapter locally:

```bash
../../scripts/install-codex-local.py
```

Then enable the `swe-harness` plugin from your Codex plugin interface.

The installer also writes the Codex custom-agent TOML files to
`~/.codex/agents/`. Use `SWE_HARNESS_SKIP_CODEX_AGENTS=1` when you only want to
test plugin marketplace installation.
