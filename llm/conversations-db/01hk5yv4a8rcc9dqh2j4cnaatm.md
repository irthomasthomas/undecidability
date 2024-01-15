**Prompt:**
format gh label list as a simple list of names and description values and no field names


**Response:**
You can use the `--json` and `--jq` flags to format the output of the `gh label list` command as a simple list of label names and description values. Here's the command you can use:

```
gh label list --json name,description --jq '.[] | "\(.name) \(.description)"'
```

This command will output a list of label names and description values, like this:

```
bug This issue is a bug
enhancement This issue is an enhancement
documentation This issue is related to documentation
```

Note that the `--json` flag is used to specify the fields to fetch (name and description), and the `--jq` flag is used to format the output using the provided jq expression (`'.[] | "\(.name) \(.description)"'`). The `\(.name)` and `\(.description)` in the jq expression are placeholders for the corresponding field values.

<details><summary>Metadata</summary>

- Duration: 3158 ms
- Datetime: 2024-01-02T20:46:30.129442
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

