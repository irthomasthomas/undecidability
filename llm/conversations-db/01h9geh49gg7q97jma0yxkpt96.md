**Prompt:**
What is the exact zsh command to: for each jpg, if exiftool -Make = "Xiaomi", mv file to ./Xiaomi/?


**Response:**
for file in *.jpg; do
  if [[ $(exiftool -Make "$file") == "Xiaomi" ]]; then
    mv "$file" ./Xiaomi/
  fi
done

<details><summary>Metadata</summary>

- Duration: 2743 ms
- Datetime: 2023-09-04T15:56:06.136150
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

