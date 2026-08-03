# Git Mastery

![Git](https://img.shields.io/badge/Git-Advanced-orange)
![GitHub](https://img.shields.io/badge/GitHub-Workflow-black)
![License](https://img.shields.io/badge/License-MIT-blue)
![Status](https://img.shields.io/badge/Status-In_Progress-green)

A hands-on collection of real-world Git and GitHub workflows — the kind used day-to-day on a real engineering team, not just a list of commands.

Every folder below documents a specific workflow: what problem it solves, the exact commands used, a real before/after example (including an actual merge conflict I hit and resolved), and the reasoning behind the approach.

## Why this repo exists

Most "Git practice" repos show that someone can commit and push. This one is meant to show *understanding* — knowing which workflow to reach for and why, not just which commands exist.

## Who this repository is for

- Students learning Git beyond the basics
- Developers preparing for interviews
- Anyone transitioning from solo projects to team workflows
- Anyone who wants worked examples instead of isolated commands

## Covered Topics

| Folder | Topic | What it demonstrates |
|---|---|---|
| [01-branching-strategy](./01-branching-strategy) | Branching | Feature/bugfix/release branch naming and structure |
| [02-merge-vs-rebase](./02-merge-vs-rebase) | Merge vs Rebase | When to use each, and how history differs |
| [03-merge-conflict-resolution](./03-merge-conflict-resolution) | Conflict resolution | A real conflict, hit and resolved, with reasoning |
| [04-interactive-rebase](./04-interactive-rebase) | Interactive rebase | Squashing, reordering, and cleaning up commits |
| [05-cherry-pick](./05-cherry-pick) | Cherry-pick | Porting a specific fix across branches |
| [06-stash](./06-stash) | Stashing | Context-switching without losing work |
| [07-reset-vs-revert](./07-reset-vs-revert) | Reset vs Revert | Undoing changes safely on shared history |
| [08-tags-and-releases](./08-tags-and-releases) | Tags & Releases | Semantic versioning and release notes |
| [09-github-workflow](./09-github-workflow) | PRs & Issues | Real pull request and issue tracking workflow |
| [10-github-actions](./10-github-actions) | CI/CD | A working GitHub Actions workflow (markdown lint) |

## Realistic scenarios covered

- Developing two features in parallel without stepping on each other
- Shipping a hotfix while another feature branch is still in progress
- Hitting and resolving a real merge conflict
- Cleaning up commit history before opening a pull request
- Recovering from a bad commit or a wrong branch

## Skills demonstrated

- Branch management and naming conventions
- Merge conflict resolution
- Interactive rebase and history cleanup
- Semantic versioning and releases
- Pull request workflow
- Issue tracking
- CI with GitHub Actions

## How to use this repo

Each folder is self-contained. Open its `README.md` for:
- **The problem** it addresses
- **The commands**, in the order they were actually run
- **A real example** (not staged) with output
- **Notes** on gotchas or things I learned along the way

## Commands practiced

`init` · `clone` · `add` · `commit` · `push` · `pull` · `branch` · `checkout` · `switch` · `merge` · `rebase` · `stash` · `cherry-pick` · `revert` · `reset` · `tag`

## Branch and commit history

Rather than a mocked-up graph, the real branch structure is visible in this repo's own history — check the [Network graph](../../network) or run:

```bash
git log --graph --oneline --all
```

## References

- [Git Documentation](https://git-scm.com/doc)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)

## Status

This repo is actively maintained as I work through and document each workflow — check the commit history and [Issues](../../issues) for what's in progress.
