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
send_note() {
#   Note_Category="$1" #Idea, #Todo, #QnA, #Shopping, #CodeSnippet, #Bookmark
  title="$1"
  body="$2"
  target_project="undecidability"
  cd $HOME/"$target_project"
  url="$(gh issue create --title "$title" --body "$body" --label "unclassified")"
  "$url"
  }


Add the following changes:
 1: Move formatting to the bash script.
 2: Nyxt lisp should only send values.
 3: Use one or more named pipes for communication between nyxt and bash.

**Response:**
Here are the changes in Nyxt Lisp:

```lisp
(define-command-global pipe-selection ()
    "Send selection to named pipe"
    (let ((selection (ps-eval (ps:chain window (get-selection) (to-string)))))
        (uiop:launch-program (list "sh" "-c" (format nil "echo %s >> /tmp/nyxt_Selection" selection)))))

(define-command-global pipe-selection-title-url ()
    (let* ((title (title (current-buffer)))
           (url (url (current-buffer)))
           (selection (ps-eval (ps:chain window (get-selection) (to-string)))))
        (uiop:launch-program
            (list "sh" "-c"
                  (concatenate 'string
                               "echo " "'" title "' > /tmp/nyxt_title" "\necho " "'" url "' > /tmp/nyxt_url" "\necho " "'" selection "' > /tmp/nyxt_selection")))))
```

Here are the changes in Bash Script:

```bash
send_note() {
    target_project="undecidability"
    cd $HOME/"$target_project"
    TITLE="$(cat /tmp/nyxt_title)"
    BODY="$(cat /tmp/nyxt_url)\n$(cat /tmp/nyxt_Selection)"
    LABEL="unclassified"
    gh issue create --title "$TITLE" --body "$BODY" --label "$LABEL"
}
```

<details><summary>Metadata</summary>

- Duration: 28186 ms
- Datetime: 2023-10-23T15:33:44.934108
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

