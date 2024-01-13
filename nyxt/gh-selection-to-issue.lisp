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
