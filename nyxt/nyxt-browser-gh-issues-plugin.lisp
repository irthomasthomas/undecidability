(define-command-global send-snippet-to-gh-issue
    nil
  "Sends URL, title, and selected text to a new GitHub issue using github_issues.py."
  (let* ((title (title (current-buffer)))
         (myurl (quri:render-uri (url (current-buffer))))
         (selection
          (ps-eval
            (parenscript:chain window (get-selection) (to-string))))
         (escaped-selection (uiop/launch-program:escape-sh-token selection))
         (repo "irthomasthomas/undecidability")
         (python-script
          "/home/thomas/Development/LLMs/label-maker/github_issues.py")
         (python-interpreter
          "/home/thomas/Development/Projects/llm/.venv/bin/python3")
         (command
          (list python-interpreter python-script  "--title" title "--url" myurl
                "--snippet" escaped-selection "--repo" repo "--embedding_db" "undecidability_gh_issues.db")))
    (uiop/run-program:run-program command :output t)))