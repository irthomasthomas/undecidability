**Prompt:**
diff --git a/index.js b/index.js
new file mode 100644
index 0000000..22456d3
--- /dev/null
+++ b/index.js
@@ -0,0 +1,36 @@
+// Import required modules
+import { getCurrentActivity } from 'kde-activities';
+import { startProcess } from 'system-utils';
+import { assignWindow } from 'window-utils';
+
+// Get current activity name
+const currentActivity = getCurrentActivity();
+
+// Check if app is already open in activity  
+function isAppOpenInActivity(appName) {
+  // Use wmctrl to check if window open   
+  const result = runCommand(`wmctrl -xa ${appName}`);
+  return result.code === 0;
+}
+
+// Start app if not open
+function startAppIfNotOpen(appName) {
+  if (!isAppOpenInActivity(appName)) {
+    // Start app in new process
+    try {
+      startProcess(appName);
+    } catch (error) {
+      console.error(`Failed to start ${appName}`, error); 
+    }
+  }
+}
+
+// Main logic
+startAppIfNotOpen('Alacritty');
+
+// Assign Alacritty window to activity
+try {
+  assignWindow(`Alacritty - ${currentActivity}`);   
+} catch (error) {
+  console.error('Failed to assign window:', error);
+}
\ No newline at end of file
diff --git a/package.json b/package.json
new file mode 100644
index 0000000..d4caa6c
--- /dev/null
+++ b/package.json
@@ -0,0 +1,5 @@
+{
+  "dependencies": {
+    "dbus": "^1.2.0"
+  }
+}
\ No newline at end of file
diff --git a/scripts/lists/Add_IDEA.sh b/scripts/lists/Add_IDEA.sh
index 8cccc79..c810484 100644
--- a/scripts/lists/Add_IDEA.sh
+++ b/scripts/lists/Add_IDEA.sh
@@ -11,14 +11,14 @@ open_after_add() {
   fi
 }
 
-active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
+Note_Category="$1"
+target_project=$2:
 
-Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
-# This needs a separate script to setup the dir on first run.
+cd $HOME/undecidability
+idea_text=$(kdialog --inputbox "QuickiDea")
+# echo "$idea_text" >> "$FILE_PATH"
+idea_text="Quick idea: $idea_text"
+url="$(gh issue create --title "$idea_text" --body "" --label "idea")"
+kdialog --msgbox "$url"
 
