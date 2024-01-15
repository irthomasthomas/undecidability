**Prompt:**
diff --git a/llm/phi2-run.py b/llm/phi2-run.py
new file mode 100644
index 0000000..e3c315d
--- /dev/null
+++ b/llm/phi2-run.py
@@ -0,0 +1,38 @@
+# from huggingface_hub import snapshot_download
+import torch
+from transformers import AutoModelForCausalLM, AutoTokenizer
+import time
+
+def generate(prompt: str, tokenizer, model, generation_params: dict = {"max_length":200})-> str : 
+    print("Generating...")
+    
+    # Start timing for prompt processing
+    prompt_time_begin = time.time()
+    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
+    prompt_time_end = time.time()
+    total_prompt_tokens = len(prompt)  # Assuming 1 token per character, adjust as needed
+    print(f"Prompts: {total_prompt_tokens} tokens, {total_prompt_tokens / (prompt_time_end - prompt_time_begin):.2f} tokens/second")
+    
+    # Start timing for token generation
+    token_time_begin = time.time()
+    outputs = model.generate(**inputs, **generation_params)
+    token_time_end = time.time()
+    total_gen_tokens = len(tokenizer.batch_decode(outputs)[0])  # Assuming 1 token per character, adjust as needed
+    print(f"Tokens: {total_gen_tokens} tokens, {total_gen_tokens / (token_time_end - token_time_begin):.2f} tokens/second")
+    
+    completion = tokenizer.batch_decode(outputs)[0]
+    return completion
+
+
+# model_path = "/home/thomas/Development/Projects/llm/phi2/MS-f16-phi-2/phi-2"
+model_path = "/home/thomas/Development/Projects/llm/phi2/phi-2"
+
+tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
+model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", trust_remote_code=True)
+
+torch.set_default_dtype(torch.float16)
+print("Testing models in float16...")
+print("---------------------------------------------------------------------------------")
+result = generate("There's always a brighter future if", tokenizer, model)  # Assuming generate function takes tokenizer and model as arguments
+print(result)
+print("---------------------------------------------------------------------------------")
diff --git a/shell_functions.sh b/shell_functions.sh
new file mode 100755
index 0000000..0fad16c
--- /dev/null
+++ b/shell_functions.sh
@@ -0,0 +1,698 @@
+#!/bin/bash
+SCRIPT_DIR="$(dirname "$0")"
+echo "SCRIPT_DIR: $SCRIPT_DIR"
+source "/home/thomas/Development/linux-stuff/copy_file_tags.sh"
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
+
+# LLM stuff
+echo "kmonad: layer keys"
+echo "FUNCTION CALLING"
+echo "MAN PAGES"
+echo "iDoDid"
+# alias llm="llm -t concise"
+
+# Example aliases
+# alias zshconfig="mate ~/.zshrc"
+# alias ohmyzsh="mate ~/.oh-my-zsh"
+alias undecidability="$HOME/undecidability"
+OPENAI_API_KEY=$(cat /$HOME/Development/AI/openai/openai_key)
+export OPENAI_API_KEY
+export EDITOR="kate"
+alias issues='gh issue list'
+export funcs=$HOME/Development/linux-stuff/shell_functions.sh
+
+alias readability="shot-scraper javascript -i $HOME/Development/linux-stuff/readability.js"
+
+open_kate_at_line() {
+  local keyword=$1
+  local file_pattern=$2
+  echo "keyword: $keyword"
+  echo "file_pattern: $file_pattern"
+
+  # Use grep to search for the keyword in the files
+  local grep_result=$(grep --with-filename --line-number "$keyword" $file_pattern)
+  echo "grep_result: $grep_result"
+  if [[ -n $grep_result ]]; then
+    # Extract the file path and line number
+    local file_path=$(echo "$grep_result" | awk -F: '{print $1}')
+    local line_number=$(echo "$grep_result" | awk -F: '{print $2}')
+    # Open the file in Kate at the specified line number
+    echo "OPENING: $file_path -l $line_number"
+    kate $file_path -l $line_number
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
+#Idea, #Todo, #QnA, #Shopping, #CodeSnippet, #Bookmark
+
+send_issue1() {
+  target_project="${1:-undecidability}"
+  title="$2"
+  body="${3:-""}"
+  labels="${4:-unclassified}"
+  cd $HOME/"$target_project"
+  # ToDo: for label in labels, append --label $label
+  url="$(gh issue create --title "$title" --body "$body" --label "idea")"
+  clip "$url"
+  nyxt -r -e "(make-window (make-buffer :url "$url"))" -q
+  }
+
+send_issue() {
+  # Send an issue to github.
+  # Usage: send_issue target_project title body labels
+  title="$1"
+  body="${2:-""}"
+  labels="${3:-unclassified}"
+  target_project="undecidability"
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
+  yad --title="$title" --text="Title: $title\nTarget: $target_project \nbody: $body\nlabels: $labels\nlabel_string: $label_string" --button="OK":0
+
+  url="$(gh issue create --title "$title" --body "$body" $label_string)"
+
+  clip "$url"
+  nyxt "$url"
+#   nyxt -r -e "(make-window (make-buffer :url \"$url\"))" -q
+}
+
+
+send_quickidea_to_gh() {
+  target_project="${1:-undecidability}"
+  note_category="quick_idea"
+  idea_text=${2:-"$(kdialog --inputbox "QuickiDea")"}
+  idea_text="Quick idea: $idea_text"
+  send_note "$note_category" "$target_project"
+}
+
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
+md() {
+
+  if [ -z "$1" ] # checks if $1 is empty
+  then
+    echo "Code body is missing."
+    return
+  fi
+  body="$1"
+  info_string_language="${2:-plain}  "
+
+  # Treat remainder of inputs if provided
+  if [ -n "$2" ]
+  then
+    shift 2
+    remainder="${*}"
+  fi
+
+  echo -e '```'"${info_string_language}"''"${remainder}"'\n'"${body}"'\n```'
+
+}
+
+x() { # open a gui command and close the terminal
+    $(basename $SHELL) -i -c "$@ &; disown"
+}
+
+function_grep() {
+    #Todo:Refactor and Fix: "Broken. only returns part of a function."
+    #Supplement: Git source code has a tone of regexes for function definitions.
+
+    echo "Does not work, only returns part of the function." && return
+    local query="$1"  # what to search for
+    local source="$2" # where to search for it: a file containing shell functions.
+    grep -Pzo '(?s)(?<=\n)(?!function)[^\n]*'"$query"'[^\n]*' "$source"
+}
+
+
+save_kagi_enrich() {
+  search_dir="$HOME/Data/kagi-enrich-results/$1"
+  # Check if the dir exists and create it if not.
+  [ -d "$search_dir" ] || mkdir -p "$search_dir"
+
+  results_filepath="$search_dir/"$1".kagi.json"
+  old_results_filepath=""$results_filepath""_$(date +%Y%m%d)""
+  [ ! -f "$results_filepath" ] || mv "$results_filepath" "$old_results_filepath"
+
+  search_result="$(kagi_enrich $1)"
+
+  [[ $(echo $search_result | jq '.data | length') -eq 0 ]] &&  touch $results_filepath ||  echo $search_result > $results_filepath
+
+  echo $results_filepath
+}
+
+
+kagi_enrich() {
+  api_key=$(cat $HOME/Development/.kagi-enrich-api)
+#  encoded_q=$(jq -rn --arg q "$1" '$q|@uri')
+  encoded_q=$(jq -rn --arg q "$1" '$q | gsub(" "; "+")')
+  echo $encoded_q
+  curl -H "Authorization: Bot $api_key" \
+  "https://kagi.com/api/v0/enrich/web?q="$encoded_q""
+
+}
+
+monitor_changes() {
+  # Function to set up watches for a given a dir.
+  # Nice API for calling scripts to use
+  # Some callback method to notify the
+  # $3 event type for inotify, default to 'modify,create,delete


**Response:**
Add shell functions and LLM code to project dir

<details><summary>Metadata</summary>

- Duration: 1610 ms
- Datetime: 2023-12-14T18:27:25.163863
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

