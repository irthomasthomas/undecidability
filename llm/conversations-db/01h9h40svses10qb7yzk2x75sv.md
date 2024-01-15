**Prompt:**
What is the exact zsh command to: loop over every man page?


**Response:**
for page in /usr/share/man/man*/*; do
    man "$page"
done

<details><summary>Metadata</summary>

- Duration: 1439 ms
- Datetime: 2023-09-04T22:11:41.145671
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

