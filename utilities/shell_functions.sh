#!/bin/bash
SCRIPT_DIR="$(dirname "$0")"
echo "SCRIPT_DIR: $SCRIPT_DIR"

alias f2p='files-to-prompt'

# Dir shortcuts
alias data='cd $HOME/Data'
alias docs='cd $HOME/Documents'
alias downloads='cd $HOME/Downloads'
alias models='cd $HOME/Code/models'
alias scripts='cd $HOME/Code/scripts'

# Github-cli gh
alias which='which -a'
alias labels='gh label list'

# Terminal navigation and search
goback() { cd $OLDPWD; } # Go back to the last dir (same as "cd -")
alias bd='cd -' # back to the last dir

alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'

# ls directories only
alias lsd="ls -d */"
#. Print a tree view of the current directory
alias treeview='ls -R | grep ":$" | sed -e "s/:$//" -e "s/[^-][^\/]*\//--/g" -e "s/^/   /" -e "s/-/|/"'
# Get the size of directories in the current folder
alias dsize='du -sh */'

# 'history' command contains only history for the current terminal session. unless you change the .zshrc
his() { history | grep "$1"; } # Useful for constraining searches to the session.
alias search=his

# search all history
gsearch() { grep "$1" ~/.zhistory; }
alias gs=gsearch

# pgrep search for processes
alias pgrep='pgrep -i'

# grep -i is case insensitive. --color=auto highlights the matches.
alias grep='grep -i --color=auto'
# grep -R is recursive.
rgrep() { grep -R "$1" . }

# open files in default app.
alias open='xdg-open'

# Start a python file server in the current directory
alias serv='python3 -m http.server'

# Formatting & Code Highlighting
alias catpyg='pygmentize -g'
alias cathi='highlight --out-format=xterm256 --style=github --force --replace-tabs=4'
alias catglow="glow"

# Defensive CLI options
alias rm='rm -I' # -I prompts before every removal
alias cp='cp -i' # -i prompts before overwrite
alias mv='mv -i' 
alias chgrp='chgrp --preserve-root' # --preserve-root is a safety feature to prevent accidental deletion of system files.
alias chmod='chmod --preserve-root' 
alias chown='chown --preserve-root'

# Process lookup
alias psg='ps aux | grep -v grep | grep -i -e VSZ -e'

# Networking
alias ports='netstat -tulanp'
alias speed='curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -'
alias myip='curl ipinfo.io/ip'

# File browsing
alias ttree='tree -L 5 -D -h -prune'

# Monitor changes in a directory:
alias watch='watch -n 1'

#Todo: make another logs alias for different levels of log .
# Quick logs
alias logs="sudo journalctl -p 0..4 -xn 100 --no-hostname"

alias venv='source ./venv/bin/activate'
alias gac='git add . && git commit -m'

# Example aliases
# OPENAI_API_KEY=$(cat /$HOME/openai_key)
export OPENAI_API_KEY
alias issues='gh issue list'
# Todo: make funcs the path of the current script
export funcs=$PWD/shell_functions_shared.sh

alias readability="shot-scraper javascript -i $HOME/linux-stuff/readability.js"

function claude_extract() {
    curl https://api.anthropic.com/v1/messages \
        --header "x-api-key: $ANTHROPIC_API_KEY" \
        --header "anthropic-version: 2023-06-01" \
        --header "content-type: application/json" \
        --data '{ 
            "model": "claude-3-5-sonnet-20240620", 
            "max_tokens": 1000, 
            "messages": [ 
                { 
                    "role": "user", 
                    "content": "Extract the name, size, price, and color from this product description as a JSON object <description> The SmartHome Mini is a compact smart home assistant available in black or white for only $49.99. At just 5 inches wide, it lets you control lights, thermostats, and other connected devices via voice or app—no matter where you place it in your home. This affordable little hub brings convenient hands-free control to your smart devices. </description>" 
                }, 
                {"role": "assistant", "content": "{"} 
            ] 
        }' 
}


open_kate_at_line() {
    # Todo: Can we make this work for other editors besides kate?
    local Usage = "Usage: open_kate_at_line 'send_issue() {' <file_path>"
    local keyword=$1
    local file_pattern=$2
    echo "keyword: $keyword"
    echo "file_pattern: $file_pattern"

    # Use grep to search for the keyword in the files
    local grep_result=$(grep --with-filename --line-number "$keyword" $file_pattern)
    echo "grep_result: $grep_result"
    if [[ -n $grep_result ]]; then
      # Extract the file path and line number
      local file_path=$(echo "$grep_result" | awk -F: '{print $1}')
      local line_number=$(echo "$grep_result" | awk -F: '{print $2}')
      # Open the file in Kate at the specified line number
      echo "OPENING: $file_path -l $line_number"
      kate $file_path -l $line_number
    else
      echo "No matches found."
    fi
}

