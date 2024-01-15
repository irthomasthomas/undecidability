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
```bash
#!/bin/bash

# Check if user input is provided
if [ -z "${1}" ]; then
  echo "No input provided"
  exit 1
fi

# Store the user input in a variable
file_path="${1}"

# Check if the file path is a git repository
if ! git -C "${file_path}" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Invalid git repository"
  exit 1
fi

# Get the list of new files added to the git repository
new_files=$(git -C "${file_path}" diff --diff-filter=A --name-only)

# Check if there are any new files
if [ -z "${new_files}" ]; then
  echo "No new files added"
  exit 1
fi

# Initialize an empty string to store the summary of new file content
summary=""

# Iterate over each new file
for file in ${new_files}; do
  # Get the content of the file and store it in a variable
  content=$(cat "${file}")

  # Generate a summary of the file content
  file_summary="${file}: $(echo "${content}" | sed -n '3p')"

  # Add the file summary to the overall summary
  summary="${summary}${file_summary}\n"
done

# Append the summary to the readme file
echo -e "${summary}" >> "${file_path}/readme.txt"
```

<details><summary>Metadata</summary>

- Duration: 9866 ms
- Datetime: 2023-07-26T07:04:28.227045
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

