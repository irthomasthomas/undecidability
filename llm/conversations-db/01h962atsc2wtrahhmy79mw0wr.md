**Prompt:**
view labels in github cli

**Response:**
To view labels in GitHub CLI, you can use the following command:

```shell
gh issue list --label <label-name>
```

Replace `<label-name>` with the specific label you want to view. This command will list all the issues with the specified label. If you don't provide a label name, it will display all the issues with any labels.

Additionally, you can use the `--limit` flag to limit the number of issues displayed.

For example:

```shell
gh issue list --label "bug" --limit 5
```

This command will list the first 5 issues with the "bug" label.

Note: Before using the GitHub CLI commands, make sure you have authenticated with your GitHub account using `gh auth login` command.

<details><summary>Metadata</summary>

- Duration: 5246 ms
- Datetime: 2023-08-31T15:10:30.060835
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

