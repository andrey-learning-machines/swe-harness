# Contributing

Thanks for improving SWE Harness.

## Principles

- Keep reusable harness behavior in `plugins/swe-harness/skills/` and
  `plugins/swe-harness/agents/`.
- Keep Codex-specific metadata in `.agents/plugins/` or
  `plugins/swe-harness/.codex-plugin/`.
- Keep Claude Code-specific metadata in `.claude-plugin/` or
  `plugins/swe-harness/.claude-plugin/`.
- Do not commit real local configuration, tokens, transcripts, telemetry, or
  vendor cache payloads.

## Before Opening A Pull Request

```bash
./scripts/validate-package.sh
```

Also run host-specific validation when available:

```bash
claude plugin validate .
claude plugin validate ./plugins/swe-harness
```

## Adding A Skill

1. Add `plugins/swe-harness/skills/<skill-name>/SKILL.md`.
2. Include YAML frontmatter with a clear `description`.
3. Keep long references in a local `references/` directory.
4. Update `catalog/inventory.md` and `catalog/package.meta.json`.
5. Run validation.

## Adding An Agent

1. Add `plugins/swe-harness/agents/<agent-name>.md`.
2. Include `name` and `description` frontmatter.
3. Keep write-capable agents scoped and explicit.
4. Update `catalog/inventory.md` and `catalog/package.meta.json`.
5. Run validation.
