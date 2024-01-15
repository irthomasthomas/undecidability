**Prompt:**
diff --git a/instructions_for_gh_actions.md b/instructions_for_gh_actions.md
new file mode 100644
index 0000000..8a9a6c3
--- /dev/null
+++ b/instructions_for_gh_actions.md
@@ -0,0 +1,64 @@
+To proceed with the implementation, follow the steps below:
+
+1. Create a file named `main.yml` in the `.github/workflows/` directory of your repository. The file name and location can be changed based on your preference. 
+
+2. In that file, use the following modified code snippet based on the previous discussion:
+
+```yaml
+name: Run Script
+on:
+   issues:
+    types: [opened, labeled]
+
+jobs:
+  auto-reply:
+    if: github.event.label.name == 'run'
+    runs-on: ubuntu-latest
+
+    steps:
+      - name: Checkout
+        uses: actions/checkout@v2
+      
+      - name: Setup GitHub CLI
+        uses: cli/setup-gh@v1
+
+      - name: Run Script
+        id: script
+        run: |
+          try {
+            output=$(./script.sh)
+            echo "::set-output name=result::$output"
+           } catch {
+           echo "The script failed to run"
+           output="An error has occurred while running the script."
+           }
+
+      - name: Post Comment
+        id: comment
+        uses: actions/github-script@v3.1.0
+        with:
+          github-token: ${{ secrets.GITHUB_TOKEN }}
+          script: |
+            const issue_number = context.issue.number;
+            const comments = await github.issues.listComments({...context.repo, issue_number});
+            const bot_comment_exists = comments.data.some(comment => comment.user.login === 'github-actions[bot]' && comment.body.includes('Your output text here'));
+            if (!bot_comment_exists) {
+              await github.issues.createComment({...context.repo, issue_number, body: '${{steps.script.outputs.result}}'});
+            }
+```
+
+Here's what this script does:
+
+1. It's triggered whenever an issue is labeled or created.
+2. Checks if the label name equals 'run'.
+3. If true, the workflow continues, otherwise, it stops.
+4. The script at `./script.sh` is executed.
+5. A list of comments on the issue is fetched.
+6. It's checked if there exists a comment by the GitHub Actions bot that includes some specific content.
+7. If such a comment doesn't exist already, a new comment is created which contains the output of your script.
+
+Make sure to replace `Your output text here` with a string which is representative of the comments made by your action.
+
+Also, please note that this is a simplified example. Exact implementation might depend on specific requirements like the content of the script to run, handling different types of errors, or parsing the output before posting it to GitHub issues.
+
+Lastly, this script assumes that you have a script named `script.sh` at the root of your repository but you can change this to wherever your script resides.
diff --git a/readability.js b/readability.js
new file mode 100644
index 0000000..02d10e8
--- /dev/null
+++ b/readability.js
@@ -0,0 +1,4 @@
+async () => {    
+  const readability = await import('https://cdn.skypack.dev/@mozilla/readability');
+  return (new readability.Readability(document)).parse();
+}
diff --git a/shell_functions.sh b/shell_functions.sh
index 8cb911a..cbc4f82 100644
--- a/shell_functions.sh
+++ b/shell_functions.sh
@@ -2,22 +2,83 @@
 # LLM stuff
 echo "FUNCTION CALLING"
 echo "FUNCTION CALLING"
-echo "FUNCTION CALLING"
-echo "FUNCTION CALLING"
-echo "MAN PAGES"
 echo "MAN PAGES"
 echo "MAN PAGES"
 echo "iDoDid"
 echo "iDoDid"
