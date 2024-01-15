**Prompt:**
Quickly, what is the exact bash command to for dir in ${(s.:.)PATH}; do for file in $dir/*; do echo $file; done; done results in error: no matches found: /usr/local/bin/*?
Reply only with the exact command text and nothing else before or after.

**Response:**
for dir in ${(s.:.)PATH}; do for file in $dir/*; do echo $file; done; done

<details><summary>Metadata</summary>

- Duration: 2356 ms
- Datetime: 2023-07-15T11:18:00.092977
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

