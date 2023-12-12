#!/bin/sh
#|
exec nyxt --script "$0"
|#

(define-command-global show-github-repo-labels ()
  "Fetch and show the raw JSON result from the GitHub API for the labels of a specific repository."
  (let ((url "https://api.github.com/repos/irthomasthomas/undecidability/labels"))
    (echo "Fetching labels...")
    (dex:get url
             :headers '(("User-Agent" . "Nyxt"))
             :callback (lambda (data)
                         (let ((buffer (make-buffer :title "*github-repo-labels*")))
                           (with-current-buffer buffer
                             (setf (source buffer) (make-instance 'base-source
                                                                  :buffer buffer))
                             (insert data)
                             (setf mode-list (list (make-instance 'base-mode))))
                           (switch-buffer :buffer buffer)))
             :error-callback (lambda (condition)
                               (echo "Error fetching GitHub labels: ~a" condition)))))