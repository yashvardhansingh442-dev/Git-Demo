# Git Mastery

![Git](https://img.shields.io/badge/Git-Workflows-orange)
![GitHub](https://img.shields.io/badge/GitHub-Workflow-black)
![License](https://img.shields.io/badge/License-MIT-blue)
![Status](https://img.shields.io/badge/Status-In_Progress-yellow)

A hands-on collection of Git and GitHub workflows, the kind used day-to-day on an engineering team, written as worked examples instead of a list of commands.

Each folder covers one workflow: the problem it solves, the commands, a practice example with output, and the reasoning behind the approach. Folders are being filled in one at a time, and the [progress tracker](#progress-tracker) shows which ones are finished.

## Table of contents

- [Why this repo exists](#why-this-repo-exists)
- [Who this repository is for](#who-this-repository-is-for)
- [Learning path](#learning-path)
- [Topics at a glance](#topics-at-a-glance)
- [Topic summaries](#topic-summaries)
- [Which command should I use?](#which-command-should-i-use)
- [Repository layout](#repository-layout)
- [How each folder is structured](#how-each-folder-is-structured)
- [Conventions used in this repo](#conventions-used-in-this-repo)
- [Quick start](#quick-start)
- [Progress tracker](#progress-tracker)
- [Skills practiced](#skills-practiced)
- [References](#references)
- [License](#license)

## Why this repo exists

Most "Git practice" repos show that someone can commit and push. This one is meant to show *understanding*: knowing which workflow to reach for and why, not just which commands exist.

Every topic answers three questions:

1. **What problem does this solve?**
2. **What are the exact commands, and what do they output?**
3. **When should I use it, and when should I avoid it?**

## Who this repository is for

- Students learning Git beyond the basics
- Developers preparing for interviews
- Anyone moving from solo projects to team workflows
- Anyone who wants worked examples instead of isolated commands

## Learning path

The folders are numbered in the order they build on each other.

| Stage | Folders | Goal |
|---|---|---|
| 1. Organize work | 01 | Give every kind of change its own branch and naming rule |
| 2. Combine work | 02, 03 | Bring branches together, and resolve conflicts when Git cannot |
| 3. Clean up and move work | 04, 05, 06 | Tidy history, copy single commits, and park unfinished changes |
| 4. Undo and mark work | 07, 08 | Reverse mistakes safely, and name release points |
| 5. Collaborate and automate | 09, 10 | Use issues, pull requests and CI the way a team does |

## Topics at a glance

| Folder | Topic | What it covers | Status |
|---|---|---|---|
| [01-branching-strategy](./01-branching-strategy) | Branching | Feature, bugfix, hotfix and release branch naming and structure | In progress |
| [02-merge-vs-rebase](./02-merge-vs-rebase) | Merge vs Rebase | When to use each, with real hashes and history graphs | Done |
| [03-merge-conflict-resolution](./03-merge-conflict-resolution) | Conflict resolution | Causing, reading and resolving a conflict | In progress |
| [04-interactive-rebase](./04-interactive-rebase) | Interactive rebase | Squashing, reordering and cleaning up commits | In progress |
| [05-cherry-pick](./05-cherry-pick) | Cherry-pick | Porting a specific fix across branches | In progress |
| [06-stash](./06-stash) | Stashing | Context-switching without losing work | In progress |
| [07-reset-vs-revert](./07-reset-vs-revert) | Reset vs Revert | Undoing changes safely on shared history | In progress |
| [08-tags-and-releases](./08-tags-and-releases) | Tags and Releases | Semantic versioning and release notes | In progress |
| [09-github-workflow](./09-github-workflow) | Issues and PRs | Issue to branch to pull request to merge | In progress |
| [10-github-actions](./10-github-actions) | CI/CD | A GitHub Actions markdown-lint workflow | In progress |

**Done** means the folder has real commands, real output and my own notes. **In progress** means the explanation and commands are written, and the example output is still to be added.

## Topic summaries

### 01 - Branching strategy

- **Problem:** Committing straight to `main` leads to half-finished work and no safe way to ship a fix while a feature is in progress.
- **Idea:** Each kind of change gets its own lane: `feature/*`, `bugfix/*`, `release/*` and `hotfix/*`, all branching from `main`.
- **Key commands:** `git switch -c`, `git push -u origin`, `git branch -d`
- **Rule:** Branches are lowercase, hyphen-separated, short-lived, and deleted after merging.

### 02 - Merge vs rebase

- **Problem:** `main` moved forward while a feature branch was in progress, and the two must be combined.
- **Idea:** Merge keeps both histories and adds a merge commit. Rebase replays your commits on top of the target, giving a straight line and new hashes.
- **Key commands:** `git merge`, `git rebase`, `git log --graph --oneline`
- **Rule:** Never rebase commits that other people may have based work on.

### 03 - Merge conflict resolution

- **Problem:** Two branches changed the same line, so Git cannot choose a winner.
- **Idea:** Read the conflict markers, decide the final text, delete the markers, then stage and commit.
- **Key commands:** `git merge`, `git status`, `git add`, `git merge --abort`
- **Rule:** Never accept one side blindly without reading both.

### 04 - Interactive rebase

- **Problem:** Frequent `wip` and `fix typo` commits make a noisy history for reviewers.
- **Idea:** Rewrite your own local commits with `pick`, `reword`, `squash`, `fixup` and `drop` before opening a pull request.
- **Key commands:** `git rebase -i`, `git rebase --abort`, `git reflog`
- **Rule:** Only rewrite commits that have not been pushed or pulled by anyone else.

### 05 - Cherry-pick

- **Problem:** One fix is needed on another branch, without the rest of the branch it was committed on.
- **Idea:** Copy a single commit onto the current branch. It gets a new hash, and `-x` records where it came from.
- **Key commands:** `git cherry-pick -x`, `--continue`, `--abort`
- **Rule:** If you need most of a branch, merge or rebase instead.

### 06 - Stash

- **Problem:** Uncommitted work blocks a branch switch when something urgent arrives.
- **Idea:** Shelve changes with a label, switch and do the urgent work, then bring the changes back.
- **Key commands:** `git stash push -u -m`, `git stash list`, `git stash pop`, `git stash apply`
- **Rule:** Stashes are local only, and untracked files need `-u`.

### 07 - Reset vs revert

- **Problem:** A bad commit is in history and must be undone.
- **Idea:** Revert adds a new commit that cancels the old one. Reset moves the branch pointer back and drops commits, in `--soft`, `--mixed` or `--hard` mode.
- **Key commands:** `git revert`, `git reset`, `git reflog`
- **Rule:** Pushed or shared means revert. Local and unpushed means reset is fine.

### 08 - Tags and releases

- **Problem:** Commit hashes are unmemorable and carry no meaning.
- **Idea:** Annotated tags give a release a permanent name, and semantic versioning (`MAJOR.MINOR.PATCH`) says what kind of change it was.
- **Key commands:** `git tag -a`, `git push origin --tags`, `git switch --detach`
- **Rule:** Tags are not pushed by default, so push them explicitly.

### 09 - GitHub workflow

- **Problem:** Git records what changed, but not why, or who agreed to it.
- **Idea:** Work flows from issue to branch to commits to pull request to review to merge, and `Closes #N` closes the issue automatically.
- **Key tools:** Issues, pull requests, merge options (merge commit, squash, rebase)
- **Rule:** No change goes straight to `main`.

### 10 - GitHub Actions

- **Problem:** People forget to run checks before merging.
- **Idea:** A workflow file in `.github/workflows/` runs a markdown linter on every push to `main` and every pull request.
- **Key concepts:** Workflow, trigger, job, runner, step
- **Rule:** Checks should run before a merge, not after.

## Which command should I use?

| Situation | Reach for | Why |
|---|---|---|
| Bring a shared or pushed branch up to date | `git merge` | Existing commits stay untouched |
| Tidy my own local branch before a PR | `git rebase` | Linear history, easier to review |
| Several noisy commits to combine | `git rebase -i` | Squash, reword, reorder or drop |
| Need one commit from another branch | `git cherry-pick -x` | Copies only that commit and records its source |
| Half-finished work, urgent task arrives | `git stash push -u -m "label"` | Clean working tree without a throwaway commit |
| Undo a commit that is already pushed | `git revert` | Adds a new commit and preserves history |
| Undo my own local, unpushed commits | `git reset` | Moves the branch back, so use `--hard` with care |
| Reset went wrong | `git reflog` | Shows where `HEAD` used to be |
| Mark a release | `git tag -a vX.Y.Z` | Permanent, readable name for a point in history |

## Repository layout

```text
Git-Demo/
├── 01-branching-strategy/
├── 02-merge-vs-rebase/
├── 03-merge-conflict-resolution/
├── 04-interactive-rebase/
├── 05-cherry-pick/
├── 06-stash/
├── 07-reset-vs-revert/
├── 08-tags-and-releases/
├── 09-github-workflow/
├── 10-github-actions/
├── .gitignore
├── LICENSE.md
└── README.md
```

Each topic folder holds a single `README.md`. Small practice files from the first Git exercises sit in the repository root and are not part of the topics.

## How each folder is structured

Every topic README follows the same template so they are easy to compare:

1. **The problem:** why the workflow exists
2. **The approach:** a comparison table or key terms
3. **Setup:** a throwaway practice repo, so experiments never touch real work
4. **The experiment:** commands in the order they are run, with output
5. **What I observed:** my own explanation of what happened
6. **Gotchas and notes:** things that went wrong or were surprising

## Conventions used in this repo

| Area | Convention |
|---|---|
| Branch names | `type/short-description`, lowercase with hyphens, such as `feature/add-login-page` |
| Commit messages | [Conventional Commits](https://www.conventionalcommits.org/), such as `docs: add stash README` |
| Versions | [Semantic Versioning](https://semver.org/), such as `v1.2.0` |
| Experiments | Run in a scratch repo under `~/`, never in this repo |
| Changes | Made on a branch and merged through a pull request |

## Quick start

```bash
# clone the repo
git clone https://github.com/yashvardhansingh442-dev/Git-Demo.git
cd Git-Demo

# read a topic
cat 02-merge-vs-rebase/README.md

# see the real history of this repo
git log --graph --oneline --all
```

To follow a topic yourself, copy its **Setup** commands into a new scratch folder and run them there.

You can also open the [Network graph](https://github.com/yashvardhansingh442-dev/Git-Demo/network) to see the branch structure.

## Progress tracker

- [x] 02 - Merge vs rebase: commands, real output and notes
- [ ] 01 - Branching strategy: add real branch list and PR link
- [ ] 03 - Merge conflict resolution: add real conflict output and reasoning
- [ ] 04 - Interactive rebase: add before and after history
- [ ] 05 - Cherry-pick: add hashes and graph
- [ ] 06 - Stash: add refusal message and stash list output
- [ ] 07 - Reset vs revert: add logs and reflog output
- [ ] 08 - Tags and releases: add tag output and a published release link
- [ ] 09 - GitHub workflow: add the real issue and pull request links
- [ ] 10 - GitHub Actions: commit the workflow files and add the run link

Check the commit history and [Issues](https://github.com/yashvardhansingh442-dev/Git-Demo/issues) for what is being worked on next.

## Skills practiced

| Skill | Folders |
|---|---|
| Branch management and naming conventions | 01 |
| Choosing between merge and rebase | 02 |
| Conflict resolution | 03 |
| History cleanup | 04 |
| Moving commits between branches | 05 |
| Context switching with stash | 06 |
| Safe undo on shared history | 07 |
| Semantic versioning and releases | 08 |
| Pull request workflow and issue tracking | 09 |
| Continuous integration | 10 |

## References

- [Git Documentation](https://git-scm.com/doc)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [GitHub Actions documentation](https://docs.github.com/en/actions)

## License

Released under the [MIT License](./LICENSE.md).
