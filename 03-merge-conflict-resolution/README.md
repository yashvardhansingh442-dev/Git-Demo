# 03 - Merge Conflict Resolution

## The problem

Two branches changed the same line of the same file. Git cannot decide which version is right, so it stops the merge and asks me to decide.

## How a conflict looks

```text
<<<<<<< HEAD
my current branch's version
=======
the incoming branch's version
>>>>>>> branch-name
```

- Between `<<<<<<<` and `=======` is the version on the branch I am on.
- Between `=======` and `>>>>>>>` is the version I am merging in.
- I must delete all three marker lines and leave the final text I want.

## Setup

Both branches start from the same commit and edit the same line of `greeting.txt`.

```bash
git switch -c feature/03-conflict-resolution
mkdir 03-merge-conflict-resolution
echo "Welcome to Git Mastery" > 03-merge-conflict-resolution/greeting.txt
git add . && git commit -m "docs: add greeting file for conflict demo"

git switch -c conflict/branch-a
echo "Welcome to Git Mastery - from branch A" > 03-merge-conflict-resolution/greeting.txt
git commit -am "feat: change greeting on branch A"

git switch feature/03-conflict-resolution
git switch -c conflict/branch-b
echo "Hello from Git Mastery - from branch B" > 03-merge-conflict-resolution/greeting.txt
git commit -am "feat: change greeting on branch B"
```

## Causing the conflict

```bash
git switch feature/03-conflict-resolution
git merge conflict/branch-a      # fast-forwards, no problem
git merge conflict/branch-b      # conflict
```

Git's message:

```text
<paste the CONFLICT message here>
```

`git status` during the conflict:

```text
<paste output of: git status>
```

The file with markers:

```text
<paste output of: cat 03-merge-conflict-resolution/greeting.txt>
```

## Resolving it

1. Open the file and decide what the final line should be.
2. Delete the three marker lines and keep the text I want.
3. Stage and finish the merge:

```bash
git add 03-merge-conflict-resolution/greeting.txt
git commit -m "merge: resolve greeting conflict between branch A and B"
```

If I want to back out instead: `git merge --abort`.

Final file:

```text
<paste output of: cat 03-merge-conflict-resolution/greeting.txt>
```

History:

```text
<paste output of: git log --graph --oneline>
```

## My reasoning

<!-- In your own words: -->
<!-- - What did I keep, and why? (A's wording, B's wording, or a mix?) -->
<!-- - How did I know which side was "right"? In a team, who would I ask? -->

## Notes and gotchas

<!-- Real things you ran into, e.g. forgetting to delete a marker line, or what `git status` said. -->

## Tips

- Search the project for leftover markers before committing: `grep -rn "<<<<<<<" .`
- Pull often so conflicts stay small.
- Never resolve a conflict by blindly accepting one side without reading both.
