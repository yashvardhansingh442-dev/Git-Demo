# 08 - Tags and Releases

## The problem

Commit hashes are hard to remember and say nothing about meaning. When I ship something, I want a permanent, human-readable name for that exact point in history, like `v1.0.0`, so I can find it, check it out, or roll back to it later. Tags give me that, and GitHub Releases turn a tag into a published version with notes.

## Two kinds of tags

| | Lightweight | Annotated |
|---|---|---|
| Command | `git tag v1` | `git tag -a v1 -m "message"` |
| What it is | Just a name pointing at a commit | A full object with author, date and message |
| Use it for | Private bookmarks | Real releases (what I use) |

## Semantic versioning

Version format is `MAJOR.MINOR.PATCH`:

- **PATCH** (`1.0.0` to `1.0.1`): backwards-compatible bug fix
- **MINOR** (`1.0.1` to `1.1.0`): new feature, still backwards-compatible
- **MAJOR** (`1.1.0` to `2.0.0`): breaking change

## Setup (a throwaway practice repo)

```bash
mkdir ~/tag-lab && cd ~/tag-lab
git init -b main

echo "v1" > app.txt
git add . && git commit -m "feat: initial app"
git tag draft-1
git tag -a v1.0.0 -m "Initial release"

echo "fix" >> app.txt
git commit -am "fix: handle empty input"
git tag -a v1.0.1 -m "Patch: fix empty input"

echo "search" >> app.txt
git commit -am "feat: add search"
git tag -a v1.1.0 -m "Minor: add search"

echo "config" >> app.txt
git commit -am "feat: change config format (breaking)"
git tag -a v2.0.0 -m "Major: breaking config change"
```

## Looking at tags

```bash
git tag
git log --oneline --decorate
git show v1.0.0
git show draft-1
```

Output of `git log --oneline --decorate`:

```text
<paste output of: git log --oneline --decorate>
```

Difference I saw between `git show v1.0.0` and `git show draft-1`:

```text
<describe or paste the difference>
```

## Going back to a release

```bash
git switch --detach v1.0.1
cat app.txt
git switch main
```

Checking out a tag puts me in "detached HEAD": I can look around, but new commits would not belong to any branch.

## Publishing to GitHub

Tags are not pushed by default.

```bash
git push origin v1.0.0         # one tag
git push origin --tags         # all tags
```

Then on GitHub: **Releases > Draft a new release**, choose the tag, write release notes, publish.

Link to my real release: `<paste link>`

## What I observed

<!-- In your own words: -->
<!-- - Why use annotated tags for releases? -->
<!-- - What version number would I give a bug fix? A new feature? A breaking change? -->
<!-- - Why is detached HEAD something to be careful about? -->

## Notes

<!-- Real things you ran into. -->
