**Prompt:**
Show me some example formatting commands for repo:irthomasthomas/undecidability


**Response:**
Here are some examples of formatting commands for the repository `irthomasthomas/undecidability`:

1. Get a list of the repository's issues in JSON format:
   ```
   gh issue list --repo irthomasthomas/undecidability --json
   ```

2. Get a list of the repository's issues in a table format:
   ```
   gh issue list --repo irthomasthomas/undecidability --json number,title,author --template "{{range .}}{{tablerow .number .title .author.login}}{{end}}{{tablerender}}"
   ```

3. Get a list of the repository's pull requests with only the pull request number and title:
   ```
   gh pr list --repo irthomasthomas/undecidability --json number,title --template "{{range .}}{{printf \"#%v: %s\n\" .number .title}}{{end}}"
   ```

4. Get detailed information about a specific pull request in a formatted manner:
   ```
   gh pr view 123 --repo irthomasthomas/undecidability --json title,body,author,createdAt --template "{{.title}}\n\n{{.body}}\n\nCreated by {{.author.login}} on {{timeago .createdAt}}"
   ```

These commands demonstrate different ways to format the output from various GitHub CLI (`gh`) commands. You can modify them according to your specific needs.

<details><summary>Metadata</summary>

- Duration: 6989 ms
- Datetime: 2024-01-02T14:23:27.546235
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