+# alias llm="llm -t concise"
+
+# Example aliases
+# alias zshconfig="mate ~/.zshrc"
+# alias ohmyzsh="mate ~/.oh-my-zsh"
+alias undecidability="$HOME/undecidability"
+OPENAI_API_KEY=$(cat /home/tommy/Development/ai/openai/openai_key)
+export OPENAI_API_KEY
+export CLAUD_SESS_KEY="/home/tommy/Development/ai/claude-sessionkey"
+export EDITOR="kate"
+alias issues='gh issue list'
+export funcs=$HOME/Development/linux-stuff/shell_functions.sh
+# export llmfuncs=$HOME/Development/scripts/llm_shell_functions.sh
+
+export GROFF_NO_SGR=1
+xmodmap -e "keycode 66 = Shift_L NoSymbol Shift_L"
+# If no x session, needs sudo:
+#  echo -e "keymaps 0-127\nkeycode 58 = Shift" | sudo loadkeys -
+
+alias readability="shot-scraper javascript -i $HOME/Development/linux-stuff/readability.js"
+
+open_kate_at_line() {
+  # Todo: split this in to two functions.
+  #   1. Return an array or tuple of file_path and line_number
+  local keyword=$1
+  local file_pattern=$2
+  # Use grep to search for the keyword in the files
+  local grep_result=$(grep --with-filename --line-number "$keyword" $file_pattern)
+  if [[ -n $grep_result ]]; then
+    # Extract the file path and line number
+    local file_path=$(echo "$grep_result" | awk -F: '{print $1}')
+    local line_number=$(echo "$grep_result" | awk -F: '{print $2}')
+    # Open the file in Kate at the specified line number
+    open $file_path -l $line_number
+  else
+    echo "No matches found."
+  fi
+}
+
+open_after_add() {
+  WINDOW_TITLE=""$Activity"_IDEAS.md"
+  WINDOW_ID=$(xdotool search --name "$WINDOW_TITLE" | head -1)
+  if [ -n "$WINDOW_ID" ]; then
+    xdotool windowactivate --sync "$WINDOW_ID"
+  else
+    kate -n "$FILE_PATH" &
+  fi
+}
+
+send_note() {
+
+  Note_Category="$1" #Idea, #Todo, #QnA, #Shopping, #CodeSnippet, #Bookmark
+  target_project="${2:-undecidability}"
+  cd $HOME/"$target_project"
+  idea_text=$(kdialog --inputbox "QuickiDea")
+  idea_text="Quick idea: $idea_text"
+  url="$(gh issue create --title "$idea_text" --body "" --label "idea")"
+  kdialog --msgbox "$url"
+
+  }
+
 
 x() { # open a gui command and close the terminal
     $(basename $SHELL) -i -c "$@ &; disown"
 }
 
