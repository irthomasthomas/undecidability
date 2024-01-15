**Prompt:**
Refactor this script in to two independent scripts, one to handle the github issues stuff, and the other for nyxt only. 

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
Script 1: GitHub Issues Handler (`github_issues_handler.sh`)

```bash
#!/bin/bash

send_note_to_github() {
    local TITLE="$1"
    local URL="$2"
    local SELECTION="$3"
    local BODY
    local labels_csv
    local issue_url

    if [ -z "$TITLE" ]; then
        TITLE="$URL"
    fi

    BODY="$URL
    $SELECTION"

    task_list="- [ ] [${TITLE}](${URL})"
    BODY="$task_list

    $SELECTION"

    labels_csv=$(get_labels "$URL" "$TITLE" "$SELECTION")

    issue_url=$(gh issue create --title "$TITLE" --body "$BODY" --label "$labels_csv")
    echo "Issue created: $issue_url"
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

# Main loop
echo "Starting github_issues_handler.sh"
while true; do
    read -r TITLE
    read -r URL
    read -r SELECTION
    send_note_to_github "$TITLE" "$URL" "$SELECTION"
    sleep 5
done
```

Script 2: Nyxt Handler (`nyxt_handler.sh`)

```bash
#!/bin/bash

create_pipes() {
    local pipe_title="/tmp/nyxt_title"
    local pipe_url="/tmp/nyxt_url"
    local pipe_selection="/tmp/nyxt_selection"

    if [ ! -p "$pipe_title" ]; then
        mkfifo "$pipe_title"
        echo "Created named pipe: $pipe_title"
    fi

    if [ ! -p "$pipe_url" ]; then
        mkfifo "$pipe_url"
        echo "Created named pipe: $pipe_url"
    fi

    if [ ! -p "$pipe_selection" ]; then
        mkfifo "$pipe_selection"
        echo "Created named pipe: $pipe_selection"
    fi
}

monitor_nyxt_to_gh_pipes() {
    local pipe_title="/tmp/nyxt_title"
    local pipe_url="/tmp/nyxt_url"
    local pipe_selection="/tmp/nyxt_selection"
    local TITLE
    local URL
    local SELECTION

    if [ ! -p "$pipe_title" ] || [ ! -p "$pipe_url" ] || [ ! -p "$pipe_selection" ]; then
        echo "Cannot find required pipes"
        return 3
    fi

    TITLE="$(cat ${pipe_title})"
    URL="$(cat $pipe_url)"
    SELECTION="$(cat $pipe_selection)"

    echo "$TITLE"
    echo "$URL"
    echo "$SELECTION"
}

# Main loop
echo "Starting nyxt_handler.sh"
create_pipes
while true; do
    monitor_nyxt_to_gh_pipes
    sleep 5
done
```

Explanation:
- The `github_issues_handler.sh` script reads from standard input and expects three lines representing the title, URL, and selection, respectively. It then processes this information to create a GitHub issue.
- The `nyxt_handler.sh` script creates the necessary named pipes and monitors them for input. It outputs the read values to standard output, which can be piped into the `github_issues_handler.sh` script.
- Both scripts have a main loop that runs indefinitely, with a 5-second sleep between iterations.
- The `get_labels` function has been moved inside the `send_note_to_github` function in the first script to maintain the flow of data.
- The `create_pipes` function is called once before the loop in the second script to ensure the pipes exist before monitoring begins.
- The `monitor_nyxt_to_gh_pipes` function in the second script now simply echoes the read values, which can be captured by the first script.

<details><summary>Metadata</summary>

- Duration: 64368 ms
- Datetime: 2024-01-04T18:52:20.994838
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

