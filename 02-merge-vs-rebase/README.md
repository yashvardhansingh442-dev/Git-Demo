# 02 - Merge vs Rebase

## The problem

Two branches have diverged: `main` moved forward while my feature branch was in progress. I need to bring them together. Git gives me two ways to do it, and they produce different histories.

## The two approaches

| | `git merge` | `git rebase` |
|---|---|---|
| What it does | Joins two histories with a new merge commit | Replays my commits on top of the target branch |
| History shape | Branching, shows when work happened in parallel | Linear, as if the work happened in sequence |
| Existing commits | Untouched | Rewritten (new hashes) |
| Safe on shared branches? | Yes | No, never rebase commits others have pulled |

## Setup (a throwaway practice repo)

I ran this in a scratch repo so the experiment could not touch anything real.

```bash
mkdir ~/git-lab && cd ~/git-lab
git init -b main
echo "base" > base.txt
git add . && git commit -m "chore: initial commit"
```

## Experiment 1: merge

```bash
git switch -c feature/merge-demo
echo "feature work" > feature1.txt
git add . && git commit -m "feat: add feature1"

git switch main
echo "main work" > main1.txt
git add . && git commit -m "chore: add main1"

git merge feature/merge-demo -m "Merge feature/merge-demo"
git log --graph --oneline
```

Result:

```text
<paste output of: git log --graph --oneline>
```

## Experiment 2: rebase

```bash
git switch -c feature/rebase-demo
echo "feature work 2" > feature2.txt
git add . && git commit -m "feat: add feature2"
git log --oneline            # note the hash of the feature commit

git switch main
echo "main work 2" > main2.txt
git add . && git commit -m "chore: add main2"

git switch feature/rebase-demo
git rebase main
git log --oneline            # compare the hash again

git switch main
git merge feature/rebase-demo
git log --graph --oneline
```

Hash before rebase: `<paste>`
Hash after rebase: `<paste>`

Result:

```text
<paste output of: git log --graph --oneline>
```

## What I observed

<!-- Write in your own words: -->
<!-- - Which history is easier to read, and why? -->
<!-- - Why did the hash change after rebase? -->
<!-- - Why did the final merge after rebase not create a merge commit? (fast-forward) -->

## When I use each

- **Merge** when the branch is shared or already pushed, or when I want to keep the record of parallel work.
- **Rebase** to tidy my own local feature branch before opening a PR, or to pick up the latest `main`.
- **Rule of thumb:** never rebase commits that other people may have based work on.

## Gotchas

<!-- Add anything real you hit, e.g. a rebase conflict and how you continued with `git rebase --continue`. -->
