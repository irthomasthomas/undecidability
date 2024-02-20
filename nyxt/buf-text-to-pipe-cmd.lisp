;; FILEPATH: /home/thomas/undecidability/nyxt/buf-text-to-pipe-cmd.lisp

;; This function retrieves the text content of a buffer and returns it as a string.
;; If a buffer is not provided, it uses the current buffer.
(defun get-buffer-text (&optional buf)
    (nyxt/mode/document:select-all buf)
    (nyxt/mode/document:copy buf)
    (trivial-clipboard:text))

;; This internal page displays the result of a command execution.
;; It takes a keyword argument 'text' which represents the output text.
(define-internal-page cmd-result (&key text) (:title "*Result*")
    (spinneret:with-html-string
        (dolist (line (str:split #\newline text))
            (:p line))))

;; This command takes an optional buffer and command as arguments.
;; It retrieves the text content of the buffer, escapes it for shell execution,
;; and executes the given command in a shell.
;; The output of the command is then loaded into an internal page buffer.
(define-command-global buf-text-to-pipe-cmd (&optional buf cmd)
    (let* ((buf (or buf (nyxt:current-buffer)))
                 (safe-text (uiop:escape-sh-token (get-buffer-text buf)))
                 (cmd (or cmd (prompt1 :prompt "cmd: " :sources 'prompter:raw-source)))
                 (cmd-output (uiop:run-program
                                            `("bash" "-c" ,(str:concat "echo '" safe-text "' | " cmd))
                                            :output :string)))        (nyxt:buffer-load-internal-page-focus 'cmd-result :text cmd-output)))

