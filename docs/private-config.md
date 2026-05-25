# Private Configuration

Published plugin files must be safe for a public repository.

## Never Commit

- GitHub tokens or personal access tokens
- Cloud credentials or service account keys
- `.env` files with real values
- Claude Code `settings.local.json`
- Codex `auth.json`
- Personal marketplace files
- Telemetry, transcripts, todo state, task state, or cached plugin payloads
- Customer names, internal project names, private repository URLs, or ticket
  links

## Use Placeholders

Use environment-variable placeholders for secrets:

```json
{
  "headers": {
    "Authorization": "{env:GITHUB_TOKEN}"
  }
}
```

## Token Hygiene

Treat tokens like passwords. If a token has been pasted into chat, terminal
history, logs, or a public repository, rotate it after use.

## Release Scan

```bash
./scripts/validate-package.sh
```

The release scan blocks common token prefixes, private keys, local home paths,
and known cache directories.
