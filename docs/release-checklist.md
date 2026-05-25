# Release Checklist

Use this before tagging or publishing a marketplace update.

## Required Checks

- [ ] `./scripts/validate-package.sh` passes.
- [ ] Codex plugin manifest validates with the current Codex tooling, if
      available.
- [ ] Claude Code marketplace validation passes.
- [ ] `ATTRIBUTION.md`, `NOTICE`, and `catalog/third-party-sources.yml` are
      current.
- [ ] No local paths, private repository URLs, customer names, internal project
      names, screenshots with private data, or task transcripts are present.
- [ ] No files from Codex or Claude Code vendor cache directories are included.
- [ ] No MCP OAuth state, `.mcp-auth/`, token-bearing local config, Linear
      workspace links, or private Linear story drafts are included.
- [ ] Any new Model Context Protocol (MCP) example uses placeholders only.
- [ ] Codex custom-agent templates use OpenAI model identifiers, not Claude
      model aliases.
- [ ] README install commands match the published repository owner and name.

## Version Bump

Update all of these together:

- `plugins/swe-harness/.codex-plugin/plugin.json`
- `plugins/swe-harness/.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`
- `catalog/package.meta.json`
- `catalog/inventory.md`
- `README.md`
- `docs/model-routing.md`, when the model matrix changes

## Smoke Tests

```bash
tmp=$(mktemp -d)
SWE_HARNESS_CODEX_PLUGIN_HOME="$tmp/plugins" \
SWE_HARNESS_CODEX_MARKETPLACE="$tmp/marketplace.json" \
  ./scripts/install-codex-local.py
python3 -m json.tool "$tmp/marketplace.json" >/dev/null
rm -rf "$tmp"
```

```bash
claude --plugin-dir ./plugins/swe-harness
```
