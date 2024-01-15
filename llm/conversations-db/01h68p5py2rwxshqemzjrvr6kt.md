**Prompt:**
Write a single script to replace all three scripts #!/bin/bash
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

# Get current Activity
CATEGORY="CODE_SNIPPET"
GLOBAL="TRUE"

open_after_add() {
  WINDOW_TITLE="$Activity_$CATEGORY.md"
  WINDOW_ID=$(xdotool search --name "$WINDOW_TITLE" | head -1)
  if [ -n "$WINDOW_ID" ]; then
    xdotool windowactivate --sync "$WINDOW_ID"
  else
    kate -n "$FILE_PATH" &
  fi
}

get_activity() {
  # May need to mkdir
  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
  Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
}

set_filepath() {
  # May need to mkdir
  FILE_PATH="$HOME/Activities/$Activity/$Activity_$CATEGORY.md"
}

add_idea() {
  text=$(kdialog --textinputbox "iDea")
  echo "$text" >> "$FILE_PATH"
}

add_thought() {
  text=$(kdialog --textinputbox "THOUGHTS")
  echo "$text" >> "$FILE_PATH"
}

if [ "$CATEGORY" == "CODE_SNIPPET" ]; then
  [$GLOBAL -eq "TRUE"] || get_activity
  set_filepath
  add_idea
  open_after_add
elif [ "$CATEGORY" == "THOUGHTS" ]; then
  [$GLOBAL -eq "TRUE"] || get_activity
  set_filepath
  add_thought
  open_after_add
fi

<details><summary>Metadata</summary>

- Duration: 11668 ms
- Datetime: 2023-07-26T08:48:30.764818
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

