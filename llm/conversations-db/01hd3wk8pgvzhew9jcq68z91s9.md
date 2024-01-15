**Prompt:**
diff --git a/.send-issue.sh.kate-swp b/.send-issue.sh.kate-swp
new file mode 100644
index 0000000..248603f
Binary files /dev/null and b/.send-issue.sh.kate-swp differ
diff --git a/curl.sh b/curl.sh
new file mode 100644
index 0000000..19819d3
--- /dev/null
+++ b/curl.sh
@@ -0,0 +1 @@
+curl 'https://openrouter.ai/_next/data/tQ_e6U-S9KJIjZjTzGkzq/api/v1/models.json' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Referer: https://openrouter.ai/docs' -H 'purpose: prefetch' -H 'x-middleware-prefetch: 1' -H 'x-nextjs-data: 1' -H 'sentry-trace: c6e08113673f447a849bbba364badb28-bfbeed8595d6f2f6-1' -H 'baggage: sentry-environment=vercel-production,sentry-release=b4e2e759726d0f9d902469e07db3eb177d0c0180,sentry-public_key=0ed8429ba9964f3fbba5d6f092ed2c8a,sentry-trace_id=c6e08113673f447a849bbba364badb28,sentry-sample_rate=1,sentry-transaction=%2Fdocs,sentry-sampled=true' -H 'Connection: keep-alive' -H 'Cookie: _ga_R8YZRJS2XN=GS1.1.1694727921.1.0.1694727960.0.0.0; _ga=GA1.1.2089034963.1694727921; __client_uat=0' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-origin' -H 'TE: 
diff --git a/send-issue.sh b/send-issue.sh
new file mode 100644
index 0000000..ec3e40b
--- /dev/null
+++ b/send-issue.sh
@@ -0,0 +1,23 @@
+#!/bin/bash
+  # Send an issue to github.
+  # Usage: send_issue target_project title body labels
+  target_project="${1:-undecidability}"
+  title="$2"
+  body="${3:-""}"
+  labels="${4:-unclassified}"
+
+  whiptail --title "$title" --msgbox "target: $target_project body: $body labels: $labels"
+
+  cd $HOME/"$target_project"
+
+  # Split labels by comma and append --label for each
+  IFS=',' read -ra label_array <<< "$labels"
+  label_string=""
+  for label in "${label_array[@]}"; do
+    label_string+="--label $label "
+  done
+
+  url="$(gh issue create --title "$title" --body "$body" $label_string)"
+
+  clip "$url"
+  nyxt "$url"
diff --git a/shell_functions.sh b/shell_functions.sh
old mode 100644
new mode 100755
index cbc4f82..9484dd2
--- a/shell_functions.sh
+++ b/shell_functions.sh
@@ -1,10 +1,81 @@
+#!/bin/bash
+
+# Github-cli gh
+alias which='which -a'
+alias labels='gh label list'
+# Terminal navigation
+alias data='cd $HOME/Data'
+alias docs='cd ~/Documents'
+alias downloads='cd ~/Downloads'
+alias dev='~/Development'
+alias proj='~/Development/08-2023/projects'
+alias scripts='~/Development/scripts'
+alias cdidodid='~/Development/Projects/iDoDid'
+alias bd='cd -' # back to the last directory
+# TIL: history contains only history for the current terminal.
+his() { history | grep "$1"; } #Useful for constraining searches to the session.
+alias search=his
+gsearch() { grep "$1" ~/.zhistory; }
+alias gs=gsearch
+goback() { cd $OLDPWD; }
+alias ..='cd ..'
+alias ...='cd ../..'
+alias ....='cd ../../..'
+alias .....='cd ../../../..'
+# ls directories only
+alias lsd="ls -d */"
+#. Print a tree view of the current directory
+alias treeview='ls -R | grep ":$" | sed -e "s/:$//" -e "s/[^-][^\/]*\//--/g" -e "s/^/   /" -e "s/-/|/"'
+# Get the size of directories in the current folder
+alias dsize='du -sh */'
+
+alias pgrep='pgrep -i'
+alias grep='grep -i --color=auto'
+rgrep() { grep -R "$1" . }
+
+alias open='xdg-open'
+
+# Start a python file server in the current directory
+alias serv='python3 -m http.server'
+
+# Formatting & Code Highlighting
+alias catpyg='pygmentize -g'
+alias cathi='highlight --out-format=xterm256 --style=github --force --replace-tabs=4'
+alias catglow="glow"
+
+# Defensive CLI
+alias rm='rm -I'
+alias cp='cp -i'
+alias mv='mv -i'
+alias chgrp='chgrp --preserve-root'
+alias chmod='chmod --preserve-root'
+alias chown='chown --preserve-root'
+
+# Process lookup
+alias psg='ps aux | grep -v grep | grep -i -e VSZ -e'
+
+# Open network ports
+alias ports='netstat -tulanp'
+alias speed='curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -'
+alias myip='curl ipinfo.io/ip'
+
+# File browsing
+alias ttree='tree -L 5 -D -h -prune'
+
+# Monitor changes in a directory:
+alias watch='watch -n 1'
+
+#Todo: make another logs alias for different levels of log .
+# Quick logs
+alias logs="sudo journalctl -p 0..4 -xn 50 --no-hostname"
+
+alias venv='source ./venv/bin/activate'
+alias gac='git add . && git commit -m'
 
 # LLM stuff
-echo "FUNCTION CALLING"
+echo "kmonad: layer keys"
 echo "FUNCTION CALLING"
 echo "MAN PAGES"
-echo "MAN PAGES"
-echo "iDoDid"
 echo "iDoDid"
 # alias llm="llm -t concise"
 
