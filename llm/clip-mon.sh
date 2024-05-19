#!/usr/bin/env bash

monitoring=false
output_file=""

toggle_monitoring() {
    if $monitoring; then
        echo "Stopping clipboard monitoring"
        dbus-monitor --profile "interface='org.kde.klipper.klipper',member='clipboardHistoryUpdated'" > /dev/null &
        monitoring=false
        dbus_monitor_pid=$!
        kill $dbus_monitor_pid
        echo "File path copied to clipboard: $output_file"
        echo "$output_file" | xclip -selection clipboard
    else
        paper_title=$(kdialog --title "Paper Title" --inputbox "Enter the title of the paper you're reading:")
        if [ -n "$paper_title" ]; then
            output_file=$(mktemp --suffix=.txt)
            echo "Monitoring clipboard for paper: $paper_title"
            echo "Copied items will be saved to: $output_file"
            echo "Notes for $paper_title" > "$output_file"
            last_clipboard_content=""
            last_update_time=0
            dbus-monitor --profile "interface='org.kde.klipper.klipper',member='clipboardHistoryUpdated'" | while read -r line; do
                if [[ $line == *"clipboardHistoryUpdated"* ]]; then
                    current_time=$(date +%s)
                    new_clip=$(qdbus org.kde.klipper /klipper org.kde.klipper.klipper.getClipboardContents)
                    if [ "$new_clip" != "$last_clipboard_content" ]; then
                        time_diff=$((current_time - last_update_time))
                        if [ $time_diff -gt 5 ]; then
                            echo "
............
" >> "$output_file"
                            echo "$new_clip" >> "$output_file"
                            last_clipboard_content="$new_clip"
                            last_update_time=$current_time
                        elif [ $time_diff -gt 1 ]; then
                            last_clipboard_content="$new_clip"
                            last_update_time=$current_time
                        fi
                    fi
                fi
            done &
            monitoring=true
            dbus_monitor_pid=$!
        else
            echo "No paper title provided. Exiting."
        fi
    fi
}


toggle_monitoring

while $monitoring; do
    read -p "Press Enter to stop monitoring, or Ctrl+C to exit: " && toggle_monitoring
done
