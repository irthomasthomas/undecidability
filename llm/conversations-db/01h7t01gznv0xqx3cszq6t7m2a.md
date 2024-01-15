**Prompt:**
five awesome bash scripts

**Response:**

```bash
#!/bin/bash

# Count number of lines in a file
function count_lines {
  wc -l $1
}

# Count number of words in a file
function count_words {
  wc -w $1
}

# Count number of characters in a file
function count_chars {
  wc -m $1
}

# Count number of lines, words, and characters in a file
function count_all {
  count_lines $1
  count_words $1
  count_chars $1
}

# Copy a file
function copy_file {
  cp $1 $2
}

# Move a file
function move_file {
  mv $1 $2
}

# Delete a file
function delete_file {
  rm $1
}

# Print a message to the console
function print_message {
  echo $1
}
```

<details><summary>Metadata</summary>

- Duration: 13911 ms
- Datetime: 2023-08-14T12:23:44.284810
- Model: mlc-chat-WizardCoder-15B-V1.0-q4f16_1

</details>

**Options:**
```json
{}
```

