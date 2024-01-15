**Prompt:**
diff --git a/tdrop/fleet-streamdeck-window.sh b/tdrop/fleet-streamdeck-window.sh
new file mode 100644
index 0000000..e72ab18
--- /dev/null
+++ b/tdrop/fleet-streamdeck-window.sh
@@ -0,0 +1,21 @@
+#!/bin/bash
+#window_title='DB Browser for SQLite - /home/thomas/.config/io.datasette.llm/logs.db'
+search_string="StreamDeck"
+
+window_ids=$(xdotool search --onlyvisible --class "jetbrains-fleet")
+
+for window_id in $window_ids; do
+    # Get the class and name of the current window
+    window_class=$(xdotool getwindowclassname $window_id)
+    window_name=$(xdotool getwindowname $window_id)
+
+    # Check if the class and name match the desired criteria
+    if [[ $window_class == *"jetbrains-fleet"* ]] && [[ $window_name == *"$search_string"* ]]; then
+        echo "found window. Activating $window_id"
+        xdotool windowactivate $window_id
+        exit
+    fi
+done
+echo "opening fleet"
+fleet /home/thomas/Development/Projects/StreamDeck-Group/StreamDeck
+
diff --git a/tdrop/sqlitebrowser-llmdb-window.sh b/tdrop/sqlitebrowser-llmdb-window.sh
index 7391396..d87d7e6 100644
--- a/tdrop/sqlitebrowser-llmdb-window.sh
+++ b/tdrop/sqlitebrowser-llmdb-window.sh
@@ -15,5 +15,5 @@ if xdotool search --name "$window_title"; then
     fi
 else
   echo "The window with title $window_title does not exist."
-  sqlitebrowser "$(llm logs path)" & 
+  sqlitebrowser "$(llm logs path)" &
 fi
\ No newline at end of file


**Response:**
Add fleet-streamdeck-window.sh and sqlitebrowser-llmdb-window.sh scripts

<details><summary>Metadata</summary>

- Duration: 3184 ms
- Datetime: 2023-10-16T20:39:28.600918
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

