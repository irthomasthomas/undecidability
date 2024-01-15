**Prompt:**
In bash, I can write multiple requests to a named pipe like so: for i in {1..5}; do
  echo "Request $i" > my_pipe &
  sleep 1
done.

How can I do the same in this lisp function?:

(define-command-global gh-send-selection-to-issue ()
    "Sends url, title and selection to new gh issue"
  (let* ((title (title (current-buffer)))
         (myurl (url (current-buffer)))
         (selection (ps-eval (ps:chain window (get-selection) (to-string))))
         (pipe-title "/tmp/nyxt_title")
         (pipe-url "/tmp/nyxt_url")
         (pipe-selection "/tmp/nyxt_selection"))
    (with-open-file (stream pipe-title
                           :direction :output
                           :if-exists :supersede
                           :if-does-not-exist :create)
      (write-string title stream))
    (with-open-file (stream pipe-url
                           :direction :output
                           :if-exists :supersede
                           :if-does-not-exist :create)
      (write-string (render-url myurl) stream))
    (with-open-file (stream pipe-selection
                           :direction :output
                           :if-exists :supersede
                           :if-does-not-exist :create)
      (write-string selection stream))))

**Response:**
To replicate the behavior of the Bash script in the Lisp function, you would need to write to the named pipe multiple times with a delay between each write. However, Common Lisp does not have a built-in sleep function like Bash's `sleep`. You would need to use `sleep` from the `sb-thread` package if using SBCL, or an equivalent in other Lisp implementations.

Here's how you could modify the Lisp function to write to a named pipe multiple times with a delay:

```lisp
(define-command-global gh-send-selection-to-issue ()
  "Sends url, title and selection to new gh issue"
  (let* ((title (title (current-buffer)))
         (myurl (url (current-buffer)))
         (selection (ps-eval (ps:chain window (get-selection) (to-string))))
         (pipe "/tmp/nyxt_pipe")) ; Assuming a single named pipe for simplicity
    (dotimes (i 5) ; Loop 5 times
      (with-open-file (stream pipe
                             :direction :output
                             :if-exists :append
                             :if-does-not-exist :create)
        (write-string (format nil "Request ~A~%" i) stream)) ; Write request number
      (sb-thread:sleep 1)))) ; Sleep for 1 second between writes
```

This code assumes you are using SBCL and have a single named pipe. It writes to the pipe five times, appending a new request each time, with a one-second delay between each write. The `dotimes` macro is used to loop five times, and `sb-thread:sleep` is used to pause execution for one second between iterations. The `:if-exists :append` argument ensures that each new write is appended to the end of the pipe rather than overwriting it.

<details><summary>Metadata</summary>

- Duration: 24576 ms
- Datetime: 2024-01-09T13:48:15.545921
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

