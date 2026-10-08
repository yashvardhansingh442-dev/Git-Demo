# 09 - GitHub Workflow: Issues and Pull Requests

## The problem

Git tracks *what* changed. GitHub's issues and pull requests track *why* it changed and *who agreed to it*. On a team, no change goes straight to `main`: it starts as an issue, gets built on a branch, and lands through a reviewed pull request.

## The workflow

```text
Issue  ->  Branch  ->  Commits  ->  Pull Request  ->  Review  ->  Merge  ->  Issue auto-closes
```

| Step | What I do |
|---|---|
| Issue | Describe the task and the reason for it; add a label |
| Branch | `feature/<name>` from an up-to-date `main` |
| Commits | Small commits with clear messages |
| Pull request | Describe the change; write `Closes #<issue number>` |
| Review | Read my own diff, add comments, wait for checks |
| Merge | Merge the PR, delete the branch |

## Issue vs pull request

| | Issue | Pull request |
|---|---|---|
| Purpose | Track a task, bug or idea | Propose and review a code change |
| Contains | Description, labels, discussion | A branch's commits and diff |
| Closed by | Manually, or by a PR that says `Closes #N` | Merging or closing |

## Merge options on GitHub

| Option | Result | Related topic |
|---|---|---|
| Create a merge commit | Keeps all commits plus a merge commit | [02 - merge](../02-merge-vs-rebase) |
| Squash and merge | All commits become one | [04 - squashing](../04-interactive-rebase) |
| Rebase and merge | Linear history, commits replayed | [02 - rebase](../02-merge-vs-rebase) |

## My real example

I used this workflow to track the remaining topics of this very repository.

**Issue:** `<paste link>` (title: `<paste title>`)

```text
<paste the issue description>
```

**Branch:** `<paste branch name>`

**Pull request:** `<paste link>`

PR description:

```text
<paste PR description, including the "Closes #N" line>
```

**Result:** the issue closed automatically when the PR was merged: `<yes/no, paste screenshot or link>`

## Commands used

```bash
git switch main
git pull origin main
git switch -c feature/<name>
# work and commit
git push -u origin feature/<name>
# open the PR on GitHub, merge it, delete the branch
git switch main
git pull origin main
git branch -d feature/<name>
```

## What I observed

<!-- In your own words: -->
<!-- - What did "Closes #N" do when I merged? -->
<!-- - Why is it better to work through an issue than to commit straight to main? -->
<!-- - Which merge option did I pick, and why? -->

## Notes

<!-- Real things you ran into. -->
