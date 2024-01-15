**Prompt:**
Only use well known and documented cli flags. Never invent new flags or options for a tool. Only use valid bash or zsh options.
"Request: " view my own repos ordered by new


**Response:**
To view your own repositories ordered by the newest, you can use the following command:

```bash
gh repo list --sort=created
```

This command uses the `gh repo list` command provided by GitHub CLI and passes the `--sort` flag with the value `created` to sort the repositories by their creation date in descending order.

You can add this command as an alias for easier access by running:

```bash
gh alias set myrepos 'repo list --sort=created'
```

After setting the alias, you can simply use `gh myrepos` to view your own repositories ordered by the newest.

<details><summary>Metadata</summary>

- Duration: 3721 ms
- Datetime: 2023-08-28T14:24:14.808657
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

