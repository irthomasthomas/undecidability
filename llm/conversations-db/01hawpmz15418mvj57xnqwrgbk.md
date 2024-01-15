**Prompt:**
Write a bash terminal command to check the size of a github repo using gh cli or curl? Be concise, but include as much code as required by the problem/solution.


**Response:**
To check the size of a GitHub repository using the `gh` CLI or `curl`, you can use the GitHub REST API. Here's how you can do it using `curl`:

```bash
curl -s https://api.github.com/repos/<username>/<repo> | grep "size"
```

Replace `<username>` with the GitHub username and `<repo>` with the repository name you want to check.

If you prefer to use the `gh` CLI, you can install it and then use the following command:

```bash
gh repo view <username>/<repo> --json size --jq '.size'
```

Again, replace `<username>` with the GitHub username and `<repo>` with the repository name you want to check.

Both commands will output the size of the repository in bytes.

<details><summary>Metadata</summary>

- Duration: 6410 ms
- Datetime: 2023-09-21T20:24:31.770713
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

