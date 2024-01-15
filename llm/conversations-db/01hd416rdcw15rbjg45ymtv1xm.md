**Prompt:**
diff --git a/.fleet/settings.json b/.fleet/settings.json
new file mode 100644
index 0000000..91c4771
--- /dev/null
+++ b/.fleet/settings.json
@@ -0,0 +1,6 @@
+{
+    "toolchains": [],
+    "editor.formatOnSave": true,
+    "nodejs.editor.formatOnSave.eslint.mode": "Auto",
+    "nodejs.editor.formatOnSave.prettier.mode": "Auto"
+}
\ No newline at end of file
diff --git a/streamdeck.service b/streamdeck.service
new file mode 100644
index 0000000..84a7979
--- /dev/null
+++ b/streamdeck.service
@@ -0,0 +1,7 @@
+[Unit]
+Description=Remove streamdeck-windows directory on startup
+[Service]
+Type=oneshot
+ExecStart=/bin/rm -r /tmp/streamdeck-windows
+[Install]
+WantedBy=multi-user.target
\ No newline at end of file
diff --git a/tdrop/fleet-streamdeck-window.sh b/tdrop/fleet-streamdeck-window.sh
index e72ab18..480a8b8 100644
--- a/tdrop/fleet-streamdeck-window.sh
+++ b/tdrop/fleet-streamdeck-window.sh
@@ -1,5 +1,4 @@
 #!/bin/bash
-#window_title='DB Browser for SQLite - /home/thomas/.config/io.datasette.llm/logs.db'
 search_string="StreamDeck"
 
 window_ids=$(xdotool search --onlyvisible --class "jetbrains-fleet")
@@ -17,5 +16,4 @@ for window_id in $window_ids; do
     fi
 done
 echo "opening fleet"
