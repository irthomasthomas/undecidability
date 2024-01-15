**Prompt:**
What is the exact zsh command to: search a public github repo isues?

**Response:**
To search for issues in a public GitHub repository using the zsh command, you can use the GitHub API with the `curl` command. Here is the command:

```zsh
curl -s "https://api.github.com/repos/{owner}/{repo}/issues?q={search_query}"
```

Replace `{owner}` with the username or organization name that owns the repository, `{repo}` with the repository name, and `{search_query}` with the keyword or search query you want to use.

For example, to search for issues with the keyword "bug" in the "octocat/Hello-World" repository, the command would be:

```zsh
curl -s "https://api.github.com/repos/octocat/Hello-World/issues?q=bug"
```

Note that you may need to provide authentication or an access token if the repository requires it.

<details><summary>Metadata</summary>

- Duration: 6289 ms
- Datetime: 2023-08-15T19:26:35.130685
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

