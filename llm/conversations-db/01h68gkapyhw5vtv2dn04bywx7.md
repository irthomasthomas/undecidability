**Prompt:**
DO NOT USE MARKDOWN.
Reply only with the text of the bash script and nothing else. Use inline code comments if you need to say anything else.
Think it through step-by-step.
Requirements (If the line is blank after this, then the user input failed. Tell the user that they did not provide any input.): Summarise content of new files added to git repo and add description to readme
Additional Goals:
  - Minimise IF statements and branching.
  - Write intelligent, self-documenting code.
  - Minimise duplication. Minimise Verbosity.
  - Write code that is modern, clean and fast.

WARNING: Do not include a markdown code block.
Beware of bugs and tricky syntax. SAY NOTHING ELSE!


**Response:**
#!/bin/bash

# Get new files added to git
new_files=$(git status --porcelain | grep '^??' | cut -c 4-)

# Check if new files exist
if [[ -z "$new_files" ]]
then
    echo "No new files added"
else
    readme='README.md'

    # Summarise content of new files and add description to readme
    for file in $new_files
    do
        # Create summary of file content
        summary=$(head -10 "$file")
        # Add file name and description to readme
        echo -e "\n## $file" >> $readme
        echo -e "\n$summary" >> $readme
    done

    echo "Description of new files added to README.md"
fi

<details><summary>Metadata</summary>

- Duration: 16095 ms
- Datetime: 2023-07-26T07:11:01.118349
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

