**Prompt:**
Get the last commit for a repository in the gh cli (manjaro/arch linux) or using curl the api.

**Response:**
To get the last commit for a repository using the GitHub CLI (`gh`) or the `curl` command-line tool on Manjaro/Arch Linux, you have a couple of options.

Using the GitHub CLI (`gh`):
1. Install the GitHub CLI if you haven't already. You can install it via AUR using the following command: 
   ```
   yay -S github-cli
   ```
2. Log in to your GitHub account using the `gh` command-line tool:
   ```
   gh auth login
   ```
3. Navigate to the root directory of the repository for which you want to retrieve the last commit.
4. Execute the following command to get the last commit information:
   ```
   gh api repos/:owner/:repo/commits | jq '.[0].commit.message'
   ```
   Replace `:owner` with the owner's GitHub username and `:repo` with the repository name. The command uses `jq` to extract the commit message. If you don't have `jq` installed, you can install it using `yay -S jq`.

Using `curl`:
1. Install `curl` if you haven't already. You can install it using the following command:
   ```
   sudo pacman -S curl
   ```
2. Execute the following `curl` command to retrieve the last commit information:
   ```
   curl -s "https://api.github.com/repos/:owner/:repo/commits" | jq '.[0].commit.message'
   ```
   Replace `:owner` with the owner's GitHub username and `:repo` with the repository name. The command uses `jq` to extract the commit message. If you don't have `jq` installed, you can install it using `yay -S jq`.

Both methods will output the commit message of the last commit for the specified repository.

<details><summary>Metadata</summary>

- Duration: 18898 ms
- Datetime: 2023-09-13T14:32:06.374907
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
and date

**Response:**
To retrieve the last commit message and date for a repository using the GitHub CLI (`gh`) or the `curl` command-line tool on Manjaro/Arch Linux, you can modify the commands provided earlier. Here's how you can do it:

Using the GitHub CLI (`gh`):
1. Install the GitHub CLI if you haven't already. You can install it via AUR using the following command: 
   ```
   yay -S github-cli
   ```
2. Log in to your GitHub account using the `gh` command-line tool:
   ```
   gh auth login
   ```
3. Navigate to the root directory of the repository for which you want to retrieve the last commit.
4. Execute the following command to get the last commit message and date information:
   ```
   gh api repos/:owner/:repo/commits | jq -r '.[0] | .commit.message, .commit.author.date'
   ```
   Replace `:owner` with the owner's GitHub username and `:repo` with the repository name. The command uses `jq` to extract the commit message and author date in a readable format. If you don't have `jq` installed, you can install it using `yay -S jq`.

Using `curl`:
1. Install `curl` if you haven't already. You can install it using the following command:
   ```
   sudo pacman -S curl
   ```
2. Execute the following `curl` command to retrieve the last commit message and date information:
   ```
   curl -s "https://api.github.com/repos/:owner/:repo/commits" | jq -r '.[0] | .commit.message, .commit.author.date'
   ```
   Replace `:owner` with the owner's GitHub username and `:repo` with the repository name. The command uses `jq` to extract the commit message and author date in a readable format. If you don't have `jq` installed, you can install it using `yay -S jq`.

Both methods will output the commit message followed by the commit author's date of the last commit for the specified repository.

<details><summary>Metadata</summary>

- Duration: 21333 ms
- Datetime: 2023-09-13T14:33:19.203156
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

