**Prompt:**
screen_recorder-slim.sh\n\n#!/bin/bash

continue_or_delay() {
  while true; do
    kdialog --passivepopup "Break Time approaches. Make a note of where you are up to."
    # Kill the pids and return, or sleep for two minutes and continue loop.
    if [ $? -eq 0 ]; then
      return
    else
      for i in 2:00 1:59 1:58 1:57 1:56
      do
        kdialog --passivepopup "$i" 1
        sleep 1
      done
        sleep 115
    fi
    done
}

kill_pids() {
    pid_file=$HOME/screen_rec_pids.txt
    while IFS= read -r line; do
      kill "$line"
      printf '%s\n kill pid:' "$line"
    done < "$pid_file"
    rm "$pid_file"
}

break_time() {
  kdialog --passivepopup "Break time!"
  sleep 0.2
  xdotool key "Ctrl+Shift+F5"
  sleep 0.2
  
  # sleep 5 minutes
  sleep 300
  # switch to $Activity
  qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.Activate "$active_activity_id"
  sleep 0.2
  echo "break time over"
}

this_pid=$$
echo $this_pid > /tmp/Pomedoro.pid

i=1
while true; do

  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
  Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
  ACTIVITY_HOME="$HOME/Activities/$Activity"
  if [ ! -d "$ACTIVITY_HOME" ]; then
    mkdir -p "$ACTIVITY_HOME"    
  fi
  
  if [ ! -f "$ACTIVITY_HOME/$Activity"_Do.md ]; then
    touch "$ACTIVITY_HOME/$Activity"_Do.md
  fi
  DO_FILE="$ACTIVITY_HOME/$Activity"_Do.md

  # First dialog should be a dropdown list of Tasks, with one of the options being New Task.
  dotext=$(kdialog --inputbox "iDo for $Activity activity" "$(tail -n 1 "$DO_FILE")")
  
  echo "$dotext" >> "$DO_FILE"
  
  SKIP_TIME=/tmp/skip_time.txt
  # Get current Activityd
  echo "$Activity" > /tmp/ACTIVE_ACTIVITY.txt

  cd "$ACTIVITY_HOME" || kdialog  --error "Cannot cd to $ACTIVITY_HOME"

  continue_or_delay

  printf '\n i is: %s\n' "$i"

  # If this is the first run there wont be a previous_dotext
  if [ "$i" -eq 1 ]; then
    i=2
  else
    didtext=$(kdialog --inputbox "DidDo for $Activity activity" "$previous_dotext")
    datetime=$(date +%Y-%m-%d_%H-%M-%S)
    DID_FILE="$ACTIVITY_HOME/$datetime_$video_name_$Activity.yaml"
    if [ ! -f "$DID_FILE" ]; then
      touch "$DID_FILE"
    fi
    echo "datetime: $datetime" > "$DID_FILE"
    echo "didtext: $didtext" >> "$DID_FILE"
    break_time
  fi
  
  previous_dotext="$dotext"
  printf '\n previous_dotext: %s\n' "$dotext"
  kill_pids
  dotext_first_line=$(echo "$dotext" | head -n 1)
  video_name=$(llm "Turn this into a filename of about 4 words, hyphenated, no spaces: $dotext_first_line")
  video_name="$Activity"_"$video_name"
  kdialog --passivepopup "Activity: $Activity: \n$dotext\nVideo name: $video_name" 60 &

  sh  $HOME/Development/Projects/iDoDid/screen_recorder.sh "$video_name"
  for i in {1..1500}
  do
    sleep 1
    if [ -f "$SKIP_TIME" ]; then
      rm "$SKIP_TIME"
      break
    fi
 done
done

**Response:**
The script has been refactored into two files: `screen_recorder-slim.sh` and `screen_recorder.sh`. The `screen_recorder-slim.sh` script is the main script that calls the `screen_recorder.sh` script.

screen_recorder-slim.sh:

