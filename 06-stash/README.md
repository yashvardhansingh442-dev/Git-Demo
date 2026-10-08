# 06 - Stash

## The problem

I am halfway through a feature with uncommitted changes when an urgent fix comes in. I do not want to commit half-finished work, and I cannot switch branches cleanly with it sitting in my working directory. `git stash` puts my uncommitted changes on a shelf so I can switch, do the urgent work, and come back.

## Commands I use

| Command | What it does |
|---|---|
| `git stash push -m "message"` | Shelve tracked changes with a label |
| `git stash push -u -m "message"` | Also shelve untracked files (`-u`) |
| `git stash list` | Show everything on the shelf |
| `git stash show -p stash@{0}` | Show what is inside a stash |
| `git stash pop` | Re-apply the newest stash and remove it from the shelf |
| `git stash apply` | Re-apply but keep it on the shelf |
| `git stash drop stash@{0}` | Delete a stash |

## Setup (a throwaway practice repo)

```bash
mkdir ~/stash-lab && cd ~/stash-lab
git init -b main
echo "v1" > app.txt
git add . && git commit -m "chore: initial commit"

git switch -c hotfix/urgent
echo "v1 - hotfixed" > app.txt
git commit -am "fix: urgent production fix"
git switch main

echo "v1 - half finished feature" > app.txt
echo "scratch notes" > notes.txt
git status
```

## Hitting the problem

```bash
git switch hotfix/urgent
```

Git refuses:

```text
<paste the error message>
```

## Stashing, switching, coming back

```bash
git stash push -u -m "wip: half finished feature"
git status                  # working tree is clean now
git stash list

git switch hotfix/urgent
echo "follow-up" >> app.txt
git commit -am "fix: follow-up on hotfix"

git switch main
git stash pop
git status
```

Output of `git stash list`:

```text
<paste output of: git stash list>
```

Output of `git status` after `git stash pop`:

```text
<paste output of: git status>
```

## What I observed

<!-- In your own words: -->
<!-- - Why did Git refuse to switch branches? -->
<!-- - What does -u do, and what would have happened to notes.txt without it? -->
<!-- - What is the difference between pop and apply? -->

## Gotchas

- Stashes are local only. They are **not** pushed to GitHub.
- By default stash ignores untracked files. Use `-u`, or the new file stays behind.
- Always label stashes with `-m`, otherwise `git stash list` becomes a guessing game.
- `git stash pop` can conflict if the branch changed; the stash stays on the shelf until the conflict is resolved.

## Notes

<!-- Real things you ran into. -->
