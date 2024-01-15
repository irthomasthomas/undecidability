**Prompt:**
Write a single genereric script, that takes paramaters, to replace all three scripts as well as being able to accept future scripts #!/bin/bash
# Get current Activity

open_after_add() {
  WINDOW_TITLE=""$Activity"_IDEAS.md"
  WINDOW_ID=$(xdotool search --name "$WINDOW_TITLE" | head -1)
  if [ -n "$WINDOW_ID" ]; then
    xdotool windowactivate --sync "$WINDOW_ID"
  else
    kate -n "$FILE_PATH" &
  fi
}

active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)

Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
# This needs a separate script to setup the dir on first run.

FILE_PATH=""$HOME"/Activities/"$Activity"/"$Activity"_IDEAS.md"

idea_text=$(kdialog --textinputbox "iDea")
echo "$idea_text" >> "$FILE_PATH"

# TEMPLATE NOTE: Make "open after add" optional.

#!/bin/bash
# Get current Activity
CATEGORY="CODE_SNIPPET"
GLOBAL="TRUE"

open_after_add() {
  WINDOW_TITLE=""$Activity"_"$CATEGORY".md"
  WINDOW_ID=$(xdotool search --name "$WINDOW_TITLE" | head -1)
  if [ -n "$WINDOW_ID" ]; then
    xdotool windowactivate --sync "$WINDOW_ID"
  else
    kate -n "$FILE_PATH" &
  fi
}

get_activity() {
  # May need2 mkdir
  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
  Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
}



[$GLOBAL -eq "TRUE"] || get_activity; FILE_PATH=""$HOME"/Activities/"$Activity"/"$Activity"_"$CATEGORY".md"



FILE_PATH=""$HOME"/Activities/"$Activity"/"$Activity"_"$CATEGORY".md"

text=$(kdialog --textinputbox "iDea")
echo "$text" >> "$FILE_PATH"

#!/bin/bash
# Get current Activity

CATEGORY="THOUGHTS"
GLOBAL="TRUE"

get_activity() {
  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
  Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
}

set_filepath() {
  # May need to mkdir.
  FILE_PATH=""$HOME"/Activities/"$Activity"/"$Activity"_"$CATEGORY".md"
}

[$GLOBAL -eq "TRUE"] || get_activity && set_filepath

FILE_PATH="$HOME/$CATEGORY.md"

# TEMPLATE $CATEGORY

text=$(kdialog --textinputbox "$CATEGORY")
echo "$text" >> "$FILE_PATH"

WINDOW_TITLE=""$Activity"_"$CATEGORY".md"

WINDOW_ID=$(xdotool search --name "$WINDOW_TITLE" | head -1)

if [ -n "$WINDOW_ID" ]; then
  xdotool windowactivate --sync "$WINDOW_ID"
else
  kate -n "$FILE_PATH" &
fi


**Response:**
#!/bin/bash

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
  [[ -n "$WINDOW_ID" ]] && xdotool windowactivate --sync "$WINDOW_ID" || kate -n "$FILE_PATH" &
}

# Main function to handle input and file operations
main() {
  CATEGORY=$1
  GLOBAL=$2

  [[ $GLOBAL == "TRUE" ]] || get_activity && set_filepath

  text=$(kdialog --textinputbox "$CATEGORY")
  [[ -z "$text" ]] && echo "You did not provide any input" && exit 1

  echo "$text" >> "$FILE_PATH"
  open_after_add
}

# Call main function with arguments
main "$@"

<details><summary>Metadata</summary>

- Duration: 21708 ms
- Datetime: 2023-07-26T08:57:49.585774
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

**Prompt:**
add a Open_After input paramater that defines if the main list should be opened after input

**Response:**
#!/bin/bash

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
  [[ -n "$WINDOW_ID" ]] && xdotool windowactivate --sync "$WINDOW_ID" || kate -n "$FILE_PATH" &
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
main "$@"

<details><summary>Metadata</summary>

- Duration: 22716 ms
- Datetime: 2023-07-26T09:09:51.992427
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

