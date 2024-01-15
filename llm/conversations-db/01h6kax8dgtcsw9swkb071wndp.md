**Prompt:**
Generate a simple filename in the form of file-name.ext (e.g. ink-check.py) for this:\n #!/bin/bash

# Define function to get current activity
get_activity() {
  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
  Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
}

# Define function to set file path
set_filepath() {
  FILE_PATH="$HOME/Activities/$Activity/${Activity}_$CATEGORY.md"
}

# Define function to open file after adding
open_after_add() {
  WINDOW_TITLE="${Activity}_${CATEGORY}.md"
  WINDOW_ID=$(xdotool search --name "$WINDOW_TITLE" | head -1)
  [[ -n "$WINDOW_ID" ]] && xdotool windowactivate --sync "$WINDOW_ID" || fleet -n "$FILE_PATH" &
}

# Main function to handle input and file operations
main() {
  CATEGORY=$1
  GLOBAL=$2
  OPEN_AFTER=$3

  [[ $GLOBAL == "TRUE" ]] || get_activity && set_filepath

  text=$(kdialog --textinputbox "$CATEGORY")
  [[ -z "$text" ]] && echo "You did not provide any input" && exit 1

  echo "$text" >> "$FILE_PATH"

  [[ $OPEN_AFTER == "TRUE" ]] && open_after_add
}

# Call main function with arguments
main "$@".

**Response:**
get-activity.sh

<details><summary>Metadata</summary>

- Duration: 782 ms
- Datetime: 2023-07-30T12:03:29.056983
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

