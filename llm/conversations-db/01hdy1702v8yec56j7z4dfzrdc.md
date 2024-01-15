**Prompt:**
diff --git a/shell_functions.sh b/shell_functions.sh
index 41a3959..f6ddd25 100755
--- a/shell_functions.sh
+++ b/shell_functions.sh
@@ -148,12 +148,10 @@ send_issue1() {
 send_issue() {
   # Send an issue to github.
   # Usage: send_issue target_project title body labels
-  target_project="${1:-undecidability}"
-  title="$2"
-  body="${3:-""}"
-  labels="${4:-unclassified}"
-
-  whiptail --title "$title" --msgbox "target: $target_project body: $body labels: $labels"
+  title="$1"
+  body="${2:-""}"
+  labels="${3:-unclassified}"
+  target_project="undecidability"
 
   cd $HOME/"$target_project"
 
@@ -164,10 +162,13 @@ send_issue() {
     label_string+="--label $label "
   done
 
+  yad --title="$title" --text="Title: $title\nTarget: $target_project \nbody: $body\nlabels: $labels\nlabel_string: $label_string" --button="OK":0
+
   url="$(gh issue create --title "$title" --body "$body" $label_string)"
 
   clip "$url"
-  nyxt -r -e "(make-window (make-buffer :url \"$url\"))" -q
+  nyxt "$url"
+#   nyxt -r -e "(make-window (make-buffer :url \"$url\"))" -q
 }
 
 
@@ -179,6 +180,16 @@ send_quickidea_to_gh() {
   send_note "$note_category" "$target_project"
 }
 
+send_note() {
+#   Note_Category="$1" #Idea, #Todo, #QnA, #Shopping, #CodeSnippet, #Bookmark
+  title="$1"
+  body="$2"
+  target_project="undecidability"
+  cd $HOME/"$target_project"
+  url="$(gh issue create --title "$title" --body "$body" --label "unclassified")"
+  "$url"
+  }
+
 md() {
 
   if [ -z "$1" ] # checks if $1 is empty
@@ -279,7 +290,7 @@ explain() {
   promptB="Explain this bash code. Be concise. Only mention serious errors.
           CODE:
           $query"
-  promptC="Use as few words as required. Explain this bash code to a linux expert. Also mention any serious errors (or say nothing.):\n$query"
+  promptC="Use as few words as required. Explain this bash code to a linux expert. Also mention any serious errors:\n$query"
 
   choice="prompt$(echo -n 'A B C' | tr ' ' '\n' | shuf -n 1)"
   echo "Choice: $choice"
@@ -300,6 +311,46 @@ mkfilename() {
   echo "$trunc_content" | llm -m 3.5 -t $llm_template -o temperature 0.2 -o max_tokens 15
   }
 
+save_codeblock_to_file_old() {
+  text=''
+  while IFS= read -r line; do
+      text="${text}\n${line}"
+  done
+
+  regex='\`\`\`(.+?)\`\`\`'
+  n=0
+  while [[ "${text}" =~ $regex ]]; do
+      code_content="${BASH_REMATCH[1]}"
+      text=${text/"```${code_content}```"/}
+
+      filename=$(mkfilename "${code_content}")
+      while [ -f "$filename" ]; do
+        read -p "The file already exists. Enter a different filename: " new_filename
+        filename="$new_filename"
+      done
+      echo -e "${code_content}" > "${filename}"
+done
+}
+
+save_codeblock_to_file() {
+  text=''
+  while IFS= read -r line; do
+      text="${text}${line}\n"
+  done
+
+  while [[ "${text}" =~ \`\`\`(.*?)\`\`\` ]]; do
+      code_content="${BASH_REMATCH[1]}"
+      text=${text#*```}
+
+      filename=$(mkfilename "${code_content}")
+      while [ -f "$filename" ]; do
+        read -p "The file already exists. Enter a different filename: " new_filename
+        filename="$new_filename"
+      done
+      echo -e "${code_content}" > "${filename}"
+  done
+}
+
 commit_old() {
   msg="$1"
   git add .
@@ -394,12 +445,6 @@ exec_dot_desktop() {
   exec_line=$(awk '/Desktop Entry/,0' "$1" | grep -E "^Exec=" | cut -d "=" -f 2-); eval $exec_line
   }
 
-# Test the dialogbox with various inputs
-testDialogbox() {
-  dialogbox     # No argument
-  dialogbox ""  # Empty message
-  dialogbox "Hello, World!" # Valid message input
-}
 
 dialogbox() {
   # ToDo: Replace as many kdialog calls with a more portable dialogbox function.


**Response:**
Refactor send_issue function and add send_note function

<details><summary>Metadata</summary>

- Duration: 4596 ms
- Datetime: 2023-10-29T15:35:30.150619
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

