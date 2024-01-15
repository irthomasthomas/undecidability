**Prompt:**
diff --git a/.gitignore b/.gitignore
index 68bc17f..aaf6b26 100644
--- a/.gitignore
+++ b/.gitignore
@@ -1,3 +1,4 @@
+.fleet
 # Byte-compiled / optimized / DLL files
 __pycache__/
 *.py[cod]
@@ -158,3 +159,5 @@ cython_debug/
 #  and can be added to the global gitignore or merged into this file.  For a more nuclear
 #  option (not recommended) you can uncomment the following to ignore the entire idea folder.
 #.idea/
+.*
+*.bak
diff --git a/Pomedoro.sh b/Pomedoro.sh
new file mode 100755
index 0000000..b4fa652
--- /dev/null
+++ b/Pomedoro.sh
@@ -0,0 +1,110 @@
+#!/bin/bash
+
+continue_or_delay() {
+  while true; do
+    kdialog --passivepopup "Break Time approaches. Make a note of where you are up to."
+    # Kill the pids and return, or sleep for two minutes and continue loop.
+    if [ $? -eq 0 ]; then
+      return
+    else
+      for i in 2:00 1:59 1:58 1:57 1:56
+      do
+        kdialog --passivepopup "$i" 1
+        sleep 1
+      done
+        sleep 115
+    fi
+    done
+}
+
+kill_pids() {
+    pid_file=$HOME/screen_rec_pids.txt
+    while IFS= read -r line; do
+      kill "$line"
+      printf '%s\n kill pid:' "$line"
+    done < "$pid_file"
+    rm "$pid_file"
+}
+
+break_time() {
+  kdialog --passivepopup "Break time!"
+  sleep 0.2
+  xdotool key "Ctrl+Shift+F5"
+  sleep 0.2
+  
+  # sleep 5 minutes
+  sleep 300
+  # switch to $Activity
+  qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.Activate "$active_activity_id"
+  sleep 0.2
+  echo "break time over"
+}
+
+this_pid=$$
+echo $this_pid > /tmp/Pomedoro.pid
+
+i=1
+while true; do
+
+  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
+  Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
+  ACTIVITY_HOME="$HOME/Activities/$Activity"
+  if [ ! -d "$ACTIVITY_HOME" ]; then
+    mkdir -p "$ACTIVITY_HOME"    
+  fi
+  
+  if [ ! -f "$ACTIVITY_HOME/$Activity"_Do.md ]; then
+    touch "$ACTIVITY_HOME/$Activity"_Do.md
+  fi
+  DO_FILE="$ACTIVITY_HOME/$Activity"_Do.md
+
+  # First dialog should be a dropdown list of Tasks, with one of the options being New Task.
+  dotext=$(kdialog --inputbox "iDo for $Activity activity" "$(tail -n 1 "$DO_FILE")")
+  
+  echo "$dotext" >> "$DO_FILE"
+  
+  SKIP_TIME=/tmp/skip_time.txt
+  # Get current Activityd
+  echo "$Activity" > /tmp/ACTIVE_ACTIVITY.txt
+
+  # While testing, I want all videos to be saved to root activities folder. Later I will probably save them to a specific folder.
+
+  cd "$ACTIVITY_HOME" || kdialog  --error "Cannot cd to $ACTIVITY_HOME"
+
+  continue_or_delay
+
+  printf '\n i is: %s\n' "$i"
+
+  # If this is the first run there wont be a previous_dotext
+  if [ "$i" -eq 1 ]; then
+    i=2
+  else
+    didtext=$(kdialog --inputbox "DidDo for $Activity activity" "$previous_dotext")
+    datetime=$(date +%Y-%m-%d_%H-%M-%S)
+    DID_FILE="$ACTIVITY_HOME/$datetime_$video_name_$Activity.yaml"
+    if [ ! -f "$DID_FILE" ]; then
+      touch "$DID_FILE"
+    fi
+    echo "datetime: $datetime" > "$DID_FILE"
+    echo "didtext: $didtext" >> "$DID_FILE"
+    break_time
+  fi
+  
+  previous_dotext="$dotext"
+  printf '\n previous_dotext: %s\n' "$dotext"
+  kill_pids
+  dotext_first_line=$(echo "$dotext" | head -n 1)
+  video_name=$(llm "Turn this into a filename of about 4 words, hyphenated, no spaces: $dotext_first_line")
+  video_name="$Activity"_"$video_name"
+  kdialog --passivepopup "Activity: $Activity: \n$dotext\nVideo name: $video_name" 60 &
+
+  sh  $HOME/Development/Projects/iDoDid/screen_recorder.sh "$video_name"
+  for i in {1..1500}
+  do
+    sleep 1
+    if [ -f "$SKIP_TIME" ]; then
+      rm "$SKIP_TIME"
+      break
+    fi
+ done
+done
diff --git a/README.md b/README.md
index 2c2feb1..e4e3860 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,68 @@
-# iDoDid
\ No newline at end of file
+# iDoDid# iDoDid README
+
+## Description
+The iDoDid project is a Bash script that helps users keep track of their tasks and breaks during work sessions. It utilizes dialog boxes and screen recording to provide a seamless workflow for task management.
+
+## Features
+- Allows users to create and save tasks for different activities
+- Provides countdown timer for breaks
+- Records screen during work sessions
+- Saves recorded videos to specified activity folders
+- Supports skipping the current task and immediately starting the break
+
+## Usage
+1. Make sure that the necessary dependencies are installed:
+   - kdialog: for displaying dialog boxes
+   - xdotool: for simulating keyboard inputs
+   - qdbus: for interacting with KDE APIs
+   - llm: custom script for generating hyphenated filenames
+
+2. Clone the iDoDid repository to your desired location:
+   ```bash
+   git clone https://github.com/your-username/iDoDid.git
+   ```
+
+3. Navigate to the cloned repository:
+   ```bash
+   cd iDoDid
+   ```
+
+4. Open the `ido.sh` file with a text editor:
+   ```bash
+   nano ido.sh
+   ```
+
+5. Edit the script to customize the following variables to your preferences:
+   - `ACTIVITY_HOME`: default location for activity folders
+   - `SKIP_TIME`: file used to skip the current task and start the break immediately
+   - `VIDEO_LOCATION`: folder to save recorded videos (optional, can be set to the same location as `ACTIVITY_HOME`)
+   - `screen_recorder.sh`: path to the screen recorder script (if different from the default location)
+
+6. Save the changes and exit the text editor.
+
+7. Run the `ido.sh` script to start using the iDoDid tool:
+   ```bash
+   ./ido.sh
+   ```
+
+8. The script will display a dialog box prompting for the current activity. Select an existing activity or choose "New Activity" to create a new one.
+
+9. Enter the tasks for the selected activity in the dialog boxes. Each task will be saved to the corresponding activity folder.
+
+10. When the break time approaches, a passive popup notification will appear, reminding you to make a note of your progress.
+
+11. Choose to continue working or delay the break. If you choose to delay, the script will display a countdown timer before automatically continuing.
+
+12. Once the break time arrives, a break notification will appear. The script will then simulate pressing "Ctrl+Shift+F5" to start the screensaver and initiate the break.
+
+13. After the break ends, the screensaver will automatically close, and the script will switch back to the previous activity.
+
+14. Repeat the process to continue managing tasks and breaks.
+
+## Tips
+- It is recommended to create a desktop shortcut or add the script to your system's autostart to easily access the iDoDid tool.
+- Customize the script according to your preferences and workflow.
+- Feel free to modify and enhance the script to fit your specific needs.
+- Make sure to have enough disk space in the video location folder, as the recorded videos can consume a significant amount of storage.
+- Test the script thoroughly before using it in a production environment.
+- Visit the [iDoDid GitHub repository](https://github.com/your-username/iDoDid) for any updates, issues, or feature requests.
diff --git a/screen_recorder.sh b/screen_recorder.sh
new file mode 100644
index 0000000..78a8708
--- /dev/null
+++ b/screen_recorder.sh
@@ -0,0 +1,88 @@
+#!/bin/bash
+# 
+# Record screen and optionally microphone audio
+# Stefan Siegert 2020, adapted from code by Steven Gordon. Updated by GPT-4 2023
+#
+# Example usage:
+#    screencast intro-to-datacomms
+# OR
+#    screencast -a intro-to-datacomms
+# The screen will be recorded. Press 'z' to stop.
+# Two files may be created: intro-to-datacomms-audio.flac (if -a flag is used), intro-to-datacomms-screen.mp4
+# this_pid=$$
+# while read -r line; do
+#     kill -9 $line
+# done < Pomedoro.pid
+
+# save pids to file
+pid_file=$HOME/screen_rec_pids.txt
+# Initialize audio flag as false
+audioFlag=false
+
+# Check for -a flag for audio recording
+if [ "$1" == "-a" ]; then
+  audioFlag=true
+  shift
+fi
+
+# Add a 5 second delay before starting. 
+echo -n "Starting in "
+for i in 5 4 3 2 1
+do
+  echo -n " $i"
+  sleep 1
+done
+echo "Press z to finish..."
+
+# Basename of file. Separate extensions for audio and screen are added
+# E.g. internet-lecture
+outfile=$1
+# Name and default options for audio output
+audioFile=${outfile}-audio.flac
+audioRate=44100
+audioBits=16
+audioChannels=1
+
+# options for screen output
+# H.265 video codec and options for fast recording
+screenFile=${outfile}-screen.mkv
+screenSize=2560x1440
+screenOffset=' '
+screenRate=10;
+screenCodec=libx264
+screenOptions=" -preset fast -crf 40" # higher crf worse quality 
+printf "outfile: $outfile\n audioFile: $audioFile\n audioRate: $audioRate\n audioBits: $audioBits\n audioChannels: $audioChannels\n screenFile: $screenFile\n screenSize: $screenSize\n screenOffset: $screenOffset\n screenRate: $screenRate\n screenCodec: $screenCodec\n screenOptions: $screenOptions\n"
+
+# Record the microphone audio using SoX, putting process in background,
+# and get the process ID (so we can kill it later)
+if $audioFlag; then
+  rec -q -r ${audioRate} -b ${audioBits} -c ${audioChannels} ${audioFile} &
+  audioPID=$!
+  echo $audioPID >> $pid_file
+fi
+
+existing_ffmpegs=$(pgrep ffmpeg)
+
+i=1
+while [ -f $screenFile ]; do
+  screenFile=${outfile}-screen-$i.mkv
+  i=$((i+1))
+done
+
+ffmpeg -v 0 -f x11grab -r ${screenRate} -s ${screenSize} -i :0.0+0,0 -vcodec ${screenCodec} ${screenOptions} ${screenFile} &
+
+new_ffmpegs=$(pgrep ffmpeg)
+# compare new_ffmpegs and existing_ffmpegs to find the new ffmpeg process
+if [ ${#new_ffmpegs} -gt ${#existing_ffmpegs} ]; then
+  for i in $new_ffmpegs; do
+    if [[ ! $existing_ffmpegs =~ $i ]]; then
+      printf "new ffmpeg process: $i\n"
+      screenPID=$i
+      echo $screenPID >> $pid_file
+    fi
+  done
+fi
+echo "screenPIDs: $screenPID \n" > `tty`
+
+
+#exit


**Response:**
Add iDoDid project files and scripts

<details><summary>Metadata</summary>

- Duration: 849 ms
- Datetime: 2023-08-25T17:11:09.193061
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

