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
User:Function caches a list of labels from https://api.github.com/repos/irthomasthomas/undecidability/labels - then prompt user to select labels and copy them to clipboard.
Response:


**Response:**
(defun cache-github-labels ()
  "Function caches a list of labels from https://api.github.com/repos/irthomasthomas/undecidability/labels - then prompt user to select labels and copy them to clipboard."
  (let* ((url "https://api.github.com/repos/irthomasthomas/undecidability/labels")
         (response (http-request:url url))
         (labels (json:decode-json-from-string (http-response:body response))))
    (setq *github-labels* labels)
    (let* ((selected-labels (prompt :prompt "Select labels" :sources (list (make-instance 'list-source :data labels))))
           (selected-label-names (mapcar #'label-name selected-labels)))
      (clipboard:copy (format nil "~{~a~^, ~}" selected-label-names))))))

<details><summary>Metadata</summary>

- Duration: 6519 ms
- Datetime: 2023-11-28T11:27:55.433197
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

