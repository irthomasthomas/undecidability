**Prompt:**
diff --git a/copy_file_tags.sh b/copy_file_tags.sh
index 31e33d1..268c03d 100755
--- a/copy_file_tags.sh
+++ b/copy_file_tags.sh
@@ -1,2 +1,44 @@
-file:///home/thomas/Downloads/facebook (1).svg#!/bin/bash
-getfattr -n user.xdg.tags --only-values $1 | xclip -selection clipboard
+#!/bin/bash
+copy_paste_file_tags() {
+    echo "copy_file_tags"
+    source="$1"
+    for target in "${@:2}"; do
+        echo "getfattr"
+        tags="$(file_tags $source)"
+        old_tags="$(file_tags "$target")"
+        tags="$tags,$old_tags"
+        set_file_tags "$target" "$tags"
+        getfattr --name=user.xdg.tags --only-values "$target"
+    done
+}
+
+copy_paste_file_rating() {
+    echo "copy_file_rating"
+    source="$1"
+    for target in "${@:2}"; do
+        rating=$(file_rating "$source")
+        set_file_rating "$target" "$rating"
+        echo "$target
+        rating: $(file_rating $target)"
+    done
+    }
+
+file_rating() {
+    getfattr --name=user.baloo.rating --only-values "$1"
+    }
+
+file_tags() {
+    getfattr --name=user.xdg.tags --only-values "$1"
+    }
+
+set_file_rating() {
+    target="$1"
+    rating="$2"
+    setfattr --name=user.baloo.rating --value="$rating" "$target"
+    }
+
+set_file_tags() {
+    target="$1"
+    tags="$2"
+    setfattr --name=user.xdg.tags --value="$tags" "$target"
+    }
\ No newline at end of file
diff --git a/gh_issues_tui.py b/gh_issues_tui.py
new file mode 100644
index 0000000..a6a926e
--- /dev/null
+++ b/gh_issues_tui.py
@@ -0,0 +1,45 @@
+import github
+from github import Github
+import datetime
+import requests
+
+#AccessToken
+g=Github("<enter your access token>")
+
+#Select the repo
+repo=g.get_repo("<Enter your repo details>")
+
+#Main Menu
+def main_menu():
+    print("""
+    1. Browse Issues
+    2. Add New Issues
+    3. Exit
+    """)
+
+#Browse Issue
+def browse_issue():
+    open_issues=repo.get_issues(state='open')
+    for issue in open_issues:
+        if issue.labels[0].name=="overseer-inbox":    
+            print(issue)
+
+#Add New Issue
+def add_issue():
+    issue_title=input("Enter the issue title: ")
+    issue_body=input("Enter the issue details: ")
+    label=repo.get_label("inbox-url")
+    repo.create_issue(title=issue_title, body=issue_body, labels=[label])
+
+#Main Implementation
+while(True):
+
+    main_menu()
+    choice=int(input("Enter your choice: "))
+    
+    if choice==1:
+        browse_issue()
+    elif choice==2:
+        add_issue()
+    else:
+        break
diff --git a/overseer_inbox.yaml b/overseer_inbox.yaml
new file mode 100644
index 0000000..ea254be
--- /dev/null
+++ b/overseer_inbox.yaml
@@ -0,0 +1,13 @@
+name: Overseer inbox workflow
+on:
+  issues:
+    types: [opened, labeled]
+ 
+jobs:
+  overseer-job:
+    runs-on: ubuntu-latest
+    if: github.event.label.name == 'inbox-url'
+    steps:
+    - name: Checkout Repository
+      uses: actions/checkout@v2
+    # Add steps for web scraping, replying to issue etc here
diff --git a/paste_file_tags.sh b/paste_file_tags.sh
index 817d721..a5b995e 100755
--- a/paste_file_tags.sh
+++ b/paste_file_tags.sh
@@ -1,31 +1,9 @@
 #!/bin/bash
