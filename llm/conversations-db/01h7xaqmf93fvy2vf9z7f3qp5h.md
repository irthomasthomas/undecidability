**Prompt:**
What is the exact zsh command to: search github api simonw/llm repo for issues containing the word constrain?

**Response:**
curl -s "https://api.github.com/search/issues?q=repo:simonw/llm+constrain" | jq '.items[].title'

<details><summary>Metadata</summary>

- Duration: 1567 ms
- Datetime: 2023-08-15T19:28:30.153710
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

