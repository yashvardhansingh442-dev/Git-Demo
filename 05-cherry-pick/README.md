# 05 - Cherry-Pick

## The problem

A bug fix was committed on a feature branch that is not ready to ship, but the release branch needs that one fix now. I do not want the whole feature branch, only that single commit. `git cherry-pick` copies one commit onto the branch I am on.

## When I use it

- Porting a hotfix from `main` to a `release/*` branch (or the other way round)
- Rescuing one good commit from an abandoned branch
- Moving a commit I made on the wrong branch

## When I avoid it

- When I actually want all the commits: merge or rebase is cleaner
- Doing it repeatedly for the same branches, because it creates duplicate commits with different hashes

## Setup (a throwaway practice repo)

```bash
mkdir ~/cherry-lab && cd ~/cherry-lab
git init -b main
echo "v1" > app.txt
git add . && git commit -m "chore: initial commit"

git switch -c release/v1.0
echo "release notes" > notes.txt
git add . && git commit -m "docs: add release notes"

git switch main
git switch -c feature/dashboard
echo "dashboard" > dashboard.txt
git add . && git commit -m "feat: add dashboard"
echo "crash fix" > fix.txt
git add . && git commit -m "fix: prevent crash on empty input"
echo "chart" > chart.txt
git add . && git commit -m "feat: add chart"
```

History of the feature branch:

```text
<paste output of: git log --oneline>
```

The commit I need on the release branch is the fix: `<hash>`.

## Cherry-picking the fix

```bash
git switch release/v1.0
git cherry-pick -x <hash of the fix commit>
git log --oneline --graph --all
```

`-x` adds a line to the message saying which commit it came from, which helps trace it later.

Result:

```text
<paste output of: git log --oneline --graph --all>
```

Original hash: `<paste>`
Hash on the release branch: `<paste>`

## What I observed

<!-- In your own words: -->
<!-- - Why is the hash different on the release branch? -->
<!-- - Did the dashboard and chart commits come along? Why not? -->
<!-- - What does the "(cherry picked from commit ...)" line tell me? -->

## If there is a conflict

```bash
git cherry-pick --continue   # after fixing the files and running git add
git cherry-pick --abort      # to give up and go back
```

## Notes and gotchas

<!-- Real things you ran into. -->
