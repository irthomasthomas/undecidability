**Prompt:**
What is the exact zsh command to: update the function: clip () {
	echo "$1" | xclip -selection clipboard
} in /home/tommy/Development/scripts/shell_functions.sh to first echo display and xsel instead if display?

**Response:**
sed -i 's/xclip -selection clipboard/xsel -b/g' /home/tommy/Development/scripts/shell_functions.sh

<details><summary>Metadata</summary>

- Duration: 1319 ms
- Datetime: 2023-08-19T16:08:17.630264
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

