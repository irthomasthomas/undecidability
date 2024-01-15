**Prompt:**
view my own repos ordered by new

**Response:**
To view your own repositories ordered by the newest ones, you can use the following command:

```shell
gh api "/users/{username}/repos?type=owner&sort=created"
```

Replace `{username}` with your GitHub username.

This command uses the `gh api` command from the GitHub CLI to interact with the GitHub API. It retrieves the list of repositories owned by the specified user (`type=owner`) and sorts them by their creation date (`sort=created`). The result will be a JSON response with the repository details, including the name, description, and creation date.

<details><summary>Metadata</summary>

- Duration: 3659 ms
- Datetime: 2023-08-28T13:21:43.510722
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

