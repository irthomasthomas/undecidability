**Prompt:**
Only use well known and documented cli flags. Never invent new flags or options for a tool. Only use valid bash or zsh options.
"Request: " add label to an issue


**Response:**
To add a label to an issue using the GitHub CLI, you can use the `gh issue edit` command with the `--add-labels` flag. Here's the syntax:

```bash
gh issue edit <issue-number> --add-labels <label1> <label2> ...
```

Replace `<issue-number>` with the number of the issue you want to edit, and `<label1> <label2> ...` with the labels you want to add to the issue.

For example, to add the labels "bug" and "priority" to issue #123, you would run:

```bash
gh issue edit 123 --add-labels bug priority
```

Make sure you are in the repository directory or provide the `--repo` flag followed by the repository identifier (`<owner>/<repo>`).

Note: Before using the `gh issue edit` command, ensure that you have authenticated with GitHub CLI using `gh auth login`.

<details><summary>Metadata</summary>

- Duration: 6438 ms
- Datetime: 2023-08-31T12:52:15.202309
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