-FILE_PATH=""$HOME"/Activities/"$Activity"/"$Activity"_IDEAS.md"
-
-idea_text=$(kdialog --textinputbox "iDea")
-echo "$idea_text" >> "$FILE_PATH"
-
-# TEMPLATE NOTE: Make "open after add" optional.
+# ToDo: Make "open after add" optional.
diff --git a/scripts/lists/Add_Note.sh b/scripts/lists/Add_Note.sh
new file mode 100644
index 0000000..736a6e7
--- /dev/null
+++ b/scripts/lists/Add_Note.sh
@@ -0,0 +1,53 @@
+#!/bin/bash
+
+source /home/tommy/Development/linux-stuff/shell_functions.sh
+
+view_new_issue() {
+    gh issue view "$1" | glow
+  # Todo: If in a terminal session, use gh cli to view the new issue, else open the url in default browser.
+}
+
+try_mkdir() {
+    if mkdir -p "$target_project_dir"
+    then
+        return 0
+    else
+        kdialog --msgbox "Failed to create the target project directory: $target_project_dir"
+        echo "Failed to create the target project directory: $target_project_dir"
+        return 1
+    fi
+}
+
+Note_Category="$1"
+# issue_body="$2"
+
+idea_text="$(kdialog --inputbox "QuickiDea")"
+idea_text="Quick idea: $idea_text"
+# Tofix: Handle the case where the labels do have spaces in them.
+labels=($(gh label list -R irthomasthomas/undecidability -L 100 | awk '{print $1}'))
+arg_list=()
+index=1
+for label in "${labels[@]}"; do
+    arg_list+=("$index" "$label" "off")
+    index=$((index + 1))
+done
+
+label_args=()
+selected_indexes=$(kdialog --checklist "Select tags:" "${arg_list[@]}")
+for index in $selected_indexes; do
+    label="${labels[$((index - 1))]}"
+    label_args+=("--label" "$label")
+done
+
+url="$(gh issue create -R irthomasthomas/undecidability --title "$idea_text" --body "" "${label_args[@]}")"
+
+clip "$url"
+
+kdialog --msgbox "$url\nHas been copied to clipboard"
+
+
+#Why do we not have more intelligent autocorrect on desktop?
+# local target_project=${2:-"$(activity_name_from_id "$(current_activity_id)")"}
+# local target_project_dir="$HOME/$target_project"
+# [ -d "$target_project_dir" ] || try_mkdir || exit 1
+# cd "$target_project_dir" || kdialog --msgbox "Failed to access $target_project_dir" || echo "Failed to access $target_project_dir" && exit 1
diff --git a/scripts/lists/Add_Note2.sh b/scripts/lists/Add_Note2.sh
new file mode 100644
index 0000000..87ea6e9
--- /dev/null
+++ b/scripts/lists/Add_Note2.sh
@@ -0,0 +1,120 @@
+#!/bin/bash
+
+# Script: quick_idea.sh
+# Description: Create a new issue using gh cli and copy the issue URL to the clipboard
+# Dependencies: gh cli, kdialog
+
+# Source external functions
+source /home/tommy/Development/linux-stuff/shell_functions.sh
+
+activity_list_names() {
+  for id in $(activity_list_ids);
+  echo "$(activity_name_from_id $id)"
+}
+
+activity_names_array() {
+  activities=$(activity_list_names)
+  echo "${activities[@]}"
+}
+
+activity_list_ids() {
+  qdbus org.kde.ActivityManager /ActivityManager/Activities ListActivities
+}
+
+activity_current_id() {
+  qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity
+  }
+
+activity_name_from_id() {
+  qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$1"
+  }
+
+activity_picker() {
+  activity_names_array | xargs kdialog --combobox "Select an activity:" --default "$(activity_name_from_id "$(activity_current_id)")"
+}
+
+gh_issues_for_activity() {
+  activity="${1:-$(activity_picker)}"
+  gh_repo="irthomasthomas/$activity"
+  gh issue list -R "$gh_repo"
+}
+
+gh_issues_labels() {
+  local gh_repo="${1:-$(activity_picker)}"
+  local labels=$(gh label list -R "irthomasthomas/$gh_repo")
+  echo "$labels"
+}
+
+# Function to view a new issue
+view_new_issue() {
+  # TODO: Implement the logic to view the new issue using gh cli or open in the default browser.
+  if [[ -t 1 ]]; then
+    # In a terminal session, use gh cli
+    gh issue view "$1"
+  else
+    # In other cases, open the URL in the default browser
+    xdg-open "$1"
+  fi
+}
+
+get_labels() {
+  # ToDo: get labels from gh cli for $target_project
+  if [ -z $1 ]; then
+    labels=("idea", "url", "code_snippet", "prompt_snippet", "prompt_template", "QnA", "function", "TIL", "ToDo")
+  else
+    labels="$(gh_issues_label_picker)"
+  echo "${labels[@]}"
+}
+
+gh_issues_label_picker() {
+  local labels="$(gh_issues_labels)"
+  if [[ -t 0 ]]; then
+    label_name=$(echo "$labels" | fzf | awk '{print $1}')
+    kdialog --msgbox "This a terminal"
+  else
+    label_name="$(echo $labels | awk '{print $1}' | xargs kdialog --combobox "Select an label:" --default "idea")"
+  fi
+  echo $label_name
+}
+
+test_idea="Use embeddings to visualise amazon reviews and look for topic changes"
+
+# $1 activity/project
+# $2 label
+# $3 title
+# $4 body
+
+# Repo
+target_project="${1:-$(activity_picker)}"
+# Label
+issue_label="${2:-$(get_labels)}"
+
+target_project_dir="$HOME/$target_project"
+# Change to the target project directory or exit with an error message
+cd "$target_project_dir" || { echo "Failed to access $target_project_dir. Make sure the path exists and has correct permissions" >&2; return 1; }
+
+# Get user input for the note text
+note_text=$(kdialog --inputbox "QuickiDea")
+if [[ $? -ne 0 ]]; then
+  echo "Failed to get user input." >&2
+  return 1
+fi
+note_text="$issue_label: $note_text"
+
+# Create the new issue and get the issue URL
+url=$(gh issue create --title "$note_text" --body "" --label "$issue_label")
+if [[ $? -ne 0 ]]; then
+  echo "Failed to create the new issue." >&2
+  return 1
+fi
+
+# Copy the issue URL to the clipboard
+echo "$url" | clip
+
+# Show a dialog box with the copied URL
+kdialog --msgbox "$url
+Has been copied to the clipboard"
+
+# TODO: Add an optional flag for opening the new issue after it's created
+
+exit 0
diff --git a/scripts/scripts-2023-07/.directory b/scripts/scripts-2023-07/.directory
new file mode 100644
index 0000000..3831ad0
--- /dev/null
+++ b/scripts/scripts-2023-07/.directory
@@ -0,0 +1,10 @@
+[Dolphin]
+GroupedSorting=true
+HeaderColumnWidths=652,88,152,168,88,302
+SortHiddenLast=true
+SortOrder=1
+SortRole=modificationtime
+Timestamp=2023,5,27,16,35,26.438
+Version=4
+ViewMode=1
+VisibleRoles=Details_text,Details_size,Details_modificationtime,Details_rating,Details_tags,Details_path,CustomizedDetails
diff --git a/scripts/scripts-2023-07/Open_Activity_Did.sh b/scripts/scripts-2023-07/Open_Activity_Did.sh
new file mode 100644
index 0000000..1ed3152
--- /dev/null
+++ b/scripts/scripts-2023-07/Open_Activity_Did.sh
@@ -0,0 +1,18 @@
+#!/bin/bash
+# Get current Activity
+active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
+Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
+
+# This needs a seperate script to setup the dir on first run.
+FILE_PATH=""$HOME"/Activities/"$Activity"/"$Activity"_Did.md"
+printf '%s\n' "$FILE_PATH"
+
+WINDOW_TITLE=""$Activity"_Did.md"
+
+WINDOW_ID=$(xdotool search --name "$WINDOW_TITLE" | head -1)
+
+if [ -n "$WINDOW_ID" ]; then
+  xdotool windowactivate --sync "$WINDOW_ID"
+else
+  kate -n "$FILE_PATH" &
+fi
diff --git a/scripts/scripts-2023-07/Open_Activity_Ideas-EDITING.sh b/scripts/scripts-2023-07/Open_Activity_Ideas-EDITING.sh
new file mode 100644
index 0000000..eb56a0d
--- /dev/null
+++ b/scripts/scripts-2023-07/Open_Activity_Ideas-EDITING.sh
@@ -0,0 +1,22 @@
+#!/bin/bash
+
+# Get current Activity
+active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
+
+Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
+# This needs a seperate script to setup the dir on first run.
+
+FILE_PATH=""$HOME"/Activities/"$Activity"/"$Activity"_IDEAS.md"
+
+idea_text=$(kdialog --textinputbox "iDea")
+echo "$idea_text" >> "$FILE_PATH"
+# check that text was added to file
+
+
+WINDOW_TITLE=""$Activity"_IDEAS.md"
+WINDOW_ID=$(xdotool search --name "$WINDOW_TITLE" |


**Response:**
Add new files and scripts for managing activity ideas and notes.

<details><summary>Metadata</summary>

- Duration: 2762 ms
- Datetime: 2023-10-16T17:52:13.822157
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

