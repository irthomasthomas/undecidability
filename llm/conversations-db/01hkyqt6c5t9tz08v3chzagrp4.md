**Prompt:**
I already forked on github and cloned my repo then set-default

**Response:**
If you have already forked a repository on GitHub and cloned it to your local machine, and now you want to set the upstream repository as the default remote repository, you can follow these steps:

1. Open the terminal or command prompt.
2. Navigate to the local repository's directory using the `cd` command.
3. Verify the list of remotes associated with your local repository by running the command: `git remote -v`. This command will show the existing remotes.
4. If you want to set the upstream repository as the default remote (usually named `origin`), you need to first remove the existing `origin` remote. Run the command: `git remote remove origin`.
5. Next, add the upstream repository (from where you forked) as the default remote by running the command: `git remote add origin <upstream_repository_url>`.
   - Replace `<upstream_repository_url>` with the URL of the upstream repository. You can usually find it on the original repository's GitHub page.
6. Verify that the new remote has been added as the default by running `git remote -v`. It should display the upstream repository's URL next to `origin`.

By setting the upstream repository as the default remote named `origin`, you can easily push changes to your forked repository and pull updates from the upstream repository.

<details><summary>Metadata</summary>

- Duration: 4769 ms
- Datetime: 2024-01-12T11:44:38.626840
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
I am irthomasthomas:

origin	git@github.com:irthomasthomas/PowerInfer.git (fetch)
origin	git@github.com:irthomasthomas/PowerInfer.git (push)
upstream	git@github.com:SJTU-IPADS/PowerInfer.git (fetch)
upstream	git@github.com:SJTU-IPADS/PowerInfer.git (push)

**Response:**
It seems that you have already set up both the `origin` and `upstream` remotes correctly. Your `origin` remote points to your forked repository (`irthomasthomas/PowerInfer.git`), while the `upstream` remote points to the original repository (`SJTU-IPADS/PowerInfer.git`).

Since you already have these remotes set up correctly, you can push changes to your forked repository using `git push origin <branch_name>`, and you can pull updates from the original repository using `git pull upstream <branch_name>`.

Replace `<branch_name>` with the specific branch you want to push or pull.

For example, if you want to push changes to the `main` branch of your forked repository, you can run:
```
git push origin main
```

And if you want to pull updates from the `main` branch of the original repository, you can run:
```
git pull upstream main
```

Remember to commit your changes before pushing them and ensure you are on the correct branch before running these commands.

<details><summary>Metadata</summary>

- Duration: 4149 ms
- Datetime: 2024-01-12T11:46:07.427466
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
Now create a markdown doc that details every command needed to be issued from the cli (assuming arch linux and authed gh cli). This should document the process from the beginning including ssh and gh cli options. Then how to create a new feature and propose a PR back to the main repo. And also how to automatically keep all work synced incase I forget. And how to download changes from the main repo regularly.

**Response:**
Certainly! Here's a step-by-step guide to using Git and GitHub CLI (gh) on Arch Linux, including SSH setup, creating a new feature, proposing a pull request, keeping your work synced, and frequently downloading changes from the main repository.

## Initial Setup:
1. Verify if Git is installed:
   ```
   git --version
   ```
   If not installed, run:
   ```
   sudo pacman -Syu git
   ```
2. Install GitHub CLI (gh):
   ```
   yay -S github-cli
   ```

## SSH Setup
1. Check if SSH keys already exist:
   ```
   ls -al ~/.ssh
   ```
2. Generate a new SSH key if needed (replace `<email>` with your GitHub email):
   ```
   ssh-keygen -t ed25519 -C "<email>"
   ```
   Press `Enter` to accept the default file location.
3. Start the ssh-agent and add the private key:
   ```
   eval `ssh-agent -s`
   ssh-add ~/.ssh/id_ed25519
   ```
4. Copy the public key to your clipboard:
   ```
   xclip -sel clip < ~/.ssh/id_ed25519.pub
   ```
5. Go to GitHub > Settings > SSH and GPG keys and add a new SSH key with the copied public key.

## Cloning and Configuring Repository
1. Fork the repository on GitHub.
2. Clone your forked repository:
   ```
   git clone git@github.com:<username>/PowerInfer.git
   ```
3. Add the main repository as an upstream remote:
   ```
   cd PowerInfer
   git remote add upstream git@github.com:SJTU-IPADS/PowerInfer.git
   ```

## Creating a New Feature
1. Create a new branch for your feature:
   ```
   git checkout -b feature/your_feature_name
   ```
2. Make your changes to the code, add new files, etc.
3. Stage your changes:
   ```
   git add .
   ```
4. Commit your changes:
   ```
   git commit -m "Your commit message"
   ```

## Proposing a Pull Request
1. Push your branch to your forked repository:
   ```
   git push origin feature/your_feature_name
   ```
2. Install GitHub CLI (gh) if not installed already:
   ```
   yay -S github-cli
   ```
3. Authenticate with GitHub using the CLI:
   ```
   gh auth login
   ```
4. Create a pull request on GitHub:
   ```
   gh pr create
   ```
   Follow the prompts to complete the pull request creation.

## Keeping Your Work Synced
1. Before starting your work, fetch the latest changes from the upstream repository:
   ```
   git fetch upstream
   ```
2. Switch to your main branch:
   ```
   git checkout main
   ```
3. Merge the latest changes from the upstream repository into your local main branch:
   ```
   git merge upstream/main
   ```
4. Switch back to your feature branch:
   ```
   git checkout feature/your_feature_name
   ```
5. Merge the latest changes from your local main branch into your feature branch:
   ```
   git merge main

## Downloading Changes from the Main Repository
1. Fetch the latest changes from the upstream repository:
   ```
   git fetch upstream
   ```
2. Merge the latest changes from the upstream repository into your local branch (e.g., main or any other branch):
   ```
   git merge upstream/main
   ```

That's it! You now have a step-by-step guide for frequently used Git and GitHub CLI commands on Arch Linux to create new features, propose pull requests, keep your work synced, and download changes from the main repository. Remember to adapt the provided commands to match your specific repository and branch names.

<details><summary>Metadata</summary>

- Duration: 15616 ms
- Datetime: 2024-01-12T11:51:13.459465
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

