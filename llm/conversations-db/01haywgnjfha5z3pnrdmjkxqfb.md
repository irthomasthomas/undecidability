**Prompt:**
diff --git a/0Pomedoro.sh b/0Pomedoro.sh
new file mode 100644
index 0000000..a38788e
--- /dev/null
+++ b/0Pomedoro.sh
@@ -0,0 +1,72 @@
+#!/bin/bash
+
+# Function to pause the ffmpeg recording process
+pause_recording() {
+  # Get the PID of the ffmpeg process
+  pid=$(pgrep -x ffmpeg)
+  if [ -n "$pid" ]; then
+    # Pause the process by sending SIGSTOP signal
+    kill -STOP "$pid"
+    echo "Recording paused - PID: $pid"
+  fi
+}
+
+# Function to unpause the ffmpeg recording process
+unpause_recording() {
+  # Get the PID of the ffmpeg process
+  pid=$(pgrep -x ffmpeg)
+  if [ -n "$pid" ]; then
+    # Unpause the process by sending SIGCONT signal
+    kill -CONT "$pid"
+    echo "Recording resumed - PID: $pid"
+  fi
+}
+
+# Function to start the ffmpeg recording process in the given activity
+start_recording() {
+  activity=$1
+  # Check if the activity already has an ffmpeg screen recording active
+  if pgrep -f "ffmpeg -f x11grab -s $(xdpyinfo | awk '/dimensions/{print $2}')"; then
+    echo "Recording already active in $activity"
+  else
+    # Start the ffmpeg recording process and log the process to the activity
+    ffmpeg -f x11grab -s $(xdpyinfo | awk '/dimensions/{print $2}') -i :0.0+0,0 -r 30 -c:v libx264 -preset ultrafast -crf 22 -pix_fmt yuv420p "$HOME/Activities/$activity/recording.mp4" &
+    echo "Recording started in $activity"
+  fi
+}
+
+# Function to switch activities
+switch_activity() {
+  previous_activity=$(cat /tmp/ACTIVE_ACTIVITY.txt)
+  new_activity=$1
+
+  # Pause the recording in the outgoing activity
+  pause_recording
+
+  # Switch to the new activity
+  qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.Activate "$new_activity"
+
+  # Unpause the recording in the new activity or start recording if not already active
+  unpause_recording
+  start_recording "$new_activity"
+
+  echo "Switched from $previous_activity to $new_activity"
+}
+
+# Main script
+this_pid=$$
+echo $this_pid > /tmp/Pomedoro.pid
+
+previous_activity=$(cat /tmp/ACTIVE_ACTIVITY.txt)
+
+while true; do
+  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
+  new_activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
+
+  if [ "$new_activity" != "$previous_activity" ]; then
+    switch_activity "$new_activity"
+  fi
+
+  # Other script logic here...
+
+done
diff --git a/1Pomedoro-m4.sh b/1Pomedoro-m4.sh
new file mode 100644
index 0000000..b7385db
--- /dev/null
+++ b/1Pomedoro-m4.sh
@@ -0,0 +1,42 @@
+Here is a refactoring of your script with a single ffmpeg process being paused and unpaused. There are several ways to approach the task of pausing and resuming a process on a KDE activity switch and the method outlined may not meet your specific use case. Also, Error handling and expected edge-cases handling might require further modifications and improvements.
+
+```bash
+#!/bin/bash
+
+# Declarating the variable to check the current activity
+currentActivity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
+
+# Store original ffmpeg pid in a file for reference
+ffmpeg -video_size 1024x768 -framerate 25 -f x11grab -i :0.0+100,200 -f alsa -i hw:0 output.mkv & echo $! > /tmp/ffmpeg_$currentActivity.pid
+
+while true; do
+  # Get the currently active KDE activity
+  newActivity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
+      
+  # Compare it with the old activity
+  if [[ "$newActivity" != "$currentActivity" ]]; then
+    # If the activities are different, pause the old recording and resume/start the new recording
+    
+    # Send stop signal to the ffmpeg process of the old activity
+    kill -STOP $(cat /tmp/ffmpeg_$currentActivity.pid)
+
+    # Check if the new activity already has a recording
+    if [[ -e "/tmp/ffmpeg_$newActivity.pid" ]]; then
+      # If it does, resume it
+      kill -CONT $(cat /tmp/ffmpeg_$newActivity.pid)
+    else
+      # Else, start a new recording for it
+      ffmpeg -video_size 1024x768 -framerate 25 -f x11grab -i :0.0+100,200 -f alsa -i hw:0 output_$newActivity.mkv & echo $! > /tmp/ffmpeg_$newActivity.pid
+    fi
+
+    # Update the recorded last activity
+    currentActivity=$newActivity
+
+  fi
+
+  # Sleep for 2 seconds before checking again - this prevents excessively frequent checks, but can be adjusted to user's needs
+  sleep 2
+done
+```
+
+Note: The script assumes that the ffmpeg command provided is suitable for your requirements, you may need to modify it according to your needs.
diff --git a/Claude/screen-record.sh b/Claude/screen-record.sh
new file mode 100644
index 0000000..b1a16b8
--- /dev/null
+++ b/Claude/screen-record.sh
@@ -0,0 +1,89 @@
+#!/bin/bash
+
+# Script to record screen and optionally audio
+
+# Global variables
+pid_file="$HOME/screen_rec_pids.txt" 
+audio_flag=false
+screen_size="2560x1440"
+screen_rate=10
+screen_codec="libx264"
+screen_options="-preset fast -crf 40"
+
+# Functions
+
+function check_audio_flag {
+  if [ "$1" == "-a" ]; then
+    audio_flag=true
+    shift 
+  fi
+}
+
+function countdown {
+  echo -n "Starting in " 
+  for i in {5..1}; do
+    echo -n " $i"
+    sleep 1
+  done
+  echo "Press z to finish..."
+}
+
+function set_output_file {
+  outfile=$1
+  screen_file="${outfile}-screen.mkv"
+
+  i=1
+  while [ -f "$screen_file" ]; do
+    screen_file="${outfile}-screen-$i.mkv"
+    i=$((i+1))
+  done
+}
+
+function print_options {
+  echo "outfile: $outfile"
+  echo "screen_file: $screen_file"
+  echo "screen_size: $screen_size" 
+  echo "screen_rate: $screen_rate"
+  echo "screen_codec: $screen_codec"
+  echo "screen_options: $screen_options"
+}
+
+function start_recording {
+  existing_ffmpegs=$(pgrep ffmpeg)
+
+  ffmpeg -f x11grab -s "$screen_size" -r "$screen_rate" -i :0.0 -c:v "$screen_codec" "$screen_options" -pix_fmt yuv420p -b:v 5000k "$screen_file"
+
+  new_ffmpegs=$(pgrep ffmpeg)
+
+  if [ ${#new_ffmpegs} -gt ${#existing_ffmpegs} ]; then
+    for pid in $new_ffmpegs; do
+      if [[ ! "$existing_ffmpegs" =~ $pid ]]; then
+        echo "New ffmpeg PID: $pid"
+        echo "$pid" >> "$pid_file" 
+      fi
+    done
+  fi
+
+  echo "Recording started, press z to stop"
+}
+
+# Main script
+
+check_audio_flag "$1"
+countdown
+set_output_file "$1"
+print_options
+start_recording
+
+while true; do
+  read -n1 key
+  if [ "$key" == "z" ]; then
+    break
+  fi
+done
+
+# Stop recording
+kill $(cat "$pid_file")
+rm "$pid_file"
+
+echo "Recording stopped"
\ No newline at end of file
diff --git a/Pomedoro.sh b/Pomedoro.sh
index b4fa652..f15e07e 100755
--- a/Pomedoro.sh
+++ b/Pomedoro.sh
@@ -2,7 +2,7 @@
 
 continue_or_delay() {
   while true; do
-    kdialog --passivepopup "Break Time approaches. Make a note of where you are up to."
+    kdialog --passivepopup "Break Time approaches. \n I noted you are working on ${current_task}."
     # Kill the pids and return, or sleep for two minutes and continue loop.
     if [ $? -eq 0 ]; then
       return
@@ -26,8 +26,9 @@ kill_pids() {
     rm "$pid_file"
 }
 
-break_time() {
-  kdialog --passivepopup "Break time!"
+break_time()
+{
+  kdialog --passivepopup "Break time! Relax, before returning to ${current_task}"ed by GPT-4 2023
   sleep 0.2
   xdotool key "Ctrl+Shift+F5"
   sleep 0.2
@@ -46,8 +47,8 @@ echo $this_pid > /tmp/Pomedoro.pid
 i=1
 while true; do
 
-  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
-  Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
+  active_activity_id=$(activity_current_id)
+  Activity=$(activity_name_from_id $active_activity_id)
   ACTIVITY_HOME="$HOME/Activities/$Activity"
   if [ ! -d "$ACTIVITY_HOME" ]; then
     mkdir -p "$ACTIVITY_HOME"    
@@ -59,27 +60,25 @@ while true; do
   DO_FILE="$ACTIVITY_HOME/$Activity"_Do.md
 
   # First dialog should be a dropdown list of Tasks, with one of the options being New Task.
-  dotext=$(kdialog --inputbox "iDo for $Activity activity" "$(tail -n 1 "$DO_FILE")")
+  current_task=$(kdialog --inputbox "iDo for $Activity activity" "$(tail -n 1 "$DO_FILE")")
   
-  echo "$dotext" >> "$DO_FILE"
+  echo "$current_task" >> "$DO_FILE"
   
   SKIP_TIME=/tmp/skip_time.txt
   # Get current Activityd
   echo "$Activity" > /tmp/ACTIVE_ACTIVITY.txt
 
-  # While testing, I want all videos to be saved to root activities folder. Later I will probably save them to a specific folder.
-
   cd "$ACTIVITY_HOME" || kdialog  --error "Cannot cd to $ACTIVITY_HOME"
 
   continue_or_delay
 
   printf '\n i is: %s\n' "$i"
 
-  # If this is the first run there wont be a previous_dotext
+  # If this is the first run there wont be a previous_current_task
   if [ "$i" -eq 1 ]; then
     i=2
   else
-    didtext=$(kdialog --inputbox "DidDo for $Activity activity" "$previous_dotext")
+    didtext=$(kdialog --inputbox "DidDo for $Activity activity" "$previous_current_task")
     datetime=$(date +%Y-%m-%d_%H-%M-%S)
     DID_FILE="$ACTIVITY_HOME/$datetime_$video_name_$Activity.yaml"
     if [ ! -f "$DID_FILE" ]; then
@@ -90,13 +89,13 @@ while true; do
     break_time
   fi
   
-  previous_dotext="$dotext"
-  printf '\n previous_dotext: %s\n' "$dotext"
+  previous_current_task="$current_task"
+  printf '\n previous_current_task: %s\n' "$current_task"
   kill_pids
-  dotext_first_line=$(echo "$dotext" | head -n 1)
-  video_name=$(llm "Turn this into a filename of about 4 words, hyphenated, no spaces: $dotext_first_line")
+  current_task_first_line=$(echo "$current_task" | head -n 1)
+  video_name=$(llm "Turn this into a filename of about 4 words, hyphenated, no spaces: $current_task_first_line")
   video_name="$Activity"_"$video_name"
-  kdialog --passivepopup "Activity: $Activity: \n$dotext\nVideo name: $video_name" 60 &
+  kdialog --passivepopup "Activity: $Activity: \n$current_task\nVideo name


**Response:**
Refactored script with a single ffmpeg process being paused and unpaused.

<details><summary>Metadata</summary>

- Duration: 1438 ms
- Datetime: 2023-09-22T16:45:36.304685
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

