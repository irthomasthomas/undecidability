**Prompt:**
Write a bash terminal command to search for deleted files on an ssd Be concise, but include as much code as needed. Do not write anything else. Ever.


**Response:**
sudo grep -a -B 100 -A 100 'search_term' /dev/sdaX > output.txt

<details><summary>Metadata</summary>

- Duration: 4665 ms
- Datetime: 2023-10-11T10:53:09.233286
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

