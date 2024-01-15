**Prompt:**
mkfilename() {
  file_content="$1"
  # Truncate to <=400 tokens
  trunc_content=$(ttok "$file_content" -t 400)
  llm_template="makefilename"
  echo "$trunc_content" | llm -m 3.5 -t $llm_template -o temperature 0 -o max_tokens 15
  }


**Response:**
To generate a file name for the supplied input, you can use the following

<details><summary>Metadata</summary>

- Duration: 1170 ms
- Datetime: 2023-08-25T16:45:07.642632
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0, "max_tokens": 15}
```

