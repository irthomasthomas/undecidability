**Prompt:**
User:Open a file from the filesystem.

The user is prompted with the prompt buffer, files are browsable with
fuzzy suggestion.
AI:(define-command-global open-file
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
AI:(defun url-bookmark-tags (url)
"Return the list of tags of the bookmark corresponding to URL."
(let ((bookmarks (files:content (bookmarks-file (current-buffer)))))
(alexandria:when-let ((existing
                       (find url bookmarks :key #'url :test #'url-equal)))
  (tags existing))))
User:Summarize the current buffer by creating a new summary buffer.
SUMMARY-LENGTH allows to list more/less summary items.
AI:(define-command-global summarize-buffer
(&key (summary-length 5) (buffer (current-buffer)))
"Summarize the current buffer by creating a new summary buffer.
SUMMARY-LENGTH allows to list more/less summary items."
(buffer-load-internal-page-focus 'summarize-buffer :summary-length
                                summary-length :id (id buffer)))
User:Inspect a mode and show it in a help buffer.
AI:(define-command-global describe-mode
(&key (mode (prompt1 :prompt "Describe mode" :sources 'mode-source)))
"Inspect a mode and show it in a help buffer."
(when mode (describe-class :class mode)))


**Response:**
User:Open a link in a new buffer.
AI:(define-command-global open-link-in-new-buffer
(&key (link (prompt1 :prompt "Open link in new buffer" :sources
                     'link-source)))
"Open a link in a new buffer."
(when link (buffer-load-internal-page-focus link :new-buffer t)))
User:Open a link in a new buffer in the background.
AI:(define-command-global open-link-in-new-buffer-background
(&key (link (prompt1 :prompt "Open link in new buffer in the background"
                     :sources 'link-source)))
"Open a link in a new buffer in the background."
(when link (buffer-load-internal-page link :new-buffer t)))
User:Open a link in a new buffer in the foreground.
AI:(define-command-global open-link-in-new-buffer-foreground
(&key (link (prompt1 :prompt "Open link in new buffer in the foreground"
                     :sources 'link-source)))
"Open a link in a new buffer in the foreground."
(when link (buffer-load-internal-page-focus link :new-buffer t)))

<details><summary>Metadata</summary>

- Duration: 2481 ms
- Datetime: 2023-11-27T20:55:49.211520
- Model: gpt-3.5-turbo-instruct

</details>

**Options:**
```json
{"temperature": 0.5}
```

