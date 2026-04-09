# Git and GitHub Guide

Git tracks changes in your project. GitHub stores a copy of your Git repository online so you can back it up, share it, and collaborate with others.

## Check Your Current Status

From the project root:

```bash
git status
```

This shows:

- Files that were changed.
- Files that are new and not tracked yet.
- Files staged and ready to commit.
- The current branch you are working on.

## Add Files To Staging

To stage one file:

```bash
git add SYLLABUS.md
```

To stage everything you changed:

```bash
git add .
```

Staging means you are choosing what should go into the next commit.

## Commit Your Changes

After staging, create a commit:

```bash
git commit -m "Add DSA syllabus and class one notes"
```

A commit is a saved checkpoint in your project history. The message should briefly explain what changed.


## Push To GitHub

After committing, upload your local commits to GitHub:

```bash
git push
```

If this is your first push on a new branch, Git may ask you to set the upstream branch:

```bash
git push -u origin main
```

For a different branch, replace `main` with your branch name.

## Common Daily Workflow

```bash
git status
git add .
git commit -m "Describe what changed"
git push
```

## See Commit History

```bash
git log --oneline
```

This shows recent commits in a shorter format.

## Create And Switch To A New Branch

```bash
git switch -c class-1-notes
```

Branches let you work on changes without disturbing the main branch.

## Switch Back To Main

```bash
git switch main
```

## Important Notes

- Run Git commands from the project root unless you know why you are running them somewhere else.
- Use `git status` often. It helps you avoid committing the wrong files.
- Do not commit `venv/`; this project already ignores it in `.gitignore`.
- Write commit messages that explain the change, not just "update".
