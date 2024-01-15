**Prompt:**
What is the exact zsh command to: Make this command case insensitive:  jq '.data[] | select(.title | contains(Git))'?


**Response:**
jq '.data[] | select(.title | contains("Git";"i"))'

<details><summary>Metadata</summary>

- Duration: 803 ms
- Datetime: 2023-08-21T11:16:07.324739
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

