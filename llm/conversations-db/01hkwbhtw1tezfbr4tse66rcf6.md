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
Here is the updated bash script:

```bash
#!/bin/bash
# nyxt_to_github.sh

create_pipe() {
    local pipe_path="$1"
    if [ ! -p "$pipe_path" ]; then
        mkfifo "$pipe_path" && echo "Created named pipe: $pipe_path" >&2
    fi
}

create_pipes() {
    echo "create pipes"
    create_pipe "$pipe_path"
    create_pipe "$pipe_url"
    create_pipe "$pipe_selection"

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

    while read -r TITLE; do
        read -r URL
        read -r SELECTION

        echo "TITLE: $TITLE
URL: $URL
SELECTION: $SELECTION
" >&2

        /home/thomas/Development/Projects/llm/label-maker/github_issues.sh "$TITLE" "$URL" "$SELECTION"
    done < "$pipe_path"
}

target_project="undecidability"
target_directory="$HOME/$target_project"
cd "$target_directory" || return 2
echo "$PWD"

pipe_path="/tmp/nyxt_gh_data"
pipe_url="/tmp/nyxt_url"
pipe_selection="/tmp/nyxt_selection"

# Main loop
echo "Starting nyxt-to-gh.sh"
while true; do
    create_pipes
    monitor_nyxt_to_gh_pipes
    sleep 5
done
```

And here is the updated Lisp code:

```lisp
(define-command-global gh-send-selection-to-issue ()
  "Sends url, title and selection to a new gh issue via a single FIFO"
  (let* ((title (title (current-buffer)))
         (myurl (url (current-buffer)))
         (selection (ps-eval (ps:chain window (get-selection) (to-string))))
         (fifo-path "/tmp/nyxt_gh_data"))
    (with-open-file (stream fifo-path
                            :direction :output
                            :if-exists :append
                            :if-does-not-exist :create)
      (format stream "Title: ~a~%URL: ~a~%Selection: ~a~%" title (render-url myurl) selection))))
```

The bash script now creates a single named pipe at `pipe_path` and reads from it in a loop. The Lisp code appends the data to the existing file at `fifo-path` instead of overwriting it.

<details><summary>Metadata</summary>

- Duration: 10882 ms
- Datetime: 2024-01-11T13:31:46.813993
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

