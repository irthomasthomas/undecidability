**Prompt:**
generate a json list of theme labels for this text. **Important** do not just extract keywords, instead read the whole text and try to summarise it in a sentence or two and THEN write the theme labels:
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
"Summarize the

**Response:**
Based on the given text, the theme labels could be:

1. Opening files from the filesystem
2. File browsing and fuzzy suggestion
3. Default directory for opening files
4. Overriding the default file opening function
5. Supported media types for file opening
6. URL bookmarking and tags
7. Summarizing buffers with a custom length

<details><summary>Metadata</summary>

- Duration: 1797 ms
- Datetime: 2023-12-30T20:19:27.504839
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

