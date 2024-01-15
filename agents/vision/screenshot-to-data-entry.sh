#!/bin/bash
# screenshot-to-data-entry.sh

# target_file should be the file that is being edited
# target_file="$1:-/home/thomas/undecidability/.scratchpad/blocked_urls_list_2.txt"
source /home/thomas/Development/Projects/llm/.venv/bin/activate

if [ -z "$1" ]; then
    target_file="/home/thomas/undecidability/.scratchpad/blocked_urls_list_2.txt"
else
    target_file="$1"
fi
# remove target_file if it exists
if [ -f "$target_file" ]; then
    rm "$target_file"
fi

screenshot_path="/home/thomas/undecidability/.scratchpad/screenshot.png"
# kdialog --passivepopup "$i" 1 # 
# notify-send -t 3000 "Augmented Intelligence system is taking over in 5 seconds. 
# Activate the window with the data you want me to read."
kdialog --passivepopup "Augmented Intelligence system is taking over in 5 seconds.Activate the window with the data you want me to read." 5
sleep 5
for i in 5 4 3 2 1;
do
  kdialog --passivepopup "$i" 1
  sleep 1
done
spectacle -a -b -n -r -o "$screenshot_path"
# send screen shot for processing
work_request="read the image and tell me the domains listed. 
Just write one url per line and SAY NOTHING ELSE. 
Write no text at all before or after."
python "/home/thomas/undecidability/agents/vision/GPT4-vision-toolkit.py" describe "$screenshot_path" "$work_request" --output md --stream > "$target_file" &
# wait for the file to be created

while [ ! -f "$target_file" ]; do # 
    sleep 1
done
notify-send -t 3000 "Reading complete. Move the cursor to the window you want me to type into."
for i in {3..1}; do
    notify-send -t 1000 "Typing output in $i seconds"
    sleep 1
done
sleep 5
split_token=":"
while IFS= read -r line; do
    # if we are on the first line, check if it contains a colon
    if [ "$line" == "$(head -n 1 "$target_file")" ]; then
        if [[ "$line" == *"$split_token"* ]]; then
            # remove everything before the colon
            line="$(echo "$line" | cut -d "$split_token" -f2-)"
        fi
    fi
    xdotool type --delay 100 "$line"
    xdotool key Return
done < "$target_file"

# when complete, delete the file
# rm "$target_file"




