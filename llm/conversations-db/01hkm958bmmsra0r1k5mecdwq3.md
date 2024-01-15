**Prompt:**
diff --git a/Bash-Doodles/activity-file-add.sh b/Bash-Doodles/activity-file-add.sh
new file mode 100644
index 0000000..56bf6f0
--- /dev/null
+++ b/Bash-Doodles/activity-file-add.sh
@@ -0,0 +1,39 @@
+#!/bin/bash
+
+# Define function to get current activity
+get_activity() {
+  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
+  Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
+}
+
+# Define function to set file path
+set_filepath() {
+  FILE_PATH="$HOME/Activities/$Activity/${Activity}_$CATEGORY.md"
+}
+
+# Define function to open file after adding
+open_after_add() {
+  WINDOW_TITLE="${Activity}_${CATEGORY}.md"
+  WINDOW_ID=$(xdotool search --name "$WINDOW_TITLE" | head -1)
+  [[ -n "$WINDOW_ID" ]] && xdotool windowactivate --sync "$WINDOW_ID" || fleet -n "$FILE_PATH" &
+}
+
+# Main function to handle input and file operations
+main() {
+  CATEGORY=$1
+  GLOBAL=$2
+  OPEN_AFTER=$3
+
+  [[ $GLOBAL == "TRUE" ]] || get_activity && set_filepath
+  FILE_PATH="$HOME/$CATEGORY.md"
+
+  text=$(kdialog --textinputbox "$CATEGORY")
+  [[ -z "$text" ]] && echo "You did not provide any input" && exit 1
+
+  echo "\n$text" >> "$FILE_PATH"
+
+  [[ $OPEN_AFTER == "TRUE" ]] && open_after_add
+}
+
+# Call main function with arguments
+main "$@"
diff --git a/Bash-Doodles/bash_script.sh b/Bash-Doodles/bash_script.sh
new file mode 100644
index 0000000..91086c5
--- /dev/null
+++ b/Bash-Doodles/bash_script.sh
@@ -0,0 +1,46 @@
+#!/usr/bin/env bash
+
+# Initialize ShellMonStatus to off
+ShellMonStatus="off"
+
+# Initialize the array to store command input/output
+output=()
+
+# Function to toggle ShellMonStatus
+toggle_ShellMonStatus() {
+  if [[ "${ShellMonStatus}" == "off" ]]; then
+    ShellMonStatus="on"
+    echo "Shell Monitoring enabled."
+  else
+    ShellMonStatus="off"
+    echo "Shell Monitoring disabled."
+  fi
+}
+
+# Function to store command input/output
+log_output() {
+  local command_output=$("$@" 2>&1)
+  if [[ "${#output[@]}" -eq 10 ]]; then
+    # Remove the oldest item if array is full
+    output=("${output[@]:1}")
+  fi
+  # Store the command output in the array
+  output+=("${command_output}")
+}
+
+# Function to access stored output by index
+get_output() {
+  if [[ ! -z "${1}" ]]; then
+    local index=$(( ${#output[@]} - 1 - $1 ))
+    if [[ "$index" -ge 0 && "$index" -lt "${#output[@]}" ]]; then
+      echo "output:$1=${output[$index]}"
+    else
+      echo "Invalid index: $1"
+    fi
+  else
+    echo "Invalid index. Usage: get_output {index}"
+  fi
+}
+
+# Invoke the functions with provided arguments
+"$@"
diff --git a/Bash-Doodles/cli2.sh b/Bash-Doodles/cli2.sh
new file mode 100644
index 0000000..591afe2
--- /dev/null
+++ b/Bash-Doodles/cli2.sh
@@ -0,0 +1,208 @@
+#!/usr/bin/env bash
+#
+# Utility funtions for the cli
+#   jaagr <c@rlberg.se>
+#
+
+include utils/log.sh
+
+test '[post-pass:require-fn=cli::parse]'
+declare -gA __map=()
+declare -gA __revmap=()
+declare -gA __values=()
+declare -gA __flags=()
+declare -ga __positional=()
+
+declare -gi CLI_FLAG_NONE=1
+declare -gi CLI_FLAG_OPTVAL=2
+declare -gi CLI_FLAG_REQVAL=4
+test '[/post-pass:require-fn]'
+
+function cli::define_flag # (short,long,helptext) ->
+{
+  local shortname="$1" ; shift
+  local longname="$1" ; shift
+  local helptext="$1" ; shift
+  local -i flags=${1:-$CLI_FLAG_NONE} ; shift
+  IFS="+"
+  __map[$longname]="$flags+$shortname+$longname+${helptext//+/\\+}"
+  __revmap[$shortname]=$longname
+}
+
+function cli::define_optflag
+{
+  echo TODO
+}
+
+function cli::define_arg
+{
+  echo TODO
+}
+
+function cli::define_optarg
+{
+  echo TODO
+}
+
+function cli::flag
+{
+  [[ "${__flags[$1]}" == "1" ]]
+}
+
+function cli::value
+{
+  echo "${__values[$1]}"
+}
+
+function cli::get_positional
+{
+  if [[ $# -eq 0 ]]; then
+    echo "${__positional[@]}"
+  elif [[ ${#__positional[@]} -ge $1 ]]; then
+    echo "${__positional[$1]}"
+  fi
+}
+
+function cli::parse
+{
+  local -a map_entry
+  local -i flags
+  local value
+
+  while [[ $# -gt 0 ]]
+  do
+    unset value
+
+    if [[ ${1:0:1} != "-" ]]; then
+      __positional+=("$1")
+      shift
+      continue
+    elif [[ ${#__map[${1%%=*}]} -gt 0 ]]; then
+      map_entry=(${__map[${1%%=*}][@]})
+      value="${1#*=}"
+      if [[ ${#value} -eq ${#1} ]]; then
+        unset value
+      fi
+      shiftcount=1
+
+    elif [[ ${#__revmap[$1]} -gt 0 ]]; then
+      map_entry=(${__map[${__revmap[$1]}][@]})
+
+      if [[ $# -gt 1 ]] && [[ ${2:0:1} != "-" ]]; then
+        value="$2"
+        shiftcount=2
+      elif [[ $# -gt 1 ]] && [[ ${2:0:1} == "-" ]]; then
+        shiftcount=1
+        unset value
+      fi
+
+    else
+      log::err "Unrecognized argument '$1'" ; exit 125
+    fi
+
+    local -n shortname="map_entry[1]"
+    local -n longname="map_entry[2]"
+    local -n flags_ref="map_entry[0]"
+
+    let flags=$flags_ref
+
+    if (( (flags & CLI_FLAG_NONE) == CLI_FLAG_NONE )); then
+      if [[ "$value" ]] && [[ $shiftcount -gt 1 ]]; then
+        let shiftcount--;
+        unset value
+      fi
+      __flags[$longname]=1
+    else
+
+      if (( (flags & CLI_FLAG_REQVAL) == CLI_FLAG_REQVAL )) && ! [[ "$value" ]]; then
+        log::err "Option '$longname' requires an argument..." ; exit 125
+      fi
+
+      if [[ ${#__values[$longname]} -gt 0 ]]; then
+        log::err "Option '$longname' defined more than once..." ; exit 125
+      fi
+
+      __values[$longname]=$value
+    fi
+
+    shift $shiftcount
+  done
+
+  # for _ in "${!__values[@]}"; do
+  #   echo "$_ == ${__values[$_]}"
+  # done
+
+  # for _ in "${!__flags[@]}"; do
+  #   echo "$_ == ${__flags[$_]}"
+  # done
+
+  # for (( iter=0; iter<${#__positional[@]}; ++iter )); do
+  #   echo "${__positional[$iter]}"
+  # done
+}
+
+function cli::usage
+{
+  local -a map_entry
+  local i maxlen=0 len=0
+
+  for _ in "${!__map[@]}"; do
+    map_entry=(${__map[$_][@]})
+    let len=${#map_entry[1]}+${#map_entry[2]}
+    maxlen=$((len>maxlen?len:maxlen))
+  done
+  let maxlen+=2
+
+  printf "%s\n\n" "Usage: ${BASH_SOURCE[1]##*/} ${1:-[OPTION...]}"
+  for _ in "${!__map[@]}"; do
+    map_entry=(${__map[$_][@]})
+    printf "  %s, %s" "${map_entry[1]}" "${map_entry[2]}"
+    printf "%*s %s\n" $(( maxlen - ${#map_entry[1]} - ${#map_entry[2]} )) " " "${map_entry[3]}"
+  done
+}
+
+function cli::usage_from_commentblock
+{
+  [[ -n "$1" ]] && script="$1" || script="$0"
+
+  local script_name
+  script_name=$(basename "$script")
+
+  local synopsis='false'
+  local options='false'
+
+  while read -r line
+  do
+    # Break at first non-comment line
+    [[ "${line:0:1}" = '#' ]] || break
+
+    [[ "${line##* }" == "Synopsis:" ]] && {
+      synopsis='true'
+      continue
+    }
+    [[ "${line##* }" == "Options:" ]] && {
+      printf "\n"
+      options='true'
+      continue
+    }
+
+    if $synopsis; then
+      line=${line:4}
+      line=${line//\$\{SCRIPT_NAME\} /}
+      line=${line//\$0 /}
+      echo "Usage: $script_name $line"
+      synopsis='false'
+      continue
+    fi
+
+    if $options; then
+      [[ "${line:0:4}" != "#   " ]] && {
+        printf "\n"
+        options='false'
+        continue
+      }
+
+      echo "${line:1}"
+    fi
+  done < "$script"
+}
diff --git a/Bash-Doodles/mangle.sh b/Bash-Doodles/mangle.sh
new file mode 100644
index 0000000..b37bc7e
--- /dev/null
+++ b/Bash-Doodles/mangle.sh
@@ -0,0 +1,10 @@
+#!/bin/bash
+mangle() {
+  echo mangle
+}
+the() {
+  echo the
+  }
+world() {
+  echo world
+   }
diff --git a/Bash-Doodles/monitor-for-key-combo.sh b/Bash-Doodles/monitor-for-key-combo.sh
new file mode 100644
index 0000000..26bfe35
--- /dev/null
+++ b/Bash-Doodles/monitor-for-key-combo.sh
@@ -0,0 +1,10 @@
+#!/bin/bash
+
+# Press the Ctrl+N key combination
+xdotool keydown ctrl+n
+
+# Follow the system logs in real-time and filter for log entries that contain the string 'ctrl+n'
+journalctl -f | grep 'ctrl+n'
+
+# Release the Ctrl+N key
+xdotool keyup ctrl+n
diff --git a/Bash-Doodles/monitor_history.sh b/Bash-Doodles/monitor_history.sh
new file mode 100644
index 0000000..7036610
--- /dev/null
+++ b/Bash-Doodles/monitor_history.sh
@@ -0,0 +1,42 @@
+#!/bin/bash
+
+# Initialize ShellMonStatus to off
+ShellMonStatus="off"
+
+# Initialize the array to store command input/output
+declare -a output
+
+# Function to toggle ShellMonStatus
+function toggle_ShellMonStatus {
+  if [[ "$ShellMonStatus" == "off" ]]; then
+    ShellMonStatus="on"
+    echo "Shell Monitoring enabled."
+  else
+    ShellMonStatus="off"
+    echo "Shell Monitoring disabled."
+  fi
+}
+
+# Function to store command input/output
+function log_output {
+  if [[ "${#output[@]}" -eq 10 ]]; then
+    # Remove the oldest item if array is full
+    output=("${output[@]:1}")
+  fi
+  # Store the command output in the array
+  output+=("$1")
+}
+
+# Function to access stored output by index
+function get_output {
+  if [[ ! -z $1 ]]; then
+    local index=$(( ${#output[@]} -


**Response:**
Add Bash-Doodles scripts: activity-file-add.sh, bash_script.sh, cli2.sh, mangle.sh, monitor-for-key-combo.sh, and monitor_history.sh

<details><summary>Metadata</summary>

- Duration: 1268 ms
- Datetime: 2024-01-08T10:16:11.647356
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.6}
```

