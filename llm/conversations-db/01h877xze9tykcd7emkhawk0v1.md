**Prompt:**
What is the exact zsh command to: how to process the results, and request further info on some repo found with gh search repos command?

**Response:**
To process the results and request further information on a repository found with the `gh search repos` command in zsh, you can use the following command:

```zsh
gh search repos <search_query> --json name,url | jq '.items[] | {name: .name, url: .url}'
```

Replace `<search_query>` with your desired search term.

This command uses the `--json` flag to output the search results in JSON format. It then pipes the output to `jq`, a command-line JSON processor, to filter and format the results. The `jq` expression `.items[] | {name: .name, url: .url}` selects the `name` and `url` fields from each item in the search results.

You can modify the `jq` expression to include additional fields or customize the output format according to your needs.

<details><summary>Metadata</summary>

- Duration: 3570 ms
- Datetime: 2023-08-19T15:51:54.582546
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

