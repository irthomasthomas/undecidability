**Prompt:**
diff --git a/scripts/lists/Add_THOUGHTS.sh b/scripts/lists/Add_THOUGHTS.sh
new file mode 100644
index 0000000..75798e7
--- /dev/null
+++ b/scripts/lists/Add_THOUGHTS.sh
@@ -0,0 +1,34 @@
+#!/bin/bash
+# Get current Activity
+
+CATEGORY="THOUGHTS"
+GLOBAL="TRUE"
+
+get_activity() {
+  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
+  Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
+}
+
+set_filepath() {
+  # May need to mkdir.
+  FILE_PATH=""$HOME"/Activities/"$Activity"/"$Activity"_"$CATEGORY".md"
+}
+
+[$GLOBAL -eq "TRUE"] || get_activity && set_filepath
+
+FILE_PATH="$HOME/$CATEGORY.md"
+
+# TEMPLATE $CATEGORY
+
+text=$(kdialog --textinputbox "$CATEGORY")
+echo "$text" >> "$FILE_PATH"
+
+WINDOW_TITLE=""$Activity"_"$CATEGORY".md"
+
+WINDOW_ID=$(xdotool search --name "$WINDOW_TITLE" | head -1)
+
+if [ -n "$WINDOW_ID" ]; then
+  xdotool windowactivate --sync "$WINDOW_ID"
+else
+  kate -n "$FILE_PATH" &
+fi


**Response:**
Add script for adding thoughts to a specific category

<details><summary>Metadata</summary>

- Duration: 828 ms
- Datetime: 2023-07-26T07:00:18.260270
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

