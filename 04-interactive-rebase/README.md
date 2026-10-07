# 04 - Interactive Rebase

## The problem

While working I commit often: `wip`, `fix typo`, `oops forgot file`. That is fine for me, but it makes a noisy history for reviewers. Interactive rebase lets me clean up my own commits **before** I open a pull request.

## The commands in the todo list

| Command | What it does |
|---|---|
| `pick` | Keep the commit as is |
| `reword` | Keep the commit, change its message |
| `squash` | Merge into the previous commit, and combine the messages |
| `fixup` | Merge into the previous commit, and discard this message |
| `drop` | Delete the commit |
| (reorder lines) | Changes the order of the commits |

The list is shown **oldest first**, the opposite of `git log`.

## Setup (a throwaway practice repo)

```bash
mkdir ~/rebase-lab && cd ~/rebase-lab
git init -b main
echo "base" > base.txt
git add . && git commit -m "chore: initial commit"

git switch -c feature/login
echo "login form" > login.txt
git add . && git commit -m "feat: add login form"

echo "validation" > validation.txt
git add . && git commit -m "wip"

echo "login form v2" > login.txt
git commit -am "fix typo"

echo "error messages" > errors.txt
git add . && git commit -m "oops forgot file"
```

History before cleanup:

```text
<paste output of: git log --oneline>
```

## Cleaning it up

```bash
git rebase -i main
```

The todo list I edited it into:

```text
<paste the final todo list you saved>
```

Goal: 2 clean commits, `feat: add login form` and `feat: add input validation`.

History after cleanup:

```text
<paste output of: git log --oneline>
```

## What I observed

<!-- In your own words: -->
<!-- - What is the difference between squash and fixup? -->
<!-- - Why did the hashes change? -->
<!-- - Why does the todo list show oldest first? -->

## Safety rules

- Only rewrite commits that **only I have** and have **not been pushed** (or that nobody else has pulled).
- If it goes wrong mid-way: `git rebase --abort`
- If it goes wrong after finishing: `git reflog` shows where `HEAD` used to be, and `git reset --hard <old-hash>` brings it back.

## Notes and gotchas

<!-- Real things you ran into: the editor that opened, the squash message screen, etc. -->
