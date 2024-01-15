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

- Duration: 1437 ms
- Datetime: 2023-12-30T22:16:18.530653
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

**Prompt:**
print newlines

**Response:**
To pretty print JSON with newlines in the terminal, you can use the `jq` command-line tool with the `-r` option and `echo`. Here's the bash command:

```bash
cat file.json | jq -r '.' | echo
```

Replace `file.json` with the path to your JSON file. This command will read the JSON from the file, pretty print it with newlines, and print it in the terminal.

<details><summary>Metadata</summary>

- Duration: 1912 ms
- Datetime: 2023-12-30T22:17:32.379921
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

**Prompt:**
print newlines

**Response:**
To print newlines between each JSON element, you can use the `jq` command-line tool with the `-r` option and `echo -e`. Here's the bash command:

```bash
cat file.json | jq -r '.[] | tostring' | echo -e
```

Replace `file.json` with the path to your JSON file. This command will read the JSON from the file, convert each JSON element to a string, separates them with newlines, and prints them in the terminal. The `-e` option for `echo` enables interpretation of backslash escapes, including newline `\n`.

<details><summary>Metadata</summary>

- Duration: 1956 ms
- Datetime: 2023-12-30T22:17:53.487035
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

