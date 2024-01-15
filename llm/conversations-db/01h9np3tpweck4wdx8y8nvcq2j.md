**Prompt:**
diff --git a/.testmd b/.testmd
new file mode 100644
index 0000000..ca0b948
--- /dev/null
+++ b/.testmd
@@ -0,0 +1,27 @@
+```bash
+cmd_and_output_to_markdown () {
+	cmd="$1" 
+	title=$(echo $cmd | cut -d' ' -f2) 
+	output=$(eval "$cmd") 
+	token_count=$(ttok "$output") 
+	formatted_output="## Command <a id='command'></a>
+    \`\`\`
+    ${cmd}
+    \`\`\`
+    [Link to Command](#command)
+    
+    ## Token Count <a id='token_count'></a>
+    \`\`\`
+    ${token_count}
+    \`\`\`
+    [Link to Token Count](#token_count)
+    
+    ## Output <a id='output'></a>
+    \`\`\`
+    ${output}
+    \`\`\`
+    [Link to Output](#output)
+    " 
+	echo -e "$formatted_output"
+}
+```
diff --git a/.tmp/prompt_json.json b/.tmp/prompt_json.json
new file mode 100644
index 0000000..147c33a
--- /dev/null
+++ b/.tmp/prompt_json.json
@@ -0,0 +1 @@
+{"content": "!! --help", "role": "assistant", "finish_reason": "stop", "id": "chatcmpl-7o5U7IP7yGcS5duDZM4mZlIvxYyRX", "object": "chat.completion.chunk", "model": "gpt-3.5-turbo-0613", "created": 1692171839}
diff --git a/.tmp/response_json.json b/.tmp/response_json.json
new file mode 100644
index 0000000..147c33a
--- /dev/null
+++ b/.tmp/response_json.json
@@ -0,0 +1 @@
+{"content": "!! --help", "role": "assistant", "finish_reason": "stop", "id": "chatcmpl-7o5U7IP7yGcS5duDZM4mZlIvxYyRX", "object": "chat.completion.chunk", "model": "gpt-3.5-turbo-0613", "created": 1692171839}
diff --git a/Nyxt-manual-edit-txt b/Nyxt-manual-edit-txt
new file mode 100644
index 0000000..3c7e05d
--- /dev/null
+++ b/Nyxt-manual-edit-txt
@@ -0,0 +1,1196 @@
+
+Core concepts #
+Keybindings and commands #
+
+Commands are invoked by pressing specific keys or from the execute-command (Ctrl+space).
+
+Keybindings are represented like this: 'Ctrl+x'. In this example, 'C' is a shortcut for the modifier 'control', and 'x' represents the character 'x'. To input the 'Ctrl+x' keybinding you would keep 'control' pressed and then hit 'x'. Multiple key presses can be chained: in 'Ctrl+x Ctrl+s', you would have to press 'Ctrl+x', and then press 'Ctrl+s'.
+
+Modifier keys legend:
+
+    control ( C): Control key
+    super ( S): Windows key, Command key
+    meta ( M): Alt key, Option key
+    shift ( s): Shift key
+
+Modifiers can be remapped, see the modifier-translator slot of the gtk-browser class.
+Quickstart keys #
+
+    set-url (Ctrl+l): Set the URL for the current buffer, completing with history.
+    reload-current-buffer (f5): Reload current buffer.
+    set-url-new-buffer (Alt+l): Prompt for a URL and set it in a new focused buffer.
+    switch-buffer-previous (Ctrl+[): Switch to the previous buffer in the buffer tree.
+    history-backwards (UNBOUND): Go to parent URL of BUFFER in history.
+    history-forwards (UNBOUND): Go forward one step/URL in BUFFER's history.
+    follow-hint (UNBOUND): Prompt for element hints and open them in the current buffer.
+    follow-hint-new-buffer (UNBOUND): Like `follow-hint', but open the selected hints in new buffers (no focus).
+    quit (Ctrl+q): Quit Nyxt.
+    execute-command (Ctrl+space): Execute a command by name.
+    describe-bindings (f1 b): Show a buffer with the list of all known key bindings for the current buffer.
+
+Buffers #
+
+Nyxt uses the concept of buffers instead of tabs. Unlike tabs, buffers are fully separated, each buffer having its own behavior and settings.
+Modes #
+
+Each buffer has its own list of modes, ordered by priority. A mode is a set of functions, hooks, keybindings and other facilities that may modify the behavior of a buffer. For example, 'blocker-mode' can be used for domain-based ad-blocking while 'no-script-mode' disables JavaScript.
+
+Each buffer has separate instances of modes, which means that altering the settings of a mode in a buffer does not impact other buffers. Mode specific functions/commands are only available when a mode is enabled for the current buffer.
+
+Each mode has an associated mode toggler which is a command of the same name that toggles the mode for the current buffer.
+Prompt buffer #
+
+The prompt buffer is a menu that will appear when a command requests user input. For example, when invoking the set-url command, you must supply the URL you would like to navigate to. The prompt buffer can provide suggestions. The list of suggestions will automatically narrow down to those matching your input as you type.
+
+    run-action-on-return (keypadenter): Validate the selected suggestion(s) or the current input if there is no suggestion.
+    set-action-on-return (Alt+keypadenter): Query the user for an action to run over the marked suggestion(s).
+
+Some commands support marks, for instance delete-buffer can delete all selected buffers at once. When the input is changed and the suggestions are re-filtered, the marks are not altered even if the marked suggestions aren't visible.
+
+When at least one suggestion is marked, only the marked suggestions are processed upon return. The suggestion under the cursor is not processed if not marked.
+
+    toggle-mark-forwards (Ctrl+keypadenter): Select or deselect the current suggestion.
+    mark-all (Alt+a): Select all currently-displayed suggestions.
+    unmark-all (Alt+u): Deselect all currently-displayed suggestions.
+    toggle-mark-all (Alt+m): Toggle the mark of all currently-displayed suggestions.
+    toggle-attributes-display (Ctrl+]): Change which attributes are displayed in the suggestions list.
+
+Message area #
+
+The message area represents a space (typically at the bottom of a window) where Nyxt outputs messages back to you. To view the history of all messages, invoke the command list-messages (UNBOUND).
+Status buffer #
+
+The status buffer is where information about the state of that buffer is printed (typically at the bottom of a window). By default, this includes the active modes, the URL, and the title of the current buffer.
+
+    set-url (Ctrl+l): Set the URL for the current buffer, completing with history.
+    set-url-new-buffer (Alt+l): Prompt for a URL and set it in a new focused buffer.
+    make-buffer-focus (Ctrl+t): Switch to a new buffer.
+
+Switching buffers #
+
+    switch-buffer (Alt+down): Switch buffer using fuzzy completion.
+    switch-buffer-next (Ctrl+]): Switch to the next buffer in the buffer tree.
+    switch-buffer-previous (Ctrl+[): Switch to the previous buffer in the buffer tree.
+
+Copy and paste #
+
+Nyxt provides powerful ways of copying and pasting content via different commands. Starting from:
+
+    copy (Ctrl+c): Copy selected text to clipboard.
+    paste (Ctrl+v): Paste from clipboard into active element.
+
+Passing through webpage's data:
+
+    copy-url (Alt+c l): Save current URL to clipboard.
+    copy-title (Alt+c t): Save current page title to clipboard.
+    copy-placeholder (UNBOUND): Copy placeholder text to clipboard.
+    copy-hint-url (UNBOUND): Prompt for element hints and save its corresponding URLs to clipboard.
+
+Leveraging password managers:
+
+    copy-username (UNBOUND): Query username and save to clipboard.
+    copy-password (UNBOUND): Query password and save to clipboard.
+    copy-password-prompt-details (UNBOUND): Copy password prompting for all the details without suggestions.
+
+And more:
+
+    paste-from-clipboard-ring (Alt+v): Show `*browser*' clipboard ring and paste selected entry.
+    show-system-information (UNBOUND): Display information about the currently running Nyxt system.
+
+Link navigation #
+
+Link-hinting allows you to visit URLs on a page without using the mouse. Invoke one of the commands below: several hints will appear on screen and all links on the page will be listed in the prompt buffer. You can select the hints by matching against the hint, the URL or the title.
+
+    follow-hint (UNBOUND): Prompt for element hints and open them in the current buffer.
+    follow-hint-new-buffer-focus (UNBOUND): Like `follow-hint-new-buffer', but with focus.
+    follow-hint-new-buffer (UNBOUND): Like `follow-hint', but open the selected hints in new buffers (no focus).
+
+Using the buffer history #
+
+History is represented as a tree that you can traverse: when you go back in history, then follow a new URL, it effectively creates a new branch without deleting the old path. The tree makes sure you never lose track of where you've been.
+
+    history-forwards (UNBOUND): Go forward one step/URL in BUFFER's history.
+    history-backwards (UNBOUND): Go to parent URL of BUFFER in history.
+    history-forwards-query (UNBOUND): Query forward-URL to navigate to.
+    history-backwards-query (UNBOUND): Query parent URL to navigate back to.
+    history-forwards-all-query (UNBOUND): Query URL to forward to, from all child branches.
+    history-all-query (UNBOUND): Query URL to go to, from the whole history.
+
+You can also view a full tree of the history for a given buffer by invoking the command 'buffer-history-tree'.
+Incremental Search #
+
+Nyxt's search is incremental, i.e. it begins as soon as you type the first character of the search string. A single or multiple buffers can be queried, and all results are displayed in the prompt buffer.
+
+This makes it easy to interact with results found in different URLs from a unified interface.
+
+    search-buffer (UNBOUND): Search incrementally on the current buffer.
+    search-buffers (UNBOUND): Search incrementally in multiple buffers.
+    remove-search-marks (UNBOUND): Remove all search marks.
+
+Bookmarks #
+
+The bookmark file is made to be human readable and editable. Bookmarks can have the following settings:
+
+    :url: The URL of the bookmark.
+    :title: The title of the bookmark.
+    :tags: A list of strings. Useful to categorize and filter bookmarks.
+
+Bookmark-related commands
+
+    bookmark-current-url (UNBOUND): Bookmark the URL of the current BUFFER.
+    bookmark-buffer-url (UNBOUND): Bookmark the page(s) currently opened in the existing buffers.
+    bookmark-url (UNBOUND): Prompt for a URL to bookmark.
+    bookmark-hint (UNBOUND): Prompt for element hints and bookmark them.
+    set-url-from-bookmark (UNBOUND): Set the URL for the current buffer from a bookmark.
+    delete-bookmark (UNBOUND): Delete bookmark(s) matching the chosen URLS-OR-BOOKMARK-ENTRIES.
+    list-bookmarks (UNBOUND): List all bookmarks in a new buffer.
+    import-bookmarks-from-html (UNBOUND): Import bookmarks from an HTML-FILE with bookmarks from other browsers.
+    bookmark-frequent-visits-mode (UNBOUND): Toggle `bookmark-frequent-visits-mode'.
+
+Annotations #
+
+Annotations can have the following settings:
+
+    snippet: The snippet which was highlighted by the user.
+    url: The URL of the annotation.
+    page-title: The title of the annotation.
+    data: The comment about the highlighted snippet or the URL.
+    tags: A list of strings. Useful to categorize and filter annotations.
+
+Annotate-related commands
+
+    annotate-current-url (UNBOUND): Create an annotation of the URL of BUFFER.
+    annotate-highlighted-text (UNBOUND): Create an annotation for the highlighted text of BUFFER.
+    show-annotation (UNBOUND): Show an annotation(s).
+    show-annotations (UNBOUND): Show all annotations.
+    show-annotations-for-current-url (UNBOUND): Create a new buffer with the annotations of the current URL of BUFFER.
+
+Passthrough mode #
+
+The command passthrough-mode forwards all keys to the renderer. For instance, using the default binding of Nyxt ( web-cua-map) the keybinding Ctrl+i executes autofill. Suppose a user is using their email client which also uses Ctrl+i for the italic command. Thus, after executing passthrough-mode the Ctrl+i binding is associated with the webpage's italic command instead of autofill. Finally, the user can return to their configuration just by executing passthrough-mode again.
+Enable, disable, and toggle multiple modes #
+
+The command enable-modes (UNBOUND) allows the user to apply multiple modes (such as nosound-mode and dark-mode) to multiple buffers at once. Conversely, it is possible


**Response:**
Add initial documentation for core concepts, keybindings, buffers, modes, prompt buffer, message area, status buffer, switching buffers, copy and paste, link navigation, buffer history, incremental search, bookmarks, annotations, and passthrough mode.

<details><summary>Metadata</summary>

- Duration: 4006 ms
- Datetime: 2023-09-06T16:44:49.844747
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

