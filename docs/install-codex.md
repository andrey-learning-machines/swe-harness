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