send_issue() {
  local target_project="$1"
  local title="$2"
  local body="${3:-""}"
  cd $HOME/"$target_project"
  gh issue create --title "$title" --body "$body" --label "idea" --web
  }

deepseek_api() {
  local model="$1"
  local content="$2"
  
  curl "https://api.deepseek.com/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $deepseek_api_key" \
  -d '{
        "model": "'"$model"'",
        "messages": [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "'"${content}"'."}
        ]
      }'
}

send_quickidea_to_gh() {
  local target_project="${1:-undecidability}"
  local note_category="quick_idea"
  local idea_text=${2:-"$(kdialog --inputbox "QuickiDea")"}
  idea_text="Quick idea: $idea_text"
  send_note "$note_category" "$target_project"
}

# Function to get the logprobs of two labels for given content
get_label_probability() {
    local content="$1"
    local label1="$2"
    local label2="$3"
    local api_key=$OPENAI_API_KEY

        # Prepare the prompt
    local prompt="Content: $content\n\nLabel this content as either '$label1' or '$label2'. Respond with only the label."

    # Make the API call
    response=$(curl -s https://api.openai.com/v1/chat/completions \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $api_key" \
        -d '{
        "model": "gpt-4-1106-preview",
        "messages": [{"role": "user", "content": "'"$prompt"'"}],
        "max_tokens": 1,
        "logprobs": 5,
        "temperature": 0
    }')

    # Extract the generated text and logprobs
    generated_text=$(echo "$response" | jq -r '.choices[0].message.content' | tr -d '\n' | tr '[:upper:]' '[:lower:]')
    logprobs=$(echo "$response" | jq -r '.choices[0].logprobs.content[0].top_logprobs')

    # Function to get probability for a label
    get_prob() {
        local label=$1
        local logprob=$(echo "$logprobs" | jq -r ".[\"$label\"] // .[\"$label:\"] // .[\" $label\"] // .[\" $label:\"] // -100")
        echo "$logprob" | bc -l
    }

    # Calculate probabilities
    logprob1=$(get_prob "$label1")
    logprob2=$(get_prob "$label2")

    # Convert logprobs to probabilities
    prob1=$(echo "e($logprob1)" | bc -l)
    prob2=$(echo "e($logprob2)" | bc -l)

    # If both probabilities are 0, use the generated text to determine the winner
    if (( $(echo "$prob1 == 0 && $prob2 == 0" | bc -l) )); then
        if [[ "$generated_text" == "$label1" ]]; then
            prob1=1
            prob2=0
        elif [[ "$generated_text" == "$label2" ]]; then
            prob1=0
            prob2=1
        fi
    fi

    # Normalize probabilities
    total=$(echo "$prob1 + $prob2" | bc -l)
    norm_prob1=$(echo "$prob1 / $total" | bc -l)
    norm_prob2=$(echo "$prob2 / $total" | bc -l)

    # Determine the label with highest probability
    if (( $(echo "$norm_prob1 > $norm_prob2" | bc -l) )); then
        winner="$label1"
        winning_prob="$norm_prob1"
    else
        winner="$label2"
        winning_prob="$norm_prob2"
    fi

    # Output result
    echo "Label: $winner"
    printf "Probability: %.4f\n" "$winning_prob"
}





