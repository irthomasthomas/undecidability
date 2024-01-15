**Prompt:**
diff --git a/check-for-change-to-openai-api.sh b/check-for-change-to-openai-api.sh
new file mode 100644
index 0000000..6804bc1
--- /dev/null
+++ b/check-for-change-to-openai-api.sh
@@ -0,0 +1,28 @@
+#!/bin/bash
+echo "script to alert to new api's"
+
+# Store the initial snapshot of data.
+initial_snapshot=$(curl -sf -X GET "https://api.openai.com/v1/models" -H "Authorization: Bearer $OPENAI_API_KEY")
+echo "initial_snapshot"
+echo "${initial_snapshot:0:40}"
+# Go into an infinite loop.
+while true; do
+    # Request the latest data.
+    latest_snapshot=$(curl -sf -X GET "https://api.openai.com/v1/models" -H "Authorization: Bearer $OPENAI_API_KEY")
+    echo "latest_snapshot"
+    echo "${latest_snapshot:0:40}"
+    # Compare the initial and latest data.
+    if [[ "$initial_snapshot" != "$latest_snapshot" ]]; then
+        # If there's any change, print out a message.
+        echo "Alert: Detected a change."
+        kdialog --msgbox "Alert: Detected a change in OpenAI API."
+
+        # Now, store the latest snapshot as the new initial snapshot.
+        initial_snapshot=$latest_snapshot
+    else
+        echo "No change"
+    fi
+
+    # Wait for 30 seconds before the next API call.
+    sleep 30
+done
diff --git a/echo b/echo
new file mode 100644
index 0000000..77fbaf5
--- /dev/null
+++ b/echo
@@ -0,0 +1,23 @@
+	Command being timed: "echo hello"
+	User time (seconds): 0.00
+	System time (seconds): 0.00
+	Percent of CPU this job got: 91%
+	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:00.00
+	Average shared text size (kbytes): 0
+	Average unshared data size (kbytes): 0
+	Average stack size (kbytes): 0
+	Average total size (kbytes): 0
+	Maximum resident set size (kbytes): 1792
+	Average resident set size (kbytes): 0
+	Major (requiring I/O) page faults: 0
+	Minor (reclaiming a frame) page faults: 105
+	Voluntary context switches: 1
+	Involuntary context switches: 1
+	Swaps: 0
+	File system inputs: 0
+	File system outputs: 0
+	Socket messages sent: 0
+	Socket messages received: 0
+	Signals delivered: 0
+	Page size (bytes): 4096
+	Exit status: 0
diff --git a/factorial-for-loop.py b/factorial-for-loop.py
new file mode 100644
index 0000000..c4b176d
--- /dev/null
+++ b/factorial-for-loop.py
@@ -0,0 +1,5 @@
+def factorial(n):
+    result = 1
+    for i in range(1, n + 1):
+        result *= i
+    return result
diff --git a/llm/interactive_llm_evals.sh b/llm/interactive_llm_evals.sh
new file mode 100644
index 0000000..42a22f8
--- /dev/null
+++ b/llm/interactive_llm_evals.sh
@@ -0,0 +1,117 @@
+#!/bin/bash
+
+DB_PATH="$HOME/logs.db"
+
+# Function to execute a SQL query and return results
+query_db() {
+  sqlite3 "$DB_PATH" "$1"
+}
+
+# Function to interactively search prompts or responses using fzf
+  search_entries() {
+    echo "search_entries"
+    local search_column="$1"
+    echo "search_column: $search_column"
+    local search_term=${2:-$(read -p "Enter search term: " search_term)}
+    echo "search_term: $search_term"
+  
+    # Add '%' wildcard for partial matching 
+    IFS=$'|'
+    query_db "SELECT id, model, prompt, response FROM responses WHERE $search_column LIKE '%${search_term}%' ORDER BY datetime_utc DESC;" | while read -r id model prompt response
+    do
+      short_prompt=${prompt:0:40}
+      short_response=${response:0:40}
+      echo "$id|$short_prompt|$short_response" | fzf --delimiter='|' --with-nth=1,2
+    done
+  }
+
+# Function to copy to clipboard
+copy_to_clipboard() {
+  local response="$1"
+  echo "$response" | xclip -selection clipboard
+  echo "Response copied to clipboard."
+}
+
+# Function to open in a new terminal
+open_in_terminal() {
+  local response="$1"
+  local tempfile=$(mktemp)
+  echo "$response" > "$tempfile"
+  x-terminal-emulator -e bash -c "cat $tempfile; exec bash"
+  echo "Response opened in new terminal."
+}
+
+# Function to score a response
+score_response() {
+  local response_id="$1"
+  echo "Scoring for response ID: $response_id"
+  local score=$(printf "-2\n-1\n0\n1\n2" | fzf --header="Choose a score (-2 to +2):")
+#  local comment=$(printf "Good\nAverage\nPoor" | fzf --header="Choose a comment:")
+   local comment=""
+
+  # Insert the score and comment into the database
+  query_db "INSERT INTO evaluations (response_id, evaluation_grade, evaluation_comment) VALUES ('$response_id', '$score', '$comment');"
+  echo "Response scored successfully."
+}
+
+# Function to evaluate a response
+evaluate_response() {
+  echo "evaluate_response"
+  local chosen_entry=$(search_entries "prompt")
+  echo "chosen_entry: $chosen_entry"
+  local response_id=$(echo $chosen_entry | cut -d '|' -f 1)
+  echo "response_id: $response_id"
+  # Display options for what to do next with the response
+  local action=$(printf "Copy to Clipboard\nOpen in Terminal\nScore Response" | fzf --header="Choose action:")
+  case $action in
+    "Copy to Clipboard")
+      local response=$(echo $chosen_entry | cut -d '|' -f 4)
+      copy_to_clipboard "$response"
+      ;;
+    "Open in Terminal")
+      local response=$(echo $chosen_entry | cut -d '|' -f 4)
+      open_in_terminal "$response"
+      ;;
+    "Score Response")
+      score_response "$response_id"
+      ;;
+    *)
+      echo "No valid action selected."
+      ;;
+  esac
+}
+
+# Text-based main menu function
+main_menu() {
+  while true; do
+    echo "Menu Options:"
+    echo "1) Search prompts"
+    echo "2) Search responses"
+    echo "3) Evaluate response"
+    echo "4) Exit"
+    echo "Please choose an option: "
+    read -r action
+
+    case "$action" in
+      1)
+        search_entries "prompt"
+        ;;
+      2)
+        search_entries "response"
+        ;;
+      3)
+        evaluate_response
+        ;;
+      4)
+        echo "Exiting..."
+        break
+        ;;
+      *)
+        echo "Invalid option, please try again."
+        ;;
+    esac
+  done
+}
+
+# Run the main menu
+main_menu
diff --git a/nyxt/auto-config.3.lisp b/nyxt/auto-config.3.lisp
new file mode 100644
index 0000000..cd98a6b
--- /dev/null
+++ b/nyxt/auto-config.3.lisp
@@ -0,0 +1,22 @@
+(defmethod customize-instance ((document-buffer document-buffer) &key)
+  (setf (slot-value document-buffer 'zoom-ratio-default) 1.1))
+
+(defmethod customize-instance ((buffer buffer) &key)
+  (setf (slot-value buffer 'default-modes)
+          '(nyxt/mode/certificate-exception:certificate-exception-mode
+            nyxt/mode/annotate:annotate-mode nyxt/mode/bookmark:bookmark-mode
+            nyxt/mode/history:history-mode nyxt/mode/password:password-mode
+            nyxt/mode/hint:hint-mode nyxt/mode/document:document-mode
+            nyxt/mode/search-buffer:search-buffer-mode
+            nyxt/mode/autofill:autofill-mode
+            nyxt/mode/spell-check:spell-check-mode base-mode)))
+
+(define-configuration (web-buffer)
+  ((default-modes (pushnew 'nyxt/mode/blocker:blocker-mode %slot-value%))))
+
+(define-configuration (web-buffer)
+  ((default-modes
+    (pushnew 'nyxt/mode/reduce-tracking:reduce-tracking-mode %slot-value%))))
+
+(defmethod customize-instance ((browser browser) &key)
+  (setf (slot-value browser 'remote-execution-p) t))
diff --git a/nyxt/config.lisp b/nyxt/config.lisp
new file mode 100644
index 0000000..0a17395
--- /dev/null
+++ b/nyxt/config.lisp
@@ -0,0 +1,30 @@
+(define-command-global pipe-selection ()
+    "Send selection to named pipe"
+  (let ((selection (ps-eval (ps:chain window (get-selection) (to-string)))))
+    (uiop:launch-program (list "sh" "-c" (concatenate 'string "echo " "'" selection "'" " > /tmp/nyxt_selection_pipe")))))
+
+
+
+(define-command-global pipe-selection-title-url-new ()
+    "Sends url, title and selection to new gh issue"
+  (let* ((title (title (current-buffer)))
+         (myurl (url (current-buffer)))
+         (selection (ps-eval (ps:chain window (get-selection) (to-string))))
+         (pipe-title "/tmp/nyxt_title")
+         (pipe-url "/tmp/nyxt_url")
+         (pipe-selection "/tmp/nyxt_selection"))
+    (with-open-file (stream pipe-title
+                           :direction :output
+                           :if-exists :supersede
+                           :if-does-not-exist :create)
+      (write-string title stream))
+    (with-open-file (stream pipe-url
+                           :direction :output
+                           :if-exists :supersede
+                           :if-does-not-exist :create)
+      (write-string (render-url myurl) stream))
+    (with-open-file (stream pipe-selection
+                           :direction :output
+                           :if-exists :supersede
+                           :if-does-not-exist :create)
+      (write-string selection stream))))
diff --git a/nyxt/nyxt-to-github.sh b/nyxt/nyxt-to-github.sh
index d40a400..388bc1e 100644
--- a/nyxt/nyxt-to-github.sh
+++ b/nyxt/nyxt-to-github.sh
@@ -1,14 +1,6 @@
 #!/bin/bash
 
-send_note_to_github() {
-    echo "Send Note To Github"
-    target_project="undecidability"
-    target_directory="$HOME/$target_project"
-
-    pipe_title="/tmp/nyxt_title"
-    pipe_url="/tmp/nyxt_url"
-    pipe_selection="/tmp/nyxt_selection"
-
+create_pipes() {
     # Create named pipes if they don't exist
     if [ ! -p "$pipe_title" ]; then
         mkfifo "$pipe_title" && echo "Created named pipe: $pipe_title"
@@ -24,8 +16,20 @@ send_note_to_github() {
 
     if [ ! -d "$target_directory" ]; then
         echo "Cannot find directory $target_directory"
-        return 1
+        exit 1
     fi
+}
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
+    create_pipes
 
     cd "$target_directory" || return 2
     echo "$PWD"
diff --git a/openai-api-models-monitor.sh b/openai-api-models-monitor.sh
new file mode 100644
index 0000000..3a6c464
--- /dev/null
+++ b/openai-api-models-monitor.sh
@@ -0,0 +1,28 @@
+#!/bin/bash
+
+# Store your API key.
+OPENAI_API_KEY=your_api_key
+
+# Run the API call and generate the initial CSV.
+initial_snapshot=$(curl -sf -X GET "https://api.openai.com/v1/models" -H "Authorization: Bearer $OPENAI_API


**Response:**
Add new scripts and configurations for OpenAI API monitoring and Nyxt browser customization.

<details><summary>Metadata</summary>

- Duration: 1593 ms
- Datetime: 2023-11-16T17:16:53.618220
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

