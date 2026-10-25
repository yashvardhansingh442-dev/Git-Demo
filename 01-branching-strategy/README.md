# 01 - Branching Strategy

## The problem

Everyone committing straight to `main` means half-finished work, broken builds, and no safe way to ship a fix while a feature is still in progress. A branching strategy gives every kind of change its own lane.

## The strategy

| Branch | Purpose | Branches from | Merges into |
|---|---|---|---|
| `main` | Always stable, always releasable | - | - |
| `feature/<name>` | New functionality | `main` | `main` (via PR) |
| `bugfix/<name>` | Non-urgent fix | `main` | `main` (via PR) |
| `release/<version>` | Final prep for a version | `main` | `main`, then tagged |
| `hotfix/<name>` | Urgent production fix | `main` | `main` |

**Naming rules I follow**
- lowercase, words separated by hyphens: `feature/add-login-page`
- prefix says the *type* of work, the rest says *what*
- short-lived: delete the branch after it is merged

## Commands (in the order I ran them)

```bash
# start from an up-to-date main
git switch main
git pull origin main

# create a feature branch and switch to it
git switch -c feature/<name>

# work, then commit
git add .
git commit -m "docs: <what changed>"

# publish the branch
git push -u origin feature/<name>

# see all branches, local and remote
git branch -a

# after merging via pull request, clean up
git switch main
git pull origin main
git branch -d feature/<name>
git push origin --delete feature/<name>
```

## Real example

<!-- Replace this section with YOUR actual output. -->

Branches I created:

```text
<paste output of: git branch -a>
```

Resulting history:

```text
<paste output of: git log --graph --oneline --all>
```

Pull request: <link to your merged PR>

## Notes and gotchas

<!-- Write 2-3 things you actually ran into. Ideas: -->
<!-- - difference between `git switch -c` and `git checkout -b` -->
<!-- - what happened when you forgot `-u` on the first push -->
<!-- - why you delete merged branches -->

## Why this approach

<!-- 2-3 sentences in your own words: why feature branches + PRs beat committing to main. -->
