**Prompt:**
Quickly, what is the exact bash command to Script that takes a dir path as $1. Get the lastfile modified with ls -lt | head -2. Then ask for user confirmation before deleting the $lastfile.?
Reply only with the exact command text and nothing else before or after.

**Response:**
read -p "Are you sure you want to delete $(ls -lt $1 | awk 'NR==2{print $9}')? (Y/N) " confirm && [[ $confirm == [Yy] ]] && rm -f $(ls -lt $1 | awk 'NR==2{print $9}')

<details><summary>Metadata</summary>

- Duration: 3182 ms
- Datetime: 2023-07-14T12:34:10.810623
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

