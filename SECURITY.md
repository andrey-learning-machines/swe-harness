# Security Policy

## Supported Versions

The public `main` branch is the supported development line until tagged
releases begin.

## Reporting A Vulnerability

Open a private security advisory on GitHub if the repository owner enables
advisories, or file an issue that avoids publishing exploit details and secrets.

Do not paste access tokens, private keys, customer data, or internal repository
URLs into issues.

## Release Safety Rules

- Never commit real tokens, credentials, cloud project identifiers, or local
  machine paths.
- Publish only placeholder Model Context Protocol (MCP) configuration such as
  `{env:GITHUB_TOKEN}`.
- Do not copy bundled vendor plugins, cached runtime files, transcripts,
  telemetry, screenshots, or personal marketplace state into this repository.
- Run `./scripts/validate-package.sh` before release.
