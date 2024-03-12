(in-package #:nyxt-user)

;;; Loading files from the same directory.
(define-nyxt-user-system-and-load nyxt-user/basic-config
  :components ("nyxt-browser-gh-issues-plugin"))

(defvar *my-search-engines*
(list
  '("google" "https://google.com/search?q=~a" "https://google.com")
  '("doi" "https://dx.doi.org/~a" "https://dx.doi.org/")
  '("python3" "https://docs.python.org/3/search.html?q=~a"
    "https://docs.python.org/3")
  '("google" "https://kagi.com/search?q=~a" "https://kagi.com"))
"List of search engines.")

(define-configuration context-buffer
"Go through the search engines above and `make-search-engine' out of them."
((search-engines
  (append %slot-default%
          (mapcar
            (lambda (engine) (apply 'make-search-engine engine))
            *my-search-engines*)))))
