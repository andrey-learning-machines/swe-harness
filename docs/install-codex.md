# Install For Codex

## Local Install

```bash
git clone https://github.com/andrey-learning-machines/swe-harness.git
cd swe-harness
./scripts/install-codex-local.py
```

The installer copies the plugin to:

```text
~/plugins/swe-harness
```

Then it creates or updates:

```text
~/.agents/plugins/marketplace.json
```

with a sanitized `swe-harness` entry.

It also installs Codex custom agents to:

```text
~/.codex/agents
```

Those agents use OpenAI model identifiers. Existing differing agent files are
backed up with a `.pre-swe-harness-<timestamp>.toml.bak` suffix before they are
replaced.

To skip custom-agent installation:

```bash
SWE_HARNESS_SKIP_CODEX_AGENTS=1 ./scripts/install-codex-local.py
```

See `docs/model-routing.md` for the model matrix and fallback policy.

## Repository Marketplace

The repository also includes:

```text
.agents/plugins/marketplace.json
```

Use it as the source of truth for team or project marketplace metadata.

## Validate

```bash
./scripts/validate-package.sh
```

If your Codex environment provides a plugin validator, also validate:

```bash
plugins/swe-harness/.codex-plugin/plugin.json
```
