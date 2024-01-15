**Prompt:**
diff --git a/nyxt/nyxt-to-github.sh b/nyxt/nyxt-to-github.sh
new file mode 100644
index 0000000..d40a400
--- /dev/null
+++ b/nyxt/nyxt-to-github.sh
@@ -0,0 +1,72 @@
+#!/bin/bash
+
+send_note_to_github() {
+    echo "Send Note To Github"
+    target_project="undecidability"
+    target_directory="$HOME/$target_project"
+
+    pipe_title="/tmp/nyxt_title"
+    pipe_url="/tmp/nyxt_url"
+    pipe_selection="/tmp/nyxt_selection"
+
+    # Create named pipes if they don't exist
+    if [ ! -p "$pipe_title" ]; then
+        mkfifo "$pipe_title" && echo "Created named pipe: $pipe_title"
+    fi
+
+    if [ ! -p "$pipe_url" ]; then
+        mkfifo "$pipe_url" && echo "Created named pipe: $pipe_url"
+    fi
+
+    if [ ! -p "$pipe_selection" ]; then
+        mkfifo "$pipe_selection" && echo "Created named pipe: $pipe_selection"
+    fi
+
+    if [ ! -d "$target_directory" ]; then
+        echo "Cannot find directory $target_directory"
+        return 1
+    fi
+
+    cd "$target_directory" || return 2
+    echo "$PWD"
+
+    if [ ! -p "$pipe_title" ] || [ ! -p "$pipe_url" ] || [ ! -p "$pipe_selection" ]; then
+        echo "Cannot find required pipes"
+        return 3
+    fi
+    echo "Found pipes"
+
+    TITLE="$(cat ${pipe_title})"
+    echo "$TITLE"
+    URL="$(cat $pipe_url)"
+    SELECTION="$(cat $pipe_selection)"
+    BODY="$URL
+$SELECTION"
+    echo "$BODY"
+    echo "TITLE: $TITLE"
+    echo "BODY: $BODY"
+    echo "LABEL: $LABEL"
+    if ! command -v gh &>/dev/null; then
+        echo "gh could not be found"
+        return 4
+    fi
+    task_list="- [ ] [${TITLE}](${URL})"
+    #Add $SELECTION text using the <details><summary>Details</summary> pattern
+    
+    BODY="$task_list
+    <details>
+    <summary>Quote</summary>
+    
+    $SELECTION
+    
+    </details>"
+    echo "Creating gh issue"
+    gh issue create --title "$TITLE" --body "$BODY" --label "unclassified" --label "inbox-url"
+    return 0
+}
+
+while true
+do
+    send_note_to_github
+    sleep 10
+done


**Response:**
Add nyxt-to-github.sh script for sending notes to GitHub

<details><summary>Metadata</summary>

- Duration: 1891 ms
- Datetime: 2023-11-02T13:58:41.274427
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

