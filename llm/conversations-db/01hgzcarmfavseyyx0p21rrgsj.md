**Prompt:**
User:Command to send selection to named pipe

Response:(define-command-global pipe-selection ()
"Send selection to named pipe"
(let ((selection (ps-eval (ps:chain window (get-selection) (to-string)))))
    (uiop:launch-program (list "sh" "-c" (concatenate 'string "echo " "'" selection "'" " > /tmp/nyxt_selection_pipe")))))


User:Send url, title and selection to new linux pipe

Response:(define-command-global pipe-selection-title-url-new ()
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


User:Return the list of tags of the bookmark corresponding to URL.

Response:(defun url-bookmark-tags (url)
"Return the list of tags of the bookmark corresponding to URL."
(let ((bookmarks (files:content (bookmarks-file (current-buffer)))))
(alexandria:when-let ((existing
                       (find url bookmarks :key #'url :test #'url-equal)))
  (tags existing))))


User:Function to summarize the current buffer by creating a new summary buffer.
SUMMARY-LENGTH allows to list more/less summary items.

Response:(define-command-global summarize-buffer
(&key (summary-length 5) (buffer (current-buffer)))
"Summarize the current buffer by creating a new summary buffer.
SUMMARY-LENGTH allows to list more/less summary items."
(buffer-load-internal-page-focus 'summarize-buffer :summary-length
                                summary-length :id (id buffer)))


User:Command to inspect a mode and show it in a help buffer.

Response:(define-command-global describe-mode
(&key (mode (prompt1 :prompt "Describe mode" :sources 'mode-source)))
"Inspect a mode and show it in a help buffer."
(when mode (describe-class :class mode)))

User: Function to spell check a word.

Response:(define-command spell-check-word
    (&key (word nil word-supplied-p))
"Spell check a word."
(let ((word
        (or (and word-supplied-p word)
            (prompt1 :prompt "Spell check word" :sources
                    'prompter:raw-source))))
    (if (spell-dict-check-p word)
        (echo "~s is spelled correctly." word)
        (echo "~s is NOT correctly spelled." word))))


User:Prompt for element hints and bookmark them.

Response:(define-command bookmark-hint
nil
"Prompt for element hints and bookmark them."
(nyxt/mode/hint:query-hints "Bookmark hint"
                            (lambda (result)
                                (dolist (url (mapcar #'url result))
                                (let ((tags
                                        (prompt :prompt "Tag(s)" :sources
                                                (list
                                                (make-instance
                                                'prompter:word-source :name
                                                "New tags" :enable-marks-p
                                                t)
                                                (make-instance 'tag-source
                                                                :marks
                                                                (url-bookmark-tags
                                                                url))))))
                                    (bookmark-add url :tags tags :title
                                                (fetch-url-title url)))))
                            :selector "a"))


User:2023 - command to read labels from https://api.github.com/repos/irthomasthomas/undecidability/labels

Response:


**Response:**
```lisp
(define-command-global fetch-github-labels ()
  "Fetch GitHub labels from a repository and display them in a buffer."
  (let ((url "https://api.github.com/repos/irthomasthomas/undecidability/labels"))
    (nyxt::with-data-unsafe (data (buffer (current-buffer)))
        (:url url
              :headers '(("User-Agent" . "Nyxt"))
              :parser #'nyxt::json-parse)
      (if data
          (let ((labels (mapcar (lambda (label)
                                  (gethash "name" label))
                                data)))
            (with-result-buffer ((title "GitHub Labels"))
              (markup:markup
               (:h1 "GitHub Labels")
               (:ul (loop for label in labels
                          collect (markup:markup (:li label))))))
            (echo "Fetched GitHub labels successfully!"))
          (echo "Failed to fetch GitHub labels."))))))
```

<details><summary>Metadata</summary>

- Duration: 14554 ms
- Datetime: 2023-12-06T10:55:57.877141
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.2}
```

