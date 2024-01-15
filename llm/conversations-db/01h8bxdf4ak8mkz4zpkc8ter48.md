**Prompt:**
What is the exact zsh command to: think carefully. Can you write a better way to do this that is case insensitive? /n jq .data[] | select(.title | contains("Git"))?


**Response:**
jq .data[] | select(.title | contains("git";"i"))

<details><summary>Metadata</summary>

- Duration: 808 ms
- Datetime: 2023-08-21T11:24:22.753015
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

**Prompt:**
jq: error: contains/2 is not defined at <top-level>, line 1:
.data[] | select(.title | contains("Git";"i"))                          
jq: 1 compile error

**Response:**
jq .data[] | select(.title | test("git";"i"))

<details><summary>Metadata</summary>

- Duration: 930 ms
- Datetime: 2023-08-21T11:25:30.495546
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

