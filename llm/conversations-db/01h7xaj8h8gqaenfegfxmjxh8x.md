**Prompt:**
What is the exact zsh command to: search a public github repo isuues?

**Response:**
To search for issues in a public GitHub repository using the zsh command, you can use the GitHub API with the `curl` command. Here's an example command:

```zsh
curl -s "https://api.github.com/repos/{owner}/{repo}/issues?q={search_query}"
```

Replace `{owner}` with the username or organization name that owns the repository, `{repo}` with the repository name, and `{search_query}` with the keyword or search query you want to use.

For example, to search for issues with the keyword "bug" in the "github/docs" repository, the command would be:

```zsh
curl -s "https://api.github.com/repos/github/docs/issues?q=bug"
```

Note that you may need to authenticate with a personal access token if you encounter rate limits or need access to private repositories.

<details><summary>Metadata</summary>

- Duration: 5778 ms
- Datetime: 2023-08-15T19:25:29.877520
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

