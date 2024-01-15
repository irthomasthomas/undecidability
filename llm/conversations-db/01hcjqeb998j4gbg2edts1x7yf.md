**Prompt:**
nyxt(define-command copy-title-and-url ()                                         1 ✘ 
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
 

1. In this case I took the released 2.1.0 version. You may prefer to use HEAD if you are using the development version. 

2. function 'copy-to-clipboard' missing (fixed with f1e1fc70e4ec5b345152a3fb5d0fe127537921a1), or (2.1.1 data.lock203 ). 

3. (nyxt:url ...) does not seem to exist, function name is: 

nyxt:browsing-aiming-url 

---

 
) 

4. (nyxt:page-title (nyxt::current-page)) fails currently due to (3002) Caught Tag of type 'NilParseTree'. 

5. Call functional (suggestions welcome): 

 (defun copy-title-and-url ()
    "Save current URL and page title to clipboard."
    (let ((url (nyxt:browsing-aiming-url (nyxt::current-page)))
          (title (nyxt::render-title (nyxt::current-page))))
      (when (and url title)
        (let ((formatted-string (format nil "[~a](~a)" title url))) 
          (nyxt:copy-to-clipboard formatted-string)
          (nyxt:echo "URL and Title copied to clipboard. URL: ~a, Title: ~a" url title)))))

(copy-title-and-url) 

I get a title+URL copy to the clipboard from there. 

-- 

Klaus

Yours seems to work "better" than mine: it only copies the URL and Title just from the Nyxt copy-to-clipboard function. I laugh, and it's my first night ;) Thanks for the tips, a lot to pull out of that document.

integrated-credential-store

Posted: Mon Jan 27 06:02:01 2020

Ah thinking about it though, it's not going to neccesarily be that consistent. If a page has a title but no URL it doesn't function. Perhaps there could be an implementation which just accepts that if you just copied the title, then it copies the URL and if you just copied the URL first, then the title? 

Don't know the implementation and how much it will do this already. 

/hopefully not annoying.

<details><summary>Metadata</summary>

- Duration: 5467 ms
- Datetime: 2023-10-12T19:57:23.789187
- Model: gpt-3.5-turbo-instruct

</details>

**Options:**
```json
{"max_tokens": 1000}
```

