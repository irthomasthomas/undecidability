**Prompt:**
Check how much will be downloaded before cloning a gh repo? in the gh cli?

**Response:**
To check how much will be downloaded before cloning a GitHub repository using the GitHub CLI (gh), you can use the `gh repo view` command.

Here are the steps to follow:

1. Open your terminal or command prompt.

2. Install the GitHub CLI (gh) if you haven't already. You can find installation instructions at https://cli.github.com/.

3. Authenticate yourself with GitHub using the `gh auth login` command and follow the prompts.

4. Navigate to the directory where you want to clone the repository.

5. Run the following command to view the repository details:

   ```shell
   gh repo view owner/repository
   ```

   Replace `owner/repository` with the actual username/organization and repository name, e.g., `github/clone`.

6. Look for the "size" field in the output. It represents the size of the repository in bytes.

   Please note that this is an approximation of the download size since it doesn't consider any compression applied during the cloning process.

By checking the size of the repository, you can get an idea of how much will be downloaded before cloning the GitHub repository using the gh CLI.

<details><summary>Metadata</summary>

- Duration: 10138 ms
- Datetime: 2023-09-04T11:42:58.505985
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

