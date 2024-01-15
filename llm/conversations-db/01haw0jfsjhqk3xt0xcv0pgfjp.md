**Prompt:**
Write a bash terminal command to perform the following function, or if impossible, write: echo "That request cannot easily be accomplished in a sigle command. Here is spec describing a script that performs the required functions.": Watch what sql commands are sent to mysqlite.db Be concise.


**Response:**
echo "SELECT * FROM sqlite_master;" | sqlite3 mysqlite.db

<details><summary>Metadata</summary>

- Duration: 1055 ms
- Datetime: 2023-09-21T13:58:47.314626
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

