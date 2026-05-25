---
name: mcp-server-builder
description: Use when designing, implementing, deploying, or reviewing Model Context Protocol (MCP) servers, especially remote HTTP MCP servers, tool schemas, write-capable tools, connector metadata, authentication, authorization, prompt-injection defenses, audit logging, deployment smoke tests, or quality assurance for MCP integrations.
---

# MCP Server Builder

## Overview

Use this skill to build Model Context Protocol (MCP) servers that are predictable for language models, safe for users, and easy to test. Prefer small, purpose-built tools with strict schemas, explicit metadata, server-side authorization, and clear quality gates.

## Workflow

1. Define the trust boundary.
   - Identify the MCP client, MCP server, downstream systems, secrets, network path, and deployment environment.
   - Choose the narrowest authority that can complete the user workflow.
   - For data writes, route through the owning service or application programming interface (API) rather than bypassing service boundaries.

2. Design the tool surface.
   - Use intent-based names like `ped.populate_table_from_spreadsheet`.
   - Keep each tool focused on one job.
   - Write descriptions that say when to use the tool, when not to use it, what it changes, and what each parameter means.
   - Use strict JSON Schema: required fields, enums for allowed values, formats, limits, and `additionalProperties: false`.
   - Return `structuredContent` that conforms to `outputSchema`, plus a concise text summary for compatibility.
   - For write tools, set annotations honestly: `readOnlyHint: false`, `destructiveHint` based on overwrite behavior, `openWorldHint` based on external publication, and `idempotentHint` when repeat calls are safe.

3. Make writes safe by construction.
   - Prefer validate or dry-run flows before commit flows.
   - Require idempotency keys for create/update operations.
   - Allow create and update only through explicit allowlists of resources and fields.
   - Do not expose delete, raw query, arbitrary table, arbitrary endpoint, shell, or pass-through tools unless the user explicitly asks and a security review approves it.
   - Require human confirmation for irreversible operations and server-side checks even when the client also asks for confirmation.

4. Implement the protocol cleanly.
   - Support `initialize`, `tools/list`, and `tools/call` at minimum.
   - For hosted servers, prefer Streamable HTTP on a single endpoint such as `/mcp`; Server-Sent Events (SSE) is acceptable when the client requires it.
   - Validate request shape, tool name, arguments, authentication, authorization, origin, and size before executing business logic.
   - Use timeouts and bounded retries for downstream calls.
   - Redact secrets and personally identifiable information from logs.

5. Verify before shipping.
   - Unit-test tool handlers directly.
   - Test JSON Schema rejection cases, not only happy paths.
   - Run a local MCP client or inspector against `tools/list` and representative `tools/call` requests.
   - Run deployed smoke tests over HTTPS.
   - Replay a golden prompt set: direct prompts, indirect prompts, and negative prompts where the tool should not be selected.

## Read When Needed

- `references/tool-design.md`: Use while drafting or reviewing tool names, descriptions, schemas, annotations, and outputs.
- `references/qa-security.md`: Use before enabling a write-capable MCP server, deploying externally, or connecting an agent to production-like data.

## Done Criteria

An MCP server is ready only when the code, deployment, and seed/configuration agree on:

- exact tool names and endpoint URL
- authentication and authorization mechanism
- allowed resources and fields
- dry-run versus commit behavior
- audit logging and correlation identifiers
- automated tests and deployed smoke-test evidence
- rollback or disable path for the MCP server or connector
