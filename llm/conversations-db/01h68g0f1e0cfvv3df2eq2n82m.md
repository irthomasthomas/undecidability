**Prompt:**
diff --git a/scripts/lists/Open_Shopping.sh b/scripts/lists/Open_Shopping.sh
new file mode 100644
index 0000000..27848e9
--- /dev/null
+++ b/scripts/lists/Open_Shopping.sh
@@ -0,0 +1,15 @@
+#!/bin/bash
+LISTFILE="SHOPPING_LIST.txt"
+FILE_PATH="$HOME/$LISTFILE"
+idea_text=$(kdialog --textinputbox "Add to Shopping List")
+echo "$idea_text" >> "$FILE_PATH"
+
+WINDOW_TITLE="$LISTFILE"
+
+WINDOW_ID=$(xdotool search --name "$WINDOW_TITLE" | head -1)
+
+if [ -n "$WINDOW_ID" ]; then
+  xdotool windowactivate --sync "$WINDOW_ID"
+else
+  kate -n "$FILE_PATH" &
+fi


**Response:**
Add Open_Shopping.sh script to manage shopping list

<details><summary>Metadata</summary>

- Duration: 828 ms
- Datetime: 2023-07-26T07:00:58.225840
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

