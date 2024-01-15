**Prompt:**
(define-command-global pipe-selection-title-url ()
    (let* ((title (title (current-buffer)))
          (url (url (current-buffer)))
          (selection (ps-eval (ps:chain window (get-selection) (to-string))))
          (pipe-title "/tmp/nyxt_title")
          (pipe-url "/tmp/nyxt_url")
          (pipe-selection "/tmp/nyxt_selection"))
        (uiop:launch-program
            (list "sh" "-c"
                  (concatenate 'string
                              "echo " "'" title "' > " pipe-title "
echo " "'" url "' > " pipe-url "
echo " "'" selection "' > " pipe-selection)))))

(define-command-global pipe-selection-title-url ()
    (let* ((title (title (current-buffer)))
          (url (url (current-buffer)))
          (selection (ps-eval (ps:chain window (get-selection) (to-string))))
          (pipe-title "/tmp/nyxt_title")
          (pipe-url "/tmp/nyxt_url")
          (pipe-selection "/tmp/nyxt_selection"))
        (uiop:launch-program
            (list "sh" "-c"
                  (concatenate 'string
                              "echo " "'" title "' > " pipe-title "
echo " "'" url "' > " pipe-url "
echo " "'" selection "' > " pipe-selection)))))

**Response:**
The provided code defines a global command named `pipe-selection-title-url` that pipes the title, URL, and selected text of the current buffer to separate temporary files.

The code can be simplified by removing the duplicate definition and combining the commands into one.

Here is the updated code:

```lisp
(define-command-global pipe-selection-title-url ()
  (let* ((title (title (current-buffer)))
         (url (url (current-buffer)))
         (selection (ps-eval (ps:chain window (get-selection) (to-string))))
         (pipe-title "/tmp/nyxt_title")
         (pipe-url "/tmp/nyxt_url")
         (pipe-selection "/tmp/nyxt_selection"))
    (uiop:launch-program
     (list "sh" "-c"
           (concatenate 'string
                        "echo " "'" title "' > " pipe-title "
echo " "'" url "' > " pipe-url "
echo " "'" selection "' > " pipe-selection))))))

```

The updated code removes the duplicate definition of `pipe-selection-title-url` and combines the commands into one.

Now, you can use the `pipe-selection-title-url` command to pipe the title, URL, and selected text of the current buffer to separate temporary files.

<details><summary>Metadata</summary>

- Duration: 21564 ms
- Datetime: 2023-10-24T14:22:54.095274
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

