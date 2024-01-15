**Prompt:**
Summarise content of new files added to git repo and add description to readme


**Response:**
#!/bin/bash

# Check if any input is provided
if [ -z "$1" ]; then
  echo "No input provided."
  exit 1
fi

# Get the list of new files added to the git repo
new_files=$(git diff --name-only --diff-filter=A)

# Check if there are any new files
if [ -z "$new_files" ]; then
  echo "No new files added to the git repo."
  exit 0
fi

# Iterate over the new files
for file in $new_files; do
  # Get the content of the file
  content=$(cat "$file")

  # Summarize the content of the file
  summary=$(echo "$content" | head -n 1)

  # Add the summary to the readme file
  echo "$summary" >> README.md
done

exit 0

<details><summary>Metadata</summary>

- Duration: 5960 ms
- Datetime: 2023-07-26T07:22:11.648880
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

