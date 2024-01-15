**Prompt:**
Summarise content of new files added to git repo and add description to readme


**Response:**
#!/bin/bash

# Check if the input is empty
if [ -z "$1" ]; then
  echo "Error: No input provided. Please specify a git repository."
  exit 1
fi

# Navigate to the git repository
cd "$1"

# Get the list of new files added to the repository
new_files=$(git diff --name-only --diff-filter=A HEAD~1..HEAD)

# Check if there are no new files
if [ -z "$new_files" ]; then
  echo "No new files added to the repository."
  exit 0
fi

# Print the summary of new files
echo "Summary of new files added to the repository:"
for file in $new_files; do
  echo "- $file"
done

# Ask for file descriptions and update the readme
echo "Adding descriptions to the readme file:"
for file in $new_files; do
  echo "Enter description for $file:"
  read description
  echo "- $file: $description" >> readme.txt
done

echo "Descriptions added to the readme file."

<details><summary>Metadata</summary>

- Duration: 7826 ms
- Datetime: 2023-07-26T07:16:45.514883
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

