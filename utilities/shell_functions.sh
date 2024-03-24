#!/bin/bash
SCRIPT_DIR="$(dirname "$0")"
echo "SCRIPT_DIR: $SCRIPT_DIR"
source "/home/thomas/Development/linux-stuff/copy_file_tags.sh"

# Github-cli gh
alias which='which -a'
alias labels='gh label list'
# Terminal navigation
alias data='cd $HOME/Data'
alias docs='cd ~/Documents'
alias downloads='cd ~/Downloads'
alias dev='~/Development'
alias proj='~/Development/08-2023/projects'
alias scripts='~/Development/scripts'
alias cdidodid='~/Development/Projects/iDoDid'
alias bd='cd -' # back to the last directory
# TIL: history contains only history for the current terminal.
his() { history | grep "$1"; } #Useful for constraining searches to the session.
alias search=his
gsearch() { grep "$1" ~/.zhistory; }
alias gs=gsearch
goback() { cd $OLDPWD; }
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

alias pgrep='pgrep -i'
alias grep='grep -i --color=auto'
rgrep() { grep -R "$1" . }

alias open='xdg-open'

# Start a python file server in the current directory
alias serv='python3 -m http.server'

# Formatting & Code Highlighting
alias catpyg='pygmentize -g'
alias cathi='highlight --out-format=xterm256 --style=github --force --replace-tabs=4'
alias catglow="glow"

# Defensive CLI
alias rm='rm -I'
alias cp='cp -i'
alias mv='mv -i'
alias chgrp='chgrp --preserve-root'
alias chmod='chmod --preserve-root'
alias chown='chown --preserve-root'

# Process lookup
alias psg='ps aux | grep -v grep | grep -i -e VSZ -e'

# Open network ports
alias ports='netstat -tulanp'
alias speed='curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -'
alias myip='curl ipinfo.io/ip'

# File browsing
alias ttree='tree -L 5 -D -h -prune'

# Monitor changes in a directory:
alias watch='watch -n 1'

#Todo: make another logs alias for different levels of log .
# Quick logs
alias logs="sudo journalctl -p 0..4 -xn 50 --no-hostname"

alias venv='source ./venv/bin/activate'
alias gac='git add . && git commit -m'

# LLM stuff
echo "kmonad: layer keys"
echo "FUNCTION CALLING"
echo "MAN PAGES"
echo "iDoDid"
# alias llm="llm -t concise"

# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
alias undecidability="$HOME/undecidability"
OPENAI_API_KEY=$(cat /$HOME/Development/AI/openai/openai_key)
export OPENAI_API_KEY
export EDITOR="kate"
alias issues='gh issue list'
export funcs=$HOME/Development/linux-stuff/shell_functions.sh

alias readability="shot-scraper javascript -i $HOME/Development/linux-stuff/readability.js"

