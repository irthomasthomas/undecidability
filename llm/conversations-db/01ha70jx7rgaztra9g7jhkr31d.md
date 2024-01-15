**Prompt:**
Reply with bash script only. Use inline code comments for writing.
Think through through step-by-step.
Think quietly about tools, algorithms, Probabilistic data-structures, cli bash tools like awk and grep, inodes and dbuses qdbuses.

[3]
Description=Window settings for konsole
activity=a8180977-de51-4672-ac40-78e487731563
activityrule=2
clientmachine=localhost
noborder=true
position=0,0
size=2560,1386
title=undecidability
titlematch=2
types=1
windowrole=MainWindow#1
windowrolematch=1
wmclass=konsole
wmclassmatch=2 This is a kderulesrc entry, part of the kde plasma window manager. It moves a terminal to a kde activity if it contains the text: undecidability. Can you write a bash script that does the same thing, so it can be used on other linux desktops apart from kde plasma

Additional Goals:
  - Minimise code dependencies.
  - Use optimised code.
  - Minimise branching and process forking.
  - Use self-documenting code.


**Response:**
#!/bin/bash
#
# Script Name: move_terminal_to_activity.sh
# Description: Move terminal window to a specified desktop activity
#
# Usage: ./move_terminal_to_activity.sh "activity_name" "window_title_match"
#
# Examples:
# 1. ./move_terminal_to_activity.sh "a8180977-de51-4672-ac40-78e487731563" "undecidability"
# 2. ./move_terminal_to_activity.sh "activity_id" "window_title"
#
# Dependencies: wmctrl command line tool (install with 'sudo apt-get install wmctrl')

# Check if wmctrl is installed
if ! command -v wmctrl &> /dev/null; then
    echo "wmctrl is not installed. Please install it using 'sudo apt-get install wmctrl'."
    exit 1
fi

# Validate and parse command line arguments
if [ $# -ne 2 ]; then
    echo "Usage: ./move_terminal_to_activity.sh <activity_name> <window_title_match>"
    exit 1
fi

activity_name="$1"
window_title_match="$2"

# Get the window ID of the terminal window with the matching title
window_id=$(wmctrl -l | awk -v win_title="$window_title_match" '$0 ~ win_title {print $1}')

# Check if a window with the matching title was found
if [ -z "$window_id" ]; then
    echo "No window found with title matching '$window_title_match'."
    exit 1
fi

# Activate the activity
qdbus org.kde.ActivityManager /ActivityManager/Activities SetCurrentActivity $activity_name

# Move the window to the desired activity
wmctrl -i -r $window_id -t 0

echo "Window moved to activity '$activity_name'."

<details><summary>Metadata</summary>

- Duration: 18375 ms
- Datetime: 2023-09-13T10:14:40.688826
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

