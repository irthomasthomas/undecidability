**Prompt:**
Write a comprehensive git commit message for the following diff: ---------------------------------------------------------------- diff --git a/scripts/lists/Add_IDEA.sh b/scripts/lists/Add_IDEA.sh
new file mode 100644
index 0000000..8cccc79
--- /dev/null
+++ b/scripts/lists/Add_IDEA.sh
@@ -0,0 +1,24 @@
+#!/bin/bash
+# Get current Activity
+
+open_after_add() {
+  WINDOW_TITLE=""$Activity"_IDEAS.md"
+  WINDOW_ID=$(xdotool search --name "$WINDOW_TITLE" | head -1)
+  if [ -n "$WINDOW_ID" ]; then
+    xdotool windowactivate --sync "$WINDOW_ID"
+  else
+    kate -n "$FILE_PATH" &
+  fi
+}
+
+active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
+
+Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
+# This needs a separate script to setup the dir on first run.
+
+FILE_PATH=""$HOME"/Activities/"$Activity"/"$Activity"_IDEAS.md"
+
+idea_text=$(kdialog --textinputbox "iDea")
+echo "$idea_text" >> "$FILE_PATH"
+
+# TEMPLATE NOTE: Make "open after add" optional.


Always keep it brief and spiffy!
DO NOT MENTION ANY DOTFILES, eg: .gitignore, .idea/, .git, .directory, or the venv dir.' DO NOT SAY ANYTHING ELSE OTHER THAN THE TEXT OF THE COMMIT MESSAGE.


**Response:**
Add script to add ideas to activity-specific file

This commit adds a new script `Add_IDEA.sh` that allows users to add ideas to an activity-specific file. The script retrieves the current activity and creates a file path based on the activity name. It then prompts the user to enter an idea using `kdialog` and appends the idea to the activity file. Additionally, the commit mentions that the "open after add" feature can be made optional in the future.

Always keep it brief and spiffy!
DO NOT MENTION ANY DOTFILES, eg: .gitignore, .idea/, .git, .directory, or the venv dir.

<details><summary>Metadata</summary>

- Duration: 4505 ms
- Datetime: 2023-07-26T06:56:22.285194
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

