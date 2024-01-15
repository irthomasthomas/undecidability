**Prompt:**
Summarise content of new files added to git repo and add description to readme


**Response:**
#!/bin/bash

# Check if there are any new files in the git repository
if [[ -z $(git status --porcelain) ]]; then
  echo "No new files added to the git repository."
  exit 0
fi

# Get the list of new files added to the git repository
new_files=$(git status --porcelain | grep "^A" | awk '{print $2}')

# Loop through each new file
for file in $new_files; do
  # Get the content of the file
  content=$(cat $file)

  # Summarize the content of the file
  summary=$(echo $content | head -n 1)

  # Add the summary to the README file
  echo "- $summary" >> README.md
done

echo "Summary of new files added to the git repository has been added to README.md."

<details><summary>Metadata</summary>

- Duration: 5597 ms
- Datetime: 2023-07-26T07:29:32.171125
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

