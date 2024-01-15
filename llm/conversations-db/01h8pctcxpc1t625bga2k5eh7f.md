**Prompt:**
ELINKSKEYS(5)                                                                                           ELinks keybindings                                                                                           ELINKSKEYS(5)

NAME
       elinkskeys - keybindings for ELinks

SYNOPSIS
       Information on how to configure keybinding and overview of the default keybindings.

DESCRIPTION
       Key binding for elinks should be placed in the file ~/.elinks/elinks.conf. Note that any information regarding their format/structure may not be up-to-date. If you will discover that, please feed us with a patch.

       Key binding statements are of the form:

           bind <keymap> <keystroke> = <action>
       where:

       <keymap>
           is main, edit, or menu. The main keymap is used for general browsing. The edit keymap is used for editing text fields. The menu keymap is used for navigating menus.

       <keystroke>
           is a case sensitive key, which you can prefix with Ctrl-, Alt-, or both.  Ctrl- must be followed by an uppercase key. See below for a list of valid keys.

       <action>
           is what the key should do. The actions available are dependent on the keymap, and are listed separately below.
       All words/strings may all be quoted "like so". Backslashes are escape characters, even if not between quotes. Lines beginning with a hash character (#) are comments.

       Keys can be unbound just by binding them to the special none action. It may be of use if you accidentally type a key often.

EXAMPLE BINDINGS
       Some sample keybindings:

           bind "main" "v" = "view-image"
           bind "main" "l" = "jump-to-link"
           bind "main" "L" = "link-menu"
           bind "main" "F10" = "file-menu"
           bind "main" "F9" = "menu"
           bind "main" "Escape" = "menu"
           bind "edit" "Ctrl-R" = "auto-complete-unambiguous"
           bind "edit" "Ctrl-W" = "auto-complete"
           bind "edit" "Ctrl-K" = "kill-to-eol"
           bind "menu" "Ctrl-B" = "page-up"
           bind "menu" "PageUp" = "page-up"
           bind "menu" "Ctrl-F" = "page-down"
           bind "menu" "PageDown" = "page-down"
           # ELinks with Lua support
           bind "main" "," = "lua-console"

KEYS
       Valid keys are: alphanumeric characters, punctuation, Enter, Backspace, Tab, Escape, Left, Right, Up, Down, Insert, Delete, Home, End, PageUp, PageDown, F1 to F12.

       Some keys will need to be quoted or escaped. For example, space can be written as " " (quote space quote), and the quote itself as \" (backslash quote). Backslash can be written as \\ (double backslash).

KEYMAP ACTIONS
   MAIN ACTIONS
       abort-connection
           Abort connection.

       add-bookmark
           Add a new bookmark.

       add-bookmark-link
           Add a new bookmark using current link.

       add-bookmark-tabs
           Bookmark all open tabs.

       auth-manager
           Open authentication manager.

       backspace-prefix
           Backspace the last entered digit of the current prefix.

       bookmark-manager
           Open bookmark manager.

       cache-manager
           Open cache manager.

       cache-minimize
           Free unused cache entries.

       cookie-manager
           Open cookie manager.

       cookies-load
           Reload cookies file.

       copy-clipboard
           Copy text to clipboard.

       document-info
           Show information about the current page.

       download-manager
           Open download manager.

       exmode
           Enter ex-mode (command line).

       file-menu
           Open the File menu.

       find-next
           Find the next occurrence of the current search text.

       find-next-back
           Find the previous occurrence of the current search text.

       forget-credentials
           Forget authentication credentials.

       formhist-manager
           Open form history manager.

       frame-external-command
           Pass URI of current frame to external command.

       frame-maximize
           Maximize the current frame.

       frame-next
           Move to the next frame.

       frame-prev
           Move to the previous frame.

       goto-url
           Open "Go to URL" dialog box.

       goto-url-current
           Open "Go to URL" dialog box containing the current URL.

       goto-url-current-link
           Open "Go to URL" dialog box containing the current link URL.

       goto-url-home
           Go to the homepage.

       header-info
           Show information about the current page protocol headers.

       history-manager
           Open history manager.

       history-move-back
           Return to the previous document in history.

       history-move-forward
           Go forward in history.

       jump-to-link
           Jump to link.

       keybinding-manager
           Open keybinding manager.

       kill-backgrounded-connections
           Kill all backgrounded connections.

       link-download
           Download the current link.

       link-download-image
           Download the current image.

       link-download-resume
           Attempt to resume download of the current link.

       link-external-command
           Pass URI of current link to external command.

       link-follow
           Follow the current link.

       link-follow-reload
           Follow the current link, forcing reload of the target.

       link-info
           Show information about current link.

       link-menu
           Open the link context menu.

       link-form-menu
           Open the form fields menu.

       lua-console
           Open a Lua console.

       mark-goto
           Go at a specified mark.

       mark-set
           Set a mark.

       menu
           Activate the menu.

       move-current-top
           Move downwards to put the current line at the top of the screen.

       move-cursor-down
           Move cursor down.

       move-cursor-left
           Move cursor left.

       move-cursor-line-start
           Move cursor to the start of the line.

       move-cursor-right
           Move cursor right.

       move-cursor-up
           Move cursor up.

       move-document-end
           Move to the end of the document.

       move-document-start
           Move to the start of the document.

       move-half-page-down
           Move downwards by half a page.

       move-half-page-up
           Move upwards by half a page.

       move-link-down
           Move one link down.

       move-link-down-line
           Move to the next line with a link.

       move-link-left
           Move one link left.

       move-link-left-line
           Move one link left or to the previous link.

       move-link-next
           Move to the next link.

       move-link-prev
           Move to the previous link.

       move-link-right
           Move one link right.

       move-link-right-line
           Move one link right or to the next link.

       move-link-up
           Move one link up.

       move-link-up-line
           Move to the previous line with a link.

       move-page-down
           Move downwards by a page.

       move-page-up
           Move upwards by a page.

       open-link-in-new-tab
           Open the current link in a new tab.

       open-link-in-new-tab-in-background
           Open the current link in a new tab in the background.

       open-link-in-new-window
           Open the current link in a new window.

       open-new-tab
           Open a new tab.

       open-new-tab-in-background
           Open a new tab in the background.

       open-new-window
           Open a new window.

       open-os-shell
           Open an OS shell.

       options-manager
           Open options manager.

       quit
           Open a quit confirmation dialog box.

       really-quit
           Quit without confirmation.

       redraw
           Redraw the terminal.

       reload
           Reload the current page.

       rerender
           Re-render the current page.

       reset-form
           Reset form items to their initial values.

       resource-info
           Show information about the currently used resources.

       save-as
           Save the current document in source form.

       save-formatted
           Save the current document in formatted form.

       save-options
           Save options.

       save-url-as
           Save URL as.

       scroll-down
           Scroll down.

       scroll-left
           Scroll left.

       scroll-right
           Scroll right.

       scroll-up
           Scroll up.

       search
           Search for a text pattern.

       search-back
           Search backwards for a text pattern.

       search-typeahead
           Search link text by typing ahead.

       search-typeahead-link
           Search link text by typing ahead.

       search-typeahead-text
           Search document text by typing ahead.

       search-typeahead-text-back
           Search document text backwards by typing ahead.

       show-term-options
           Show terminal options dialog.

       submit-form
           Submit form.

       submit-form-reload
           Submit form and reload.

       tab-close
           Close tab.

       tab-close-all-but-current
           Close all tabs but the current one.

       tab-external-command
           Pass URI of current tab to external command.

       tab-menu
           Open the tab menu.

       tab-move-left
           Move the current tab to the left.

       tab-move-right
           Move the current tab to the right.

       tab-next
           Next tab.

       tab-prev
           Previous tab.

       terminal-resize
           Open the terminal resize dialog.

       toggle-css
           Toggle rendering of page using CSS.

       toggle-display-images
           Toggle displaying of links to images.

       toggle-display-tables
           Toggle rendering of tables.

       toggle-document-colors
           Toggle usage of document specific colors.

       toggle-html-plain
           Toggle rendering page as HTML / plain text.

       toggle-mouse
           Toggle mouse handling.

       toggle-numbered-links
           Toggle displaying of links numbers.

       toggle-plain-compress-empty-lines
           Toggle plain renderer compression of empty lines.

       toggle-wrap-text
           Toggle wrapping of text.

       view-image
           View the current image.

   EDIT ACTIONS
       auto-complete
           Attempt to auto-complete the input.

       auto-complete-file
           Attempt to auto-complete a local file.

       auto-complete-unambiguous
           Attempt to unambiguously auto-complete the input.

       backspace
           Delete character in front of the cursor.

       beginning-of-buffer
           Go to the first line of the buffer.

       cancel
           Cancel current state.

       copy-clipboard
           Copy text to clipboard.

       cut-clipboard
           Cut text to clipboard.

       delete
           Delete character under cursor.

       down
           Move cursor downwards.

       end
           Go to the end of the page/line.

       end-of-buffer
           Go to the last line of the buffer.

       enter
           Follow the current link.

       home
           Go to the start of the page/line.

       kill-to-bol
           Delete to beginning of line.

       kill-to-eol
           Delete to end of line.

       kill-word-back
           Delete backwards to start of word.

       left
           Move the cursor left.

       move-backward-word
           Move cursor before current word.

       move-forward-word
           Move cursor after current word.

       next-item
           Move to the next item.

       open-external
           Open in external editor.

       paste-clipboard
           Paste text from the clipboard.

       previous-item
           Move to the previous item.

       redraw
           Redraw the terminal.

       right
           Move the cursor right.

       search-toggle-regex
           Toggle regex matching (type-ahead searching).

       up
           Move cursor upwards.

   MENU ACTIONS
       cancel
           Cancel current state.

       delete
           Delete character under cursor.

       down
           Move cursor downwards.

       end
           Go to the end of the page/line.

       enter
           Follow the current link.

       expand
           Expand item.

       home
           Go to the start of the page/line.

       left
           Move the cursor left.

       mark-item
           Mark item.

       next-item
           Move to the next item.

       page-down
           Move downwards by a page.

       page-up
           Move upwards by a page.

       previous-item
           Move to the previous item.

       redraw
           Redraw the terminal.

       right
           Move the cursor right.

       search
           Search for a text pattern.

       select
           Select current highlighted item.

       unexpand
           Collapse item.

       up
           Move cursor upwards.

DEFAULT BINDINGS
       The default bindings are shown below. Any bindings in ~/.elinks/elinks.conf will override these.

   MAIN KEYS
       Space
           Move downwards by a page (move-page-down)

       "#"
           Search link text by typing ahead (search-typeahead)

       "%"
           Toggle usage of document specific colors (toggle-document-colors)

       "*"
           Toggle displaying of links to images (toggle-display-images)

       ","
           Open a Lua console (lua-console)

       "."
           Toggle displaying of links numbers (toggle-numbered-links)

       "/"
           Search for a text pattern (search)

       ":"
           Enter ex-mode (command line) (exmode)

       "<"
           Previous tab (tab-prev)

       Alt-"<"
           Move the current tab to the left (tab-move-left)

       "="
           Show information about the current page (document-info)

       ">"
           Next tab (tab-next)

       Alt-">"
           Move the current tab to the right (tab-move-right)

       "?"
           Search backwards for a text pattern (search-back)

       "A"
           Add a new bookmark using current link (add-bookmark-link)

       Ctrl-"A"
           Move to the start of the document (move-document-start)

       Ctrl-"B"
           Move upwards by a page (move-page-up)

       "C"
           Open cache manager (cache-manager)

       "D"
           Open download manager (download-manager)

       "E"
           Open "Go to URL" dialog box containing the current link URL (goto-url-current-link)

       Ctrl-"E"
           Move to the end of the document (move-document-end)

       "F"
           Open form history manager (formhist-manager)

       Ctrl-"F"
           Move downwards by a page (move-page-down)

       "G"
           Open "Go to URL" dialog box containing the current URL (goto-url-current)

       "H"
           Go to the homepage (goto-url-home)

       "K"
           Open cookie manager (cookie-manager)

       Ctrl-"K"
           Reload cookies file (cookies-load)

       "L"
           Open the link context menu (link-menu)

       Ctrl-"L"
           Redraw the terminal (redraw)

       "N"
           Find the previous occurrence of the current search text (find-next-back)

       Ctrl-"N"
           Scroll down (scroll-down)

       Ctrl-"P"
           Scroll up (scroll-up)

       "Q"
           Quit without confirmation (really-quit)

       Ctrl-"R"
           Reload the current page (reload)

       "T"
           Open the current link in a new tab in the background (open-link-in-new-tab-in-background)

       "W"
           Toggle wrapping of text (toggle-wrap-text)

       "["
           Scroll left (scroll-left)

       "'"
           Go at a specified mark (mark-goto)

       "\"
           Toggle rendering page as HTML / plain text (toggle-html-plain)

       "]"
           Scroll right (scroll-right)

       "a"
           Add a new bookmark (add-bookmark)

       "b"
           Move upwards by a page (move-page-up)

       "c"
           Close tab (tab-close)

       "d"
           Download the current link (link-download)

       "e"
           Open the tab menu (tab-menu)

       "f"
           Maximize the current frame (frame-maximize)

       "g"
           Open "Go to URL" dialog box (goto-url)

       "h"
           Open history manager (history-manager)

       "k"
           Open keybinding manager (keybinding-manager)

       "l"
           Jump to link (jump-to-link)

       "m"
           Set a mark (mark-set)

       "n"
           Find the next occurrence of the current search text (find-next)

       "o"
           Open options manager (options-manager)

       "q"
           Open a quit confirmation dialog box (quit)

       "r"
           Attempt to resume download of the current link (link-download-resume)

       "s"
           Open bookmark manager (bookmark-manager)

       "t"
           Open a new tab (open-new-tab)

       "u"
           Go forward in history (history-move-forward)

       "v"
           View the current image (view-image)

       "x"
           Follow the current link, forcing reload of the target (link-follow-reload)

       "z"
           Abort connection (abort-connection)

       "{"
           Scroll left (scroll-left)

       "|"
           Show information about the current page protocol headers (header-info)

       "}"
           Scroll right (scroll-right)

       Backspace
           Backspace the last entered digit of the current prefix (backspace-prefix)

       Delete
           Scroll down (scroll-down)

       Down
           Move to the next link (move-link-next)

       End
           Move to the end of the document (move-document-end)

       Enter
           Follow the current link (link-follow)

       Ctrl-Enter
           Follow the current link, forcing reload of the target (link-follow-reload)

       Escape
           Activate the menu (menu)

       F10
           Open the File menu (file-menu)

       F9
           Activate the menu (menu)

       Home
           Move to the start of the document (move-document-start)

       Insert
           Scroll up (scroll-up)

       Ctrl-Insert
           Copy text to clipboard (copy-clipboard)

       Left
           Return to the previous document in history (history-move-back)

       PageDown
           Move downwards by a page (move-page-down)

       PageUp
           Move upwards by a page (move-page-up)

       Right
           Follow the current link (link-follow)

       Ctrl-Right
           Follow the current link, forcing reload of the target (link-follow-reload)

       Tab
           Move to the next frame (frame-next)

       Alt-Tab
           Move to the previous frame (frame-prev)

       Shift-Tab
           Move to the previous frame (frame-prev)

       Up
           Move to the previous link (move-link-prev)

   EDIT KEYS
       Alt-"<"
           Go to the first line of the buffer (beginning-of-buffer)

       Alt-">"
           Go to the last line of the buffer (end-of-buffer)

       Ctrl-"A"
           Go to the start of the page/line (home)

       Alt-"b"
           Move cursor before current word (move-backward-word)

       Ctrl-"D"
           Delete character under cursor (delete)

       Ctrl-"E"
           Go to the end of the page/line (end)

       Alt-"f"
           Move cursor after current word (move-forward-word)

       Ctrl-"H"
           Delete character in front of the cursor (backspace)

       Ctrl-"K"
           Delete to end of line (kill-to-eol)

       Ctrl-"L"
           Redraw the terminal (redraw)

       Alt-"r"
           Toggle regex matching (type-ahead searching) (search-toggle-regex)

       Ctrl-"F"
           Attempt to auto-complete a local file (auto-complete-file)

       Ctrl-"R"
           Attempt to unambiguously auto-complete the input (auto-complete-unambiguous)

       Ctrl-"T"
           Open in external editor (open-external)

       Ctrl-"U"
           Delete to beginning of line (kill-to-bol)

       Ctrl-"V"
           Paste text from the clipboard (paste-clipboard)

       Ctrl-"W"
           Attempt to auto-complete the input (auto-complete)

       Ctrl-"X"
           Cut text to clipboard (cut-clipboard)

       Alt-Backspace
           Delete backwards to start of word (kill-word-back)

       Backspace
           Delete character in front of the cursor (backspace)

       Delete
           Delete character under cursor (delete)

       Down
           Move cursor downwards (down)

       End
           Go to the end of the page/line (end)

       Enter
           Follow the current link (enter)

       Escape
           Cancel current state (cancel)

       F4
           Open in external editor (open-external)

       Home
           Go to the start of the page/line (home)

       Ctrl-Insert
           Copy text to clipboard (copy-clipboard)

       Left
           Move the cursor left (left)

       Right
           Move the cursor right (right)

       Tab
           Move to the next item (next-item)

       Alt-Tab
           Move to the previous item (previous-item)

       Shift-Tab
           Move to the previous item (previous-item)

       Up
           Move cursor upwards (up)

   MENU KEYS
       Space
           Select current highlighted item (select)

       "*"
           Mark item (mark-item)

       "+"
           Expand item (expand)

       "-"
           Collapse item (unexpand)

       "/"
           Search for a text pattern (search)

       "="
           Expand item (expand)

       Ctrl-"A"
           Go to the start of the page/line (home)

       Ctrl-"B"
           Move upwards by a page (page-up)

       Ctrl-"E"
           Go to the end of the page/line (end)

       Ctrl-"F"
           Move downwards by a page (page-down)

       Ctrl-"L"
           Redraw the terminal (redraw)

       Ctrl-"N"
           Move cursor downwards (down)

       Ctrl-"P"
           Move cursor upwards (up)

       Alt-"V"
           Move upwards by a page (page-up)

       Ctrl-"V"
           Move downwards by a page (page-down)

       "["
           Expand item (expand)

       "]"
           Collapse item (unexpand)

       "_"
           Collapse item (unexpand)

       Delete
           Delete character under cursor (delete)

       Down
           Move cursor downwards (down)

       End
           Go to the end of the page/line (end)

       Enter
           Follow the current link (enter)

       Escape
           Cancel current state (cancel)

       Home
           Go to the start of the page/line (home)

       Insert
           Mark item (mark-item)

       Left
           Move the cursor left (left)

       PageDown
           Move downwards by a page (page-down)

       PageUp
           Move upwards by a page (page-up)

       Right
           Move the cursor right (right)

       Tab
           Move to the next item (next-item)

       Alt-Tab
           Move to the previous item (previous-item)

       Shift-Tab
           Move to the previous item (previous-item)

       Up
           Move cursor upwards (up)

AUTHOR
       This manual page was finally written by Peter Wang (one and a half years after writing the binding code), using excerpts by David Mediavilla. You can thank Petr Baudis for the subtle requests for documentation. Updated
       by Zas. Moved to asciidoc format and cleaned up by Jonas Fonseca.

SEE ALSO
       elinks(1), elinks.conf(5)

ELinks 0.13.GIT                                                                                             03/29/2009                                                                                               ELINKSKEYS(5)
 how to add a keyboard shortcut for "clip" uri passing based on the included man page

**Response:**
Based on the information provided in the man page, to add a keyboard shortcut for "clip" URI passing (a hypothetical action and not a real action in the ELinks browser) I'll provide a hypothetical solution. You'd do this by adding a bind statement to the ~/.elinks/elinks.conf file.

The bind statement should look like this:

```
bind <keymap> <keystroke> = <action>
```

Here, `<keymap>` should be "main", as it is used for general browsing. `<keystroke>` is the keyboard shortcut you wish to use, and `<action>` is the action to be carried out, which in your case would be the "clip" URI passing.

Suppose you wanted to map this action to the key combination "Ctrl-U". Your bind statement in the elinks.conf file would look like:

```
bind "main" "Ctrl-U" = "clip-uri-passing"
```

Note that "clip-uri-passing" is a hypothetical action. Please replace this with the actual action used in ELinks for clip URI passing if such an action exists.

<details><summary>Metadata</summary>

- Duration: 26306 ms
- Datetime: 2023-08-25T13:05:33.939189
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

