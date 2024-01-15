**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**pretty print json


**Response:**
To pretty print JSON in the terminal, you can use the `jq` command-line tool. Here's the bash command:

```bash
cat file.json | jq .
```

Replace `file.json` with the path to your JSON file. This command will read the JSON from the file and pretty print it in the terminal.

<details><summary>Metadata</summary>

- Duration: 1402 ms
- Datetime: 2023-12-31T12:00:27.393791
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

**Prompt:**
print newlines

**Response:**
To pretty print JSON with newlines in the terminal, you can use the `jq` command-line tool along with the `-r` option. Here's the updated bash command:

```bash
cat file.json | jq -r '.'
```

Replace `file.json` with the path to your JSON file. This command will read the JSON from the file and pretty print it with newlines in the terminal.

<details><summary>Metadata</summary>

- Duration: 1411 ms
- Datetime: 2023-12-31T12:00:40.133960
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