-fungrep() {
+function_grep() {
+    #Todo:Refactor and Fix: "Broken. only returns part of a function."
+    #Supplement: Git source code has a tone of regexes for function definitions.
+
     echo "Does not work, only returns part of the function." && return
-    query="$1"  # what to search for
-    source="$2" # where to search for it: a file containing shell functions.
+    local query="$1"  # what to search for
+    local source="$2" # where to search for it: a file containing shell functions.
     grep -Pzo '(?s)(?<=\n)(?!function)[^\n]*'"$query"'[^\n]*' "$source"
 }
 
@@ -33,7 +94,7 @@ check_md_info_string() {
   }
 
 md() {
-  
+
   if [ -z "$1" ] # checks if $1 is empty
   then
     echo "Code body is missing."
@@ -41,37 +102,38 @@ md() {
   fi
   body="$1"
   info_string_language="${2:-plain}  "
-  
+
   # Treat remainder of inputs if provided
-  if [ -n "$2" ] 
+  if [ -n "$2" ]
   then
     shift 2
     remainder="${*}"
   fi
-  
+
   echo -e '```'"${info_string_language}"''"${remainder}"'\n'"${body}"'\n```'
 
 }
 
 kagi_enrich() {
   search_dir="$HOME/Data/kagi-enrich-results/$1"
+  # Check if the dir exists and create it if not.
   [ -d "$search_dir" ] || mkdir -p "$search_dir"
-  
+
   results_filepath="$search_dir/"$1".kagi.json"
   old_results_filepath=""$results_filepath""_$(date +%Y%m%d)""
   [ ! -f "$results_filepath" ] || mv "$results_filepath" "$old_results_filepath"
-  
+
   api_key=$(cat $HOME/Development/.kagi-enrich-api)
   encoded_q=$(jq -rn --arg q "$1" '$q|@uri')
-  
+
   printf "$encoded_q\n"
-      
+
   search_result=$( curl -H "Authorization: Bot $api_key" \
-  "https://kagi.com/api/v0/enrich/web?q=$encoded_q" ) 
+  "https://kagi.com/api/v0/enrich/web?q=$encoded_q" )
 
   [[ $(echo $search_result | jq '.data | length') -eq 0 ]] &&  touch $results_filepath ||  echo $search_result > $results_filepath
-    
-  echo $results_filepath 
+
+  echo $results_filepath
 }
 
 monitor_changes() {
@@ -84,7 +146,7 @@ monitor_changes() {
   local hook="${2}"
   local type="${3:-modify,create,delete}"
   local ext="${4}"
-  
+
   if [ ! -d "$dir" ]; then
     echo "Directory $dir does not exist."
     return 1
@@ -111,7 +173,7 @@ mkfilename() {
   # Truncate to <=400 tokens
   trunc_content=$(ttok "$file_content" -t 400)
   llm_template="makefilename"
-  echo "$trunc_content" | llm -m 3.5 -t $llm_template -o temperature 0 -o max_tokens 15
+  echo "$trunc_content" | llm -m 3.5 -t $llm_template -o temperature 0.2 -o max_tokens 15
   }
 
 commit() {
@@ -180,16 +242,17 @@ testDialogbox() {
 }
 
 dialogbox() {
-  # ToDo: Replace as many kdialog calls with a more portable dialogbox function. 
-  # Note: Zenity (at least) does not work, for some reason, when in Fleet's Terminal. Probably some subshell thing.
+  # ToDo: Replace as many kdialog calls with a more portable dialogbox function.
   local USAGE="Usage: dialogbox [message]\nDisplay a message in the first available dialog box app.\n"
   local message="$1"
 
+  # Todo: Grok this mess...
+  # check if the number of arguments passed to the script is not equal to 1 or if the variable "message" is empty
   if [ "$#" -ne 1 ] || [ -z "$message" ]; then
     echo "$USAGE"
     return 1
   fi
-    
+
     if command -v zenity >/dev/null; then
         zenity --info --text="$message"
     elif command -v kdialog >/dev/null; then
@@ -211,14 +274,63 @@ mangrep() {
   }
 
 timer() {
-  time -o $HOME/.timehistory -a "$@"
+  /bin/time -v -q -o $HOME/.timehistory -a "$@"
+  tail -n 1 $HOME/.timehistory
   }
 
+timer-old() {
+    # Function that times commands and records the command that was run
+
+    # Check if command argument is provided
+    if [ -z "$1" ]; then
+        echo "No command provided" >&2
+        return 1
+    fi
+
+    # Get the command from arguments
+    cmd="$@"
+
+    # Record the command that was run
+    echo "Command: $cmd" >> $HOME/command_log.txt
+
+    # Run the command and time it
+    {
+        start=$(date +%s)
+        eval "$cmd"
+        end=$(date +%s)
+    } 2>> $HOME/command_log.txt
+
+    # Calculate the execution time
+    execution_time="$((end-start))"
+
+    # Record the execution time
+    {
+        echo "Execution Time: $execution_time seconds"
+        echo "-------------------------------------"
+    } >> $HOME/command_log.txt
+    echo "Total Execution Time: $execution_time seconds"
+}
+
+
 did() {
   echo "$1" >> "/$HOME/DONE.txt"
 }
 
-current_activity_id() {
+activity_list_names() {
+  for id in $(activity_list_ids);
+  echo "$(activity_name_from_id $id)"
+}
+
+activity_names_array() {
+  activities=$(activity_list_names)
+  echo "${activities[@]}"
+}
+
+activity


**Response:**
Add instructions for implementing GitHub Actions workflow to run a script and post the output as a comment on an issue.

<details><summary>Metadata</summary>

- Duration: 1838 ms
- Datetime: 2023-09-12T19:21:27.153715
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

