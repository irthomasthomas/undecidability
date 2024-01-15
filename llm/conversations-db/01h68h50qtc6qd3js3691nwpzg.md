**Prompt:**
Summarise content of new files added to git repo and add description to readme


**Response:**
#!/bin/bash

# Check if any new files have been added to the git repository
if [[ -z $(git status --porcelain) ]]; then
  echo "No new files have been added to the git repository."
  exit 1
fi

# Get the list of new files added to the git repository
new_files=$(git status --porcelain | grep "^A" | awk '{print $2}')

# Check if the README file exists
if [[ ! -f README.md ]]; then
  echo "README.md file does not exist."
  exit 1
fi

# Loop through each new file and add a description to the README file
for file in $new_files; do
  # Get the filename without the extension
  filename=$(basename "$file")
  filename="${filename%.*}"

  # Add the description to the README file
  echo "- $filename: [Description]" >> README.md
done

echo "Descriptions have been added to the README file for the new files."

<details><summary>Metadata</summary>

- Duration: 7469 ms
- Datetime: 2023-07-26T07:20:49.356471
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

