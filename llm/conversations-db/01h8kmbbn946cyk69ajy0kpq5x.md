**Prompt:**
What is the exact zsh command to: how to search for man pages and pipe the man page for each result??


**Response:**
apropos keyword | awk '{print $1}' | xargs -n1 man

<details><summary>Metadata</summary>

- Duration: 3447 ms
- Datetime: 2023-08-24T11:19:49.297553
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

