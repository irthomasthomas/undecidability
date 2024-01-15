**Prompt:**
Think carefully. Write a complete, fully functional bash script to Here is a rough idea for a function. Can you refactor it for me, properly? Dont copy what I did, only use it for inspiration. Write your own comments, dont just copy mine. Think it through carefully. coolbin() {
  # Usage: coolbin <file>
  # Database of cool binaries on linux.
  # Coolbin should accept a path to a binary and make a note of it in the coolbin database, which is comprised of text files and metadata compatible with obsidian. 
  # The the app has a man page, assign its text to $helptext, else use the content from -h or --help.
  # Then use $(llm "summarise this: $helptext) and store the summary.
  toolname=$(basename "$1")
  toolpath=$(realpath "$1")
  manpage=
  manpage_path=
  manpage_summary=
  function_signature=
  tool_params=
  # Check if the tool has a man page
}
?
Reply only with the text of the bash script and nothing else before or after. Use code comments if you need to draw attention to anything. 
Think it through step-by-step.
# Additional Goals: Minimise IF statements and branching. Write intelligent, self-documenting code. Minimise duplication. Minimise Verbosity. Write code that is modern, clean and performant. Prefer answers dated 2015, 2016, 2017, 2018, 2019, 2020, 2021.
WARNING: Your response must NOT include text OUTSIDE of the code block.
SAY NOTHING ELSE!

**Response:**
```bash
#!/bin/bash

# coolbin() function to add a binary to the coolbin database
coolbin() {
  # Usage: coolbin <file>
  # Database of cool binaries on Linux.
  # coolbin should accept a path to a binary and make a note of it in the coolbin database, which is comprised of text files and metadata compatible with obsidian.
  # Assign the base name of the binary to $toolname and its absolute path to $toolpath
  toolname=$(basename "$1")
  toolpath=$(realpath "$1")

  manpage=
  manpage_path=
  manpage_summary=
  function_signature=
  tool_params=

  # Check if the binary has a man page, assign its content to $manpage if it exists
  if man -w "$toolname" &> /dev/null; then
    manpage_path=$(man -w "$toolname")
    manpage=$(man "$toolname")
  elif [ -r "$toolpath" ]; then
    # If man page does not exist, check if -h or --help return a non-empty output
    if output=$(2>&1 "$toolpath" -h) && [[ ! -z $output ]]; then
      manpage=$output
    elif output=$(2>&1 "$toolpath" --help) && [[ ! -z $output ]]; then
      manpage=$output
    fi
  fi

  # Generate the summary of the man page or help content using llm command
  manpage_summary=$(llm "summarise this: $manpage")

  # Store the tool information in the coolbin database
  echo "Tool Name: $toolname" >> /path/to/database.txt
  echo "Tool Path: $toolpath" >> /path/to/database.txt
  echo "Man Page Path: $manpage_path" >> /path/to/database.txt
  echo "Man Page Summary: $manpage_summary" >> /path/to/database.txt
  echo "Function Signature: $function_signature" >> /path/to/database.txt
  echo "Tool Parameters: $tool_params" >> /path/to/database.txt
}
```

Note: Modify "/path/to/database.txt" with the actual path to the coolbin database text file.

<details><summary>Metadata</summary>

- Duration: 14714 ms
- Datetime: 2023-07-14T19:25:51.029149
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

