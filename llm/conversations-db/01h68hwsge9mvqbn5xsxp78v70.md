**Prompt:**
Summarise content of new files added to git repo and add description to readme


**Response:**
```bash
#!/bin/bash

# Get the list of new files added to the git repository
new_files=$(git diff --name-only --diff-filter=A)

# Check if there are any new files
if [[ -z $new_files ]]; then
  echo "No new files added to the git repository."
  exit 0
fi

# Loop through each new file and summarize its content
for file in $new_files; do
  echo "Summary of $file:"
  head -n 5 $file
  echo
done

# Add a description of the new files to the README file
echo "New files added to the git repository:" >> README.md
echo >> README.md
for file in $new_files; do
  echo "- $file" >> README.md
done

echo "Summary and description added to README.md."
```


<details><summary>Metadata</summary>

- Duration: 7118 ms
- Datetime: 2023-07-26T07:33:48.735335
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

