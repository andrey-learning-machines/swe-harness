# Harness Inventory

This inventory records what was packaged and what was intentionally excluded.

## Included Skills

- `adk-agent-engine`
- `adk-vertex-genai`
- `frontend-skill`
- `gherkin`
- `harness-improvement`
- `linear-gherkin-stories`
- `mcp-server-builder`
- `playwright`
- `spec-acceptance-harness`
- `ui-ux-pro-max`
- `unicorn-code-reading`
- `unicorn-domain-devops`
- `unicorn-estimation`
- `unicorn-javascript`
- `unicorn-language-learning`
- `unicorn-orchestrator`
- `unicorn-pattern-transfer`
- `unicorn-python`
- `unicorn-security`
- `unicorn-self-verification`
- `unicorn-technical-debt`
- `unicorn-testing`

## Included Agents

- `unicorn_architect`
- `unicorn_developer`
- `unicorn_qa_security`
- `unicorn_devops`
- `unicorn_polyglot`
- `ui_ux_designer`
- `ui_frontend_builder`
- `ux_auditor`

## Included Codex Agent Templates

- `templates/codex/agents/unicorn_architect.toml`
- `templates/codex/agents/unicorn_developer.toml`
- `templates/codex/agents/unicorn_qa_security.toml`
- `templates/codex/agents/unicorn_devops.toml`
- `templates/codex/agents/unicorn_polyglot.toml`
- `templates/codex/agents/ui_ux_designer.toml`
- `templates/codex/agents/ui_frontend_builder.toml`
- `templates/codex/agents/ux_auditor.toml`

## Excluded Assets

- Codex system skills from `~/.codex/skills/.system`
- Codex plugin cache payloads from `~/.codex/plugins/cache`
- Claude Code installed plugin cache payloads from `~/.claude/plugins/data`
- Claude task, plan, todo, telemetry, authentication, and local settings files
- Personal marketplace files from the user home directory
- Any real GitHub, cloud, service, or application tokens
