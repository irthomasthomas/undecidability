**Prompt:**
User:Open a file from the filesystem.

The user is prompted with the prompt buffer, files are browsable with
fuzzy suggestion.
Response:(define-command-global open-file
(&key
 (default-directory
  (if (quri.uri.file:uri-file-p (url (current-buffer)))
      (uiop/pathname:pathname-directory-pathname
       (quri.uri:uri-path (url (current-buffer))))
      *default-pathname-defaults*)))
"Open a file from the filesystem.

The user is prompted with the prompt buffer, files are browsable with
fuzzy suggestion.

DEFAULT-DIRECTORY specifies which directory to start from. Defaults to user home
directory.

By default, it uses the `xdg-open' command. The user can override the
`open-file-function' of `file-source' which takes the filename (or
directory name) as parameter.

`file-source' also has `supported-media-types'. You can append new types to
it. Every type in `supported-media-types' will be opened directly in Nyxt."
(prompt :prompt "Open file" :extra-modes 'file-manager-mode :input
        (uiop/filesystem:native-namestring default-directory) :sources
        'open-file-source))

User:Return the list of tags of the bookmark corresponding to URL.
Response:(defun url-bookmark-tags (url)
"Return the list of tags of the bookmark corresponding to URL."
(let ((bookmarks (files:content (bookmarks-file (current-buffer)))))
(alexandria:when-let ((existing
                       (find url bookmarks :key #'url :test #'url-equal)))
  (tags existing))))
User:Summarize the current buffer by creating a new summary buffer.
SUMMARY-LENGTH allows to list more/less summary items.
Response:(define-command-global summarize-buffer
(&key (summary-length 5) (buffer (current-buffer)))
"Summarize the current buffer by creating a new summary buffer.
SUMMARY-LENGTH allows to list more/less summary items."
(buffer-load-internal-page-focus 'summarize-buffer :summary-length
                                summary-length :id (id buffer)))
User:Inspect a mode and show it in a help buffer.
Response:(define-command-global describe-mode
(&key (mode (prompt1 :prompt "Describe mode" :sources 'mode-source)))
"Inspect a mode and show it in a help buffer."
(when mode (describe-class :class mode)))
User:Function displays list of labels from https://api.github.com/repos/irthomasthomas/undecidability/labels 
Response:


**Response:**
```lisp
(define-command-global fetch-github-labels ()
  "Fetch and display list of labels from a GitHub repository."
  (let ((url "https://api.github.com/repos/irthomasthomas/undecidability/labels"))
    (nyxt::with-data-unsafe (data (url)
                                  :as 'json)
      (if data
          (let ((labels (mapcar (lambda (label)
                                  (gethash "name" label))
                                data)))
            (with-result (buffer (make-buffer :title "GitHub Labels"))
              (with-current-buffer buffer
                (markup:markup
                 (:html
                  (:head
                   (:title "GitHub Labels"))
                  (:body
                   (:h1 "GitHub Labels")
                   (:ul
                    (loop for label in labels
                          collect (markup:markup (:li label)))))))))
            (switch-buffer :buffer buffer))
          (echo "Failed to fetch GitHub labels.")))))
```

Please note that this function assumes that the JSON response from the GitHub API is a list of objects where each object has a "name" key representing the label. Adjust the parsing logic if the API response structure is different.

<details><summary>Metadata</summary>

- Duration: 17992 ms
- Datetime: 2023-11-28T15:23:09.202181
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

