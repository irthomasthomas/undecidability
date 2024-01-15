**Prompt:**
Here is a bash script 

#!/bin/bash
# nyxt_to_github.sh

create_pipes() {
    echo "create pipes"
    if [ ! -p "$pipe_title" ]; then
        mkfifo "$pipe_title" && echo "Created named pipe: $pipe_title" >&2
    fi

    if [ ! -p "$pipe_url" ]; then
        mkfifo "$pipe_url" && echo "Created named pipe: $pipe_url" >&2
    fi

    if [ ! -p "$pipe_selection" ]; then
        mkfifo "$pipe_selection"   && echo "Created named pipe: $pipe_selection" >&2
    fi

    if [ ! -d "$target_directory" ]; then
        echo "Cannot find directory $target_directory" >&2
        exit 1
    fi
}

monitor_nyxt_to_gh_pipes() {
    local TITLE
    local URL
    local SELECTION
    local issue_url
    echo "monitoring pipes" >&2

    TITLE="$(cat ${pipe_title})"
    URL="$(cat $pipe_url)"
    SELECTION="$(cat $pipe_selection)"

    echo "TITLE: $TITLE
URL: $URL
 SELECTION: $SELECTION
" >&2
    /home/thomas/Development/Projects/llm/label-maker/github_issues.sh "$TITLE" "$URL" "$SELECTION"
}

target_project="undecidability"
target_directory="$HOME/$target_project"
cd "$target_directory" || return 2
echo "$PWD"

pipe_title="/tmp/nyxt_title"
pipe_url="/tmp/nyxt_url"
pipe_selection="/tmp/nyxt_selection"


# Main loop
echo "Starting nyxt-to-gh.sh"
while true; do
    create_pipes
    monitor_nyxt_to_gh_pipes
    sleep 5
done

and an updated streamlined lisp client.

(define-command-global gh-send-selection-to-issue ()
  "Sends url, title and selection to a new gh issue via a single FIFO"
  (let* ((title (title (current-buffer)))
         (myurl (url (current-buffer)))
         (selection (ps-eval (ps:chain window (get-selection) (to-string))))
         (fifo-path "/tmp/nyxt_gh_data"))
    (with-open-file (stream fifo-path
                            :direction :output
                            :if-exists :supersede
                            :if-does-not-exist :create)
      (format stream "Title: ~a~%URL: ~a~%Selection: ~a~%" title (render-url myurl) selection))))

Update the bash code to work with the new single file format. Also update the lisp to be non-blocking and to append to rather than overwrite existing files.

**Response:**
Bash script update:

```bash
#!/bin/bash
# nyxt_to_github.sh

monitor_nyxt_to_gh_pipe() {
    local fifo_path="/tmp/nyxt_gh_data"
    local issue_data
    local TITLE
    local URL
    local SELECTION
    local issue_url

    echo "monitoring pipe" >&2

    while IFS= read -r line; do
        case "$line" in
            Title:*) TITLE="${line#Title: }" ;;
            URL:*) URL="${line#URL: }" ;;
            Selection:*) SELECTION="${line#Selection: }" ;;
        esac
    done < "$fifo_path"

    echo "TITLE: $TITLE
URL: $URL
SELECTION: $SELECTION
" >&2
    /home/thomas/Development/Projects/llm/label-maker/github_issues.sh "$TITLE" "$URL" "$SELECTION"
}

target_project="undecidability"
target_directory="$HOME/$target_project"
cd "$target_directory" || exit 2
echo "$PWD"

fifo_path="/tmp/nyxt_gh_data"
if [ ! -p "$fifo_path" ]; then
    mkfifo "$fifo_path" && echo "Created named pipe: $fifo_path" >&2
fi

# Main loop
echo "Starting nyxt-to-gh.sh"
while true; do
    monitor_nyxt_to_gh_pipe
    sleep 5
done
```

Lisp client update:

```lisp
(define-command-global gh-send-selection-to-issue ()
  "Sends url, title and selection to a new gh issue via a single FIFO"
  (let* ((title (title (current-buffer)))
         (myurl (url (current-buffer)))
         (selection (ps-eval (ps:chain window (get-selection) (to-string))))
         (fifo-path "/tmp/nyxt_gh_data"))
    (uiop:run-program (format nil "echo 'Title: ~a~%URL: ~a~%Selection: ~a~%' >> ~a" title (render-url myurl) selection fifo-path)
                      :output :interactive)))
```

The Bash script now reads from a single FIFO and parses the input based on the prefixed labels (Title:, URL:, Selection:). The Lisp client uses `uiop:run-program` to echo the formatted string into the FIFO in a non-blocking manner and appends to the file instead of overwriting it.

<details><summary>Metadata</summary>

- Duration: 30997 ms
- Datetime: 2024-01-11T13:32:23.738889
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

