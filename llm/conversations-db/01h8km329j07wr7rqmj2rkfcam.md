**Prompt:**
What is the exact zsh command to: for page in {man -k "^gh-"} | ttok $page?


**Response:**
for page in $(man -k "^gh-"); do ttok $page; done

<details><summary>Metadata</summary>

- Duration: 1511 ms
- Datetime: 2023-08-24T11:15:19.498646
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

