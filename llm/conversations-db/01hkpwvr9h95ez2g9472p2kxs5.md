**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**use fzf to display all jupyter notebooks


**Response:**
```bash
find ~/ -name "*.ipynb" | fzf
```

<details><summary>Metadata</summary>

- Duration: 1261 ms
- Datetime: 2024-01-09T10:39:00.675769
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

**Prompt:**
only display in dir/file format, trim the start of the path string to make it easier to read 

**Response:**
```bash
find ~/ -name "*.ipynb" | fzf | sed -e "s/.*\///"
```

<details><summary>Metadata</summary>

- Duration: 975 ms
- Datetime: 2024-01-09T10:41:05.956839
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

