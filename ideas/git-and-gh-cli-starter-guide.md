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

