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
*   a0273eb (HEAD -> main) Merge feature/merge-demo
|\
| * 46d70fd (feature/merge-demo) feat: add feature1
* | 635246c chore: add main1
|/
* 61cf702 chore: initial commit
```

The merge created a new commit (`a0273eb`) with two parents. The original commits kept their hashes.

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

Hash before rebase: `f0133b2`
Hash after rebase: `f76149e`

Result:

```text
* f76149e (HEAD -> main, feature/rebase-demo) feat: add feature2
* 1d7652e chore: add main2
*   a0273eb Merge feature/merge-demo
|\
| * 46d70fd (feature/merge-demo) feat: add feature1
* | 635246c chore: add main1
|/
* 61cf702 chore: initial commit
```

## What I observed

- The rebased history is one straight line, so it is easier to read. The merge history shows two paths, but it also shows that the work happened in parallel.
- Rebase replayed my commit on top of the new main commit. Its parent changed, so its hash changed from `f0133b2` to `f76149e`.
- After the rebase, my feature branch was directly ahead of main, so Git only had to move the main pointer forward. That is a fast-forward, so no merge commit was created.

## When I use each

- **Merge** when the branch is shared or already pushed, or when I want to keep the record of parallel work.
- **Rebase** to tidy my own local feature branch before opening a PR, or to pick up the latest `main`.
- **Rule of thumb:** never rebase commits that other people may have based work on.

## Gotchas

- `git commit` without `-m` treats the text as a file name and fails with a pathspec error.
- A scratch repo made with `git init` has no remote, so `git push` fails with "No configured push destination".
- `git log` opens a pager; press `q` to leave it.
- In zsh, an exclamation mark inside double quotes triggers history expansion and breaks the command. Use single quotes instead.
