**Prompt:**
view my own repos only

**Response:**
To view your own repositories only, you can use the following command:

```
gh s -E -u @me
```

This command uses the `-u` flag to specify that you want to search for repositories owned by the currently authenticated user (`@me`). The `-E` flag is used to filter the results to only show repository URLs.

You can also set an alias for this command to make it easier to execute in the future. For example, you can set the alias `mine` for this command using the following command:

```
gh alias set mine 's -E -u @me'
```

After setting the alias, you can simply execute `gh mine` to view your own repositories.

<details><summary>Metadata</summary>

- Duration: 4237 ms
- Datetime: 2023-08-28T12:46:45.236195
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

