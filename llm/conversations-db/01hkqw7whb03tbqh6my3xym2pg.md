**Prompt:**
diff --git a/logs.db b/logs.db
new file mode 100644
index 0000000..7238bb4
Binary files /dev/null and b/logs.db differ
diff --git a/nyxt/nyxt-to-gh.sh b/nyxt/nyxt-to-gh.sh
index 24eeee6..d4e4936 100755
--- a/nyxt/nyxt-to-gh.sh
+++ b/nyxt/nyxt-to-gh.sh
@@ -1,5 +1,19 @@
 #!/bin/bash
 
+test_gh() {
+    # use the file pipes in order to test functionality
+    echo "Test Pipes"
+    target_project="undecidability"
+    target_directory="$HOME/$target_project"
+    cd "$target_directory" || return 2
+    echo "$PWD"
+    
+    TITLE="bash - Using aliases in shell scripts - Stack Overflow"
+    URL="https://stackoverflow.com/questions/5228345/using-aliases-in-bash-shell-script"
+    SELECTION="I have a bash script that I want to use aliases in. I have set up the alias in the .bashrc file, but it doesn\'t work in the script."
+    send_note_to_github
+}
+
 create_pipes() {
     # Create named pipes if they don't exist
     if [ ! -p "$pipe_title" ]; then
@@ -20,17 +34,8 @@ create_pipes() {
     fi
 }
 
-send_note_to_github() {
-    echo "Send Note To Github"
-    target_project="undecidability"
-    target_directory="$HOME/$target_project"
-
-    pipe_title="/tmp/nyxt_title"
-    pipe_url="/tmp/nyxt_url"
-    pipe_selection="/tmp/nyxt_selection"
-
-    create_pipes
-
+monitor_nyxt_to_gh_pipes() {
+    echo "Monitoring pipes"
     cd "$target_directory" || return 2
     echo "$PWD"
 
@@ -39,20 +44,15 @@ send_note_to_github() {
         return 3
     fi
     echo "Found pipes"
-
+    
     TITLE="$(cat ${pipe_title})"
     URL="$(cat $pipe_url)"
-    SELECTION="$(cat $pipe_selection)"
-    # If title is blank, set title to URL
+    SELECTION="$(cat $pipe_selection)" # This is the text that was selected from the page. Usually a gh description or good quote.
     if [ -z "$TITLE" ]; then
         TITLE="$URL"
     fi
     BODY="$URL
-$SELECTION"
-    echo "$BODY"
-    echo "TITLE: $TITLE"
-    echo "BODY: $BODY"
-    echo "LABEL: $LABEL"
+    $SELECTION"
     if ! command -v gh &>/dev/null; then
         echo "gh could not be found"
         return 4
@@ -63,13 +63,44 @@ $SELECTION"
     BODY="$task_list
 
     $SELECTION"
-    echo "Creating gh issue"
-    gh issue create --title "$TITLE" --body "$BODY" --web --label "unclassified" --label "inbox-url" &
+}
+
+get_labels() {
+    echo "get labels"
+    labels=$(python /home/thomas/Development/linux-stuff/label_maker.py --url "$URL" --title "$TITLE" --selection "$SELECTION")
+    echo "$labels"
+    labels_csv=$(echo "$labels" | tr -d [])
+    labels_csv=$(echo "$labels_csv" | tr -d \' | tr -d ' ')
+    echo "$labels_csv"
+}
+
+send_note_to_github() {
+    issue_url=$(gh issue create --title "$TITLE" --body "$BODY" --label "$labels_csv")
+    nyxt "$issue_url"
+    nyxt_pid=$(pgrep -f nyxt)
+    nyxt_wid=$(xdotool search --pid "$nyxt_pid")
+    xdotool windowactivate "$nyxt_wid"
     return 0
 }
 
+# test_gh
+echo "Starting nyxt-to-gh.sh"
 while true
 do
+    target_project="undecidability"
+    target_directory="$HOME/$target_project"
+    pipe_title="/tmp/nyxt_title"
+    pipe_url="/tmp/nyxt_url"
+    pipe_selection="/tmp/nyxt_selection"
+    echo "create pipes"
+    create_pipes
+    echo "monitor pipes"
+    monitor_nyxt_to_gh_pipes
+    echo "get labels"
+    get_labels
     send_note_to_github
-    sleep 10
+    echo "sent note to github"
+    echo "sleep"
+    sleep 5
 done
+


**Response:**
Refactor nyxt-to-gh.sh script to improve readability and add label functionality.

<details><summary>Metadata</summary>

- Duration: 1223 ms
- Datetime: 2024-01-09T19:47:24.132084
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.6}
```