-tags=$(xclip -selection clipboard -o)
-old_tags=$(getfattr -n user.xdg.tags --only-values "$1")
-# if old_tags is not empty, open a kdialog and ask the user to append, overwrite or cancel.
 
-if [ -n "$old_tags" ]; then
-    kdialog --title "Tags" --yesnocancel "Tags exist already. Do you want to append (Yes), overwrite (No) the tags or cancel?"
-    case $? in
-        0)
-            # append
-            tags="$old_tags,$tags"
-            ;;
-
-        1)
-            # overwrite
-            ;;
-
-        2)
-            # cancel
-            exit 0
-            ;;
-
-        *)
-            # error
-            ;;
-
-    esac
-
-fi
-
-setfattr -n user.xdg.tags -v "$tags" "$1"
+paste_file_tags() {
+    tags_pipe="/tmp/file_tags_pipe"
+    tags="$(cat ${tags_pipe})"
+    old_tags=$(getfattr -n user.xdg.tags --only-values "$1")
+    tags="$tags,$old_tags"
+    setfattr -n user.xdg.tags -v "$tags" "$1"
+    }
\ No newline at end of file
diff --git a/shell_functions.sh b/shell_functions.sh
index f6ddd25..d94af50 100755
--- a/shell_functions.sh
+++ b/shell_functions.sh
@@ -1,4 +1,8 @@
 #!/bin/bash
+SCRIPT_DIR="$(dirname "$0")"
+echo "SCRIPT_DIR: $SCRIPT_DIR"
+source "$SCRIPT_DIR/copy_file_tags.sh"
+source "$SCRIPT_DIR/paste_file_tags.sh"
 
 # Github-cli gh
 alias which='which -a'
@@ -318,7 +322,7 @@ save_codeblock_to_file_old() {
   done
 
   regex='\`\`\`(.+?)\`\`\`'
-  n=0
+
   while [[ "${text}" =~ $regex ]]; do
       code_content="${BASH_REMATCH[1]}"
       text=${text/"```${code_content}```"/}
@@ -333,22 +337,43 @@ done
 }
 
 save_codeblock_to_file() {
-  text=''
+  # Initialize variables
+  in_code_block=false
+  filename=""
+  n=1
+  text=""
+
+  # Read from stdin
   while IFS= read -r line; do
-      text="${text}${line}\n"
+    text="${text}
+${line}"
+
+    # Check if the line starts a code block
+    if [[ $line == \`\`\`* ]]; then
+      if $in_code_block; then
+        # If we're in a code block, this line ends it
+        in_code_block=false
+        # Close the file
+        exec 3>&-
+      else
+        # If we're not in a code block, this line starts it
+        in_code_block=true
+        # Generate a filename with n
+        filename="mkfilename_${n}_$(date +%s)"
+        # Open the file for writing
+        exec 3>"$filename"
+      fi
+    elif $in_code_block; then
+      # If we're in a code block, write the line to the file
+      echo "$line" >&3
+    fi
+    ((n++))
   done
 
-  while [[ "${text}" =~ \`\`\`(.*?)\`\`\` ]]; do
-      code_content="${BASH_REMATCH[1]}"
-      text=${text#*```}
-
-      filename=$(mkfilename "${code_content}")
-      while [ -f "$filename" ]; do
-        read -p "The file already exists. Enter a different filename: " new_filename
-        filename="$new_filename"
-      done
-      echo -e "${code_content}" > "${filename}"
-  done
+  # If we're still in a code block at the end, close the file
+  if $in_code_block; then
+    exec 3>&-
+  fi
 }
 
 commit_old() {
@@ -398,6 +423,7 @@ commit() {
     done
 
     git commit -m ""$msg""
+    git push
 }
 
 


**Response:**
Add shell functions for copying and pasting file tags, and update the commit function to push changes.

<details><summary>Metadata</summary>

- Duration: 2390 ms
- Datetime: 2023-11-05T13:36:04.897769
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

