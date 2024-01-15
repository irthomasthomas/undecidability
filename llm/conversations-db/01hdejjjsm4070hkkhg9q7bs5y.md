**Prompt:**
Here is the original nyxt lisp script: 
(define-command-global pipe-selection ()
    "Send selection to named pipe"
  (let ((selection (ps-eval (ps:chain window (get-selection) (to-string)))))
    (uiop:launch-program (list "sh" "-c" (concatenate 'string "echo " "'" selection "'" " > /tmp/nyxt_selection_pipe")))))

(define-command-global pipe-selection-title-url ()
  (let* ((title (title (current-buffer)))
         (url (url (current-buffer)))
         (selection (ps-eval (ps:chain window (get-selection) (to-string))))
         (formatted-output
            (format nil "~a~%~a~%~a" title url selection)))
    (uiop:launch-program
        (list "sh" "-c"
            (concatenate 'string
                         "echo "
                         "'" formatted-output "'"
                         " > /tmp/nyxt_selection_pipe")))))

And here is the bash function: 



Add the following changes:
 1: Move formatting to the bash script.
 2: Nyxt lisp should only send values.
 3: Use one or more named pipes for communication between nyxt and bash.

**Response:**
Editing the lisp script and bash functions accordingly:

Nyxt Lisp script changes:

Rather than formatting and concatenating the title, url and selection in the Nyxt script, we will simply return these three things as list:

```lisp
(define-command-global pipe-selection ()
    "Send selection to named pipe"
    (let ((selection (ps-eval (ps:chain window (get-selection) (to-string)))))
        (uiop:launch-program (list "sh" "-c" (format nil "echo ~a > /tmp/nyxt_selection_pipe" selection)))))

(define-command-global pipe-selection-title-url ()
    (let* ((title (title (current-buffer)))
           (url (url (current-buffer)))
           (selection (ps-eval (ps:chain window (get-selection) (to-string)))))
        (uiop:launch-program
            (list "sh" "-c"
                  (format nil "echo ~a > /tmp/nyxt_selection_pipe" (list title url selection))))))
```

Bash function changes:

You would want to read from the named pipes, do your formatting and process it:

```bash
nyxt_bash() {
    while true; do
        if read -r line </tmp/nyxt_selection_pipe; then
            # IFS: Internal Field Separator
            IFS=', ' read -r title url selection <<< "$line"

            # Do your formatting here
            formatted_output="$title\n$url\n$selection"

            # Process $formatted_output
            # ...
        fi
    done
}
```

Before running the bash function, make sure to create the named pipe if it doesn't exist:

```bash
[ -p /tmp/nyxt_selection_pipe ] || mkfifo /tmp/nyxt_selection_pipe
nyxt_bash &
```

This code will ensure your named pipe exists at /tmp/nyxt_selection_pipe. If it doesn't it will create it, and then start the nyxt_bash function as a background process.

<details><summary>Metadata</summary>

- Duration: 46367 ms
- Datetime: 2023-10-23T15:30:22.869026
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

