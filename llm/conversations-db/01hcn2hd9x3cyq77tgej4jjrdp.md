**Prompt:**
nyxt(define-command copy-title-and-url ()
   "Save current URL and page title to clipboard."
   (let* ((buffer (current-buffer))
      (url (and buffer (render-url (url buffer))))
      (title (and buffer (title buffer))))
     (when (and url title)
       (let ((formatted-string (format nil "[~a](~a)" title url))) 
         (copy-to-clipboard formatted-string)
         (echo "URL and Title copied to clipboard. URL: ~a, Title: ~a" url title))))) 

It seems like you're using Nyxt browser to generate the title and URL. Instead of copying them to the clipboard and then extracting them from there programmatically, you can directly retrieve the values within your script. Here's an updated version of your code:

**Response:**
nyxt(define-command copy-title-and-url ()
   "Save current URL and page title to clipboard."
   (with-buffer (buffer)
     (let ((url (render-url (url buffer)))
           (title (title buffer)))
       (when (and url title)
         (let ((formatted-string (format nil "[~a](~a)" title url))) 
           (copy-to-clipboard formatted-string)
           (echo "URL and Title copied to clipboard. URL: ~a, Title: ~a" url title))))))

<details><summary>Metadata</summary>

- Duration: 10778 ms
- Datetime: 2023-10-13T17:49:42.050048
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

