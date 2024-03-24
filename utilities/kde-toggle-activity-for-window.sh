#!/bin/bash

# Get the current active window ID
current_window=$(xdotool getactivewindow)

# Get the list of all activity IDs
activity_ids=($(qdbus org.kde.ActivityManager /ActivityManager/Activities ListActivities))

# Get the number of activities (expecting 2 for this script)
num_activities=${#activity_ids[@]}

# Check if there are exactly two activities
if [ "$num_activities" -ne 2 ]; then
    echo "This script requires exactly two activities to be set up."
    exit 1
fi

# Get the current activity of the window
current_activity=$(qdbus org.kde.KWin /KWin org.kde.KWin.queryWindow "$current_window" "activities")

# Determine the target activity (the one that is not the current activity)
if [[ "$current_activity" == ${activity_ids[0]}* ]]; then
    target_activity=${activity_ids[1]}
else
    target_activity=${activity_ids[0]}
fi

# Move the window to the target activity
qdbus org.kde.KWin /KWin org.kde.KWin.setWindowActivity "$current_window" "$target_activity"
