**Prompt:**
Write a comprehensive git commit message for the following diff: ---------------------------------------------------------------- diff --git a/scripts/lists/Add_SNIPPET.sh b/scripts/lists/Add_SNIPPET.sh
new file mode 100644
index 0000000..9f11c5b
--- /dev/null
+++ b/scripts/lists/Add_SNIPPET.sh
@@ -0,0 +1,31 @@
+#!/bin/bash
+# Get current Activity
+CATEGORY="CODE_SNIPPET"
+GLOBAL="TRUE"
+
+open_after_add() {
+  WINDOW_TITLE=""$Activity"_"$CATEGORY".md"
+  WINDOW_ID=$(xdotool search --name "$WINDOW_TITLE" | head -1)
+  if [ -n "$WINDOW_ID" ]; then
+    xdotool windowactivate --sync "$WINDOW_ID"
+  else
+    kate -n "$FILE_PATH" &
+  fi
+}
+
+get_activity() {
+  # May need2 mkdir
+  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
+  Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
+}
+
+
+
+[$GLOBAL -eq "TRUE"] || get_activity; FILE_PATH=""$HOME"/Activities/"$Activity"/"$Activity"_"$CATEGORY".md"
+
+
+
+FILE_PATH=""$HOME"/Activities/"$Activity"/"$Activity"_"$CATEGORY".md"
+
+text=$(kdialog --textinputbox "iDea")
+echo "$text" >> "$FILE_PATH"


Always keep it brief and spiffy!
DO NOT MENTION ANY DOTFILES, eg: .gitignore, .idea/, .git, .directory, or the venv dir.' DO NOT SAY ANYTHING ELSE OTHER THAN THE TEXT OF THE COMMIT MESSAGE.


**Response:**
Add script to add code snippets to activity-specific markdown file

<details><summary>Metadata</summary>

- Duration: 844 ms
- Datetime: 2023-07-26T06:53:01.736996
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

