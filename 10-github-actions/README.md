# 10 - GitHub Actions (CI)

## The problem

Humans forget to check things. A CI workflow runs an automatic check on every push and pull request, so problems are caught before they reach `main`. Here the check is a **markdown linter**, because this repository is mostly documentation.

## Key terms

| Term | Meaning |
|---|---|
| Workflow | A YAML file in `.github/workflows/` describing an automated process |
| Trigger (`on`) | The event that starts it, e.g. `push` or `pull_request` |
| Job | A group of steps that runs on one machine |
| Runner | The machine that runs the job (`ubuntu-latest`) |
| Step | One command or reusable action inside a job |

## The workflow

File: `.github/workflows/markdown-lint.yml`

```yaml
name: Markdown Lint

on:
  push:
    branches: [main]
  pull_request:

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Lint markdown files
        run: npx --yes markdownlint-cli2 "**/*.md"
```

Linter settings: `.markdownlint-cli2.jsonc`

```jsonc
{
  "config": {
    "MD013": false,
    "MD033": false,
    "MD041": false
  },
  "ignores": ["LICENSE.md"]
}
```

I turned off line-length (`MD013`), inline HTML (`MD033`) and first-line-heading (`MD041`) because they do not suit these docs.

## What happened

### First run

```text
<paste or describe the result of the first run: passed or failed>
```

If it failed, these were the errors:

```text
<paste the lint errors from the Actions log>
```

### The fix

```text
<describe what I changed to fix each error>
```

### Second run

```text
<paste or describe: passed>
```

Link to the workflow run: `<paste link>`

## What I observed

<!-- In your own words: -->
<!-- - What triggered the workflow? -->
<!-- - What did a failing check look like on the pull request? -->
<!-- - Why is it useful that the check runs before merging, not after? -->

## Notes

<!-- Real things you ran into. -->