open_kate_at_line() {
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

open_after_add() {
  WINDOW_TITLE=""$Activity"_IDEAS.md"
  WINDOW_ID=$(xdotool search --name "$WINDOW_TITLE" | head -1)
  if [ -n "$WINDOW_ID" ]; then
    xdotool windowactivate --sync "$WINDOW_ID"
  else
    kate -n "$FILE_PATH" &
  fi
}

#Idea, #Todo, #QnA, #Shopping, #CodeSnippet, #Bookmark

send_issue1() {
  target_project="${1:-undecidability}"
  title="$2"
  body="${3:-""}"
  labels="${4:-unclassified}"
  cd $HOME/"$target_project"
  # ToDo: for label in labels, append --label $label
  url="$(gh issue create --title "$title" --body "$body" --label "idea")"
  clip "$url"
  nyxt -r -e "(make-window (make-buffer :url "$url"))" -q
  }

send_issue() {
  # Send an issue to github.
  # Usage: send_issue target_project title body labels
  title="$1"
  body="${2:-""}"
  labels="${3:-unclassified}"
  target_project="undecidability"

  cd $HOME/"$target_project"

  # Split labels by comma and append --label for each
  IFS=',' read -ra label_array <<< "$labels"
  label_string=""
  for label in "${label_array[@]}"; do
    label_string+="--label $label "
  done

  yad --title="$title" --text="Title: $title\nTarget: $target_project \nbody: $body\nlabels: $labels\nlabel_string: $label_string" --button="OK":0

  url="$(gh issue create --title "$title" --body "$body" $label_string)"

  clip "$url"
  nyxt "$url"
#   nyxt -r -e "(make-window (make-buffer :url \"$url\"))" -q
}


send_quickidea_to_gh() {
  target_project="${1:-undecidability}"
  note_category="quick_idea"
  idea_text=${2:-"$(kdialog --inputbox "QuickiDea")"}
  idea_text="Quick idea: $idea_text"
  send_note "$note_category" "$target_project"
}

send_note() {
#   Note_Category="$1" #Idea, #Todo, #QnA, #Shopping, #CodeSnippet, #Bookmark
  title="$1"
  body="$2"
  target_project="undecidability"
  cd $HOME/"$target_project"
  url="$(gh issue create --title "$title" --body "$body" --label "unclassified")"
  "$url"
  }

md() {

  if [ -z "$1" ] # checks if $1 is empty
  then
    echo "Code body is missing."
    return
  fi
  body="$1"
  info_string_language="${2:-plain}  "

  # Treat remainder of inputs if provided
  if [ -n "$2" ]
  then
    shift 2
    remainder="${*}"
  fi

  echo -e '```'"${info_string_language}"''"${remainder}"'\n'"${body}"'\n```'

}

x() { # open a gui command and close the terminal
    $(basename $SHELL) -i -c "$@ &; disown"
}

function_grep() {
    #Todo:Refactor and Fix: "Broken. only returns part of a function."
    #Supplement: Git source code has a tone of regexes for function definitions.

    echo "Does not work, only returns part of the function." && return
    local query="$1"  # what to search for
    local source="$2" # where to search for it: a file containing shell functions.
    grep -Pzo '(?s)(?<=\n)(?!function)[^\n]*'"$query"'[^\n]*' "$source"
}


save_kagi_enrich() {
  search_dir="$HOME/Data/kagi-enrich-results/$1"
  # Check if the dir exists and create it if not.
  [ -d "$search_dir" ] || mkdir -p "$search_dir"

  results_filepath="$search_dir/"$1".kagi.json"
  old_results_filepath=""$results_filepath""_$(date +%Y%m%d)""
  [ ! -f "$results_filepath" ] || mv "$results_filepath" "$old_results_filepath"

  search_result="$(kagi_enrich $1)"

  [[ $(echo $search_result | jq '.data | length') -eq 0 ]] &&  touch $results_filepath ||  echo $search_result > $results_filepath

  echo $results_filepath
}


kagi_enrich() {
  api_key=$(cat $HOME/Development/.kagi-enrich-api)
#  encoded_q=$(jq -rn --arg q "$1" '$q|@uri')
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



explain1() {
  query="${1:-$(paster)}"
  echo "$query" | llm -o temperature 0.1 "Using as few words as possible, explain:\n"
  }

explain() {
  query="${1:-$(paster)}"
  promptA="**System: Arch - Linux Kernel 6.0.**
          Explain this bash code. Mention serious errors if there are any.:
          $query"
  promptB="Explain this bash code. Be concise. Only mention serious errors.
          CODE:
          $query"
  promptC="Use as few words as required. Explain this bash code to a linux expert. Also mention any serious errors:\n$query"

  choice="prompt$(echo -n 'A B C' | tr ' ' '\n' | shuf -n 1)"
  echo "Choice: $choice"
  prompt_picked="$(eval echo \$$choice)"
  echo "$prompt_picked"
  llm -o temperature 0 "$prompt_picked" -m 4t
  }

cllm() {
  echo "$1" | claude --key $CLAUD_SESS_KEY
  }

mkfilename() {
  file_content="$1"
  # Truncate to <=400 tokens
  trunc_content=$(ttok "$file_content" -t 400)
  llm_template="makefilename"
  echo "$trunc_content" | llm -m 3.5 -t $llm_template -o temperature 0.2 -o max_tokens 15
  }

save_codeblock_to_file_old() {
  text=''
  while IFS= read -r line; do
      text="${text}\n${line}"
  done

  regex='\`\`\`(.+?)\`\`\`'

  while [[ "${text}" =~ $regex ]]; do
      code_content="${BASH_REMATCH[1]}"
      text=${text/"```${code_content}```"/}

      filename=$(mkfilename "${code_content}")
      while [ -f "$filename" ]; do
        read -p "The file already exists. Enter a different filename: " new_filename
        filename="$new_filename"
      done
      echo -e "${code_content}" > "${filename}"
done
}

save_codeblock_to_file() {
  # Initialize variables
  in_code_block=false
  filename=""
  n=1
  text=""

  # Read from stdin
  while IFS= read -r line; do
    text="${text}
${line}"

    # Check if the line starts a code block
    if [[ $line == \`\`\`* ]]; then
      if $in_code_block; then
        # If we're in a code block, this line ends it
        in_code_block=false
        # Close the file
        exec 3>&-
      else
        # If we're not in a code block, this line starts it
        in_code_block=true
        # Generate a filename with n
        filename="mkfilename_${n}_$(date +%s)"
        # Open the file for writing
        exec 3>"$filename"
      fi
    elif $in_code_block; then
      # If we're in a code block, write the line to the file
      echo "$line" >&3
    fi
    ((n++))
  done

  # If we're still in a code block at the end, close the file
  if $in_code_block; then
    exec 3>&-
  fi
}

commit_old() {
  msg="$1"
  git add .

  [[ ! -z "$msg" ]] && git commit -m "$msg"

    while true; do
      msg=$(llm -t commit135 -o temperature 0.3 "$(git diff --cached | ttok -t 3000)") # -m 3.5-16k
      echo "Commit Msg: "$msg""
      echo "Confirm push to repo? [y] or regenerate msg? [n]"
      read confirm
      [[ "$confirm" == "y" ]] || continue
      break
    done

    git commit -m ""$msg""
}

commit() {

  msg="$1"

  git add .

  [[ ! -z "$msg" ]] && git commit -m "$msg"

    while true; do
      msg=$(llm -t commit135 -o temperature 0.3 "$(git diff --cached | ttok -t 3000)")
      echo "Commit Msg: "$msg""
      echo "Confirm push to repo? [y], edit msg? [e] or regenerate msg? [n]"
      read confirm
      if [[ "$confirm" == "y" ]]; then
        break
      elif [[ "$confirm" == "e" ]]; then
        echo "Enter your customized commit message:"
        read custom_msg
        msg="$custom_msg"
        echo "Commit Msg: "$msg""
        echo "Confirm push to repo with edited message? [y] or regenerate msg? [n]"
        read confirm_edited
        [[ "$confirm_edited" == "y" ]] && break
      else
        continue
      fi
    done

    git commit -m ""$msg""
    git push
}


# TODO nolog() { llm  }


help () {
        print -z $(llm -o temperature 0 -t shellhelp "$1" "${@:2}")
}


gwern() {
  llm -o temperature 0 -t gwern "$1" "${@:2}"
}

terminator() {
  llm -t man-terminator "$1" -o temperature 0 -m 4t
}

mkscript() {
  input="$1"
  model="$2"
  llm -t shellscript "$input" "$model" -o temperature 0.2
}

advisor() {
  model="$2"
  llm -t advisor "$1" "$model" -o temperature 0.2
  }

klippy() {
  model="$2"
  llm -t kde "$1" "$model" -o temperature 0.2
  }

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################


# Search man files
mangrep() {
  echo man "$1" | grep "$2"
  }

man2gh() {
  tool="$1"
  body=$(zcat $(man -w "$tool") | pandoc -f man -t markdown | strip-tags)
  }

exec_dot_desktop() {
  # Execute the .desktop file.
  # $1 is path to application .desktop file.
  exec_line=$(awk '/Desktop Entry/,0' "$1" | grep -E "^Exec=" | cut -d "=" -f 2-); eval $exec_line
  }


dialogbox() {
  # ToDo: Replace as many kdialog calls with a more portable dialogbox function.
  local USAGE="Usage: dialogbox [message]\nDisplay a message in the first available dialog box app.\n"
  local message="$1"

  # Todo: Grok this mess...
  # check if the number of arguments passed to the script is not equal to 1 or if the variable "message" is empty
  if [ "$#" -ne 1 ] || [ -z "$message" ]; then
    echo "$USAGE"
    return 1
  fi

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
  if [ "$1" = "-f" ]; then
    if [ -d "$2" ] ; then
      file="$2"/timers.txt
    elif [ -f "$2" ]; then
      file="$2"
    else
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

# Function to create a directory and handle errors
try_mkdir() {
  local target_project_dir="$1"
  mkdir -p "$target_project_dir"
  if [[ $? -ne 0 ]]; then
    echo "Failed to create the target project directory: $target_project_dir" >&2
    return 1
  fi
}

did() {
  echo "$1" >> "/$HOME/DONE.txt"
}

activity_list_names() {
  for id in $(activity_list_ids)
    do
      echo "$(activity_name_from_id $id)"
    done
}

activity_names_array() {
  activities=$(activity_list_names)
  echo "${activities[@]}"
}

activity_list_ids() {
  qdbus org.kde.ActivityManager /ActivityManager/Activities ListActivities
}

activity_current_id() {
  qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity
  }

activity_name_from_id() {
  qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$1"
  }

activity_picker() {
  activity_names_array | xargs kdialog --combobox "Select an activity:" --default "$(activity_name_from_id "$(activity_current_id)")"
}

gh_issues_for_activity() {
  activity="${1:-$(activity_picker)}"
  gh_repo="irthomasthomas/$activity"
  gh issue list -R "$gh_repo"
}

gh_issues_labels() {
  local gh_repo="${1:-$(activity_picker)}"
  local labels=$(gh label list -R "irthomasthomas/$gh_repo")
  echo "$labels"
}

# CALL THIS FROM A WRAPPER SCRIPT
gh_issues_label_picker() {
  local labels="$(gh_issues_labels)"
  if [[ -t 0 ]]; then
    label_name=$(echo "$labels" | fzf | awk '{print $1}')
    kdialog --msgbox "This a terminal"
  else
    label_name="$(echo $labels | awk '{print $1}' | xargs kdialog --combobox "Select an label:" --default "idea")"
  fi
  echo $label_name
}


get_window_id() {
  SEARCH_TERM="$1"
  wmctrl -l -x | grep "$SEARCH_TERM" | awk '{print $1}'
}

swap_two_keybindings() {
  # extract keyboard bindings and commands
  bindkey1=$(echo $1 | cut -d" " -f1,2)
  cmd1=$(echo $1 | cut -d" " -f3)
  bindkey2=$(echo $2 | cut -d" " -f1,2)
  cmd2=$(echo $2 | cut -d" " -f3)

  #swap commands
  echo "$bindkey1 $cmd2"
  echo "$bindkey2 $cmd1"
  }

gitinit() { mkdir -p "$1" && cd "$1" && git init; }
mkcd() { mkdir -p "$1" && cd "$1"; }
alias emptytrash='rm -rf ~/.local/share/Trash/*'
alias backupdir='tar -czvf "$(basename "$(pwd)")_$(date "+%Y-%m-%d_%H-%M-%S").tar.gz" *'
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


#############
# CLIPBOARD #
#############

clip() {
  echo "$1" | xsel -b
}
alias copystring=clip

pathclip() {
  echo -n $(realpath "$1") | xsel -b
}
alias copypath=pathclip

fileclip() {
  cat "$1" | xsel -b
}
alias copyfile=fileclip

paster() {
  echo "$(xsel -b -o)"
}

selection() {
  # xclip -selection clipboard -o || xsel --clipboard --output
  # fix to use selection buffer

  xclip -selection primary -o 2>/dev/null || xsel --primary --output 2>/dev/null
  # Todo: silence the warning when xclip not found
  }

writescript() {
    current_shell=$(ps -p $$ -ocomm=)
    [[ $1 != *"#!"* ]] && echo "#!${current_shell}"
    echo "$1"
}

create_file_from_clipbrd() {
# This function creates a new file with a name generated from user input.
# $1 is used as the file content. $2 is the filename
# TAGS CURRENTLY DISABLED > # If a third argument is provided, it is used to set a tag on the file.
  clipboard="$1"
  [[ -z "$clipboard" ]] && echo "Clipboard was empty" && return
  printf "$2 \n"
  while true; do
      if [ $(ttok "$clipboard") -gt 2000 ]; then
        clipboard=$(ttok "$clipboard" -t 1000)
      fi
      # The ${2:-"alternate"} Specifies a default value if not provided.
      filename="${2:-$(llm "Think about this quietly. Generate a descriptive and simple filename, in the form of file-name.ext (e.g. ink-check.py) for this script: \n\n $clipboard.")}"
      if [ -t 0 ]; then
        printf "Confirm create file: $filename [y] or regenerate filename? [n] "
        read confirm
        [[ "$confirm" == "y" ]] && break
      else
        confirm=$(kdialog --yesno "Accept filename [Yes] or Regenerate [No]?")
        [[ "$confirm" -eq "0" ]] && break
      fi
  done
  echo "$clipboard" > "$filename"
  echo "$filename"
#  [[ -n "$3" ]] && setfattr -n user.xdg.tags -v "$3" "$filename"

}

alias copy='xsel -b'

alias v='paster'