```bash
#!/bin/bash

source ./screen_recorder.sh

this_pid=$$
echo $this_pid > /tmp/Pomedoro.pid

i=1
while true; do
  active_activity_id=$(get_active_activity_id)
  Activity=$(get_activity_name "$active_activity_id")
  ACTIVITY_HOME="$HOME/Activities/$Activity"
  create_activity_home "$ACTIVITY_HOME"
  DO_FILE="$ACTIVITY_HOME/$Activity"_Do.md
  create_do_file "$DO_FILE"

  dotext=$(get_dotext "$Activity" "$DO_FILE")
  echo "$dotext" >> "$DO_FILE"
  
  SKIP_TIME=/tmp/skip_time.txt
  echo "$Activity" > /tmp/ACTIVE_ACTIVITY.txt

  cd "$ACTIVITY_HOME" || error_exit "Cannot cd to $ACTIVITY_HOME"

  continue_or_delay

  printf '\n i is: %s\n' "$i"

  if [ "$i" -eq 1 ]; then
    i=2
  else
    didtext=$(get_didtext "$Activity" "$previous_dotext")
    datetime=$(date +%Y-%m-%d_%H-%M-%S)
    DID_FILE="$ACTIVITY_HOME/$datetime_$video_name_$Activity.yaml"
    create_did_file "$DID_FILE" "$datetime" "$didtext"
    break_time
  fi
  
  previous_dotext="$dotext"
  printf '\n previous_dotext: %s\n' "$dotext"
  kill_pids
  dotext_first_line=$(get_dotext_first_line "$dotext")
  video_name=$(get_video_name "Turn this into a filename of about 4 words, hyphenated, no spaces: $dotext_first_line")
  video_name="$Activity"_"$video_name"
  show_activity_popup "$Activity" "$dotext" "$video_name"

  record_screen "$video_name"
  for i in {1..1500}
  do
    sleep 1
    if [ -f "$SKIP_TIME" ]; then
      rm "$SKIP_TIME"
      break
    fi
 done
done
```

screen_recorder.sh:

```bash
#!/bin/bash

get_active_activity_id() {
  qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity
}

get_activity_name() {
  local active_activity_id=$1
  qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id"
}

create_activity_home() {
  local ACTIVITY_HOME=$1
  if [ ! -d "$ACTIVITY_HOME" ]; then
    mkdir -p "$ACTIVITY_HOME"    
  fi
}

create_do_file() {
  local DO_FILE=$1
  if [ ! -f "$DO_FILE" ]; then
    touch "$DO_FILE"
  fi
}

get_dotext() {
  local Activity=$1
  local DO_FILE=$2
  kdialog --inputbox "iDo for $Activity activity" "$(tail -n 1 "$DO_FILE")"
}

get_didtext() {
  local Activity=$1
  local previous_dotext=$2
  kdialog --inputbox "DidDo for $Activity activity" "$previous_dotext"
}

create_did_file() {
  local DID_FILE=$1
  local datetime=$2
  local didtext=$3
  if [ ! -f "$DID_FILE" ]; then
    touch "$DID_FILE"
  fi
  echo "datetime: $datetime" > "$DID_FILE"
  echo "didtext: $didtext" >> "$DID_FILE"
}

get_dotext_first_line() {
  local dotext=$1
  echo "$dotext" | head -n 1
}

get_video_name() {
  local dotext_first_line=$1
  llm "Turn this into a filename of about 4 words, hyphenated, no spaces: $dotext_first_line"
}

show_activity_popup() {
  local Activity=$1
  local dotext=$2
  local video_name=$3
  kdialog --passivepopup "Activity: $Activity: \n$dotext\nVideo name: $video_name" 60 &
}

record_screen() {
  local video_name=$1
  sh  $HOME/Development/Projects/iDoDid/screen_recorder.sh "$video_name"
}
```

The functions in `screen_recorder.sh` are sourced into `screen_recorder-slim.sh` and used to simplify the main script. This makes the code more modular and easier to maintain.

<details><summary>Metadata</summary>

- Duration: 85064 ms
- Datetime: 2023-09-04T19:45:14.738526
- Model: gpt-4-0613

</details>

**Options:**
```json
{"temperature": 0.1}
```

