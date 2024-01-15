**Prompt:**
What is the best terminal command, small function, or script to run in order to: change branch in gh?


**Response:**
To change the branch in GitHub (gh), you can use the following terminal command:

```
gh repo view --json default_branch -q .default_branch
```

This command will display the default branch of the GitHub repository.

<details><summary>Metadata</summary>

- Duration: 2549 ms
- Datetime: 2023-09-09T15:40:02.584885
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