-fleet /home/thomas/Development/Projects/StreamDeck-Group/StreamDeck
-
+fleet /home/thomas/Development/Projects/StreamDeck-Group/StreamDeck
\ No newline at end of file
diff --git a/tdrop/fleet-undecidability-window-2.sh b/tdrop/fleet-undecidability-window-2.sh
new file mode 100644
index 0000000..3da4308
--- /dev/null
+++ b/tdrop/fleet-undecidability-window-2.sh
@@ -0,0 +1,42 @@
+#!/bin/bash
+
+project="undecidability"
+tmp_dir="/tmp/streamdeck_windows"
+mkdir -p "$tmp_dir"
+pid_file="$tmp_dir/fleet-$project.pid"
+
+if [ ! -f "$pid_file" ]; then
+    echo "opening fleet"
+    fleet "$HOME/Projects/$project" &
+    echo $! > "$pid_file"
+    echo "cat pid file"
+    cat "$pid_file"
+    window_pid="$(cat "$pid_file")"
+    echo "window_pid = $window_pid"
+    sleep 2
+    wait $window_pid 
+    if [ $? -eq 0 ]; then
+        echo "$project window just exited"
+        rm "$pid_file"
+    fi
+    exit
+else
+    window_ids=$(xdotool search --onlyvisible --class "jetbrains-fleet")
+    for window_id in $window_ids; do
+        window_class=$(xdotool getwindowclassname $window_id)
+        window_name=$(xdotool getwindowname $window_id)
+        if [[ $window_class == *"jetbrains-fleet"* ]] && [[ $window_name == *"$project"* ]]; then
+            echo "found window. Activating $window_id"
+            map_state=$(xwininfo -id "$window_id" | grep "Map State")
+            if [[ $map_state == *"IsViewable"* ]]; then
+                echo "The window is mapped (visible)"
+                xdotool search --name "$window_name" windowunmap --sync
+            elif [[ $map_state == *"IsUnMapped"* ]]; then
+                echo "The window is unmapped (hidden)"
+                xdotool search --name "$window_name" windowmap --sync
+                xdotool search --name "$window_name" windowactivate --sync
+            fi
+            exit
+        fi
+    done
+fi
diff --git a/tdrop/fleet-undecidability-window.sh b/tdrop/fleet-undecidability-window.sh
new file mode 100644
index 0000000..2745200
--- /dev/null
+++ b/tdrop/fleet-undecidability-window.sh
@@ -0,0 +1,47 @@
+#!/bin/bash
+
+# Should match the project's dir name e.g. $HOME/Projects/undecidability
+project="undecidability"
+
+# streamdeck.service removes /tmp/streamdeck-windows at startup.
+tmp_dir="/tmp/streamdeck_windows"
+mkdir -p "$tmp_dir"
+pid_file="$tmp_dir/fleet-$project.pid"
+
+if [ ! -f "$pid_file" ]; then
+    echo "opening fleet"
+    fleet "$HOME/Projects/$project" &
+    echo $! > "$pid_file"
+    echo "cat pid file"
+    cat "$pid_file"
+    window_pid="$(cat "$pid_file")"
+    echo "window_pid = $window_pid"
+    sleep 2
+    wait $window_pid 
+    if [ $? -eq 0 ]; then
+        echo "$project window just exited"
+        rm "$pid_file"
+    fi
+    exit
+else
+    window_ids=$(xdotool search --onlyvisible --class "jetbrains-fleet")
+    for window_id in $window_ids; do
+        # Get the class and name of the current window
+        window_class=$(xdotool getwindowclassname $window_id)
+        # We do this as we need to substring match $project & $window_name.
+        window_name=$(xdotool getwindowname $window_id)
+        # Check if the class and name match the desired criteria
+        if [[ $window_class == *"jetbrains-fleet"* ]] && [[ $window_name == *"$project"* ]]; then
+            echo "found window. Activating $window_id"
+            if xwininfo -id "$window_id" | grep "Map State: IsViewable"; then
+                echo "The window is mapped (visable)"
+                xdotool search --name "$window_name" windowunmap --sync
+            else
+                echo "The window is unmapped (hidden)"
+                xdotool search --name "$window_name" windowmap --sync
+                xdotool search --name "$window_name" windowactivate --sync
+            fi
+            exit
+        fi
+    done
+fi
\ No newline at end of file
diff --git a/tdrop/nyxt_window.sh b/tdrop/nyxt_window.sh
new file mode 100644
index 0000000..96bd53a
--- /dev/null
+++ b/tdrop/nyxt_window.sh
@@ -0,0 +1,19 @@
+#!/bin/bash
+wm_class_string=("nyxt")
+
+window_id=`xdotool search --class ${wm_class_string} | head -1`
+
+if [ "$window_id" != "" ]; then
+  echo "The window with class ${wm_class_string} exists."
+  if xwininfo -id $window_id | grep "Map State: IsViewable"; then
+    echo "The window is mapped (visible)"
+    xdotool windowminimize $window_id
+  else
+    echo "The window is unmapped (hidden)"
+    xdotool windowmap $window_id
+    xdotool windowactivate $window_id
+  fi
+else
+  echo "The window with class ${wm_class_string} does not exist."
+  nyxt
+fi
diff --git a/tdrop/sqlitebrowser-llmdb-window.sh b/tdrop/sqlitebrowser-llmdb-window.sh
index d87d7e6..2acb31e 100644
--- a/tdrop/sqlitebrowser-llmdb-window.sh
+++ b/tdrop/sqlitebrowser-llmdb-window.sh
@@ -1,19 +1,19 @@
 #!/bin/bash
-window_title='DB Browser for SQLite - /home/thomas/.config/io.datasette.llm/logs.db'
+window_name='DB Browser for SQLite - /home/thomas/.config/io.datasette.llm/logs.db'
 
-if xdotool search --name "$window_title"; then
-  echo "The window with title $window_title
+if xdotool search --name "$window_name"; then
+  echo "The window with title $window_name
     echo "Window is not mapped"
  exists."
-  if xwininfo -name "$window_title" | grep "Map State: IsViewable"; then
+  if xwininfo -name "$window_name" | grep "Map State: IsViewable"; then
     echo "The window is mapped (visable)"
-    xdotool search --name "$window_title" windowunmap --sync
+    xdotool search --name "$window_name" windowunmap --sync
   else
     echo "The window is unmapped (hidden)"
-    xdotool search --name "$window_title" windowmap --sync
-    xdotool search --name "$window_title" windowactivate --sync
+    xdotool search --name "$window_name" windowmap --sync
+    xdotool search --name "$window_name" windowactivate --sync
     fi
 else
-  echo "The window with title $window_title does not exist."
+  echo "The window with title $window_name does not exist."
   sqlitebrowser "$(llm logs path)" &
-fi
\ No newline at end of file
+fi


**Response:**
Add new fleet settings, streamdeck service, and fleet scripts for various windows

<details><summary>Metadata</summary>

- Duration: 2384 ms
- Datetime: 2023-10-19T13:15:09.275505
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

