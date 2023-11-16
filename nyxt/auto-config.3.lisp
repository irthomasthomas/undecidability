(defmethod customize-instance ((document-buffer document-buffer) &key)
  (setf (slot-value document-buffer 'zoom-ratio-default) 1.1))

(defmethod customize-instance ((buffer buffer) &key)
  (setf (slot-value buffer 'default-modes)
          '(nyxt/mode/certificate-exception:certificate-exception-mode
            nyxt/mode/annotate:annotate-mode nyxt/mode/bookmark:bookmark-mode
            nyxt/mode/history:history-mode nyxt/mode/password:password-mode
            nyxt/mode/hint:hint-mode nyxt/mode/document:document-mode
            nyxt/mode/search-buffer:search-buffer-mode
            nyxt/mode/autofill:autofill-mode
            nyxt/mode/spell-check:spell-check-mode base-mode)))

(define-configuration (web-buffer)
  ((default-modes (pushnew 'nyxt/mode/blocker:blocker-mode %slot-value%))))

(define-configuration (web-buffer)
  ((default-modes
    (pushnew 'nyxt/mode/reduce-tracking:reduce-tracking-mode %slot-value%))))

(defmethod customize-instance ((browser browser) &key)
  (setf (slot-value browser 'remote-execution-p) t))