llmc() {
    local continue_conversation=false
    local prompt_key=""
    local other_args=()

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case "$1" in
            -c|--continue)
                continue_conversation=true
                shift
                ;;
            -p|--prompt)
                prompt_key="$2"
                shift 2
                ;;
            *)
                other_args+=("$1")
                shift
                ;;
        esac
    done

    # Prepare the command
    local cmd=("llm")
    [[ -n "$prompt_key" ]] && cmd+=("$prompt_key")
    [[ ${#other_args[@]} -gt 0 ]] && cmd+=("${other_args[@]}")

    if $continue_conversation; then
        if [[ -n "$CONVERSATION_ID" ]]; then
            echo "Using conversation_id: $CONVERSATION_ID"
            cmd+=("--cid" "$CONVERSATION_ID")
        else
            echo "No active conversation. Starting a new one."
        fi
    fi

    # Execute the llm command
    "${cmd[@]}"

    # If not continuing a conversation, update the CONVERSATION_ID
    if ! $continue_conversation && [[ -n "$prompt_key" ]]; then
        db_query="SELECT conversation_id FROM responses WHERE prompt LIKE '%$prompt_key%' ORDER BY id DESC LIMIT 1"
        conversation_id=$(sqlite3 /home/ShellLM/.config/io.datasette.llm/logs.db "$db_query")
        if [[ -n "$conversation_id" ]]; then
            export CONVERSATION_ID="$conversation_id"
            echo "New conversation_id set: $CONVERSATION_ID"
        else
            echo "No conversation_id found for prompt: $prompt_key"
        fi
    fi
}


md() {
    if [ -z "$1" ] # checks if $1 is empty
    then
      echo "Code body is missing."
      return
    fi
    local body="$1"
    local info_string_language="${2:-plain}  "

    # Treat remainder of inputs if provided
    if [ -n "$2" ]
    then
      shift 2
      local remainder="${*}"
    fi

    echo -e '```'"${info_string_language}"''"${remainder}"'\n'"${body}"'\n```'

}


x() { 
    # open a gui command and close the terminal
    $(basename $SHELL) -i -c "$@ &; disown"
}


function_grep() {
    #Todo:Refactor and Fix: "Broken. only returns part of a function."
    #Supplemental: Git source code has a lot of regexes for function definitions.

    echo "Does not work, only returns part of the function." && return
    local query="$1"  # what to search for
    local source="$2" # where to search for it: a file containing shell functions.
    grep -Pzo '(?s)(?<=\n)(?!function)[^\n]*'"$query"'[^\n]*' "$source"
}


save_kagi_enrich() {
  local search_dir="$HOME/Data/kagi-enrich-results/$1"
  # Check if the dir exists and create it if not.
  [ -d "$search_dir" ] || mkdir -p "$search_dir"
  local results_filepath="$search_dir/"$1".kagi.json"
  local old_results_filepath=""$results_filepath""_$(date +%Y%m%d)""
  [ ! -f "$results_filepath" ] || mv "$results_filepath" "$old_results_filepath"

  local search_result="$(kagi_enrich $1)"

  [[ $(echo $search_result | jq '.data | length') -eq 0 ]] &&  touch $results_filepath ||  echo $search_result > $results_filepath

  echo $results_filepath
}


kagi_enrich() {
    local api_key=$(cat $HOME/Development/.kagi-enrich-api)
    encoded_q=$(jq -rn --arg q "$1" '$q | gsub(" "; "+")')
    echo $encoded_q
    curl -H "Authorization: Bot $api_key" \
    "https://kagi.com/api/v0/enrich/web?q="$encoded_q""
}

monitor_changes() {
  # Function to set up watches for a given a dir.
  # Nice API for calling scripts to use
  # Some callback method to notify the
  # $3 event type for inotify, default to 'modify,create,delete'
  # $4 file extensions to be monitored
  local dir="${1}"
  local hook="${2}"
  local type="${3:-modify,create,delete}"
  local ext="${4}"

  if [ ! -d "$dir" ]; then
    echo "Directory $dir does not exist."
    return 1
  fi

  while inotifywait -q -r -e "$type" --exclude '.*\..*' "$dir"; do
    # execute the hook
    "${hook}"
  done
}

explain() {
    # explain <command> # Explain a command
    # explain <command> -m <model> # Explain a command with a specified model
    # explain <model> # Explain clipboard using default model
    # explain <model> -m <model> # Explain clipboard using specified model
    
    # Initialize variables
    local model="openrouter/openai/gpt-4o"
    local query=""
    local args=("$@")

    # Check for -m option in any position
    for (( i=1; i<${#args[@]}; i++ )); do
      if [[ "${args[$i]}" == "-m" ]]; then # && (( i+1 < ${#args[@]} )); then
        model="${args[$i+1]}"
        # Remove -m and model from args
        unset 'args[$i]'
        unset 'args[$i+1]'
        break
      fi
    done

    # If no arguments are provided, use the clipboard
    if [[ ${#args[@]} -gt 0 ]]; then # If there are arguments
      # strip empty strings
      query="${args[@]}"
      # If query is empty
      if [[ -z "$query" ]] || [[ "$query" == " " ]] || [[ "$query" == "" ]]; then 
        query="$(paster)"
      fi
    else
      # echo remaining args
      query="${args[0]}"
    fi

    prompts=("Explain this shell code. 
Be concise.
Mention only serious errors.
    CODE:
    "
    "Using as few words as required.
    Explain this shell code to a linux expert. 
    Mention any serious errors:
    ")
    choice=$(( RANDOM % ${#prompts[@]} + 1 ))
    prompt_picked="${prompts[$choice]}"
    echo "Prompt: $prompt_picked $query"
    llm -o temperature 0 "$prompt_picked $query" -m "$model"
}

stripticks () {                                                                                                                                                                                                                               ✔  27s  
    sed -n "s/^.*'''\\(.*\\)'''.*$/\\1/p" # need to also strip single quotes and backticks.
}

highlightz() {
  # This script strips lines containing triple backticks followed by "python"
  # from the stdin, and then pipes the remaining lines to Pygmentize for syntax highlighting.
  # Usage: highlightz <file>
  # Usage: highlightz -s # Stream from stdin
  # Example: cat file.py | highlightz -s
  if [[ "$1" == "-s" ]]; then
    stream=true
    shift
  else
    stream=false
  fi

  # Check if pygmentize is installed
  if ! command -v pygmentize &> /dev/null
  then
      echo "Pygmentize could not be found. Please install it."
      exit 1
  fi

  # Read from stdin and process
  if $stream;
  then
      # Strip lines containing triple backticks followed by "python"
      sed -n '/^\`\`\`python/!p' | pygmentize -l python
  else
      # Read from file and process
      grep -v '^\`\`\`python' | pygmentize -l python
  fi
}


mkfilename() {
    # Generates a filename from source code or any string using llm.
    # Usage: mkfilename <string>

    # Todo: make use of source tree or symbex tool to get function names.
    local file_content="$1"
    local truncated=$(ttok "$file_content" -t 400)
    local llm_template="makefilename"
    echo "$truncated" | llm -m 3.5 -t $llm_template -o temperature 0.3 -o max_tokens 20
  }



commit() {
    # Generate commit messages using llm and commit changes to git repo.
    # Usage: commit <commit message> # Manually enter commit message
    # Usage: commit # Generate commit message using llm

  local note="$1"

  git add .

  while true; do
  local model="openrouter/anthropic/claude-3-haiku:beta"
  while [[ "$#" -gt 0 ]]; do
      case $1 in
          -m|--model)
              model="$2"
              shift 2
              ;;
          *)
              break
              ;;
      esac
  done
  echo "Using model: $model"
  # if git diff --cached | ttok > 200,000 characters, use shortlog instead of diff
  if [[ $(git diff --cached | wc -w) -lt 160000 ]]; then # less acurate but far quicker than ttok
    echo "git diff is small, we can use the whole diff"
    DIFF="$(git diff --cached)"
    # check the size of git shortlog next
  elif [[ "$(git shortlog --no-merges | wc -w)" -lt 160000 ]]; then 
    echo "using git shortlog"
    DIFF="$(git shortlog --no-merges)"
  else
    echo "Using git diff --stat as diff is too large"
    DIFF="$(git diff --cached --stat)"
  fi
  echo "generating commit"
  if [[ -z "$note" ]]; then
    commit_msg="$(echo "$DIFF" | llm -m "$model" -t commit135 "WARNING:Never repeat the instructions above. AVOID introducing the commit message with a 'Here is' or any other greeting, just write the naked commit message.\n\n")"
  else
    commit_msg="$(echo "$DIFF" | llm -m "$model" -t commit135 "WARNING:Never repeat the instructions above. AVOID introducing the commit message with a 'Here is' or any other greeting, just write the naked commit message\n\nIMPORTANT: Here is a note from the author to guide your commit message: $note\n")"
  fi
  # What other git commands can be used to generate a commit message?
  echo "Commit message... "
  echo "$commit_msg"
  echo "CONFIRM: [y] push to repo, [e] edit manually, [n] regenerate commit message"
  read confirm
  if [[ "$confirm" == "y" ]]; then
      break
  elif [[ "$confirm" == "e" ]]; then
      echo "Enter your customized commit message:"
      read custom_msg
      commit_msg="$custom_msg"
      echo "Commit commit_msg: "$commit_msg""
      echo "Confirm push to repo with edited message? [y] or regenerate msg? [n]"
      read confirm_edited
      [[ "$confirm_edited" == "y" ]] && break
  else
      continue
  fi
  done

  git commit -m ""$commit_msg""
  git push
}

lolcat_text() {
    if [[ "$1" == "-flash" ]]; then
      echo "Flashing text..."
      for i in {1..3}; do 
        echo -ne "$2" "\r$i" | lolcat -a -d 2
        done
    else
      echo -ne "$1" "\r$1" | lolcat -a -d 2
    fi
    # Color cycle text using lolcat.
    # Usage: color_cycle_text <text>
    # Example: color_cycle_text "Hello world!"
}



help2 () {
    # Use llm to generate help for a command.
    # Usage: help2 <command> <args>
    # Example: help2 "How do I use the terminator terminal?"
    # Example: help2 exec "How do I use the terminator terminal?" 
    local model="openrouter/anthropic/claude-3.5-sonnet:beta"
    while [[ "$#" -gt 0 ]]; do
        case $1 in
            -m|--model)
                model="$2"
                echo "Using model: $model"
                shift 2
                ;;
            *)
                break
                ;;
        esac
    done
    local cmd="$1"
  
    if [[ "$cmd" == "exec" ]]; then
      cmd="$2"
      shift 2
      cmd_to_exec="$(llm -m $model -t shellhelp "$cmd" "${@:2}")"
      llm -m $model "Explain this command: $cmd_to_exec"
      print -z "$cmd_to_exec"
      return
    fi
      
    if [[ "$cmd" == "-c" ]]; then # continueing
      cmd="$2"
      shift 2
      print -z $(llm -c "$cmd" "${@:2}")
    else
      print -z $(llm -o temperature 0 -t shellhelp "$cmd" "${@:2}")
    fi
}

shelp () {
    # Use llm to generate help for a command.
    local model="openrouter/openai/gpt-4o"
    while [[ "$#" -gt 0 ]]; do
        case $1 in
            -m|--model)
                model="$2"
                shift 2
                ;;
            *)
                break
                ;;
        esac
    done
    local cmd="$1"
    if [[ "$cmd" == "-c" ]]; then 
      cmd="$2"
      shift 2
      print -z $(llm -c "$cmd" "${@:2}")
    else
      response="$(llm -m $model -t shellhelp "$cmd" "${@:2}")" #  -o temperature 0 not supported in claude-3
      
      print -z "$response"
    fi
}

openrouter_models_array=(openrouter/open-orca/mistral-7b-openorca
      or-nr-capybara-34b
      openrouter/nousresearch/nous-hermes-llama2-13b
      openrouter/nousresearch/nous-hermes-yi-34b
      openrouter/meta-llama/codellama-34b-instruct
      openrouter/phind/phind-codellama-34b
      openrouter/intel/neural-chat-7b
      or-nh2-mixtral-dpo
      or-nh2-mixtral-sft # 4 secs
      or-capybara-7b
      openrouter/teknium/openhermes-2.5-mistral-7b
      openrouter/01-ai/yi-6b
      openrouter/01-ai/yi-34b
      openrouter/01-ai/yi-34b-chat
      openrouter/openai/gpt-3.5-turbo-1106 # Error, Error
      openrouter/openai/gpt-3.5-turbo # Error
      openrouter/openai/gpt-4-turbo-preview
      openrouter/openai/gpt-4-1106-preview
      or-free-mythomist-7b-32k
      freemistral7b
      free-openchat-7b)

models_array=(gpt-4-1106-preview
      gpt-4-0125-preview
      gpt-4-turbo-preview
      chatgpt
      3.5-instruct
      anycodellama-instruct
      anymix
      anyorca7b
      DiscoResearch/DiscoLM-mixtral-8x7b-v2
      NousResearch/Nous-Capybara-7B-V1p9
      NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO
      NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT
      NousResearch/Nous-Hermes-2-Yi-34B
      NousResearch/Nous-Hermes-Llama2-13b
      phind-34b-v2
      to-wizardlm-13b
      togethercomputer/Llama-2-7B-32K-Instruct
      togethercomputer/RedPajama-INCITE-7B-Instruct)


llm-rand() {
  # passthrough function to llm with random model
  # Usage: llm-rand <prompt>
  model_log="$HOME/undecidability/.scratchpad/llm-models-used.log"
  local model="${models_array[$RANDOM % ${#models_array[@]}]}"
  input_tokens=$(ttok "$1")
  time_start=$(date +%s)
  llm -m "$model" "$1" "${@:2}"
  total_time=$(($(date +%s) - $time_start))
  echo "$model $total_time $input_tokens" >> "$model_log"
}

term-keys () {
    local model="claude-3-haiku"
    while [[ "$#" -gt 0 ]]; do
        case $1 in
            -m|--model)
                model="$2"
                echo "Using model: $model"
                shift 2
                ;;
            *)
                break
                ;;
        esac
    done

    time_start=$(date +%s)
    model="claude-3-haiku"
    # echo "Using model: $model"
    template="terminator-keys-help"
    response="$(llm -m $model -t "$template" "$1" "${@:2}")"
    answer_text="$(echo "$response" | awk 'BEGIN{RS="```"} NR==1')"
    answer_command="$(echo "$response" | awk 'BEGIN{RS="```"} NR==2' | sed 's/```//g')"
    total_time=$(($(date +%s) - $time_start))
    echo "Answer retrieved in $total_time seconds."
    echo "$answer_text"
    echo 
    print -z 'xdotool key '"$answer_command"
}

term-keys-oai () {
    time_start=$(date +%s)
    model="gpt-3.5-turbo"
    # echo "Using model: $model"
    template="terminator-keys-help"
    response="$(llm -m $model -t "$template" "$1" "${@:2}")"
    answer_text="$(echo "$response" | awk 'BEGIN{RS="```"} NR==1')"
    answer_command="$(echo "$response" | awk 'BEGIN{RS="```"} NR==2' | sed 's/```//g')"
    total_time=$(($(date +%s) - $time_start))
    echo "Answer retrieved in $total_time seconds."
    echo "$answer_text"
    echo 
    print -z 'xdotool key '"$answer_command"
}

alias llm-keys=term-keys
gwern() {
  llm -o temperature 0 -t gwern "$1" "${@:2}"
}

terminator_help() {
    # Use llm man page template to generate help for terminator terminal.
    # Usage: terminator_help <request>
    # Example: terminator_help "How do I use the terminator terminal?"
    llm -t terminatorsys "$1" -o temperature 0 -m 4t
}
alias th=terminator_help
alias thx=term-keys


mkscript() {
    # use an llm prompt template to generate a shell script.
    # Usage: mkscript <request> <model>
    local input="$1"
    local model="${2:-'3.5'}" # default to 3.5 if no model is provided in the second argument.
    llm -t shellscript "$input" "-m $model" -o temperature 0.2
}

advisor() {
  local model="$2"
  llm -t advisor "$1" "$model" -o temperature 0.2
  }

klippy() {
    # Use llm template "kde" to get help with KDE Plasma desktop.
    local query="$1"
    local model="${2:-'3.5'}"
    llm -t kde "$query" "-m $model" -o temperature 0.2
  }


# Search man files
mangrep() {
  echo man "$1" | grep "$2"
  }

man2md() {
  local tool="$1"
  local body=$(zcat $(man -w "$tool") | pandoc -f man -t markdown | strip-tags)
  echo "$body" 
  }

exec_dot_desktop() {
  # Execute application from a .desktop file.
  # $1 is path to application .desktop file.
  local exec_line=$(awk '/Desktop Entry/,0' "$1" | grep -E "^Exec=" | cut -d "=" -f 2-)
  eval $exec_line
  }


dialogbox() {
    # Display a message in the first available dialog box app.
    local USAGE="Usage: dialogbox [message]"

    if [ "$#" -ne 1 ]; then
        echo "$USAGE"
        return 1
    fi
    local message="$1"

    if command -v zenity >/dev/null; then
        zenity --info --text="$message"
    elif command -v kdialog >/dev/null; then
        kdialog --msgbox "$message"
    elif command -v yad >/dev/null; then
        yad --text "$message"
    elif command -v dialog >/dev/null; then
        dialog --msgbox "$message" 10 40
    elif command -v xmessage >/dev/null; then
        xmessage "$message"
    else
        echo "$message"
    fi
}

timer() {
    # Time a command and append the results to a file.
    # Usage: timer <command> <file>
    # Example: timer "ls -l" ~/Tests/timers.txt # Append result to ~/Tests/timers.txt
    # Example: timer "ls -l" # Defaults to ~/timers.txt
    local file
    if [ "$1" = "-f" ]; then # Check if the first argument is -f
        if [ -d "$2" ] ; then # Check if the second argument is a directory
        file="$2"/timers.txt # If it is, append timers.txt to the directory
        elif [ -f "$2" ]; then # Check if the second argument is a file
        file="$2" # If it is, use it as the file
    else # If it's neither a file nor a directory, print an error message
        case "$2" in
        /*) echo "This is an absolute path"; file="$2" && touch "$2";;
        *//*) echo "This is not a valid path"; return ;;
        *) echo "This is a relative path"; file="$PWD/$2" && touch "$PWD/$2" ;;
        esac
        fi
    else
        file="$HOME/.timehistory"
    fi
    echo "$file"
    /bin/time -v -q -o "$file" -a "$@"
    tail -n 1 "$file"
  }

# GIT and GITHUB #

# Make a dir, cd into it, and initialize a git repo.
gitinit() { mkdir -p "$1" && cd "$1" && git init; }

gh_issues_for_activity() {
  # Assumes that you have a git repo with the same name as the KDE activity.
  local activity="${1:-$(activity_picker)}"
  local gh_repo="irthomasthomas/$activity"
  gh issue list -R "$gh_repo"
}

gh_issues_labels() {
    # List the labels for a given repo.
    local gh_repo="${1:-$(activity_picker)}"
    local labels=$(gh label list -R "irthomasthomas/$gh_repo")
    echo "$labels"
}

# CALL THIS FROM A WRAPPER SCRIPT
gh_issues_label_picker() {
  local label_name
  local labels="$(gh_issues_labels)"
  if [[ -t 0 ]]; then
    label_name=$(echo "$labels" | fzf | awk '{print $1}')
  else
    label_name="$(echo $labels | awk '{print $1}' | xargs kdialog --combobox "Select an label:" --default "idea")"
  fi
  echo $label_name
}

get_window_id() {
  local SEARCH_TERM="$1"
  wmctrl -l -x | grep "$SEARCH_TERM" | awk '{print $1}'
}

# FILE MANAGEMENT #

# Make a dir and cd into it.
mkcd() { mkdir -p "$1" && cd "$1"; }

# Create a directory and handle errors
try_mkdir() {
    local Usage="Usage: try_mkdir <directory>"
    local target_project_dir="$1"
    mkdir -p "$target_project_dir"
    if [[ $? -ne 0 ]]; then
        echo "Failed to create the target project directory: $target_project_dir" >&2
        return 1
    fi
}

# Empty the trash.
alias emptytrash='rm -rf ~/.local/share/Trash/*'

# Backup the current directory.
alias backupdir='tar -czvf "$(basename "$(pwd)")_$(date "+%Y-%m-%d_%H-%M-%S").tar.gz" *'


# CLIPBOARD #

clip() {
    # Copy a string to the clipboard.
    echo "$1" | xclip -selection clipboard
}
alias copystring=clip

pathclip() {
    # Copy the path of a file to the clipboard.
    echo -n $(realpath "$1") | xclip -selection clipboard
}
alias copypath=pathclip

fileclip() {
    # Copy the contents of a file to the clipboard.
    cat "$1" | xclip -selection clipboard
}
alias copyfile=fileclip

paster() {
    # Paste the contents of the clipboard.
    echo "$(xclip -selection clipboard -o)"
}
alias v='paster'

selection() {
    # Paste the contents of the selection buffer.
    xclip -selection primary -o 2>/dev/null || xclip -selection clipboard -o 2>/dev/null
  }

# FILE MANAGEMENT #
writescript() {
    # Write a script to a file.
    local current_shell=$(ps -p $$ -ocomm=)
    [[ $1 != *"#!"* ]] && echo "#!${current_shell}"
    echo "$1"
}

create_file_from_text() {
    # This function creates a new file with a name generated from user input.
    # $1 is used as the file content. $2 is the filename
    # TAGS CURRENTLY DISABLED > # If a third argument is provided, it is used to set a tag on the file.
    local filename
    local text="$1"
    [[ -z "$text" ]] && echo "Text was empty" && return
    printf "$2 \n"
    while true; do
        if [ $(ttok "$text") -gt 2000 ]; then
            text=$(ttok "$text" -t 1000)
        fi 
        # The ${2:-"alternate"} command specifies a default value if not provided.
        filename="${2:-$(llm "Think about this quietly. 
                        Generate a descriptive and simple filename, in the form of file-name.ext 
                        (e.g. ink-check.py) for this source code.: 
                        $text.")}"
        if [ -t 0 ]; then
            printf "Confirm create file: $filename [y] or regenerate filename? [n] "
            read confirm
            [[ "$confirm" == "y" ]] && break
        else
            confirm=$(kdialog --yesno "Accept filename [Yes] or Regenerate [No]?")
            [[ "$confirm" -eq "0" ]] && break
        fi
    done
    echo "$text" > "$filename"
    echo "$filename"

}

# Extract any compressed file based on its extension
extract() {
  if [ -f "$1" ]; then
    case "$1" in
      *.tar.bz2) tar xjf "$1" ;;
      *.tar.gz) tar xzf "$1" ;;
      *.bz2) bunzip2 "$1" ;; *.rar) unrar e "$1" ;;
      *.gz) gunzip "$1" ;;
      *.tar) tar xf "$1" ;;
      *.tbz2) tar xjf "$1" ;;
      *.tgz) tar xzf "$1" ;;
      *.zip) unzip "$1" ;;
      *.Z) uncompress "$1" ;;
      *.7z) 7z x "$1" ;;
      *) echo "'$1' cannot be extracted via extract()" ;;
    esac
  else echo "'$1' is not a valid file"; fi;
}

save_clipboard_entry() {
    clipboard_content=$(xclip -selection clipboard -o)
    datetime=$(get_datetime)
    # Set the path to the JSON file
    json_file="${1:-$HOME/clipboard_entries.json}"

    # Create an empty JSON file if it doesn't exist
    if [ ! -f "$json_file" ]; then
      echo "{}" > "$json_file"
    fi

    # Escape double quotes and backslashes in the clipboard content
    clipboard_content=$(echo "$clipboard_content" | sed 's/\\/\\\\/g' | sed 's/"/\\"/g')

    # Add the new entry to the JSON file
    jq --arg datetime "$datetime" --arg content "$clipboard_content" '. + {($datetime): $content}' "$json_file" > "$json_file.tmp" && mv -f "$json_file.tmp" "$json_file"
}

get_datetime() {
  date +"%Y-%m-%d %H:%M:%S"
}

monitor_clipboard_loop() {
  previous_clipboard=""
  while true; do
    current_clipboard="$(xclip -selection clipboard -o)"

    if [ "$current_clipboard" != "$previous_clipboard" ]; then
      save_clipboard_entry "$json_file"
      previous_clipboard="$current_clipboard"
    fi

    sleep 1
  done
}

stop_monitoring() {
  kill -9 $monitor_pid
  echo "Clipboard monitoring stopped."
}

start_monitoring() {
  json_file="${1:-$HOME/clipboard_entries.json}"
  # Create an empty JSON file if it doesn't exist
  if [ ! -f "$json_file" ]; then
    echo "{}" > "$json_file"
  fi
  monitor_clipboard_loop "$json_file" &
  monitor_pid=$!
  echo "Clipboard monitoring started."
}

monitor_clipboard() {
  case "$1" in
    start)
      start_monitoring "$2"
      ;;
    stop)
      stop_monitoring
      ;;
    *)
      echo "Usage: monitor_clipboard [start [json_file]|stop]"
      ;;
  esac
}

function code2prompt() {

    # wrap the code2prompt command in a function that sets a number of default excludes
    # https://github.com/mufeedvh/code2prompt/

    local arguments excludeFiles excludeFolders templatesFolder excludeExtensions
    
    templatesFolder="${HOME}/git/code2prompt/templates"
    excludeFiles=".editorconfig,.eslintignore,.eslintrc,tsconfig.json,.gitignore,.npmrc,LICENSE,esbuild.config.mjs,manifest.json,package-lock.json,\
    version-bump.mjs,versions.json,yarn.lock,CONTRIBUTING.md,CHANGELOG.md,SECURITY.md,.nvmrc,.env,.env.production,.prettierrc,.prettierignore,.stylelintrc,\
    CODEOWNERS,commitlint.config.js,renovate.json,pre-commit-config.yaml,.vimrc,poetry.lock,changelog.md,contributing.md,.pretterignore,.prettierrc.json,\
    .prettierrc.yml,.prettierrc.js,.eslintrc.js,.eslintrc.json,.eslintrc.yml,.eslintrc.yaml,.stylelintrc.js,.stylelintrc.json,.stylelintrc.yml,.stylelintrc.yaml"
    excludeFolders="screenshots,dist,node_modules,.git,.github,.vscode,build,coverage,tmp,out,temp,logs"
    excludeExtensions="png,jpg,jpeg,gif,svg,mp4,webm,avi,mp3,wav,flac,zip,tar,gz,bz2,7z,iso,bin,exe,app,dmg,deb,rpm,apk,fig,xd,blend,fbx,obj,tmp,swp,\
    lock,DS_Store,sqlite,log,sqlite3,dll,woff,woff2,ttf,eot,otf,ico,icns,csv,doc,docx,ppt,pptx,xls,xlsx,pdf,cmd,bat,dat,baseline,ps1,bin,exe,app,tmp,diff,bmp,ico"

    echo "---"
    echo "Available templates:"
    ls -1 "$templatesFolder"
    echo "---"

    echo "Excluding files: $excludeFiles"
    echo "Excluding folders: $excludeFolders"
    echo "Run with -nn to disable the default excludes"

    # array of build arguments
    arguments=("--tokens")

    # if -t and a template name is provided, append the template flag with the full path to the template to the arguments array
    if [[ $1 == "-t" ]]; then
      arguments+=("--template" "$templatesFolder/$2")
      shift 2
    fi

    if [[ $1 == "-nn" ]]; then
      command code2prompt "${arguments[@]}" "${@:2}" # remove the -nn flag
    else
      command code2prompt "${arguments[@]}" --exclude-files "$excludeFiles" --exclude-folders "$excludeFolders" --exclude "$excludeExtensions" "${*}"
    fi
  }

clipimgur() {
    import png:- | imgur
  }


catselect() {
  # Path to store the state and selections
  STATE_FILE="/tmp/selection_stitch_state"
  SELECTION_FILE="/tmp/selection_stitch_selection"

  # Initialize state and selection storage if not present
  if [ ! -f "$STATE_FILE" ]; then
      echo "IDLE" > "$STATE_FILE"
      echo "" > "$SELECTION_FILE"
  fi

  # Read current state
  STATE=$(cat "$STATE_FILE")

  case $STATE in
      IDLE)
          # Capture the first selection and transition to FIRST_SELECTION_CAPTURED
          xclip -o -selection primary > "$SELECTION_FILE"
          echo "FIRST_SELECTION_CAPTURED" > "$STATE_FILE"
          kdialog --passivepopup "First selection captured." 2
          ;;
      FIRST_SELECTION_CAPTURED)
          # Capture the second selection, stitch with the first, copy to clipboard, and transition to IDLE
          FIRST_SELECTION=$(cat "$SELECTION_FILE")
          SECOND_SELECTION=$(xclip -o -selection primary)
          echo "$FIRST_SELECTION $SECOND_SELECTION" | xclip -selection clipboard
          echo "IDLE" > "$STATE_FILE"
          kdialog --passivepopup "Selection stitched and copied to clipboard." 2
          ;;
      *)
          # Reset to IDLE state in case of unexpected state
          echo "IDLE" > "$STATE_FILE"
          ;;
  esac
}
monitor_clipboard() {
    xclip -selection clipboard -o | while IFS= read -r previous; do
        while true; do
            current=$(xclip -selection clipboard -o)
            if [[ "$current" != "$previous" ]]; then
                echo "$current"
                previous="$current"
            fi
            sleep 1
        done
    done
}
