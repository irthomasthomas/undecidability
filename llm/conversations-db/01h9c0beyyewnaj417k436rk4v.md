**Prompt:**
What is the exact zsh command to: grep "shot-scraper" ~/.zhistory     let user interactively select a result to copy?


**Response:**
grep "shot-scraper" ~/.zhistory | fzf --preview 'echo {}' | awk '{print $2}' | xclip -selection clipboard

<details><summary>Metadata</summary>

- Duration: 1430 ms
- Datetime: 2023-09-02T22:31:23.974623
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

