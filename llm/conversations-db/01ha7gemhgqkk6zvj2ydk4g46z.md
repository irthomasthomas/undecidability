**Prompt:**
#!/bin/bash

# Script: quick_idea.sh
# Description: Create a new issue using gh cli and copy the issue URL to the clipboard
# Dependencies: gh cli, kdialog

# Source external functions
source /home/tommy/Development/linux-stuff/shell_functions.sh

activity_list_names() {
  for id in $(activity_list_ids);
  echo "$(activity_name_from_id $id)"
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

# Function to view a new issue
view_new_issue() {
  # TODO: Implement the logic to view the new issue using gh cli or open in the default browser.
  if [[ -t 1 ]]; then
    # In a terminal session, use gh cli
    gh issue view "$1"
  else
    # In other cases, open the URL in the default browser
    xdg-open "$1"
  fi
}

get_labels() {
  # ToDo: get labels from gh cli for $target_project
  if [ -z $1 ]; then
    labels=("idea", "url", "code_snippet", "prompt_snippet", "prompt_template", "QnA", "function", "TIL", "ToDo")
  else
    labels="$(gh_issues_label_picker)"
  echo "${labels[@]}"
}

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

local test_idea="Use embeddings to visualise amazon reviews and look for topic changes"

# $1 activity/project
# $2 label
# $3 title
# $4 body

# Repo
local target_project="${1:-$(activity_picker)}"
# Label
local issue_label="${2:-$(get_labels)}"

local target_project_dir="$HOME/$target_project"
# Change to the target project directory or exit with an error message
cd "$target_project_dir" || { echo "Failed to access $target_project_dir. Make sure the path exists and has correct permissions" >&2; return 1; }

# Get user input for the note text
note_text=$(kdialog --inputbox "QuickiDea")
if [[ $? -ne 0 ]]; then
  echo "Failed to get user input." >&2
  return 1
fi
note_text="$issue_label: $note_text"

# Create the new issue and get the issue URL
url=$(gh issue create --title "$note_text" --body "" --label "$issue_label")
if [[ $? -ne 0 ]]; then
  echo "Failed to create the new issue." >&2
  return 1
fi

# Copy the issue URL to the clipboard
echo "$url" | clip

# Show a dialog box with the copied URL
kdialog --msgbox "$url
Has been copied to the clipboard"

# TODO: Add an optional flag for opening the new issue after it's created

exit 0


**Response:**
The script seems fine, but there are a few areas that need to be corrected for it to function as expected. 

1. In `get_labels` function, the `if` block needs to include user input or an argument.
2. The `gh_issues_label_picker` function, there's a use of `fzf` without it being listed in dependencies.
3. `activity_picker` function is missing, it needs to be added to make the script complete.
4. Variables `target_project`, `issue_label` and `target_project_dir` aren't `local` since they aren't within function, so you have to remove `local` keyword.

Here's the corrected version:

```bash
#!/bin/bash

source /home/tommy/Development/linux-stuff/shell_functions.sh

activity_list_names() {
  for id in $(activity_list_ids);
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

view_new_issue() {
  if [[ -t 1 ]]; then
    gh issue view "$1"
  else
    xdg-open "$1"
  fi
}

get_labels() {
  if [ -z $1 ]; then
    labels=("idea", "url", "code_snippet", "prompt_snippet", "prompt_template", "QnA", "function", "TIL", "ToDo")
  else
    labels="$(gh_issues_label_picker)"
  fi
  echo "${labels[@]}"
}

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

test_idea="Use embeddings to visualise amazon reviews and look for topic changes"

target_project="${1:-$(activity_picker)}"
issue_label="${2:-$(get_labels)}"

target_project_dir="$HOME/$target_project"

cd "$target_project_dir" || { echo "Failed to access $target_project_dir. Make sure the path exists and has correct permissions" >&2; return 1; }

note_text=$(kdialog --inputbox "QuickiDea")
if [[ $? -ne 0 ]]; then
  echo "Failed to get user input." >&2
  return 1
fi
note_text="$issue_label: $note_text"

url=$(gh issue create --title "$note_text" --body "" --label "$issue_label")
if [[ $? -ne 0 ]]; then
  echo "Failed to create the new issue." >&2
  return 1
fi

echo "$url" | clip

kdialog --msgbox "$url
Has been copied to the clipboard"

exit 0
```

<details><summary>Metadata</summary>

- Duration: 112493 ms
- Datetime: 2023-09-13T14:50:23.810445
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

