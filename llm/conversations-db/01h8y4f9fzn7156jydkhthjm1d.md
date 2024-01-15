**Prompt:**
view my own repos ordered by new

**Response:**
To view your own repositories ordered by new, you can use the following command:

```
gh s -E -u @me | xargs -n1 gh repo view --loginsort --sort created
```

This command uses `gh s` to search for all your repositories with the `-E` flag to include empty strings, and the `-u @me` flag to narrow the search down to your repositories. The `xargs` command takes the output of `gh s` and passes it as an argument to `gh repo view`. The `--loginsort` flag sorts the repositories by the login name of the repository owner, and the `--sort created` flag orders the repositories by creation date, with the newest repositories appearing first.

Note that you need to have the GitHub CLI (`gh`) installed and authenticated for this command to work.

<details><summary>Metadata</summary>

- Duration: 4850 ms
- Datetime: 2023-08-28T13:13:58.283712
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

