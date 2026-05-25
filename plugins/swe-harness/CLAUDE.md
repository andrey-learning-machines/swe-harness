# SWE Harness

Use this plugin when software work benefits from durable intent, bounded
delegation, deterministic validation, and explicit safety gates.

Core loop:

1. Understand the codebase and active constraints before changing files.
2. Use the smallest suitable skill or specialist agent.
3. Give writable agents explicit ownership boundaries.
4. Require evidence: files changed, tests run, review findings, risks, and
   open questions.
5. Keep private configuration outside committed files.

For multi-agent work, start with the `unicorn-orchestrator` skill. For harness
design, use `harness-improvement`. For Model Context Protocol (MCP) server
work, use `mcp-server-builder`. For Specification Kit (Spec Kit) feature
coverage, use `spec-acceptance-harness` to connect specifications, Gherkin,
Playwright acceptance tests, and `story_matrix.py` route or capability checks.