@@ -12,16 +83,16 @@ echo "iDoDid"
 # alias zshconfig="mate ~/.zshrc"
 # alias ohmyzsh="mate ~/.oh-my-zsh"
 alias undecidability="$HOME/undecidability"
-OPENAI_API_KEY=$(cat /home/tommy/Development/ai/openai/openai_key)
+OPENAI_API_KEY=$(cat /$HOME/Development/AI/openai/openai_key)
 export OPENAI_API_KEY
-export CLAUD_SESS_KEY="/home/tommy/Development/ai/claude-sessionkey"
+export CLAUD_SESS_KEY="/$HOME/Development/AI/claude-sessionkey"
 export EDITOR="kate"
 alias issues='gh issue list'
 export funcs=$HOME/Development/linux-stuff/shell_functions.sh
 # export llmfuncs=$HOME/Development/scripts/llm_shell_functions.sh
 
-export GROFF_NO_SGR=1
-xmodmap -e "keycode 66 = Shift_L NoSymbol Shift_L"
+# export GROFF_NO_SGR=1
+# xmodmap -e "keycode 66 = Shift_L NoSymbol Shift_L"
 # If no x session, needs sudo:
 #  echo -e "keymaps 0-127\nkeycode 58 = Shift" | sudo loadkeys -
 
@@ -32,14 +103,19 @@ open_kate_at_line() {
   #   1. Return an array or tuple of file_path and line_number
   local keyword=$1
   local file_pattern=$2
+  echo "keyword: $keyword"
+  echo "file_pattern: $file_pattern"
+
   # Use grep to search for the keyword in the files
   local grep_result=$(grep --with-filename --line-number "$keyword" $file_pattern)
+  echo "grep_result: $grep_result"
   if [[ -n $grep_result ]]; then
     # Extract the file path and line number
     local file_path=$(echo "$grep_result" | awk -F: '{print $1}')
     local line_number=$(echo "$grep_result" | awk -F: '{print $2}')
     # Open the file in Kate at the specified line number
-    open $file_path -l $line_number
+    echo "OPENING: $file_path -l $line_number"
+    kate $file_path -l $line_number
   else
     echo "No matches found."
   fi
@@ -55,43 +131,53 @@ open_after_add() {
   fi
 }
 
-send_note() {
+#Idea, #Todo, #QnA, #Shopping, #CodeSnippet, #Bookmark
 
-  Note_Category="$1" #Idea, #Todo, #QnA, #Shopping, #CodeSnippet, #Bookmark
-  target_project="${2:-undecidability}"
+send_issue1() {
+  target_project="${1:-undecidability}"
+  title="$2"
+  body="${3:-""}"
+  labels="${4:-unclassified}"
   cd $HOME/"$target_project"
-  idea_text=$(kdialog --inputbox "QuickiDea")
-  idea_text="Quick idea: $idea_text"
-  url="$(gh issue create --title "$idea_text" --body "" --label "idea")"
-  kdialog --msgbox "$url"
-
+  # ToDo: for label in labels, append --label $label
+  url="$(gh issue create --title "$title" --body "$body" --label "idea")"
+  clip "$url"
+  nyxt -r -e "(make-window (make-buffer :url "$url"))" -q
   }
 
+send_issue() {
+  # Send an issue to github.
+  # Usage: send_issue target_project title body labels
+  target_project="${1:-undecidability}"
+  title="$2"
+  body="${3:-""}"
+  labels="${4:-unclassified}"
 
-x() { # open a gui command and close the terminal
-    $(basename $SHELL) -i -c "$@ &; disown"
-}
+  whiptail --title "$title" --msgbox "target: $target_project body: $body labels: $labels"
 
-function_grep() {
-    #Todo:Refactor and Fix: "Broken. only returns part of a function."
-    #Supplement: Git source code has a tone of regexes for function definitions.
+  cd $HOME/"$target_project"
 
-    echo "Does not work, only returns part of the function." && return
-    local query="$1"  # what to search for
-    local source="$2" # where to search for it: a file containing shell functions.
-    grep -Pzo '(?s)(?<=\n)(?!function)[^\n]*'"$query"'[^\n]*' "$source"
+  # Split labels by comma and append --label for each
+  IFS=',' read -ra label_array <<< "$labels"
+  label_string=""
+  for label in "${label_array[@]}"; do
+    label_string+="--label $label "
+  done
+
+  url="$(gh issue create --title "$title" --body "$body" $label_string)"
+
+  clip "$url"
+  nyxt -r -e "(make-window (make-buffer :url \"$url\"))" -q
 }
 
-check_md_info_string() {
-  string="$1"
-  case "$string" in
-    js|ts|jsx|tsx|c|cpp|cs|java|python|php|rust|glsl|sql|wasm|webidl|css|scss|less|html|svg|xml|mathml|md|latex|bash|batch|powershell|json|ini|yaml|toml|ignore|apacheconf|nginx|django|svelte|handlebars|pug|plain|diff|http|regex|uri)
-        echo "Your info string is correct."
-        ;;
-    *)
-        ;;
-  esac
-  }
+
+send_quickidea_to_gh() {
+  target_project="${1:-undecidability}"
+  note_category="quick_idea"
+  idea_text=${2:-"$(kdialog --inputbox "QuickiDea")"}
+  idea_text="Quick idea: $idea_text"
+  send_note "$note_category" "$target_project"
+}
 
 md() {
 
@@ -114,7 +200,


**Response:**
Add new files and update shell functions.

<details><summary>Metadata</summary>

- Duration: 1915 ms
- Datetime: 2023-10-19T11:54:36.755933
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

