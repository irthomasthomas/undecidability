**Prompt:**
diff --git a/copy_file_tags.sh b/copy_file_tags.sh
index 268c03d..0b6191e 100755
--- a/copy_file_tags.sh
+++ b/copy_file_tags.sh
@@ -41,4 +41,9 @@ set_file_tags() {
     target="$1"
     tags="$2"
     setfattr --name=user.xdg.tags --value="$tags" "$target"
+    }
+
+copy_tags_ratings() {
+    copy_paste_file_tags "$@"
+    copy_paste_file_rating "$@"
     }
\ No newline at end of file
diff --git a/paste_file_tags.sh b/paste_file_tags.sh
deleted file mode 100755
index a5b995e..0000000
--- a/paste_file_tags.sh
+++ /dev/null
@@ -1,9 +0,0 @@
-#!/bin/bash
-
-paste_file_tags() {
-    tags_pipe="/tmp/file_tags_pipe"
-    tags="$(cat ${tags_pipe})"
-    old_tags=$(getfattr -n user.xdg.tags --only-values "$1")
-    tags="$tags,$old_tags"
-    setfattr -n user.xdg.tags -v "$tags" "$1"
-    }
\ No newline at end of file
diff --git a/shell_functions.sh b/shell_functions.sh
index d94af50..bed6536 100755
--- a/shell_functions.sh
+++ b/shell_functions.sh
@@ -2,7 +2,6 @@
 SCRIPT_DIR="$(dirname "$0")"
 echo "SCRIPT_DIR: $SCRIPT_DIR"
 source "$SCRIPT_DIR/copy_file_tags.sh"
-source "$SCRIPT_DIR/paste_file_tags.sh"
 
 # Github-cli gh
 alias which='which -a'
@@ -89,22 +88,13 @@ echo "iDoDid"
 alias undecidability="$HOME/undecidability"
 OPENAI_API_KEY=$(cat /$HOME/Development/AI/openai/openai_key)
 export OPENAI_API_KEY
-export CLAUD_SESS_KEY="/$HOME/Development/AI/claude-sessionkey"
 export EDITOR="kate"
 alias issues='gh issue list'
 export funcs=$HOME/Development/linux-stuff/shell_functions.sh
-# export llmfuncs=$HOME/Development/scripts/llm_shell_functions.sh
-
-# export GROFF_NO_SGR=1
-# xmodmap -e "keycode 66 = Shift_L NoSymbol Shift_L"
-# If no x session, needs sudo:
-#  echo -e "keymaps 0-127\nkeycode 58 = Shift" | sudo loadkeys -
 
 alias readability="shot-scraper javascript -i $HOME/Development/linux-stuff/readability.js"
 
 open_kate_at_line() {
-  # Todo: split this in to two functions.
-  #   1. Return an array or tuple of file_path and line_number
   local keyword=$1
   local file_pattern=$2
   echo "keyword: $keyword"
@@ -499,44 +489,26 @@ dialogbox() {
     fi
 }
 
-
 timer() {
-  /bin/time -v -q -o $HOME/.timehistory -a "$@"
-  tail -n 1 $HOME/.timehistory
-  }
-
-timer-old() {
-    # Function that times commands and records the command that was run
-
-    # Check if command argument is provided
-    if [ -z "$1" ]; then
-        echo "No command provided" >&2
-        return 1
+  if [ "$1" = "-f" ]; then
+    if [ -d "$2" ] ; then
+      file="$2"/timers.txt
+    elif [ -f "$2" ]; then
+      file="$2"
+    else
+      case "$2" in
+      /*) echo "This is an absolute path"; file="$2" && touch "$2";;
+      *//*) echo "This is not a valid path"; return ;;
+      *) echo "This is a relative path"; file="$PWD/$2" && touch "$PWD/$2" ;;
+      esac
     fi
-
-    # Get the command from arguments
-    cmd="$@"
-
-    # Record the command that was run
-    echo "Command: $cmd" >> $HOME/command_log.txt
-
-    # Run the command and time it
-    {
-        start=$(date +%s)
-        eval "$cmd"
-        end=$(date +%s)
-    } 2>> $HOME/command_log.txt
-
-    # Calculate the execution time
-    execution_time="$((end-start))"
-
-    # Record the execution time
-    {
-        echo "Execution Time: $execution_time seconds"
-        echo "-------------------------------------"
-    } >> $HOME/command_log.txt
-    echo "Total Execution Time: $execution_time seconds"
-}
+  else
+    file="$HOME/.timehistory"
+  fi
+  echo "$file"
+  /bin/time -v -q -o "$file" -a "$@"
+  tail -n 1 "$file"
+  }
 
 # Function to create a directory and handle errors
 try_mkdir() {


**Response:**
Refactor shell functions and remove unused code

<details><summary>Metadata</summary>

- Duration: 756 ms
- Datetime: 2023-11-09T13:10:40.290819
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

