**Prompt:**
What is the exact zsh command to: for page in {man -k "^gh-"} do man $page | ttok?


**Response:**
for page in $(man -k "^gh-"); do man $page | ttok; done

<details><summary>Metadata</summary>

- Duration: 1452 ms
- Datetime: 2023-08-24T11:17:19.687012
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

