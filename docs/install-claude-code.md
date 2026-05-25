# Install For Claude Code

## From GitHub

```bash
claude plugin marketplace add andrey-learning-machines/swe-harness
claude plugin install swe-harness@swe-harness
```

## Local Development

```bash
git clone https://github.com/andrey-learning-machines/swe-harness.git
cd swe-harness
claude --plugin-dir ./plugins/swe-harness
```

## Validate

```bash
claude plugin validate .
claude plugin validate ./plugins/swe-harness
```

If Claude Code is not installed, run the repository validator instead:

```bash
./scripts/validate-package.sh
```

## Agent Names

Claude Code loads plugin agents from `plugins/swe-harness/agents/`. Plugin agent
names are namespaced by the plugin when shown in Claude Code.
