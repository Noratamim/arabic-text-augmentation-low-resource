# Publish this project on GitHub

## Recommended first setting: Private repository

Create a **private** repository initially because this is an active course project and the dataset redistribution terms should be checked before any raw text is republished. The raw and processed data folders are ignored by `.gitignore`.

## Option A — GitHub website / GitHub Desktop

1. Sign in to GitHub and create a new repository named `arabic-text-augmentation-low-resource`.
2. Choose **Private**. Do not add another README, `.gitignore`, or license because this starter package already contains project files.
3. Extract this starter ZIP on your computer.
4. Open the extracted folder in GitHub Desktop, choose **Add an Existing Repository** (or initialize it as a repository), review the changed files, commit them, and select **Publish repository**.
5. Confirm the raw dataset is not listed among files to be published.

## Option B — Git command line

From inside the extracted project folder:

```bash
git init
git add .
git status
# Confirm data/raw and data/processed files are NOT staged
git commit -m "Initialize Arabic text augmentation project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/arabic-text-augmentation-low-resource.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Never paste a personal access token, password, or secret key into notebooks or commit history.

## Collaboration

After the repository is published, add the other two students as collaborators from GitHub repository Settings → Collaborators. Give them the access level approved by the team. Use separate branches for substantial changes and pull requests for review.
