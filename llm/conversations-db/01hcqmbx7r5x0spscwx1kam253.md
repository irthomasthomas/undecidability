**Prompt:**
IS THERE A WAY TO MAKE THIS LISP MORE READABLE? (define-command-global pipe-selection-title-url ()
  (let* ((title (title (current-buffer)))
         (url (url (current-buffer)))
         (selection (ps-eval (ps:chain window (get-selection) (to-string))))
         (formatted-output (format nil "~a~%~a~%~a" title url selection)))
    (uiop:launch-program (list "sh" "-c" (concatenate 'string "echo " "'" formatted-output "'" " > /tmp/nyxt_selection_pipe")))))

**Response:**
Yes, there are a few ways to make this Lisp code more readable:

1. Use meaningful variable names: Instead of using single letter variable names like `url`, `title`, and `selection`, you can choose more descriptive names. For example, `current-url`, `current-title`, and `current-selection`.

2. Split long lines: Break long lines into multiple lines to improve readability. For example, you can split the `formatted-output` line into two lines.

3. Indentation: Use consistent indentation to make the code structure more clear. Indentation also helps to visually separate blocks of code.

Here's an example of the code with these improvements:

```lisp
(define-command-global pipe-selection-title-url ()
  (let* ((current-title (title (current-buffer)))
         (current-url (url (current-buffer)))
         (current-selection (ps-eval (ps:chain window (get-selection) (to-string))))
         (formatted-output (format nil "~a~%~a~%~a" current-title current-url current-selection)))
    (uiop:launch-program
     (list "sh" "-c" (concatenate 'string "echo " "'" formatted-output "'" " > /tmp/nyxt_selection_pipe")))))
```

<details><summary>Metadata</summary>

- Duration: 37372 ms
- Datetime: 2023-10-14T17:39:18.395215
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

