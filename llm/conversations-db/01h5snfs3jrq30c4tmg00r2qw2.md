**Prompt:**

Reply only with the text of the bash script and nothing else before or after. Use code comments if you need to draw attention to anything. 
Think it through step-by-step.
# Additional Goals: Minimise IF statements and branching. Write intelligent, self-documenting code. Minimise duplication. Minimise Verbosity. Write code that is modern, clean and fast. Prefer answers dated 2015, 2016, 2017, 2018, 2019, 2020, 2021.
WARNING: Your response must NOT include text OUTSIDE of the code block. Beware of bugs and tricky syntax. SAY NOTHING ELSE!


**Response:**
```bash
#!/bin/bash

# Target filename
FILE="my_database"
# Define empty string cleanup function
function cleanup() {
  # Temporary backup file prefix
  local TMP_STRING="_temp"
  local DATE=$(date +"%m%d%Y_%H%M%S")

  # Rename the original file to a temporary backup
  mv ${FILE} ${FILE}${TMP_STRING}_${DATE}

  # Use awk to remove all empty strings inside the file.
  awk -v RS= '!NF{$1=$1};1' ${FILE}${TMP_STRING}_${DATE} > ${FILE}

  # Print completion message and return
  echo "${FILE} has been cleaned of empty strings."
}

# Run the cleanup function
cleanup
```

<details><summary>Metadata</summary>

- Duration: 15726 ms
- Datetime: 2023-07-20T12:47:51.555676
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

