**Prompt:**
What is the exact zsh command to: get sqlite db schema?


**Response:**
sqlite3 -header -column <database_name> "PRAGMA table_info(<table_name>);"

<details><summary>Metadata</summary>

- Duration: 1742 ms
- Datetime: 2023-08-23T17:58:29.427231
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

