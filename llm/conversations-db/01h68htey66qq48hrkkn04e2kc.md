**Prompt:**
Summarise content of new files added to git repo and add description to readme


**Response:**
#!/bin/bash

# Check if there are any new files added to the git repo
if [[ -n $(git status --porcelain) ]]; then
  # Get the list of new files
  new_files=$(git status --porcelain | grep "^A" | awk '{print $2}')
  
  # Loop through each new file
  for file in $new_files; do
    # Get the content summary of the file
    summary=$(git diff --stat HEAD $file)
    
    # Add the content summary to the readme file
    echo "$summary" >> README.md
  done
  
  echo "Content summary of new files added to git repo has been added to README.md"
else
  echo "No new files added to git repo"
fi

<details><summary>Metadata</summary>

- Duration: 5805 ms
- Datetime: 2023-07-26T07:32:33.687975
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

