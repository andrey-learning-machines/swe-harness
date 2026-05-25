# Tool Design Reference

Use this when an MCP server exposes tools to a language model.

## Naming

- Prefer `domain.action_object` names.
- Keep names stable once clients depend on them.
- Avoid generic names like `write`, `sync`, `run`, or `execute`.
- Avoid verbs that imply broader power than the tool has.

## Description Template

Use this shape for every tool description:

```text
Use this when [specific user intent]. It [specific action] against [specific system or resource].
Do not use it for [negative cases]. It can [create/update/read] only [allowed scope].
Parameter notes: [important field semantics, limits, formats, idempotency behavior].
Operational notes: [dry-run behavior, confirmation, audit, latency, downstream dependency].
```

## Schema Rules

- Top-level type is `object`.
- Set `additionalProperties: false`.
- Use `enum` for resource names, modes, statuses, and constrained actions.
- Use `minLength`, `maxLength`, `minimum`, `maximum`, and `format` where useful.
- Keep file inputs explicit: URL, uploaded file token, or base64 payload with size limits.
- Use arrays with `minItems` and `maxItems`.
- Prefer field mappings over raw table or column names for user-supplied spreadsheets.

## Write Tool Rules

- Include `dry_run` or `commit` behavior. Default to validation when possible.
- Require `idempotency_key` for calls that create or update records.
- Require an operator-visible reason such as `change_reason`.
- Return counts, validation issues, accepted rows, rejected rows, and changed record identifiers.
- Never accept raw database statements, arbitrary endpoint URLs, or arbitrary table names.
- If bulk writes are supported, process rows through the same validation path as single writes.

## Output Rules

Return structured content with:

- `status`: `validated`, `applied`, or `rejected`
- `summary`
- `target_resource`
- `created_count`
- `updated_count`
- `rejected_count`
- `record_ids`
- `validation_errors`
- `correlation_id`

Also include a short text content block summarizing the result for clients that do not consume structured content.
