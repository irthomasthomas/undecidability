**Prompt:**
Summarise content of new files added to git repo and add description to readme


**Response:**
#!/bin/bash

# Check if there are any new files added to the git repository
if [[ -z $(git status --porcelain) ]]; then
  echo "No new files added to the git repository."
  exit 0
fi

# Get the list of new files added to the git repository
new_files=$(git status --porcelain | grep "^A" | awk '{print $2}')

# Check if there are any new files
if [[ -z $new_files ]]; then
  echo "No new files added to the git repository."
  exit 0
fi

# Loop through each new file
for file in $new_files; do
  # Get the content of the file
  content=$(cat $file)

  # Summarize the content of the file
  summary=$(echo $content | head -n 1)

  # Add the summary to the README file
  echo "- $summary" >> README.md
done

echo "Summary of new files added to the git repository has been added to the README file."

<details><summary>Metadata</summary>

- Duration: 7322 ms
- Datetime: 2023-07-26T07:27:56.036115
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

