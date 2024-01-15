**Prompt:**
What is the exact zsh command to: for file in $PATH; check if it is script file with a #!, if it is, print the file path?

**Response:**
for file in $PATH; do
    if [[ -x $file && -f $file && $(head -n 1 $file) == "#!"* ]]; then
        echo $file
    fi
done

<details><summary>Metadata</summary>

- Duration: 2041 ms
- Datetime: 2023-08-15T17:57:58.762400
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

