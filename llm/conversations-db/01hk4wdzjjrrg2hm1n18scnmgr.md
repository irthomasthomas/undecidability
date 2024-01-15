**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**get notified of new issues in a gh repo


**Response:**
To get notified of new issues in a GitHub repository, you can use the following command:

```bash
curl -s https://api.github.com/repos/{owner}/{repo}/issues | grep -oP '"title": "\K[^"]+' | sort | uniq
```

Replace `{owner}` with the username or organization name that owns the repository, and `{repo}` with the name of the repository.

This command uses `curl` to fetch the issues from the GitHub API, then `grep` to extract the titles of the issues, and finally `sort` and `uniq` to remove duplicates and display the unique issue titles. The `-s` flag is used with `curl` to silence the progress output.

<details><summary>Metadata</summary>

- Duration: 3452 ms
- Datetime: 2024-01-02T10:45:07.406636
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

