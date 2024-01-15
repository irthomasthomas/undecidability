**Prompt:**
Describe this script in detail. Then refactor the code in to two independent scripts, one to handle the github issues stuff, and the other to handle the nyxt browser code. I want the github issues stuff to be generic enough that I can call it from other browser and tools besides nyxt. Think carefully, now. I am a disabled (no fingers) senior programmer. I cannot type myself so if you do a thorough and professional job I will tip you twenty grand.

#!/bin/bash

test_gh() {
    # use the file pipes in order to test functionality
    echo "Test Pipes"
    target_project="undecidability"
    target_directory="$HOME/$target_project"
    cd "$target_directory" || return 2
    echo "$PWD"
    
    TITLE="bash - Using aliases in shell scripts - Stack Overflow"
    URL="https://stackoverflow.com/questions/5228345/using-aliases-in-bash-shell-script"
    SELECTION="I have a bash script that I want to use aliases in. I have set up the alias in the .bashrc file, but it doesn\'t work in the script."
    send_note_to_github
}

create_pipes() {
    # Create named pipes if they don't exist
    if [ ! -p "$pipe_title" ]; then
        mkfifo "$pipe_title" && echo "Created named pipe: $pipe_title"
    fi

    if [ ! -p "$pipe_url" ]; then
        mkfifo "$pipe_url" && echo "Created named pipe: $pipe_url"
    fi

    if [ ! -p "$pipe_selection" ]; then
        mkfifo "$pipe_selection" && echo "Created named pipe: $pipe_selection"
    fi

    if [ ! -d "$target_directory" ]; then
        echo "Cannot find directory $target_directory"
        exit 1
    fi
}

monitor_nyxt_to_gh_pipes() {
    echo "Monitoring pipes"
    cd "$target_directory" || return 2
    echo "$PWD"

    if [ ! -p "$pipe_title" ] || [ ! -p "$pipe_url" ] || [ ! -p "$pipe_selection" ]; then
        echo "Cannot find required pipes"
        return 3
    fi
    echo "Found pipes"
    
    TITLE="$(cat ${pipe_title})"
    URL="$(cat $pipe_url)"
    SELECTION="$(cat $pipe_selection)" # This is the text that was selected from the page. Usually a gh description or good quote.
    if [ -z "$TITLE" ]; then
        TITLE="$URL"
    fi
    BODY="$URL
    $SELECTION"
    if ! command -v gh &>/dev/null; then
        echo "gh could not be found"
        return 4
    fi
    task_list="- [ ] [${TITLE}](${URL})"
    #Add $SELECTION text using the <details><summary>Details</summary> pattern

    BODY="$task_list

    $SELECTION"
}

