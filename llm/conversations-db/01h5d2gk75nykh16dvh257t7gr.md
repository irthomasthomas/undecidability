**Prompt:**
Quickly, what is the exact bash command to change editor to kate for both ~/.zshrc and ~/.bashrc ?
Reply only with the exact command text and nothing else before or after.

**Response:**
sed -i 's/^export EDITOR=.*/export EDITOR=kate/' ~/.zshrc ~/.bashrc

<details><summary>Metadata</summary>

- Duration: 1313 ms
- Datetime: 2023-07-15T15:25:36.579573
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

