**Prompt:**
Generate a simple filename in the form of file-name.ext (e.g. ink-check.py) for: coolbin() {
  # Usage: coolbin <file>
  # Database of cool binaries on linux.
  
  if [ ! -f "$1" ]; then
    echo "The specified file does not exist"
    return 1
  fi

  toolname=$(basename "$1")
  toolpath=$(readlink -f "$1")
  
  # Check if the tool has a man page
  if man "$toolname" > /dev/null 2>&1; then 
    manpage=$(man "$toolname")
    manpage_path=$(man -w "$toolname")
    manpage_summary=$(llm "summarise this: $manpage")
  else
    echo "No man page found for $toolname. Checking for help text..."
    if "$toolpath" --help > /dev/null 2>&1; then
      helptext=$("$toolpath" --help)
      manpage_summary=$(llm "summarise this: $helptext")
    elif "$toolpath" -h > /dev/null 2>&1; then
      helptext=$("$toolpath" -h)
      manpage_summary=$(llm "summarise this: $helptext")
    else
      echo "No help text found for $toolname."
      return 1
    fi
  fi

  # Prepare the content for the Obsidian file in Markdown format
  obsidian_file_content="---
layout: language
title:  '$toolname'
date:   $(date)
---

## Description

$manpage_summary

## Usage

\`\`\`
$toolname [options]
\`\`\`

## Help Text

\`\`\`
$helptext
\`\`\`

## Man Page Path

$manpage_path
"

  # Create a Markdown file in the coolbin database with the Obsidian content
  echo "$obsidian_file_content" > "$toolname.md"
  echo "Information stored in the coolbin database"
  return 0
}.

**Response:**
file-name.sh

<details><summary>Metadata</summary>

- Duration: 1071 ms
- Datetime: 2023-07-14T19:56:01.562843
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

