# Claude Code Example

Use this example when testing the Claude Code adapter locally:

```bash
claude --plugin-dir ../../plugins/swe-harness
```

For marketplace testing:

```bash
claude plugin validate ../..
claude plugin marketplace add ../..
claude plugin install swe-harness@swe-harness
```
