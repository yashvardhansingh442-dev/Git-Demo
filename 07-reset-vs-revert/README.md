# 07 - Reset vs Revert

## The problem

A bad commit got into my history and I need to undo it. Git has two very different tools for this, and picking the wrong one on shared history causes real damage for teammates.

## The two approaches

| | `git revert` | `git reset` |
|---|---|---|
| What it does | Adds a **new commit** that undoes an old one | **Moves the branch pointer** back, dropping commits |
| History | Preserved, nothing is erased | Rewritten, commits disappear from the branch |
| Safe on shared/pushed branches? | **Yes** | **No** (needs a force push, breaks teammates) |
| Use it for | Undoing something already pushed | Cleaning up my own local, unpushed commits |

### The three modes of reset

| Mode | Commits | Staging area | Working files |
|---|---|---|---|
| `--soft` | undone | kept (staged) | kept |
| `--mixed` (default) | undone | cleared | kept |
| `--hard` | undone | cleared | **thrown away** |

## Setup (a throwaway practice repo)

```bash
mkdir ~/reset-lab && cd ~/reset-lab
git init -b main
echo "one" > a.txt && git add . && git commit -m "feat: add a"
echo "two" > b.txt && git add . && git commit -m "feat: add b"
echo "bad" > c.txt && git add . && git commit -m "feat: add c (buggy)"
git log --oneline
```

Starting history:

```text
<paste output of: git log --oneline>
```

## Experiment 1: revert

```bash
git switch -c demo/revert
git revert HEAD --no-edit
git log --oneline
ls
```

Result:

```text
<paste output of: git log --oneline>
```

The buggy commit is still in history, and a new revert commit undoes it. `c.txt` is gone from the folder.

## Experiment 2: reset --hard

```bash
git switch main
git switch -c demo/reset
git reset --hard HEAD~1
git log --oneline
ls
```

Result:

```text
<paste output of: git log --oneline>
```

The buggy commit has disappeared from this branch's history.

## Recovering from a reset

`reset --hard` is not always the end: Git remembers where `HEAD` used to be.

```bash
git reflog
git reset --hard <hash of the commit before the reset>
```

Output of `git reflog`:

```text
<paste output of: git reflog>
```

## What I observed

<!-- In your own words: -->
<!-- - What is the difference in the log between revert and reset? -->
<!-- - Why is reset dangerous on a branch other people have pulled? -->
<!-- - How did reflog help me? -->

## Rule of thumb

- Already pushed or shared: **revert**.
- Local only, not pushed: **reset** is fine.
- Not sure: revert. It never loses anything.

## Notes

<!-- Real things you ran into. -->
