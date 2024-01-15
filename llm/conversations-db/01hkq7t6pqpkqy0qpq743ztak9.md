**Prompt:**
In bash, I can write multiple requests to a named pipe like so: for i in {1..5}; do
  echo "Request $i" > my_pipe &
  sleep 1
done.

How can I do similar in this lisp function?: (I don't mean the sleep, but writing to a file and continueing with the & so that it can be called again even before the pipe is read from.

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
In Common Lisp, there is no direct equivalent to the shell's `&` for background processing. However, you can achieve concurrency using threads. Here's how you could adapt your function to write to the pipes potentially concurrently:

```lisp
(sb-thread:make-thread
 (lambda ()
   (with-open-file (stream pipe-title
                           :direction :output
                           :if-exists :supersede
                           :if-does-not-exist :create)
     (write-string title stream))))

(sb-thread:make-thread
 (lambda ()
   (with-open-file (stream pipe-url
                           :direction :output
                           :if-exists :supersede
                           :if-does-not-exist :create)
     (write-string (render-url myurl) stream))))

(sb-thread:make-thread
 (lambda ()
   (with-open-file (stream pipe-selection
                           :direction :output
                           :if-exists :supersede
                           :if-does-not-exist :create)
     (write-string selection stream))))
```

This code uses SBCL's threading capabilities (`sb-thread:make-thread`) to create a new thread for each write operation. Each thread will execute independently, allowing other operations to continue before the write completes, similar to using `&` in bash. Note that this assumes you are using SBCL as your Lisp implementation; if you are using a different implementation, you will need to use its threading API.

<details><summary>Metadata</summary>

- Duration: 39368 ms
- Datetime: 2024-01-09T13:49:46.127090
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