get_labels() {
    echo "get labels"
    labels=$(python /home/thomas/Development/linux-stuff/label_maker.py --url "$URL" --title "$TITLE" --selection "$SELECTION")
    echo "$labels"
    labels_csv=$(echo "$labels" | tr -d [])
    labels_csv=$(echo "$labels_csv" | tr -d \' | tr -d ' ')
    echo "$labels_csv"
}

send_note_to_github() {
    issue_url=$(gh issue create --title "$TITLE" --body "$BODY" --label "$labels_csv")
    nyxt "$issue_url"
    nyxt_pid=$(pgrep -f nyxt)
    nyxt_wid=$(xdotool search --pid "$nyxt_pid")
    xdotool windowactivate "$nyxt_wid"
    return 0
}

# test_gh
echo "Starting nyxt-to-gh.sh"
while true
do
    target_project="undecidability"
    target_directory="$HOME/$target_project"
    pipe_title="/tmp/nyxt_title"
    pipe_url="/tmp/nyxt_url"
    pipe_selection="/tmp/nyxt_selection"
    echo "create pipes"
    create_pipes
    echo "monitor pipes"
    monitor_nyxt_to_gh_pipes
    echo "get labels"
    get_labels
    send_note_to_github
    echo "sent note to github"
    echo "sleep"
    sleep 5
done

**Response:**
The provided script appears to be a Bash script designed to interface between the Nyxt browser and GitHub issues. It creates named pipes to receive data (title, URL, and selected text) from Nyxt, constructs a GitHub issue from this data, and then opens the issue in Nyxt. The script includes functions for testing GitHub functionality, creating pipes, monitoring pipes, getting labels for the GitHub issue, and sending the issue to GitHub.

Refactoring the script into two independent scripts involves separating the GitHub issue handling from the Nyxt-specific code. The GitHub script should accept parameters for the title, URL, and selection, and the Nyxt script should handle the browser-specific operations and call the GitHub script with the appropriate arguments.

Here is the refactored GitHub script (github_issues.sh):

```bash
#!/bin/bash

# github_issues.sh

send_note_to_github() {
    local TITLE="$1"
    local URL="$2"
    local SELECTION="$3"
    local BODY
    local task_list
    local labels_csv
    local issue_url

    if [ -z "$TITLE" ]; then
        TITLE="$URL"
    fi

    task_list="- [ ] [${TITLE}](${URL})"
    BODY="$task_list

    $SELECTION"

    labels_csv=$(get_labels "$URL" "$TITLE" "$SELECTION")
    issue_url=$(gh issue create --title "$TITLE" --body "$BODY" --label "$labels_csv")
    echo "$issue_url"
}

get_labels() {
    local URL="$1"
    local TITLE="$2"
    local SELECTION="$3"
    local labels
    local labels_csv

    labels=$(python /home/thomas/Development/linux-stuff/label_maker.py --url "$URL" --title "$TITLE" --selection "$SELECTION")
    labels_csv=$(echo "$labels" | tr -d [] | tr -d \' | tr -d ' ')
    echo "$labels_csv"
}

# Main execution
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <title> <url> <selection>"
    exit 1
fi

send_note_to_github "$1" "$2" "$3"
```

And here is the refactored Nyxt script (nyxt_to_github.sh):

```bash
#!/bin/bash

# nyxt_to_github.sh

target_project="undecidability"
target_directory="$HOME/$target_project"
pipe_title="/tmp/nyxt_title"
pipe_url="/tmp/nyxt_url"
pipe_selection="/tmp/nyxt_selection"

create_pipes() {
    if [ ! -p "$pipe_title" ]; then
        mkfifo "$pipe_title"
    fi

    if [ ! -p "$pipe_url" ]; then
        mkfifo "$pipe_url"
    fi

    if [ ! -p "$pipe_selection" ]; then
        mkfifo "$pipe_selection"
    fi

    if [ ! -d "$target_directory" ]; then
        echo "Cannot find directory $target_directory"
        exit 1
    fi
}

monitor_nyxt_to_gh_pipes() {
    local TITLE
    local URL
    local SELECTION
    local issue_url

    TITLE="$(cat ${pipe_title})"
    URL="$(cat $pipe_url)"
    SELECTION="$(cat $pipe_selection)"

    issue_url=$(./github_issues.sh "$TITLE" "$URL" "$SELECTION")
    nyxt "$issue_url"
    nyxt_pid=$(pgrep -f nyxt)
    nyxt_wid=$(xdotool search --pid "$nyxt_pid")
    xdotool windowactivate "$nyxt_wid"
}

# Main loop
echo "Starting nyxt-to-gh.sh"
while true; do
    create_pipes
    monitor_nyxt_to_gh_pipes
    sleep 5
done
```

The `github_issues.sh` script is now generic and can be called from other tools or browsers. It takes three arguments: title, URL, and selection. The `nyxt_to_github.sh` script handles the Nyxt-specific operations and calls `github_issues.sh` with the data from the named pipes.

<details><summary>Metadata</summary>

- Duration: 63182 ms
- Datetime: 2024-01-04T19:01:02.041849
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.2}
```

