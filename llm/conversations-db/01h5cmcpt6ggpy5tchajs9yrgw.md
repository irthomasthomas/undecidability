**Prompt:**
Quickly, what is the exact bash command to for dir in ${(s.:.)PATH}; do for file in $dir/*; do echo $file; done; done error: no matches found: /usr/local/bin/*?
Reply only with the exact command text and nothing else before or after.

**Response:**
for dir in $(echo $PATH | tr ":" " "); do for file in $dir/*; do echo $file; done; done

<details><summary>Metadata</summary>

- Duration: 1833 ms
- Datetime: 2023-07-15T11:18:48.605060
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

