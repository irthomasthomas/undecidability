Nyxt browser: Documentation

<div>

::: {.menu-header .flex-container}
::: menu-brand
[![Nyxt Logo](/image/nyxt_square_corner_128x128.png)](/)
:::

::: sub-menu
[FAQ](/faq){.pure-menu-link
target="_self"}[Manual](/documentation){.pure-menu-link
.pure-menu-selected target="_self"}[Download](/purchase){.pure-menu-link
target="_self"}
:::

::: sub-menu
[Forum](https://discourse.atlas.engineer/){.pure-menu-link
target="_blank"}[Newsletter](/newsletter){.pure-menu-link
target="_self"}[Articles](/articles){.pure-menu-link target="_self"}
:::

::: sub-menu
[Chat](https://kiwiirc.com/nextclient/irc.libera.chat/nyxt){.pure-menu-link
target="_blank"}[Source](https://github.com/atlas-engineer/nyxt){.pure-menu-link
target="_blank"}
:::

::: sub-menu
[Feed](/feed){.pure-menu-link
target="_self"}[Extensions](/extensions){.pure-menu-link target="_self"}
:::

::: sub-menu
[Login](/login){.pure-menu-link target="_self"}
:::
:::

</div>

::: {role="main"}
# Version 3.9.2

# Nyxt manual

This manual first includes the tutorial, then covers the configuration
of Nyxt.

::: {#table-of-contents .section .section}
::: {style="display: inline"}
## Table of contents {#table-of-contents style="display: inline"}

[\#](#table-of-contents){.link}
:::

-   [Core concepts](#core-concepts)

-   -   [Keybindings and commands](#keybindings-and-commands)
    -   [Quickstart keys](#quickstart-keys)
    -   [Buffers](#buffers)
    -   [Modes](#modes)
    -   [Prompt buffer](#prompt-buffer)
    -   [Message area](#message-area)
    -   [Status buffer](#status-buffer)

```{=html}
<!-- -->
```
-   [Basic controls](#basic-controls)

-   -   [Moving within a buffer](#moving-within-a-buffer)
    -   [Setting the URL](#setting-the-url)
    -   [Switching buffers](#switching-buffers)
    -   [Copy and paste](#copy-and-paste)
    -   [Link navigation](#link-navigation)
    -   [Using the buffer history](#using-the-buffer-history)
    -   [Incremental Search](#incremental-search)
    -   [Bookmarks](#bookmarks)
    -   [Annotations](#annotations)
    -   [Passthrough mode](#passthrough-mode)
    -   [Enable, disable, and toggle multiple
        modes](#enable-disable-and-toggle-multiple-modes)
    -   [Light navigation](#light-navigation)
    -   [Structural navigation](#structural-navigation)
    -   [Spelling check](#spelling-check)
    -   [Visual mode](#visual-mode)
    -   [Automation](#automation)
    -   [Miscellaneous](#miscellaneous)

```{=html}
<!-- -->
```
-   [The Nyxt help system](#the-nyxt-help-system)

-   

```{=html}
<!-- -->
```
-   [Configuration](#configuration)

-   

```{=html}
<!-- -->
```
-   [Slot configuration](#slot-configuration)

-   

```{=html}
<!-- -->
```
-   [Different types of buffers](#different-types-of-buffers)

-   

```{=html}
<!-- -->
```
-   [Keybinding configuration](#keybinding-configuration)

-   

```{=html}
<!-- -->
```
-   [Search engines](#search-engines)

-   

```{=html}
<!-- -->
```
-   [History](#history)

-   

```{=html}
<!-- -->
```
-   [Downloads](#downloads)

-   

```{=html}
<!-- -->
```
-   [Proxy and Tor](#proxy-and-tor)

-   

```{=html}
<!-- -->
```
-   [Blocker mode](#blocker-mode)

-   

```{=html}
<!-- -->
```
-   [URL-dispatchers](#url-dispatchers)

-   

```{=html}
<!-- -->
```
-   [Auto rules](#auto-rules)

-   

```{=html}
<!-- -->
```
-   [Custom commands](#custom-commands)

-   

```{=html}
<!-- -->
```
-   [Custom URL schemes](#custom-url-schemes)

-   -   [nyxt: URLs and internal pages](#nyxt-urls-and-internal-pages)

```{=html}
<!-- -->
```
-   [Hooks](#hooks)

-   

```{=html}
<!-- -->
```
-   [Data paths and data profiles](#data-paths-and-data-profiles)

-   

```{=html}
<!-- -->
```
-   [Password management](#password-management)

-   -   [KeePassXC support](#keepassxc-support)

```{=html}
<!-- -->
```
-   [Appearance](#appearance)

-   -   [Status buffer appearance](#status-buffer-appearance)

```{=html}
<!-- -->
```
-   [Scripting](#scripting)

-   

```{=html}
<!-- -->
```
-   [User scripts](#user-scripts)

-   

```{=html}
<!-- -->
```
-   [Headless mode](#headless-mode)

-   

```{=html}
<!-- -->
```
-   [Built-in REPL](#built-in-repl)

-   -   [Extending the REPL](#extending-the-repl)

```{=html}
<!-- -->
```
-   [Advanced configuration](#advanced-configuration)

-   

```{=html}
<!-- -->
```
-   [Extensions](#extensions)

-   

```{=html}
<!-- -->
```
-   [Troubleshooting](#troubleshooting)

-   -   [Debugging and reporting
        errors](#debugging-and-reporting-errors)
    -   [Playing videos](#playing-videos)
    -   [Website crashes](#website-crashes)
    -   [Input method support (CJK,
        etc.)](#input-method-support-cjk-etc)
    -   [HiDPI displays](#hidpi-displays)
    -   [StumpWM mouse scroll](#stumpwm-mouse-scroll)
    -   [Blank WebKit web-views](#blank-webkit-web-views)
    -   [Missing cursor icons](#missing-cursor-icons)
:::

::: {#core-concepts .section .section}
::: {style="display: inline"}
## Core concepts {#core-concepts style="display: inline"}

[\#](#core-concepts){.link}
:::

::: {#keybindings-and-commands .section .section}
::: {style="display: inline"}
### Keybindings and commands {#keybindings-and-commands style="display: inline"}

[\#](#keybindings-and-commands){.link}
:::

Commands are invoked by pressing specific keys or from the
[`execute-command (Ctrl+space)`](nyxt:describe-function?fn=%1Bexecute-command "[COMMAND] Execute a command by name."){.link
target="_blank"}.

Keybindings are represented like this: \'C-x\'. In this example, \'C\'
is a shortcut for the modifier \'control\', and \'x\' represents the
character \'x\'. To input the \'C-x\' keybinding you would keep
\'control\' pressed and then hit \'x\'. Multiple key presses can be
chained: in \'C-x C-s\', you would have to press \'C-x\', and then press
\'C-s\'.

Modifier keys legend:

-   `control` ( `C`): Control key
-   `super` ( `S`): Windows key, Command key
-   `meta` ( `M`): Alt key, Option key
-   `shift` ( `s`): Shift key

Modifiers can be remapped, see the `modifier-translator` slot of the
`gtk-browser` class.
:::

::: {#quickstart-keys .section .section}
::: {style="display: inline"}
### Quickstart keys {#quickstart-keys style="display: inline"}

[\#](#quickstart-keys){.link}
:::

-   [`set-url (Ctrl+l)`](nyxt:describe-function?fn=%1Bset-url "[COMMAND] Set the URL for the current buffer, completing with history."){.link
    target="_blank"}: Set the URL for the current buffer, completing
    with history.
-   [`reload-current-buffer (f5)`](nyxt:describe-function?fn=%1Breload-current-buffer "[COMMAND] Reload current buffer."){.link
    target="_blank"}: Reload current buffer.
-   [`set-url-new-buffer (Alt+l)`](nyxt:describe-function?fn=%1Bset-url-new-buffer "[COMMAND] Prompt for a URL and set it in a new focused buffer."){.link
    target="_blank"}: Prompt for a URL and set it in a new focused
    buffer.
-   [`switch-buffer-previous (Ctrl+[)`](nyxt:describe-function?fn=%1Bswitch-buffer-previous "[COMMAND] Switch to the previous buffer in the buffer tree."){.link
    target="_blank"}: Switch to the previous buffer in the buffer tree.
-   [`history-backwards (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-backwards "[COMMAND] Go to parent URL of BUFFER in history."){.link
    target="_blank"}: Go to parent URL of BUFFER in history.
-   [`history-forwards (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-forwards "[COMMAND] Go forward one step/URL in BUFFER's history."){.link
    target="_blank"}: Go forward one step/URL in BUFFER\'s history.
-   [`follow-hint (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhint%3Afollow-hint "[COMMAND] Prompt for element hints and open them in the current buffer."){.link
    target="_blank"}: Prompt for element hints and open them in the
    current buffer.
-   [`follow-hint-new-buffer (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhint%3Afollow-hint-new-buffer "[COMMAND] Like `follow-hint', but open the selected hints in new buffers (no focus)."){.link
    target="_blank"}: Like \`follow-hint\', but open the selected hints
    in new buffers (no focus).
-   [`quit (Ctrl+q)`](nyxt:describe-function?fn=%1Bquit "[COMMAND] Quit Nyxt."){.link
    target="_blank"}: Quit Nyxt.
-   [`execute-command (Ctrl+space)`](nyxt:describe-function?fn=%1Bexecute-command "[COMMAND] Execute a command by name."){.link
    target="_blank"}: Execute a command by name.
-   [`describe-bindings (f1 b)`](nyxt:describe-function?fn=%1Bdescribe-bindings "[COMMAND] Show a list of all available keybindings in the current buffer."){.link
    target="_blank"}: Show a list of all available keybindings in the
    current buffer.
:::

::: {#buffers .section .section}
::: {style="display: inline"}
### Buffers {#buffers style="display: inline"}

[\#](#buffers){.link}
:::

Nyxt uses the concept of buffers instead of tabs. Unlike tabs, buffers
are fully separated, each buffer having its own behavior and settings.
:::

::: {#modes .section .section}
::: {style="display: inline"}
### Modes {#modes style="display: inline"}

[\#](#modes){.link}
:::

Each buffer has its own list of modes, ordered by priority. A mode is a
set of functions, hooks, keybindings and other facilities that may
modify the behavior of a buffer. For example, \'blocker-mode\' can be
used for domain-based ad-blocking while \'no-script-mode\' disables
JavaScript.

Each buffer has separate instances of modes, which means that altering
the settings of a mode in a buffer does not impact other buffers. Mode
specific functions/commands are only available when a mode is enabled
for the current buffer.

Each mode has an associated *mode toggler* which is a command of the
same name that toggles the mode for the current buffer.
:::

::: {#prompt-buffer .section .section}
::: {style="display: inline"}
### Prompt buffer {#prompt-buffer style="display: inline"}

[\#](#prompt-buffer){.link}
:::

The prompt buffer is a menu that will appear when a command requests
user input. For example, when invoking the `set-url` command, you must
supply the URL you would like to navigate to. The prompt buffer can
provide suggestions. The list of suggestions will automatically narrow
down to those matching your input as you type.

-   [`run-action-on-return (keypadenter)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fprompt-buffer%3Arun-action-on-return "[COMMAND] Have the PROMPT-BUFFER return the marks, then quit."){.link
    target="_blank"}: Validate the selected suggestion(s) or the current
    input if there is no suggestion.
-   [`set-action-on-return (Alt+keypadenter)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fprompt-buffer%3Aset-action-on-return "[COMMAND] Prompt for an action to run over PROMPT-BUFFER `prompter:marks'."){.link
    target="_blank"}: Query the user for an action to run over the
    marked suggestion(s).

Some commands support marks, for instance `delete-buffer` can delete all
selected buffers at once. When the input is changed and the suggestions
are re-filtered, the marks are not altered even if the marked
suggestions aren\'t visible.

When at least one suggestion is marked, only the marked suggestions are
processed upon return. The suggestion under the cursor is not processed
if not marked.

-   [`toggle-mark-forwards (Ctrl+keypadenter)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fprompt-buffer%3Atoggle-mark-forwards "[COMMAND] Mark current suggestion and `next-suggestion'."){.link
    target="_blank"}: Select or deselect the current suggestion.
-   [`mark-all (Alt+a)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fprompt-buffer%3Amark-all "[COMMAND] Mark all visible suggestions in current source."){.link
    target="_blank"}: Select all currently-displayed suggestions.
-   [`unmark-all (Alt+u)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fprompt-buffer%3Aunmark-all "[COMMAND] Unmark all visible suggestions in current source."){.link
    target="_blank"}: Deselect all currently-displayed suggestions.
-   [`toggle-mark-all (Alt+m)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fprompt-buffer%3Atoggle-mark-all "[COMMAND] Toggle the mark over all visible suggestions in current source."){.link
    target="_blank"}: Toggle the mark of all currently-displayed
    suggestions.
-   [`toggle-attributes-display (Ctrl+])`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fprompt-buffer%3Atoggle-attributes-display "[COMMAND] Prompt for which prompter attributes to display."){.link
    target="_blank"}: Change which attributes are displayed in the
    suggestions list.
:::

::: {#message-area .section .section}
::: {style="display: inline"}
### Message area {#message-area style="display: inline"}

[\#](#message-area){.link}
:::

The message area represents a space (typically at the bottom of a
window) where Nyxt outputs messages back to you. To view the history of
all messages, invoke the command
[`list-messages (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fmessage%3Alist-messages "[COMMAND] Show the *Messages* buffer."){.link
target="_blank"}.
:::

::: {#status-buffer .section .section}
::: {style="display: inline"}
### Status buffer {#status-buffer style="display: inline"}

[\#](#status-buffer){.link}
:::

The status buffer is where information about the state of that buffer is
printed (typically at the bottom of a window). By default, this includes
the active modes, the URL, and the title of the current buffer.
:::
:::

::: {#basic-controls .section .section}
::: {style="display: inline"}
## Basic controls {#basic-controls style="display: inline"}

[\#](#basic-controls){.link}
:::

::: {#moving-within-a-buffer .section .section}
::: {style="display: inline"}
### Moving within a buffer {#moving-within-a-buffer style="display: inline"}

[\#](#moving-within-a-buffer){.link}
:::

To move within a buffer, several commands are provided:

-   [`scroll-down (keypaddown)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Ascroll-down "[COMMAND] Scroll down the current page."){.link
    target="_blank"}: Scroll down the current page.
-   [`scroll-up (keypadup)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Ascroll-up "[COMMAND] Scroll up the current page."){.link
    target="_blank"}: Scroll up the current page.
-   [`scroll-page-down (keypadnext)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Ascroll-page-down "[COMMAND] Scroll down by one page height."){.link
    target="_blank"}: Scroll down by one page height.
-   [`scroll-page-up (keypadpageup)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Ascroll-page-up "[COMMAND] Scroll up by one page height."){.link
    target="_blank"}: Scroll up by one page height.
-   [`scroll-to-bottom (Ctrl+down)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Ascroll-to-bottom "[COMMAND] Scroll to the bottom of the current page."){.link
    target="_blank"}: Scroll to the bottom of the current page.
-   [`scroll-to-top (Ctrl+up)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Ascroll-to-top "[COMMAND] Scroll to the top of the current page."){.link
    target="_blank"}: Scroll to the top of the current page.
:::

::: {#setting-the-url .section .section}
::: {style="display: inline"}
### Setting the URL {#setting-the-url style="display: inline"}

[\#](#setting-the-url){.link}
:::

When ambiguous URLs are inputted, Nyxt will attempt the best guess it
can. If you do not supply a protocol in a URL, HTTPS will be assumed. To
visit a site supporting only the less secure HTTP, you must explicitly
type the full URL including the \'http://\' prefix.

-   [`set-url (Ctrl+l)`](nyxt:describe-function?fn=%1Bset-url "[COMMAND] Set the URL for the current buffer, completing with history."){.link
    target="_blank"}: Set the URL for the current buffer, completing
    with history.
-   [`set-url-new-buffer (Alt+l)`](nyxt:describe-function?fn=%1Bset-url-new-buffer "[COMMAND] Prompt for a URL and set it in a new focused buffer."){.link
    target="_blank"}: Prompt for a URL and set it in a new focused
    buffer.
-   [`make-buffer-focus (Ctrl+t)`](nyxt:describe-function?fn=%1Bmake-buffer-focus "[COMMAND] Switch to a new buffer."){.link
    target="_blank"}: Switch to a new buffer.
:::

::: {#switching-buffers .section .section}
::: {style="display: inline"}
### Switching buffers {#switching-buffers style="display: inline"}

[\#](#switching-buffers){.link}
:::

-   [`switch-buffer (Alt+down)`](nyxt:describe-function?fn=%1Bswitch-buffer "[COMMAND] Switch buffer using fuzzy completion."){.link
    target="_blank"}: Switch buffer using fuzzy completion.
-   [`switch-buffer-next (Ctrl+])`](nyxt:describe-function?fn=%1Bswitch-buffer-next "[COMMAND] Switch to the next buffer in the buffer tree."){.link
    target="_blank"}: Switch to the next buffer in the buffer tree.
-   [`switch-buffer-previous (Ctrl+[)`](nyxt:describe-function?fn=%1Bswitch-buffer-previous "[COMMAND] Switch to the previous buffer in the buffer tree."){.link
    target="_blank"}: Switch to the previous buffer in the buffer tree.
:::

::: {#copy-and-paste .section .section}
::: {style="display: inline"}
### Copy and paste {#copy-and-paste style="display: inline"}

[\#](#copy-and-paste){.link}
:::

Unlike other web browsers, Nyxt provides powerful ways of copying and
pasting content via different commands. Starting from:

-   [`copy (Ctrl+c)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Acopy "[COMMAND] Copy selected text to clipboard."){.link
    target="_blank"}: Copy selected text to clipboard.
-   [`paste (Ctrl+v)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Apaste "[COMMAND] Paste from clipboard into active element."){.link
    target="_blank"}: Paste from clipboard into active element.

Passing through webpage\'s data:

-   [`copy-url (Alt+c l)`](nyxt:describe-function?fn=%1Bcopy-url "[COMMAND] Save current URL to clipboard."){.link
    target="_blank"}: Save current URL to clipboard.
-   [`copy-title (Alt+c t)`](nyxt:describe-function?fn=%1Bcopy-title "[COMMAND] Save current page title to clipboard."){.link
    target="_blank"}: Save current page title to clipboard.
-   [`copy-placeholder (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Acopy-placeholder "[COMMAND] Copy placeholder text to clipboard."){.link
    target="_blank"}: Copy placeholder text to clipboard.
-   [`copy-hint-url (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhint%3Acopy-hint-url "[COMMAND] Prompt for element hints and save its corresponding URLs to clipboard."){.link
    target="_blank"}: Prompt for element hints and save its
    corresponding URLs to clipboard.

Leveraging password managers:

-   [`copy-username (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fpassword%3Acopy-username "[COMMAND] Query username and save to clipboard."){.link
    target="_blank"}: Query username and save to clipboard.
-   [`copy-password (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fpassword%3Acopy-password "[COMMAND] Query password and save to clipboard."){.link
    target="_blank"}: Query password and save to clipboard.
-   [`copy-password-prompt-details (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fpassword%3Acopy-password-prompt-details "[COMMAND] Copy password prompting for all the details without suggestions."){.link
    target="_blank"}: Copy password prompting for all the details
    without suggestions.

And more:

-   [`paste-from-clipboard-ring (Alt+v)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Apaste-from-clipboard-ring "[COMMAND] Show `*browser*' clipboard ring and paste selected entry."){.link
    target="_blank"}: Show \`\*browser\*\' clipboard ring and paste
    selected entry.
-   [`show-system-information (unbound)`](nyxt:describe-function?fn=%1Bshow-system-information "[COMMAND] Display information about the currently running Nyxt system."){.link
    target="_blank"}: Display information about the currently running
    Nyxt system.
:::

::: {#link-navigation .section .section}
::: {style="display: inline"}
### Link navigation {#link-navigation style="display: inline"}

[\#](#link-navigation){.link}
:::

Link-hinting allows you to visit URLs on a page without using the mouse.
Invoke one of the commands below: several hints will appear on screen
and all links on the page will be listed in the prompt buffer. You can
select the hints by matching against the hint, the URL or the title.

-   [`follow-hint (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhint%3Afollow-hint "[COMMAND] Prompt for element hints and open them in the current buffer."){.link
    target="_blank"}: Prompt for element hints and open them in the
    current buffer.
-   [`follow-hint-new-buffer-focus (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhint%3Afollow-hint-new-buffer-focus "[COMMAND] Like `follow-hint-new-buffer', but with focus."){.link
    target="_blank"}: Like \`follow-hint-new-buffer\', but with focus.
-   [`follow-hint-new-buffer (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhint%3Afollow-hint-new-buffer "[COMMAND] Like `follow-hint', but open the selected hints in new buffers (no focus)."){.link
    target="_blank"}: Like \`follow-hint\', but open the selected hints
    in new buffers (no focus).
:::

::: {#using-the-buffer-history .section .section}
::: {style="display: inline"}
### Using the buffer history {#using-the-buffer-history style="display: inline"}

[\#](#using-the-buffer-history){.link}
:::

History is represented as a tree that you can traverse: when you go back
in history, then follow a new URL, it effectively creates a new branch
without deleting the old path. The tree makes sure you never lose track
of where you\'ve been.

-   [`history-forwards (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-forwards "[COMMAND] Go forward one step/URL in BUFFER's history."){.link
    target="_blank"}: Go forward one step/URL in BUFFER\'s history.
-   [`history-backwards (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-backwards "[COMMAND] Go to parent URL of BUFFER in history."){.link
    target="_blank"}: Go to parent URL of BUFFER in history.
-   [`history-forwards-query (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-forwards-query "[COMMAND] Query forward-URL to navigate to."){.link
    target="_blank"}: Query forward-URL to navigate to.
-   [`history-backwards-query (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-backwards-query "[COMMAND] Query parent URL to navigate back to."){.link
    target="_blank"}: Query parent URL to navigate back to.
-   [`history-forwards-all-query (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-forwards-all-query "[COMMAND] Query URL to forward to, from all child branches."){.link
    target="_blank"}: Query URL to forward to, from all child branches.
-   [`history-all-query (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-all-query "[COMMAND] Query URL to go to, from the whole history."){.link
    target="_blank"}: Query URL to go to, from the whole history.

You can also view a full tree of the history for a given buffer by
invoking the command \'buffer-history-tree\'.
:::

::: {#incremental-search .section .section}
::: {style="display: inline"}
### Incremental Search {#incremental-search style="display: inline"}

[\#](#incremental-search){.link}
:::

Nyxt\'s search is incremental, i.e. it begins as soon as you type the
first character of the search string. A single or multiple buffers can
be queried, and all results are displayed in the prompt buffer.

This makes it easy to interact with results found in different URLs from
a unified interface.

-   [`search-buffer (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fsearch-buffer%3Asearch-buffer "[COMMAND] Search incrementally on the current buffer."){.link
    target="_blank"}: Search incrementally on the current buffer.
-   [`search-buffers (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fsearch-buffer%3Asearch-buffers "[COMMAND] Search incrementally in multiple buffers."){.link
    target="_blank"}: Search incrementally in multiple buffers.
-   [`remove-search-marks (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fsearch-buffer%3Aremove-search-marks "[COMMAND] Remove all search marks."){.link
    target="_blank"}: Remove all search marks.
:::

::: {#bookmarks .section .section}
::: {style="display: inline"}
### Bookmarks {#bookmarks style="display: inline"}

[\#](#bookmarks){.link}
:::

The bookmark file is made to be human readable and editable. Bookmarks
can have the following settings:

-   `:url`: The URL of the bookmark.
-   `:title`: The title of the bookmark.
-   `:tags`: A list of strings. Useful to categorize and filter
    bookmarks.

Bookmark-related commands

-   [`bookmark-current-url (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fbookmark%3Abookmark-current-url "[COMMAND] Bookmark the URL of the current BUFFER."){.link
    target="_blank"}: Bookmark the URL of the current BUFFER.
-   [`bookmark-buffer-url (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fbookmark%3Abookmark-buffer-url "[COMMAND] Bookmark the page(s) currently opened in the existing buffers."){.link
    target="_blank"}: Bookmark the page(s) currently opened in the
    existing buffers.
-   [`bookmark-url (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fbookmark%3Abookmark-url "[COMMAND] Prompt for a URL to bookmark."){.link
    target="_blank"}: Prompt for a URL to bookmark.
-   [`bookmark-hint (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fbookmark%3Abookmark-hint "[COMMAND] Prompt for element hints and bookmark them."){.link
    target="_blank"}: Prompt for element hints and bookmark them.
-   [`set-url-from-bookmark (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fbookmark%3Aset-url-from-bookmark "[COMMAND] Set the URL for the current buffer from a bookmark."){.link
    target="_blank"}: Set the URL for the current buffer from a
    bookmark.
-   [`delete-bookmark (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fbookmark%3Adelete-bookmark "[COMMAND] Delete bookmark(s) matching the chosen URLS-OR-BOOKMARK-ENTRIES."){.link
    target="_blank"}: Delete bookmark(s) matching the chosen
    URLS-OR-BOOKMARK-ENTRIES.
-   [`list-bookmarks (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fbookmark%3Alist-bookmarks "[COMMAND] List all bookmarks in a new buffer."){.link
    target="_blank"}: List all bookmarks in a new buffer.
-   [`import-bookmarks-from-html (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fbookmark%3Aimport-bookmarks-from-html "[COMMAND] Import bookmarks from an HTML-FILE with bookmarks from other browsers."){.link
    target="_blank"}: Import bookmarks from an HTML-FILE with bookmarks
    from other browsers.
-   [`bookmark-frequent-visits-mode (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fbookmark-frequent-visits%3Abookmark-frequent-visits-mode "[COMMAND] Toggle `bookmark-frequent-visits-mode'."){.link
    target="_blank"}: Toggle \`bookmark-frequent-visits-mode\'.
:::

::: {#annotations .section .section}
::: {style="display: inline"}
### Annotations {#annotations style="display: inline"}

[\#](#annotations){.link}
:::

Annotations can have the following settings:

-   [`snippet`](nyxt:describe-slot?name=%1Bnyxt%2Fmode%2Fannotate%3Asnippet&class=%1Bnyxt%2Fmode%2Fannotate%3Asnippet-annotation "[SLOT of SNIPPET-ANNOTATION] Auto-generated accessor function for slot SNIPPET."){.link
    target="_blank"}: The snippet which was highlighted by the user.
-   [`url`](nyxt:describe-slot?name=%1Burl&class=%1Bnyxt%2Fmode%2Fannotate%3Aurl-annotation "[SLOT of URL-ANNOTATION] Auto-generated accessor function for slot URL."){.link
    target="_blank"}: The URL of the annotation.
-   [`page-title`](nyxt:describe-slot?name=%1Bnyxt%2Fmode%2Fannotate%3Apage-title&class=%1Bnyxt%2Fmode%2Fannotate%3Aurl-annotation "[SLOT of URL-ANNOTATION] Auto-generated accessor function for slot PAGE-TITLE."){.link
    target="_blank"}: The title of the annotation.
-   [`data`](nyxt:describe-slot?name=%1Bnyxt%2Fmode%2Fannotate%3A%3Adata&class=%1Bnyxt%2Fmode%2Fannotate%3Aannotation "[SLOT of ANNOTATION] Auto-generated accessor function for slot DATA."){.link
    target="_blank"}: The comment about the highlighted snippet or the
    URL.
-   [`tags`](nyxt:describe-slot?name=%1Bnyxt%2Fmode%2Fannotate%3Atags&class=%1Bnyxt%2Fmode%2Fannotate%3Aannotation "[SLOT of ANNOTATION] Auto-generated accessor function for slot TAGS."){.link
    target="_blank"}: A list of strings. Useful to categorize and filter
    annotations.

Annotate-related commands

-   [`annotate-current-url (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fannotate%3Aannotate-current-url "[COMMAND] Create an annotation of the URL of BUFFER."){.link
    target="_blank"}: Create an annotation of the URL of BUFFER.
-   [`annotate-highlighted-text (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fannotate%3Aannotate-highlighted-text "[COMMAND] Create an annotation for the highlighted text of BUFFER."){.link
    target="_blank"}: Create an annotation for the highlighted text of
    BUFFER.
-   [`show-annotation (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fannotate%3Ashow-annotation "[COMMAND] Show an annotation(s)."){.link
    target="_blank"}: Show an annotation(s).
-   [`show-annotations (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fannotate%3Ashow-annotations "[COMMAND] Show all annotations"){.link
    target="_blank"}: Show all annotations.
-   [`show-annotations-for-current-url (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fannotate%3Ashow-annotations-for-current-url "[COMMAND] Create a new buffer with the annotations of the current URL of BUFFER."){.link
    target="_blank"}: Create a new buffer with the annotations of the
    current URL of BUFFER.
:::

::: {#passthrough-mode .section .section}
::: {style="display: inline"}
### Passthrough mode {#passthrough-mode style="display: inline"}

[\#](#passthrough-mode){.link}
:::

The command `passthrough-mode` forwards all keys to the renderer. For
instance, using the default binding of Nyxt ( `web-cua-map`) the
keybinding `C-i` executes `autofill`. Suppose a user is using their
email client which also uses `C-i` for the italic command. Thus, after
executing `passthrough-mode` the `C-i` binding is associated with the
webpage\'s italic command instead of `autofill`. Finally, the user can
return to their configuration just by executing `passthrough-mode`
again.
:::

::: {#enable-disable-and-toggle-multiple-modes .section .section}
::: {style="display: inline"}
### Enable, disable, and toggle multiple modes {#enable-disable-and-toggle-multiple-modes style="display: inline"}

[\#](#enable-disable-and-toggle-multiple-modes){.link}
:::

The command
[`enable-modes (unbound)`](nyxt:describe-function?fn=%1Benable-modes "[COMMAND] Enable MODES for BUFFERS prompting for either or both."){.link
target="_blank"} allows the user to apply multiple modes (such as
`nosound-mode` and `dark-mode`) to multiple buffers at once. Conversely,
it is possible to revert this action by executing
[`disable-modes (unbound)`](nyxt:describe-function?fn=%1Bdisable-modes "[COMMAND] Disable MODES for BUFFERS."){.link
target="_blank"} while choosing exactly the same buffers and modes
previously selected. Finally, `toggle-mode` also allows activation and
deactivation of multiple modes, but only for the current buffer.
:::

::: {#light-navigation .section .section}
::: {style="display: inline"}
### Light navigation {#light-navigation style="display: inline"}

[\#](#light-navigation){.link}
:::

Reduce bandwidth usage via:

-   [`no-image-mode (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fno-image%3Ano-image-mode "[COMMAND] Toggle `no-image-mode'."){.link
    target="_blank"}: Toggle \`no-image-mode\'.
-   [`no-script-mode (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fno-script%3Ano-script-mode "[COMMAND] Toggle `no-script-mode'."){.link
    target="_blank"}: Toggle \`no-script-mode\'.
-   [`no-webgl-mode (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fno-webgl%3Ano-webgl-mode "[COMMAND] Toggle `no-webgl-mode'."){.link
    target="_blank"}: Toggle \`no-webgl-mode\'.

It is possible to enable these three modes at once with:
`reduce-bandwidth-mode`.
:::

::: {#structural-navigation .section .section}
::: {style="display: inline"}
### Structural navigation {#structural-navigation style="display: inline"}

[\#](#structural-navigation){.link}
:::

It is possible to navigate using the structure in between the file:

-   [`jump-to-heading (Ctrl+h)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Ajump-to-heading "[COMMAND] Jump to a particular heading, of type h1, h2, h3, h4, h5, or h6."){.link
    target="_blank"}: Jump to a particular heading, of type h1, h2, h3,
    h4, h5, or h6.
-   [`previous-heading (Alt+{)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Aprevious-heading "[COMMAND] Scroll to the previous heading of the BUFFER."){.link
    target="_blank"}: Scroll to the previous heading of the BUFFER.
-   [`next-heading (Alt+})`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Anext-heading "[COMMAND] Scroll to the next heading of the BUFFER."){.link
    target="_blank"}: Scroll to the next heading of the BUFFER.
-   [`jump-to-heading-buffers (Ctrl+Alt+h)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Ajump-to-heading-buffers "[COMMAND] Jump to a particular heading, of type h1, h2, h3, h4, h5, or h6 across a set"){.link
    target="_blank"}: Jump to a particular heading, of type h1, h2, h3,
    h4, h5, or h6 across a set of buffers.

And navigate to interconnected files:

-   [`go-next (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Ago-next "[COMMAND] Navigate to the next element according to the HTML 'rel' attribute."){.link
    target="_blank"}: Navigate to the next element according to the HTML
    \'rel\' attribute.
-   [`go-previous (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Ago-previous "[COMMAND] Navigate to the previous element according to the HTML 'rel' attribute."){.link
    target="_blank"}: Navigate to the previous element according to the
    HTML \'rel\' attribute.
-   [`go-up (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Ago-up "[COMMAND] Navigate to the upper level in the URL path hierarchy."){.link
    target="_blank"}: Navigate to the upper level in the URL path
    hierarchy.
-   [`go-to-homepage (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Ago-to-homepage "[COMMAND] Navigate to the homepage."){.link
    target="_blank"}: Navigate to the homepage.
:::

::: {#spelling-check .section .section}
::: {style="display: inline"}
### Spelling check {#spelling-check style="display: inline"}

[\#](#spelling-check){.link}
:::

Several commands are provided to spell check words. The default is
English but it is possible to change the slot
[`spell-check-language`](nyxt:describe-slot?name=%1Bnyxt%2Fmode%2Fspell-check%3Aspell-check-language&class=%1Bnyxt%2Fmode%2Fspell-check%3Aspell-check-mode "[SLOT of SPELL-CHECK-MODE] Auto-generated accessor function for slot SPELL-CHECK-LANGUAGE."){.link
target="_blank"} for other languages:

-   [`spell-check-word (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fspell-check%3Aspell-check-word "[COMMAND] Spell check a word."){.link
    target="_blank"}: Spell check a word.
-   [`spell-check-word-at-cursor (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fspell-check%3Aspell-check-word-at-cursor "[COMMAND] Spell check the word at the cursor."){.link
    target="_blank"}: Spell check the word at the cursor.
-   [`spell-check-suggest-word (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fspell-check%3Aspell-check-suggest-word "[COMMAND] Suggest a spelling for a given word."){.link
    target="_blank"}: Suggest a spelling for a given word.
-   [`spell-check-highlighted-word (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fspell-check%3Aspell-check-highlighted-word "[COMMAND] Spell check a highlighted word. If a word is incorrectly spelled,"){.link
    target="_blank"}: Spell check a highlighted word.
-   [`spell-check-list-languages (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fspell-check%3Aspell-check-list-languages "[COMMAND] List all languages supported on your machine."){.link
    target="_blank"}: List all languages supported on your machine.
-   [`spell-check-text-input (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fspell-check%3Aspell-check-text-input "[COMMAND] Spell check full text input provided by the user."){.link
    target="_blank"}: Spell check full text input provided by the user.
:::

::: {#visual-mode .section .section}
::: {style="display: inline"}
### Visual mode {#visual-mode style="display: inline"}

[\#](#visual-mode){.link}
:::

Select text without a mouse. Nyxt\'s `visual-mode` imitates Vim\'s
visual mode (and comes with the CUA and Emacs-like keybindings out of
the box, too). Activate it with the
[`visual-mode (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Avisual-mode "[COMMAND] Toggle `visual-mode'."){.link
target="_blank"} command.

Visual mode provides the following commands:

-   [`visual-mode (Ctrl+c)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Avisual-mode "[COMMAND] Toggle `visual-mode'."){.link
    target="_blank"}: Quit visual mode.
-   [`select-paragraph (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Aselect-paragraph "[COMMAND] Add hints to text elements on the page and query them."){.link
    target="_blank"}: Add hints to text elements on the page and query
    them.
-   [`toggle-mark (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Atoggle-mark "[COMMAND] Toggle the mark."){.link
    target="_blank"}: Toggle the mark.
-   [`forward-char (right)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Aforward-char "[COMMAND] Move caret forward by a character."){.link
    target="_blank"}: Move caret forward by a character.
-   [`backward-char (backspace)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Abackward-char "[COMMAND] Move caret backward by a character."){.link
    target="_blank"}: Move caret backward by a character.
-   [`forward-word (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Aforward-word "[COMMAND] Move caret forward by a word."){.link
    target="_blank"}: Move caret forward by a word.
-   [`backward-word (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Abackward-word "[COMMAND] Move caret backward by a word."){.link
    target="_blank"}: Move caret backward by a word.
-   [`forward-line (down)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Aforward-line "[COMMAND] Move caret forward by a line."){.link
    target="_blank"}: Move caret forward by a line.
-   [`backward-line (up)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Abackward-line "[COMMAND] Move caret backward by a line."){.link
    target="_blank"}: Move caret backward by a line.
-   [`beginning-line (keypadhome)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Abeginning-line "[COMMAND] Move caret to the beginning of the line."){.link
    target="_blank"}: Move caret to the beginning of the line.
-   [`end-line (keypadend)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Aend-line "[COMMAND] Move caret to the end of the line."){.link
    target="_blank"}: Move caret to the end of the line.
-   [`forward-sentence (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Aforward-sentence "[COMMAND] Move caret forward to next end of sentence."){.link
    target="_blank"}: Move caret forward to next end of sentence.
-   [`backward-sentence (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Abackward-sentence "[COMMAND] Move caret backward to start of sentence."){.link
    target="_blank"}: Move caret backward to start of sentence.

Commands designed to ease the use for CUA users (but available to all
users):

-   [`forward-char-with-selection (Shift+right)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Aforward-char-with-selection "[COMMAND] Set mark and move caret forward by a character."){.link
    target="_blank"}: Set mark and move caret forward by a character.
-   [`backward-char-with-selection (Shift+left)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Abackward-char-with-selection "[COMMAND] Set mark and move caret backward by a character."){.link
    target="_blank"}: Set mark and move caret backward by a character.
-   [`forward-line-with-selection (Shift+down)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Aforward-line-with-selection "[COMMAND] Set mark and move caret forward by a line."){.link
    target="_blank"}: Set mark and move caret forward by a line.
-   [`backward-line-with-selection (Shift+up)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Abackward-line-with-selection "[COMMAND] Set mark and move caret backward by a line."){.link
    target="_blank"}: Set mark and move caret backward by a line.

A note for `emacs-mode` users: unlike in Emacs, in Nyxt the command
[`toggle-mark (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fvisual%3Atoggle-mark "[COMMAND] Toggle the mark."){.link
target="_blank"} is bound to Shift-space, as C-space is bound to
\'execute-command, overriding any mode keybinding. If you want to toggle
mark with C-space, you\'ll need to set your own override-map such that
C-space is not bound. An example:

::: {style="position: relative"}
          
           Act on codeCopy
           Add To Auto-Config
           Try In Repl
          (define-configuration input-buffer
      ((override-map
        (let ((map (make-keymap "override-map")))
          (define-key map "M-x" 'execute-command)))))
:::
:::

::: {#automation .section .section}
::: {style="display: inline"}
### Automation {#automation style="display: inline"}

[\#](#automation){.link}
:::

Nyxt has many facilities for automation. For instance, it is possible to
automate the reading experience:

-   [`cruise-control-mode (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fcruise-control%3Acruise-control-mode "[COMMAND] Toggle `cruise-control-mode'."){.link
    target="_blank"}: Toggle \`cruise-control-mode\'.

Symmetrically, it is possible to automate the filling of forms:

-   [`autofill (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fautofill%3Aautofill "[COMMAND] Fill in a field with a value from a saved list."){.link
    target="_blank"}: Fill in a field with a value from a saved list.
-   [`toggle-checkboxes (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fbookmarklets%3Atoggle-checkboxes "[COMMAND] Toggle all checkboxes."){.link
    target="_blank"}: Toggle all checkboxes.

In addition, it is possible to automate actions over time:

-   [`watch-mode (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fwatch%3Awatch-mode "[COMMAND] Toggle `watch-mode'."){.link
    target="_blank"}: Toggle \`watch-mode\'.
-   [`repeat-every (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepeat%3Arepeat-every "[COMMAND] Prompt for FUNCTION to be run every SECONDS."){.link
    target="_blank"}: Prompt for function to be run every seconds.

Or even automate actions based on conditions:

-   [`repeat-mode (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepeat%3Arepeat-mode "[COMMAND] Toggle `repeat-mode'."){.link
    target="_blank"}: Toggle \`repeat-mode\'.
-   [`preview-mode (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fpreview%3Apreview-mode "[COMMAND] Toggle `preview-mode'."){.link
    target="_blank"}: Toggle \`preview-mode\'.

Nyxt also offers a no-code interface to build automation via Common Lisp
macros:

-   [`edit-macro (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fmacro-edit%3Aedit-macro "[COMMAND] Edit a macro."){.link
    target="_blank"}: Edit a macro.

Lastly, the
[`process-mode`](nyxt:describe-class?class=%1Bnyxt%2Fmode%2Fprocess%3Aprocess-mode "[MODE] Conditionally execute a file/directory-related `action' in a separate thread."){.link
target="_blank"} must be highlighted:

[`process-mode`](nyxt:describe-class?class=%1Bnyxt%2Fmode%2Fprocess%3Aprocess-mode "[MODE] Conditionally execute a file/directory-related `action' in a separate thread."){.link
target="_blank"} is actually a building block for other modes previously
mentioned, such as
[`repeat-mode`](nyxt:describe-class?class=%1Bnyxt%2Fmode%2Frepeat%3Arepeat-mode "[MODE] Repeat the execution of a command while enabled."){.link
target="_blank"}. The extension relationship goes further, since
[`cruise-control-mode`](nyxt:describe-class?class=%1Bnyxt%2Fmode%2Fcruise-control%3Acruise-control-mode "[MODE] Mode for automatically scrolling up and down the page."){.link
target="_blank"} is in its turn an extension and a composition of
[`repeat-mode`](nyxt:describe-class?class=%1Bnyxt%2Fmode%2Frepeat%3Arepeat-mode "[MODE] Repeat the execution of a command while enabled."){.link
target="_blank"} and
[`scroll-down (keypaddown)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Ascroll-down "[COMMAND] Scroll down the current page."){.link
target="_blank"}. Further extensions and compositions can be creatively
tailor-made by users to automate their own use of Nyxt.
:::

::: {#miscellaneous .section .section}
::: {style="display: inline"}
### Miscellaneous {#miscellaneous style="display: inline"}

[\#](#miscellaneous){.link}
:::

-   [`zoom-page (Ctrl++)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Azoom-page "[COMMAND] Zoom in the current page BUFFER."){.link
    target="_blank"}: Zoom in the current page BUFFER.
-   [`unzoom-page (Ctrl+button5)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Aunzoom-page "[COMMAND] Zoom out the current page in BUFFER."){.link
    target="_blank"}: Zoom out the current page in BUFFER.
-   [`reset-page-zoom (Ctrl+0)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdocument%3Areset-page-zoom "[COMMAND] Reset the BUFFER zoom to the `zoom-ratio-default' or RATIO."){.link
    target="_blank"}: Reset the BUFFER zoom to the
    \`zoom-ratio-default\' or RATIO.
-   [`autofill (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fautofill%3Aautofill "[COMMAND] Fill in a field with a value from a saved list."){.link
    target="_blank"}: Fill in a field with a value from a saved list.
-   [`download-open-file (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Ffile-manager%3Adownload-open-file "[COMMAND] Open file in Nyxt or externally."){.link
    target="_blank"}: Open file in Nyxt or externally.
-   [`edit-with-external-editor (Ctrl+u Ctrl+o)`](nyxt:describe-function?fn=%1Bedit-with-external-editor "[COMMAND] Edit the current input field using `external-editor-program'."){.link
    target="_blank"}: Edit the current input field using
    \`external-editor-program\'.
:::
:::

::: {#the-nyxt-help-system .section .section}
::: {style="display: inline"}
## The Nyxt help system {#the-nyxt-help-system style="display: inline"}

[\#](#the-nyxt-help-system){.link}
:::

Nyxt provides introspective and help capabilities. All commands,
classes, slots, variables, functions and bindings can be inspected for
definition and documentation.

-   [`tutorial (f1 t)`](nyxt:describe-function?fn=%1Btutorial "[COMMAND] Display Nyxt tutorial."){.link
    target="_blank"}: Display Nyxt tutorial.
-   [`describe-key (f1 k)`](nyxt:describe-function?fn=%1Bdescribe-key "[COMMAND] Display binding of user-inputted keys."){.link
    target="_blank"}: Display binding of user-inputted keys.
-   [`describe-bindings (f1 b)`](nyxt:describe-function?fn=%1Bdescribe-bindings "[COMMAND] Show a list of all available keybindings in the current buffer."){.link
    target="_blank"}: Show a list of all available keybindings in the
    current buffer.
-   [`describe-command (f1 c)`](nyxt:describe-function?fn=%1Bdescribe-command "[COMMAND] Inspect a command and show it in a help buffer."){.link
    target="_blank"}: Inspect a command and show it in a help buffer.
-   [`describe-function (f1 f)`](nyxt:describe-function?fn=%1Bdescribe-function "[COMMAND] Inspect a function and show it in a help buffer."){.link
    target="_blank"}: Inspect a function and show it in a help buffer.
-   [`describe-variable (f1 v)`](nyxt:describe-function?fn=%1Bdescribe-variable "[COMMAND] Inspect a variable and show it in a help buffer."){.link
    target="_blank"}: Inspect a variable and show it in a help buffer.
-   [`describe-class (f1 C)`](nyxt:describe-function?fn=%1Bdescribe-class "[COMMAND] Inspect a class and show it in a help buffer."){.link
    target="_blank"}: Inspect a class and show it in a help buffer.
-   [`describe-slot (f1 s)`](nyxt:describe-function?fn=%1Bdescribe-slot "[COMMAND] Inspect a slot and show it in a help buffer."){.link
    target="_blank"}: Inspect a slot and show it in a help buffer.
-   [`describe-any (f1 a)`](nyxt:describe-function?fn=%1Bdescribe-any "[COMMAND] Inspect anything and show it in a help buffer."){.link
    target="_blank"}: Inspect anything and show it in a help buffer.

A good starting point is to study the documentation of the classes
`browser`, `window`, `buffer` and `prompt-buffer`.
:::

::: {#configuration .section .section}
::: {style="display: inline"}
## Configuration {#configuration style="display: inline"}

[\#](#configuration){.link}
:::

Nyxt is written in the Common Lisp programming language which offers a
great perk: everything in the browser can be customized by the user,
even while it\'s running!

To get started with Common Lisp, we recommend checking out our web page:
[Learn Lisp](https://nyxt-browser.com/learn-lisp). It contains numerous
pointers to other resources, including free books both for beginners and
seasoned programmers.

Nyxt provides a mechanism for new users unfamiliar with Lisp to
customize Nyxt. Start by invoking the commands
[`describe-class (f1 C)`](nyxt:describe-function?fn=%1Bdescribe-class "[COMMAND] Inspect a class and show it in a help buffer."){.link
target="_blank"} or
[`describe-slot (f1 s)`](nyxt:describe-function?fn=%1Bdescribe-slot "[COMMAND] Inspect a slot and show it in a help buffer."){.link
target="_blank"}. You can press the button marked \'Configure\' to
change the value of a setting. The settings will be applied immediately
and saved for future sessions. Please note that these settings will not
alter existing object instances.

Settings created by Nyxt are stored in
`/home/doe/.config/nyxt/auto-config.3.lisp`.

Any settings can be overridden manually by
`/home/doe/.config/nyxt/config.lisp`.

The following section assumes knowledge of basic Common Lisp or a
similar programming language.

The user needs to manually create the Nyxt configuration file, and the
parent folders if necessary.

Example:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (define-configuration web-buffer
      ((default-modes
        (pushnew 'nyxt/mode/no-script:no-script-mode %slot-value%))))
:::

The above turns on the \'no-script-mode\' (disables JavaScript) by
default for every buffer.

The
[`define-configuration`](nyxt:describe-function?fn=%1Bdefine-configuration "[MACRO] Helper macro to customize the class slots of the CLASSES."){.link
target="_blank"} macro can be used to customize the slots of classes
like the browser, buffers, windows, etc. Refer to the class and slot
documentation for the individual details.

To find out about all modes known to Nyxt, run
[`describe-command (f1 c)`](nyxt:describe-function?fn=%1Bdescribe-command "[COMMAND] Inspect a command and show it in a help buffer."){.link
target="_blank"} and type \'mode\'.
:::

::: {#slot-configuration .section .section}
::: {style="display: inline"}
## Slot configuration {#slot-configuration style="display: inline"}

[\#](#slot-configuration){.link}
:::

Slot values can be queried and tweaked, enabling many customization
possibilities. For instance, slot
[`zoom-ratio-default`](nyxt:describe-slot?name=%1Bzoom-ratio-default&class=%1Bdocument-buffer "[SLOT of DOCUMENT-BUFFER] Auto-generated accessor function for slot ZOOM-RATIO-DEFAULT."){.link
target="_blank"} has the default value of `1.0`. Follow the steps below
to tweak it:

1.  Execute command
    [`describe-slot (f1 s)`](nyxt:describe-function?fn=%1Bdescribe-slot "[COMMAND] Inspect a slot and show it in a help buffer."){.link
    target="_blank"};
2.  Type `zoom-ratio-default` to select the one from `document-buffer`;
3.  Press the `Configure` button;
4.  Type the desired value, for instance, `1.3`.
5.  After restarting Nyxt, every page will be zoomed accordingly.

There are plenty of customizable slots and these can be discovered by
inspecting classes via
[`describe-class (f1 C)`](nyxt:describe-function?fn=%1Bdescribe-class "[COMMAND] Inspect a class and show it in a help buffer."){.link
target="_blank"}.
:::

::: {#different-types-of-buffers .section .section}
::: {style="display: inline"}
## Different types of buffers {#different-types-of-buffers style="display: inline"}

[\#](#different-types-of-buffers){.link}
:::

There are multiple buffer classes, such as
[`document-buffer`](nyxt:describe-class?class=%1Bdocument-buffer "[CLASS] Buffers holding structured documents."){.link
target="_blank"} (for structured documents) and
[`input-buffer`](nyxt:describe-class?class=%1Binput-buffer "[CLASS] A buffer in which the user can input."){.link
target="_blank"} (for buffers that can receive user input). A
[`web-buffer`](nyxt:describe-class?class=%1Bweb-buffer "[CLASS] Buffer for browsing the web."){.link
target="_blank"} class is used for web pages,
[`prompt-buffer`](nyxt:describe-class?class=%1Bprompt-buffer "[CLASS] The prompt buffer is the interface for user interactions."){.link
target="_blank"} for, well, the prompt buffer. Some buffer classes may
inherit from multiple other classes. For instance
[`web-buffer`](nyxt:describe-class?class=%1Bweb-buffer "[CLASS] Buffer for browsing the web."){.link
target="_blank"} and
[`prompt-buffer`](nyxt:describe-class?class=%1Bprompt-buffer "[CLASS] The prompt buffer is the interface for user interactions."){.link
target="_blank"} both inherit from
[`input-buffer`](nyxt:describe-class?class=%1Binput-buffer "[CLASS] A buffer in which the user can input."){.link
target="_blank"}.

You can configure one of the parent
[`buffer`](nyxt:describe-class?class=%1Bbuffer "[CLASS] A buffer is the fundamental unit of displayed content."){.link
target="_blank"} classes slots and the new values will automatically
cascade down as a new default for all child classes- unless this slot is
specialized by these child classes. For instance if you configure the
[`override-map`](nyxt:describe-slot?name=%1Boverride-map&class=%1Binput-buffer "[SLOT of INPUT-BUFFER] Auto-generated accessor function for slot OVERRIDE-MAP."){.link
target="_blank"} slot in
[`input-buffer`](nyxt:describe-class?class=%1Binput-buffer "[CLASS] A buffer in which the user can input."){.link
target="_blank"}, both
[`panel-buffer`](nyxt:describe-class?class=%1Bpanel-buffer "[CLASS] Panel buffer (also known as sidebar): small view on the side of the screen."){.link
target="_blank"} and
[`web-buffer`](nyxt:describe-class?class=%1Bweb-buffer "[CLASS] Buffer for browsing the web."){.link
target="_blank"} classes will inherit from the new value.
:::

::: {#keybinding-configuration .section .section}
::: {style="display: inline"}
## Keybinding configuration {#keybinding-configuration style="display: inline"}

[\#](#keybinding-configuration){.link}
:::

Nyxt supports multiple *bindings schemes* such as CUA (the default),
Emacs or vi. Changing scheme is as simple as setting the corresponding
mode as default, e.g.
[`emacs-mode`](nyxt:describe-class?class=%1Bnyxt%2Fmode%2Femacs%3Aemacs-mode "[CLASS] Enable Emacs inspired keybindings."){.link
target="_blank"}. To make the change persistent across sessions, add the
following to your configuration:

-   vi bindings:

    ::: {style="position: relative"}
              
               Act on codeCopy
               Add To Auto-Config
               Try In Repl
              (define-configuration buffer
          ((default-modes
            (pushnew 'nyxt/mode/vi:vi-normal-mode %slot-value%))))
    :::
-   Emacs bindings:

    ::: {style="position: relative"}
              
               Act on codeCopy
               Add To Auto-Config
               Try In Repl
              (define-configuration buffer
          ((default-modes
            (pushnew 'nyxt/mode/emacs:emacs-mode %slot-value%))))
    :::

You can create new scheme names with
[`make-keyscheme`](nyxt:describe-function?fn=%1Bnkeymaps%2Fcore%3Amake-keyscheme "[FUNCTION] Return a new `keyscheme' object."){.link
target="_blank"}. Also see the
[`define-keyscheme-map macro`](nyxt:describe-function?fn=%1Bdefine-keyscheme-map "[FUNCTION] Return a keyscheme-map, a hash table with `keyscheme's as key and `keymap's"){.link
target="_blank"}.

To extend the bindings of a specific mode, you can configure the mode
with
[`define-configuration`](nyxt:describe-function?fn=%1Bdefine-configuration "[MACRO] Helper macro to customize the class slots of the CLASSES."){.link
target="_blank"} and extend its
[`keyscheme-map`](nyxt:describe-slot?name=%1Bkeyscheme-map&class=%1Bmode "[SLOT of MODE] Auto-generated accessor function for slot KEYSCHEME-MAP."){.link
target="_blank"} with
[`define-keyscheme-map`](nyxt:describe-function?fn=%1Bdefine-keyscheme-map "[FUNCTION] Return a keyscheme-map, a hash table with `keyscheme's as key and `keymap's"){.link
target="_blank"}. For example:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (define-configuration base-mode
      "Note the :import part of the define-keyscheme-map.
    It re-uses the other keymap (in this case, the one that was slot value before
    the configuration) and merely adds/modifies it."
      ((keyscheme-map
        (define-keyscheme-map "my-base" (list :import %slot-value%)
                              keyscheme:vi-normal
                              (list "g b"
                                    (lambda-command switch-buffer*
                                        nil
                                      (switch-buffer :current-is-last-p
                                                     t)))))))
:::

The
[`override-map`](nyxt:describe-slot?name=%1Boverride-map&class=%1Binput-buffer "[SLOT of INPUT-BUFFER] Auto-generated accessor function for slot OVERRIDE-MAP."){.link
target="_blank"} is a keymap that has priority over all other keymaps.
By default, it has few bindings like the one for
[`execute-command (Ctrl+space)`](nyxt:describe-function?fn=%1Bexecute-command "[COMMAND] Execute a command by name."){.link
target="_blank"}. You can use it to set keys globally:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (define-configuration input-buffer
      ((override-map
        (let ((map (make-keymap "override-map")))
          (define-key map "M-x" 'execute-command "C-space" 'nothing)))))
:::

The
[`nothing (unbound)`](nyxt:describe-function?fn=%1Bnothing "[COMMAND] A command that does nothing."){.link
target="_blank"} command is useful to override bindings to do nothing.
Note that it\'s possible to bind any command, including those of
disabled modes that are not listed in
[`execute-command (Ctrl+space)`](nyxt:describe-function?fn=%1Bexecute-command "[COMMAND] Execute a command by name."){.link
target="_blank"}. Binding to
[`nothing (unbound)`](nyxt:describe-function?fn=%1Bnothing "[COMMAND] A command that does nothing."){.link
target="_blank"} and binding to NIL means different things (see the
documentation of
[`define-key`](nyxt:describe-function?fn=%1Bdefine-key "[FUNCTION] Bind KEYS to BOUND-VALUE in KEYMAP."){.link
target="_blank"} for details):

[`nothing (unbound)`](nyxt:describe-function?fn=%1Bnothing "[COMMAND] A command that does nothing."){.link target="_blank"}
:   Binds the key to a command that does nothing. Still discovers the
    key and recognizes it as pressed.

NIL
:   Un-binds the key, removing all the bindings that it had in a given
    mode/keyscheme-map. If you press the un-bound key, the bindings that
    used to be there will not be found anymore, and the key will be
    forwarded to the renderer.

Any other symbol/command
:   Replaces the command that was there before, with the new one. When
    the key is pressed, the new command will fire instead of the old
    one.

In addition, a more flexible approach is to create your own mode with
your custom keybindings. When this mode is added first to the buffer
mode list, its keybindings have priorities over the other modes. Note
that this kind of global keymaps also have priority over regular
character insertion, so you should probably not bind anything without
modifiers in such a keymap.

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (defvar *my-keymap* (make-keymap "my-map"))

    (define-key *my-keymap* "C-f" 'nyxt/mode/history:history-forwards
                "C-b" 'nyxt/mode/history:history-backwards)

    (define-mode my-mode
        nil
      "Dummy mode for the custom key bindings in *my-keymap*."
      ((keyscheme-map
        (nkeymaps/core:make-keyscheme-map keyscheme:cua *my-keymap*
                                          keyscheme:emacs *my-keymap*
                                          keyscheme:vi-normal
                                          *my-keymap*))))

    (define-configuration web-buffer
      "Enable this mode by default."
      ((default-modes (pushnew 'my-mode %slot-value%))))
:::

Bindings are subject to various translations as per
[`*translator*`](nyxt:describe-variable?variable=%1Bnkeymaps%2Fcore%3A%2Atranslator%2A "[VARIABLE] Key translator to use in `keymap' objects."){.link
target="_blank"}. By default if it fails to find a binding it tries
again with inverted shifts. For instance if `C-x C-F` fails to match
anything `C-x C-f` is tried.See the default value of
[`*translator*`](nyxt:describe-variable?variable=%1Bnkeymaps%2Fcore%3A%2Atranslator%2A "[VARIABLE] Key translator to use in `keymap' objects."){.link
target="_blank"} to learn how to customize it or set it to `nil` to
disable all forms of translation.
:::

::: {#search-engines .section .section}
::: {style="display: inline"}
## Search engines {#search-engines style="display: inline"}

[\#](#search-engines){.link}
:::

See the
[`search-engines`](nyxt:describe-slot?name=%1Bsearch-engines&class=%1Bcontext-buffer "[SLOT of CONTEXT-BUFFER] Auto-generated accessor function for slot SEARCH-ENGINES."){.link
target="_blank"} buffer slot documentation. Bookmarks can also be used
as search engines, see the corresponding section.

Nyxt comes with default search engines for
`en.wikipedia.org, duckduckgo.com, search.atlas.engineer`. The following
example shows one way to add new search engines.

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (defvar *my-search-engines*
      (list
       '("google" "https://google.com/search?q=~a" "https://google.com")
       '("python3" "https://docs.python.org/3/search.html?q=~a"
         "https://docs.python.org/3")
       '("doi" "https://dx.doi.org/~a" "https://dx.doi.org/"))
      "List of search engines.")

    (define-configuration context-buffer
      "Go through the search engines above and make-search-engine out of them."
      ((search-engines
        (append
         (mapcar (lambda (engine) (apply 'make-search-engine engine))
                 *my-search-engines*)
         %slot-default%))))
:::

Note that the last search engine is the default one. For example, in
order to make python3 the default, the above code can be slightly
modified as follows.

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (defvar *my-search-engines*
      (list
       '("google" "https://google.com/search?q=~a" "https://google.com")
       '("doi" "https://dx.doi.org/~a" "https://dx.doi.org/")
       '("python3" "https://docs.python.org/3/search.html?q=~a"
         "https://docs.python.org/3"))
      "List of search engines.")

    (define-configuration context-buffer
      "Go through the search engines above and make-search-engine out of them."
      ((search-engines
        (append %slot-default%
                (mapcar
                 (lambda (engine) (apply 'make-search-engine engine))
                 *my-search-engines*)))))
:::

If you don\'t want to use
[`make-search-engine`](nyxt:describe-function?fn=%1Bmake-search-engine "[FUNCTION] Utility to create simple `search-engine's."){.link
target="_blank"} and want to try building the engines yourself, you can
always make new
[`search-engine`](nyxt:describe-class?class=%1Bsearch-engine "[CLASS] A representation of search engine, as used in Nyxt."){.link
target="_blank"} and add it to
[`search-engines`](nyxt:describe-slot?name=%1Bsearch-engines&class=%1Bcontext-buffer "[SLOT of CONTEXT-BUFFER] Auto-generated accessor function for slot SEARCH-ENGINES."){.link
target="_blank"} list:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (define-configuration context-buffer
      "Add a single search engine manually."
      ((search-engines
        (pushnew
         (make-instance 'search-engine :name "Reddit" :shortcut "r"
                        :search-url "https://reddit.com/search/?q=~a"
                        :fallback-url "https://reddit.com")
         %slot-value%))))
:::
:::

::: {#history .section .section}
::: {style="display: inline"}
## History {#history style="display: inline"}

[\#](#history){.link}
:::

Nyxt history model is a tree whose nodes are URLs. It branches out
through all the buffers. If you create a new buffer (via
[`follow-hint-new-buffer (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhint%3Afollow-hint-new-buffer "[COMMAND] Like `follow-hint', but open the selected hints in new buffers (no focus)."){.link
target="_blank"} or
[`make-buffer (unbound)`](nyxt:describe-function?fn=%1Bmake-buffer "[COMMAND] Create a new buffer."){.link
target="_blank"}), it becomes a new history branch originating from the
branch of the previous buffer.

History can be navigated with the arrow keys in the status buffer, or
with commands like
[`history-backwards (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-backwards "[COMMAND] Go to parent URL of BUFFER in history."){.link
target="_blank"} and
[`history-forwards (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-forwards "[COMMAND] Go forward one step/URL in BUFFER's history."){.link
target="_blank"} (which the arrows are bound to).

If the beyond-buffer-boundaries behavior sounds like too much to you, or
you prefer the behavior of Nyxt 2, where the history was still a tree,
but was not spilling across the buffers, then configure
[`global-history-p`](nyxt:describe-slot?name=%1Bglobal-history-p&class=%1Bcontext-buffer "[SLOT of CONTEXT-BUFFER] Auto-generated accessor function for slot GLOBAL-HISTORY-P."){.link
target="_blank"} to be NIL:

::: {style="position: relative"}
         
          Act on codeCopy
          Add To Auto-Config
          Try In Repl
         (define-configuration :context-buffer
      (global-history-p nil))
:::

This would make all buffers to have their own history, not connected to
the other buffers at all. All the history commands (like
[`history-backwards (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-backwards "[COMMAND] Go to parent URL of BUFFER in history."){.link
target="_blank"} and
[`history-forwards (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-forwards "[COMMAND] Go forward one step/URL in BUFFER's history."){.link
target="_blank"}) will only work inside the buffer history then.

Nyxt supra-buffer history has benefits, though: it optimizes browsing
patterns into more intuitive and productive structures. One particular
pattern Nyxt history optimizes is hub-and-spoke search, where you keep
returning to a certain hub to start your search/navigation from a
familiar point. You can enable the optimization (merely going back in
history to the hub page, instead of creating a new history node) for
this strategy by configuring
[`backtrack-to-hubs-p`](nyxt:describe-slot?name=%1Bnyxt%2Fmode%2Fhistory%3Abacktrack-to-hubs-p&class=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-mode "[SLOT of HISTORY-MODE] Auto-generated accessor function for slot BACKTRACK-TO-HUBS-P."){.link
target="_blank"} to T.

Another useful side to Nyxt tree-like history are braching-aware history
commands, like
[`history-forwards-query (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-forwards-query "[COMMAND] Query forward-URL to navigate to."){.link
target="_blank"}, allowing one to choose which branch of history they
are going to visit, if there are several. If there\'s only one branch,
then this command behaves much like regular
[`history-forwards (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-forwards "[COMMAND] Go forward one step/URL in BUFFER's history."){.link
target="_blank"}.

There are commands that allow to move across all the history before or
after the current node:

-   [`history-backwards-query (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-backwards-query "[COMMAND] Query parent URL to navigate back to."){.link
    target="_blank"}: Query parent URL to navigate back to.
-   [`history-forwards-all-query (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-forwards-all-query "[COMMAND] Query URL to forward to, from all child branches."){.link
    target="_blank"}: Query URL to forward to, from all child branches.
-   [`history-all-query (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fhistory%3Ahistory-all-query "[COMMAND] Query URL to go to, from the whole history."){.link
    target="_blank"}: Query URL to go to, from the whole history.

If you need to know more: most of the optimizations and data structures
are in
[`history-tree`](nyxt:describe-package?package=%1B%3Ahistory-tree "[PACKAGE]"){.link
target="_blank"} library, while most of the Nyxt-specific interface is
in
[`nyxt/mode/history-tree`](nyxt:describe-package?package=%1B%3Anyxt%2Fmode%2Fhistory-tree "[PACKAGE] Package for `history-tree-mode', mode for history-trees styling."){.link
target="_blank"}.
:::

::: {#downloads .section .section}
::: {style="display: inline"}
## Downloads {#downloads style="display: inline"}

[\#](#downloads){.link}
:::

See the
[`list-downloads (Ctrl+Shift+Y)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fdownload%3Alist-downloads "[COMMAND] Display a buffer listing all downloads."){.link
target="_blank"} command and the
[`download-path`](nyxt:describe-slot?name=%1Bdownload-path&class=%1Bbuffer "[SLOT of BUFFER]"){.link
target="_blank"} buffer slot documentation.
:::

::: {#proxy-and-tor .section .section}
::: {style="display: inline"}
## Proxy and Tor {#proxy-and-tor style="display: inline"}

[\#](#proxy-and-tor){.link}
:::

See the
[`proxy-mode`](nyxt:describe-class?class=%1Bnyxt%2Fmode%2Fproxy%3Aproxy-mode "[CLASS] Enable forwarding of all network requests to a specific host."){.link
target="_blank"} documentation.
:::

::: {#blocker-mode .section .section}
::: {style="display: inline"}
## Blocker mode {#blocker-mode style="display: inline"}

[\#](#blocker-mode){.link}
:::

This mode blocks access to websites related to specific hosts. To see
all hosts being blocked, execute command `describe-variable`, choose
variable `NYXT/MODE/BLOCKER:*DEFAULT-HOSTLIST*`, and read data on
`nyxt/mode/blocker:url-body` slot. To customize host blocking, read the
[`blocker-mode`](nyxt:describe-class?class=%1Bnyxt%2Fmode%2Fblocker%3Ablocker-mode "[CLASS] Enable blocking of listed hosts."){.link
target="_blank"} documentation.
:::

::: {#url-dispatchers .section .section}
::: {style="display: inline"}
## URL-dispatchers {#url-dispatchers style="display: inline"}

[\#](#url-dispatchers){.link}
:::

You can configure which actions to take depending on the URL to be
loaded. For instance, you can configure which Torrent program to start
to load magnet links. See the
[`url-dispatching-handler`](nyxt:describe-function?fn=%1Burl-dispatching-handler "[FUNCTION] Return a `hook-request' handler apply its ACTION on the URLs conforming to TEST."){.link
target="_blank"} function documentation.
:::

::: {#auto-rules .section .section}
::: {style="display: inline"}
## Auto rules {#auto-rules style="display: inline"}

[\#](#auto-rules){.link}
:::

Auto-rules toggle modes when the URL satisfies the given conditions.
URL-dispatchers can also be used for this, but it is simpler to use an
auto-rule. Given that Nyxt\'s functionality is mode-based, the
consequences are far reaching.

These can be used in the following ways:

Manually, by calling:

[`save-non-default-modes-for-future-visits (unbound)`](nyxt:describe-function?fn=%1Bsave-non-default-modes-for-future-visits "[COMMAND] Save the modes present in `default-modes' and not present in current modes as"){.link target="_blank"}
:   which saves \"unusual\" modes - non-default modes that were toggled
    exclusively for a given URL.

[`save-exact-modes-for-future-visits (unbound)`](nyxt:describe-function?fn=%1Bsave-exact-modes-for-future-visits "[COMMAND] Store the exact list of enabled modes to auto-rules for all the future visits"){.link target="_blank"}
:   which saves the exact list of enabled modes for a given URL.

Automatically, by setting
[`prompt-on-mode-toggle-p`](nyxt:describe-slot?name=%1Bprompt-on-mode-toggle-p&class=%1Bmodable-buffer "[SLOT of MODABLE-BUFFER] Auto-generated accessor function for slot PROMPT-ON-MODE-TOGGLE-P."){.link
target="_blank"} to non-nil (refer to the [configuration
section](#configuration) for help).

All rules are stored at `/home/doe/.local/share/nyxt/auto-rules.lisp`,
which [is meant to be human-readable and human-writable]{.underline}.
You can find instructions at the top of it. The gist is that rules are
mere Lisp lists which start with a condition that checks the URL. When
conditions are met, modes are toggled. Besides user-defined conditions,
the following are often useful:

-   [`match-domain`](nyxt:describe-function?fn=%1Bmatch-domain "[FUNCTION] Return a predicate for URL designators matching one of DOMAIN or OTHER-DOMAINS."){.link
    target="_blank"}
-   [`match-host`](nyxt:describe-function?fn=%1Bmatch-host "[FUNCTION] Return a predicate for URL designators matching one of HOST or OTHER-HOSTS."){.link
    target="_blank"}
-   [`match-url`](nyxt:describe-function?fn=%1Bmatch-url "[FUNCTION] Return a predicate for URLs exactly matching ONE-URL or OTHER-URLS."){.link
    target="_blank"}
-   [`match-regex`](nyxt:describe-function?fn=%1Bmatch-regex "[FUNCTION] Return a predicate for URL designators matching one of REGEX or OTHER-REGEX."){.link
    target="_blank"}
-   [`match-scheme`](nyxt:describe-function?fn=%1Bmatch-scheme "[FUNCTION] Return a predicate for URL designators matching one of SCHEME or OTHER-SCHEMES."){.link
    target="_blank"}

By default,
[`apply-all-matching-auto-rules-p`](nyxt:describe-slot?name=%1Bapply-all-matching-auto-rules-p&class=%1Bmodable-buffer "[SLOT of MODABLE-BUFFER] Auto-generated accessor function for slot APPLY-ALL-MATCHING-AUTO-RULES-P."){.link
target="_blank"} is nil meaning that only the most specific rules are
honored.

Auto-rules can also be defined for custom use-cases via
[`define-auto-rule`](nyxt:describe-function?fn=%1Bdefine-auto-rule "[FUNCTION] Define a new default `auto-rule'."){.link
target="_blank"} and un-defined with
[`undefine-auto-rule`](nyxt:describe-function?fn=%1Bundefine-auto-rule "[FUNCTION] Remove the rule with TOKEN test."){.link
target="_blank"}.
:::

::: {#custom-commands .section .section}
::: {style="display: inline"}
## Custom commands {#custom-commands style="display: inline"}

[\#](#custom-commands){.link}
:::

Creating your own invocable commands is similar to creating a Common
Lisp function, except the form is `define-command` instead of `defun`.
If you want this command to be invocable outside of the context of a
mode, use `define-command-global`.

Example:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (define-command-global my-bookmark-url
        nil
      "Query which URL to bookmark."
      (let ((url
             (prompt :prompt "Bookmark URL" :sources
                     'prompter:raw-source)))
        (nyxt/mode/bookmark:bookmark-add url)))
:::

See the
[`prompt-buffer`](nyxt:describe-class?class=%1Bprompt-buffer "[CLASS] The prompt buffer is the interface for user interactions."){.link
target="_blank"} class documentation for how to write custom prompt
buffers.

You can also create your own context menu entries binding those to Lisp
commands, using
[`ffi-add-context-menu-command`](nyxt:describe-function?fn=%1Bffi-add-context-menu-command "[FUNCTION] Add COMMAND as accessible in context menus with LABEL displayed for it."){.link
target="_blank"} function. You can bind the `bookmark-url` like this:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (ffi-add-context-menu-command 'my-bookmark-url "Bookmark URL")
:::

Currently, context menu commands don\'t have access to the renderer
objects (and shouldn\'t hope to). Commands you bind to context menu
actions should deduce most of the information from their surroundings,
using JavaScript and Lisp functions Nyxt provides. For example, one can
use the
[`url-at-point`](nyxt:describe-slot?name=%1Burl-at-point&class=%1Bbuffer "[SLOT of BUFFER] Auto-generated accessor function for slot URL-AT-POINT."){.link
target="_blank"} to get thep URL currently under pointer.

With this, one can improve the bookmarking using
[`url-at-point`](nyxt:describe-slot?name=%1Burl-at-point&class=%1Bbuffer "[SLOT of BUFFER] Auto-generated accessor function for slot URL-AT-POINT."){.link
target="_blank"}:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (ffi-add-context-menu-command
     (lambda ()
       (nyxt/mode/bookmark:bookmark-add (url-at-point (current-buffer))))
     "Bookmark Link")
:::
:::

::: {#custom-url-schemes .section .section}
::: {style="display: inline"}
## Custom URL schemes {#custom-url-schemes style="display: inline"}

[\#](#custom-url-schemes){.link}
:::

If there\'s a scheme that Nyxt doesn\'t support, but you want it to, you
can always define the handler for this scheme so that it\'s
Nyxt-openable.

As a totally hypothetical example, you can define a nonsense scheme
`bleep` to generate a page with random text:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (define-internal-scheme "bleep"
                            (lambda (url buffer)
                              (values
                               (spinneret:with-html-string
                                 (:h1 "Bleep bloop?")
                                 (:p
                                  (loop repeat (parse-integer
                                                (quri.uri:uri-path
                                                 (url url))
                                                :junk-allowed t)
                                        collect (:li
                                                 (elt '("bleep" "bloop")
                                                      (random 2))))))
                               "text/html;charset=utf8"))
                            :local-p t)
:::

What this piece of code does is

-   Define a new scheme.

-   Make a handler for it that takes the URL (as a string) and a buffer
    it\'s being opened in.

-   Read the path (the part after the bleep:) of the URL and interpret
    it as a number.

-   -   (Note that you need to wrap the URL into a
        [`url`](nyxt:describe-function?fn=%1Burl "[FUNCTION] Auto-generated accessor function for slot URL."){.link
        target="_blank"} call so that it turns into a
        [`uri`](nyxt:describe-class?class=%1Bquri.uri%3Auri "[CLASS]"){.link
        target="_blank"} for the convenience of path (and other
        elements) fetching.)

-   Generate a random list of \"bleep\" and \"bloop\".

-   Return it as a `text/html` content.

The next time you run Nyxt and open `bleep:20`, you\'ll see a list of
twenty bleeps and bloops.

Internal schemes can return any type of content (both strings and arrays
of bytes are recognized), and they are capable of being
[`CORS-enabled`](nyxt:describe-slot?name=%1Bcors-enabled-p&class=%1Bscheme "[SLOT of SCHEME] Auto-generated accessor function for slot CORS-ENABLED-P."){.link
target="_blank"},
[`protected`](nyxt:describe-slot?name=%1Blocal-p&class=%1Bscheme "[SLOT of SCHEME] Auto-generated accessor function for slot LOCAL-P."){.link
target="_blank"}, and are in general capable of whatever the
renderer-provided schemes do.

::: {#nyxt-urls-and-internal-pages .section .section}
::: {style="display: inline"}
### nyxt: URLs and internal pages {#nyxt-urls-and-internal-pages style="display: inline"}

[\#](#nyxt-urls-and-internal-pages){.link}
:::

You can create pages out of Lisp commands, and make arbitrary
computations for the content of those. More so: these pages can invoke
Lisp commands on demand, be it on button click or on some page event.
The macros and functions to look at are:

-   [`define-internal-page`](nyxt:describe-function?fn=%1Bdefine-internal-page "[MACRO] Define an `internal-page'."){.link
    target="_blank"} to create new pages.
-   [`buffer-load-internal-page-focus`](nyxt:describe-function?fn=%1Bbuffer-load-internal-page-focus "[FUNCTION] Make internal-page for NAME (a symbol) and switch to it."){.link
    target="_blank"} to either get or create the buffer for the page.
-   [`nyxt-url`](nyxt:describe-function?fn=%1Bnyxt-url "[FUNCTION] Generate a nyxt: URL from the given FUNCTION-NAME applied to ARGS."){.link
    target="_blank"} to reference the internal pages by their name.
-   [`define-internal-page-command`](nyxt:describe-function?fn=%1Bdefine-internal-page-command "[MACRO] Define a command called NAME creating an `internal-page'."){.link
    target="_blank"} to generate a mode-specific command loading the
    internal page.
-   [`define-internal-page-command-global`](nyxt:describe-function?fn=%1Bdefine-internal-page-command-global "[MACRO] Define a global command called NAME creating an `internal-page'."){.link
    target="_blank"} to generate a global command loading the internal
    page.

Using the facilities Nyxt provides, you can make a random number
generator page:

::: {style="position: relative"}
          
           Act on codeCopy
           Add To Auto-Config
           Try In Repl
          (define-internal-page-command-global random-number
        (&key (max 1000000))
        (buffer "*Random*")
      "Generates a random number on every reload."
      (spinneret:with-html-string
        (:h1 (princ-to-string (random max)))
        (:button.button :onclick
         (parenscript:ps
           (nyxt/parenscript:lisp-eval
            (:title "re-load/re-generate the random number")
            (reload-buffer buffer)))
         :title "Re-generate the random number again" "New number")))
:::

Several things to notice here:

-   Internal page command is much like a regular command in being a Lisp
    function that you can call either from the REPL or from the
    [`execute-command (Ctrl+space)`](nyxt:describe-function?fn=%1Bexecute-command "[COMMAND] Execute a command by name."){.link
    target="_blank"} menu.

-   -   With one important restriction: internal page commands should
        only have keyword arguments. Other argument types are not
        supported. This is to make them invocable through the URL they
        are assigned. For example, when you invoke the `random-number`
        command you\'ve written, you\'ll see the
        `nyxt:nyxt-user:random-number?max=%1B1000000` URL in the status
        buffer. The keyword argument is being seamlessly translated into
        a URL query parameter.
    -   There\'s yet another important restriction: the values you
        provide to the internal page command should be serializable to
        URLs. Which restricts the arguments to numbers, symbols, and
        strings, for instance.

-   Those commands should return the content of the page in their body,
    like internal schemes do.

-   If you want to return HTML, then
    [`with-html-string`](nyxt:describe-function?fn=%1Bspinneret%3Awith-html-string "[MACRO] Like WITH-HTML, but capture the output as a string."){.link
    target="_blank"} is your best friend, but no one restricts you from
    producing HTML in any other way, including simply writing it by hand
    ;)

-   `nyxt/ps:lisp-eval` is a Parenscript macro to request Nyxt to run
    arbitrary code. The signature is:
    `((&key (buffer '(nyxt:current-buffer)) title callback) &body form)`.
    You can bind it to a `<button>`\'s `onClick` event, for example.

If you\'re making an extension, you might find other macros more useful.
[`define-internal-page-command`](nyxt:describe-function?fn=%1Bdefine-internal-page-command "[MACRO] Define a command called NAME creating an `internal-page'."){.link
target="_blank"}, for example, defines a command to only be visible when
in the corresponding mode is enabled. Useful to separate the
context-specific commands from the universally useful ( `-global`) ones.
If there\'s a page that you\'d rather not have a command for, you can
still define it as:

::: {style="position: relative"}
          
           Act on codeCopy
           Add To Auto-Config
           Try In Repl
          (define-internal-page not-a-command
        nil
        (:title "*Hello*" :page-mode 'base-mode)
      "Hello there!")
:::

and use as:

::: {style="position: relative"}
          
           Act on codeCopy
           Add To Auto-Config
           Try In Repl
          (buffer-load-internal-page-focus 'not-a-command)
:::

See the slots and documentation of
[`internal-page`](nyxt:describe-class?class=%1Binternal-page "[CLASS] Each instance is a unique internal page generator for the"){.link
target="_blank"} to understand what you can pass to
[`define-internal-page`](nyxt:describe-function?fn=%1Bdefine-internal-page "[MACRO] Define an `internal-page'."){.link
target="_blank"}.
:::
:::

::: {#hooks .section .section}
::: {style="display: inline"}
## Hooks {#hooks style="display: inline"}

[\#](#hooks){.link}
:::

Hooks provide a powerful mechanism to tweak the behavior of various
events that occur in the context of windows, buffers, modes, etc.

A hook holds a list of *handlers*. Handlers are named and typed
functions. Each hook has a dedicated handler constructor.

Hooks can be \'run\', that is, their handlers are run according to the
[`combination`](nyxt:describe-slot?name=%1Bhooks%3Acombination&class=%1Bhooks%3Ahook "[SLOT of HOOK]"){.link
target="_blank"} slot of the hook. This combination is a function of the
handlers. Depending on the combination, a hook can run the handlers
either in parallel, or in order until one fails, or even *compose* them
(pass the result of one as the input of the next). The handler types
specify which input and output values are expected.

To add or delete a hook, you only need to know a couple of functions:

-   [`handler`](nyxt:describe-class?class=%1Bhooks%3Ahandler "[CLASS] Handlers are wrappers around functions used in typed hooks."){.link
    target="_blank"} a class to wrap hook handlers in.
-   [`add-hook`](nyxt:describe-function?fn=%1Bsera%3Aadd-hook "[FUNCTION] Add FN to the value of HOOK."){.link
    target="_blank"} (also known as `hooks:add-hook`) allows you to add
    a handler to a hook,for it to be invoked when the hook fires.
-   `nhooks:on` (also available as `hooks:on`) as a shorthand for the
    `nhooks:add-hook`.
-   [`remove-hook`](nyxt:describe-function?fn=%1Bsera%3Aremove-hook "[FUNCTION] Remove FN from the symbol value of HOOK."){.link
    target="_blank"} (also available as `hooks:remove-hook`) that
    removes the handler from a certain hook.
-   `nhooks:once-on` (also available as `hooks:once-on`) as a one-shot
    version of `nhooks:on` that removes the handler right after it\'s
    completed.

Many hooks are executed at different points in Nyxt, among others:

-   Global hooks, such as
    [`after-init-hook`](nyxt:describe-slot?name=%1Bafter-init-hook&class=%1Bbrowser "[SLOT of BROWSER] Auto-generated accessor function for slot AFTER-INIT-HOOK."){.link
    target="_blank"} or
    [`after-startup-hook`](nyxt:describe-slot?name=%1Bafter-startup-hook&class=%1Bbrowser "[SLOT of BROWSER] Auto-generated accessor function for slot AFTER-STARTUP-HOOK."){.link
    target="_blank"}.

-   Window- or buffer-related hooks.

-   -   [`window-make-hook`](nyxt:describe-slot?name=%1Bwindow-make-hook&class=%1Bwindow "[SLOT of WINDOW] Auto-generated accessor function for slot WINDOW-MAKE-HOOK."){.link
        target="_blank"} for when a new window is created.
    -   [`window-delete-hook`](nyxt:describe-slot?name=%1Bwindow-delete-hook&class=%1Bwindow "[SLOT of WINDOW] Auto-generated accessor function for slot WINDOW-DELETE-HOOK."){.link
        target="_blank"} for when a window is deleted.
    -   [`window-set-buffer-hook`](nyxt:describe-slot?name=%1Bwindow-set-buffer-hook&class=%1Bwindow "[SLOT of WINDOW] Auto-generated accessor function for slot WINDOW-SET-BUFFER-HOOK."){.link
        target="_blank"} for when the
        [`current-buffer`](nyxt:describe-function?fn=%1Bcurrent-buffer "[FUNCTION] Get the active buffer for WINDOW, or the active window otherwise."){.link
        target="_blank"} changes in the window.
    -   [`buffer-load-hook`](nyxt:describe-slot?name=%1Bbuffer-load-hook&class=%1Bnetwork-buffer "[SLOT of NETWORK-BUFFER]"){.link
        target="_blank"} for when there\'s a new page loading in the
        buffer.
    -   [`buffer-loaded-hook`](nyxt:describe-slot?name=%1Bbuffer-loaded-hook&class=%1Bnetwork-buffer "[SLOT of NETWORK-BUFFER] Auto-generated accessor function for slot BUFFER-LOADED-HOOK."){.link
        target="_blank"} for when this page is mostly done loading (some
        scripts/image/styles may not be fully loaded yet, so you may
        need to wait a bit after it fires.)
    -   [`request-resource-hook`](nyxt:describe-slot?name=%1Brequest-resource-hook&class=%1Bnetwork-buffer "[SLOT of NETWORK-BUFFER] Auto-generated accessor function for slot REQUEST-RESOURCE-HOOK."){.link
        target="_blank"} for when a new request happens. Allows
        redirecting and blocking requests, and is a good place to do
        something conditioned on the links being loaded.
    -   [`prompt-buffer-ready-hook`](nyxt:describe-slot?name=%1Bprompt-buffer-ready-hook&class=%1Bprompt-buffer "[SLOT of PROMPT-BUFFER] Auto-generated accessor function for slot PROMPT-BUFFER-READY-HOOK."){.link
        target="_blank"} fires when the prompt buffer is ready for user
        input. You may need to call
        [`all-ready-p`](nyxt:describe-function?fn=%1Bprompter%3Aall-ready-p "[FUNCTION] Return non-nil when all PROMPTER sources are ready."){.link
        target="_blank"} on the prompt to ensure all the sources it
        contains are ready too, and then you can safely set new inputs
        and select the necessary suggestions.

-   Commands :before and :after methods.

-   -   Try, for example,
        `(defmethod set-url :after (&key (prefill-current-url-p t)) ...)`
        to do something after the set-url finishes executing.

-   Modes \'enable\' and \'disable\' methods and their :before, :after,
    and :around methods.

-   Mode-specific hooks, like
    [`before-download-hook`](nyxt:describe-slot?name=%1Bnyxt%2Fmode%2Fdownload%3Abefore-download-hook&class=%1Bnyxt%2Fmode%2Fdownload%3Adownload-mode "[SLOT of DOWNLOAD-MODE] Auto-generated accessor function for slot BEFORE-DOWNLOAD-HOOK."){.link
    target="_blank"} and
    [`after-download-hook`](nyxt:describe-slot?name=%1Bnyxt%2Fmode%2Fdownload%3Aafter-download-hook&class=%1Bnyxt%2Fmode%2Fdownload%3Adownload-mode "[SLOT of DOWNLOAD-MODE] Auto-generated accessor function for slot AFTER-DOWNLOAD-HOOK."){.link
    target="_blank"} for
    [`download`](nyxt:describe-class?class=%1Bnyxt%2Fmode%2Fdownload%3Adownload "[CLASS] This class is used to represent a download within the *Downloads* buffer."){.link
    target="_blank"}.

For instance, if you want to force \'old.reddit.com\' over
\'www.reddit.com\', you can set a hook like the following in your
configuration file:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (defun old-reddit-handler (request-data)
      (let ((url (url request-data)))
        (setf (url request-data)
                (if (search "reddit.com" (quri.uri:uri-host url))
                    (progn
                     (setf (quri.uri:uri-host url) "old.reddit.com")
                     (log:info "Switching to old Reddit: ~s"
                               (render-url url))
                     url)
                    url)))
      request-data)

    (define-configuration web-buffer
      ((request-resource-hook
        (sera:add-hook %slot-default% 'old-reddit-handler))))
:::

(See
[`url-dispatching-handler`](nyxt:describe-function?fn=%1Burl-dispatching-handler "[FUNCTION] Return a `hook-request' handler apply its ACTION on the URLs conforming to TEST."){.link
target="_blank"} for a simpler way to achieve the same result.)

Or, if you want to set multiple handlers at once,

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (define-configuration web-buffer
      ((request-resource-hook
        (reduce #'sera:add-hook '(old-reddit-handler auto-proxy-handler)
                :initial-value %slot-default%))))
:::

Some hooks like the above example expect a return value, so it\'s
important to make sure we return
[`request-data`](nyxt:describe-class?class=%1Brequest-data "[CLASS] Representation of HTTP(S) request."){.link
target="_blank"} here. See the documentation of the respective hooks for
more details.
:::

::: {#data-paths-and-data-profiles .section .section}
::: {style="display: inline"}
## Data paths and data profiles {#data-paths-and-data-profiles style="display: inline"}

[\#](#data-paths-and-data-profiles){.link}
:::

Nyxt provides a uniform configuration interface for all data files
persisted to disk (bookmarks, cookies, etc.). To each file corresponds a
[`nyxt-file`](nyxt:describe-class?class=%1Bnyxt-file "[CLASS] All Nyxt files."){.link
target="_blank"} object. An
[`nyxt-profile`](nyxt:describe-class?class=%1Bnyxt-profile "[CLASS] With the default profile all data is persisted to the"){.link
target="_blank"} is a customizable object that helps define general
rules for data storage. Both nyxt-file and nyxt-profile compose, so
it\'s possible to define general rules for all files (even for those not
known in advance) while it\'s also possible to specialize some data
given an nyxt-profile.

The profile can be set from command line and from the configuration
file.You can list all known profiles (including the user-defined
profiles) with the `--list-profiles` command-line option.

The nyxt-files can be passed a hint from the `--with-file` command line
option, but each nyxt-file and profile rules are free to ignore it.

When a path ends with the `.gpg` extension, by default your GnuPG key is
used to decrypt and encrypt the file transparently. Refer to the GnuPG
documentation for how to set it up.

Note that the socket and the initialization nyxt-paths cannot be set in
your configuration (the socket is used before the initialization file is
loaded). Instead you can specify these paths from their respective
command-line option. You can instantiate a unique, separate Nyxt
instance when you provide a new socket path. This is particularly useful
in combination with profiles, say to develop Nyxt or extensions.

Example to create a development profile that stores all data in
`/tmp/nyxt` and stores bookmark in an encrypted file:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (define-class dev-profile (nyxt-profile)
                  ((files:name :initform "nyxt-dev"))
                  (:documentation "Development profile."))

    (defmethod files:resolve ((profile dev-profile) (path nyxt-file))
      "Expand all data paths inside a temporary directory."
      (sera:path-join
       (files:expand (make-instance 'nyxt-temporary-directory))
       (uiop/pathname:relativize-pathname-directory (call-next-method))))

    (defmethod files:resolve ((profile dev-profile) (file history-file))
      "Persist history to default location."
      (files:resolve (global-profile) file))

    (define-configuration web-buffer
      "Make new profile the default."
      ((profile
        (make-instance
         (or (find-profile-class (getf *options* :profile))
             'dev-profile)))))
:::

Then you can start a separate instance of Nyxt using this profile with
`nyxt --profile dev --socket /tmp/nyxt.socket`.
:::

::: {#password-management .section .section}
::: {style="display: inline"}
## Password management {#password-management style="display: inline"}

[\#](#password-management){.link}
:::

Nyxt provides a uniform interface to some password managers including
[KeepassXC](https://keepassxc.org/) and [Password
Store](https://www.passwordstore.org/). The supported installed password
manager is automatically detected.See the `password-interface` buffer
slot for customization.

You may use the
[`define-configuration`](nyxt:describe-function?fn=%1Bdefine-configuration "[MACRO] Helper macro to customize the class slots of the CLASSES."){.link
target="_blank"} macro with any of the password interfaces to configure
them. Please make sure to use the package prefixed class name/slot
designators within the
[`define-configuration`](nyxt:describe-function?fn=%1Bdefine-configuration "[MACRO] Helper macro to customize the class slots of the CLASSES."){.link
target="_blank"}.

-   [`save-new-password (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fpassword%3Asave-new-password "[COMMAND] Save password to password interface."){.link
    target="_blank"}: Query for name and new password to persist in the
    database.
-   [`copy-password (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fpassword%3Acopy-password "[COMMAND] Query password and save to clipboard."){.link
    target="_blank"}: Query password and save to clipboard.

::: {#keepassxc-support .section .section}
::: {style="display: inline"}
### KeePassXC support {#keepassxc-support style="display: inline"}

[\#](#keepassxc-support){.link}
:::

The interface for KeePassXC should cover most use-cases for KeePassXC,
as it supports password database locking with

-   [`master-password`](nyxt:describe-slot?name=%1Bpassword%3Amaster-password&class=%1Bpassword%3Akeepassxc-interface "[SLOT of KEEPASSXC-INTERFACE] Auto-generated accessor function for slot MASTER-PASSWORD."){.link
    target="_blank"},
-   [`key-file`](nyxt:describe-slot?name=%1Bpassword%3Akey-file&class=%1Bpassword%3Akeepassxc-interface "[SLOT of KEEPASSXC-INTERFACE] Auto-generated accessor function for slot KEY-FILE."){.link
    target="_blank"},
-   and
    [`yubikey-slot`](nyxt:describe-slot?name=%1Bpassword%3Ayubikey-slot&class=%1Bpassword%3Akeepassxc-interface "[SLOT of KEEPASSXC-INTERFACE] Auto-generated accessor function for slot YUBIKEY-SLOT."){.link
    target="_blank"}

To configure KeePassXC interface, you might need to add something like
this snippet to your config:

::: {style="position: relative"}
          
           Act on codeCopy
           Add To Auto-Config
           Try In Repl
          (defmethod initialize-instance :after
               ((interface password:keepassxc-interface)
                &key &allow-other-keys)
      "It's obviously not recommended to set master password here,
    as your config is likely unencrypted and can reveal your password to someone
    peeking at the screen."
      (setf (password:password-file interface)
              "/path/to/your/passwords.kdbx"
            (password:key-file interface) "/path/to/your/keyfile"
            (password:yubikey-slot interface) "1:1111"))

    (define-configuration nyxt/mode/password:password-mode
      ((nyxt/mode/password:password-interface
        (make-instance 'password:keepassxc-interface))))

    (define-configuration buffer
      ((default-modes
        (append (list 'nyxt/mode/password:password-mode) %slot-value%))))
:::
:::
:::

::: {#appearance .section .section}
::: {style="display: inline"}
## Appearance {#appearance style="display: inline"}

[\#](#appearance){.link}
:::

Much of the visual style can be configured by the user. You can use the
facilities provided by
[`theme`](nyxt:describe-package?package=%1B%3Atheme "[PACKAGE]"){.link
target="_blank"} and
[`browser theme slot`](nyxt:describe-slot?name=%1Btheme&class=%1Bbrowser "[SLOT of BROWSER] Auto-generated accessor function for slot THEME."){.link
target="_blank"}. The simplest option would be to use a built-in theme:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (define-configuration browser
      ((theme theme:+dark-theme+ :doc "Setting dark theme.
    The default is theme:+light-theme+.")))
:::

There\'s also an option of creating a custom theme. For example, to set
a theme to a midnight-like one, you can add this snippet to your
configuration file:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (define-configuration browser
      ((theme
        (make-instance 'theme:theme :background-color "black"
                       :action-color "#37a8e4" :primary-color "#808080"
                       :secondary-color "darkgray" :text-color
                       "lightgray" :contrast-text-color "black")
        :doc
        "You can omit the colors you like in default theme, and they will stay as they were.")))
:::

This, on the next restart of Nyxt, will repaint all the interface
elements into a dark-ish theme.

As a more involved theme example, here\'s how one can redefine most of
the semantic colors Nyxt uses to be compliant with Solarized Light
theme:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (define-configuration browser
      ((theme
        (make-instance 'theme:theme :background-color "#eee8d5"
                       :action-color "#268bd2" :primary-color "#073642"
                       :secondary-color "#586e75" :success-color
                       "#2aa198" :warning-color "#dc322f"
                       :highlight-color "#d33682" :codeblock-color
                       "#6c71c4" :text-color "#002b36"
                       :contrast-text-color "#fdf6e3")
        :doc
        "Covers all the semantic groups (warning-color, codeblock-color etc.)
    Note that you can also define more nuanced colors, like warning-color+, so
    that the interface gets even nicer. Otherwise Nyxt generates the missing colors
    automatically, which should be good enough... for most cases.")))
:::

As an alternative to the all-encompassing themes, you can alter the
style of every individual class controlling Nyxt interface elements. All
such classes have a
[`style`](nyxt:describe-function?fn=%1Bstyle "[FUNCTION] Auto-generated accessor function for slot STYLE."){.link
target="_blank"} slot that you can configure with your own CSS like
this:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (define-configuration nyxt/mode/style:dark-mode
      ((style
        (theme:themed-css (theme *browser*)
          `(* :background-color ,theme:background "!important"
              :background-image none "!important" :color "red"
              "!important")
          `(a :background-color ,theme:background "!important"
            :background-image none "!important" :color "#AAAAAA"
            "!important"))))
      :doc
      "Notice the use of theme:themed-css for convenient theme color injection.")
:::

This snippet alters the
[`style`](nyxt:describe-slot?name=%1Bstyle&class=%1Bnyxt%2Fmode%2Fstyle%3Adark-mode "[SLOT of DARK-MODE] Auto-generated accessor function for slot STYLE."){.link
target="_blank"} of Nyxt dark mode to have a more theme-compliant
colors, using the `theme:themed-css` macro (making all the theme colors
you\'ve configured earlier available as variables like
`theme:on-primary`.)

::: {#status-buffer-appearance .section .section}
::: {style="display: inline"}
### Status buffer appearance {#status-buffer-appearance style="display: inline"}

[\#](#status-buffer-appearance){.link}
:::

You can customize the layout and styling of
[`status-buffer`](nyxt:describe-class?class=%1Bstatus-buffer "[CLASS]"){.link
target="_blank"} using the methods it uses for layout. These methods
are:

[`format-status`](nyxt:describe-function?fn=%1Bformat-status "[FUNCTION] Render all of the STATUS."){.link target="_blank"}
:   General layout of the status buffer, including the parts it consists
    of.

[`format-status-buttons`](nyxt:describe-function?fn=%1Bformat-status-buttons "[FUNCTION] Render interactive buttons to HTML string."){.link target="_blank"}
:   The (\"Back\", \"Forward\", \"Reload\") buttons section.

[`format-status-url`](nyxt:describe-function?fn=%1Bformat-status-url "[FUNCTION] Formats the currently open URL for the STATUS buffer."){.link target="_blank"}
:   The current URL display section.

[`format-status-tabs`](nyxt:describe-function?fn=%1Bformat-status-tabs "[FUNCTION] Render the open buffers to HTML string suitable for STATUS."){.link target="_blank"}
:   Tab listing.

[`format-status-modes`](nyxt:describe-function?fn=%1Bformat-status-modes "[FUNCTION] Render the enabled modes to HTML string."){.link target="_blank"}
:   List of modes.

To complement the layout produced by these `format-*` functions, you
might need to add more rules or replace the
[`style of status buffer`](nyxt:describe-slot?name=%1Bstyle&class=%1Bstatus-buffer "[SLOT of STATUS-BUFFER] Auto-generated accessor function for slot STYLE."){.link
target="_blank"}.
:::
:::

::: {#scripting .section .section}
::: {style="display: inline"}
## Scripting {#scripting style="display: inline"}

[\#](#scripting){.link}
:::

You can evaluate code from the command line with `--eval` and `--load`.
From a shell:

::: {style="position: relative"}
        
         Act on codeSpinneret::Copy
         Funcall
        $ nyxt --no-config --eval '+version+' 
      --load my-lib.lisp --eval '(format t "Hello ~a!~&" (my-lib:my-world))'
:::

You can evaluate multiple \--eval and \--load in a row, they are
executed in the order they appear.

You can also evaluate a Lisp file from the Nyxt interface with the
[`load-file (Ctrl+O)`](nyxt:describe-function?fn=%1Bload-file "[COMMAND] Load the prompted Lisp file."){.link
target="_blank"} command. For convenience,
[`load-config-file (unbound)`](nyxt:describe-function?fn=%1Bload-config-file "[COMMAND] Load or reload the CONFIG-FILE."){.link
target="_blank"} (re)loads your initialization file.

You can even make scripts. Here is an example foo.lisp:

::: {style="position: relative"}
        
         Act on codeSpinneret::Copy
         Funcall
        #!/bin/sh
    #|
    exec nyxt --script "$0"
    |#

    ;; Your code follows:
    (format t "~a~&" +version+)
:::

\--eval and \--load can be commanded to operate over an existing
instance instead of a separate instance that exits immediately.

The
[`remote-execution-p`](nyxt:describe-slot?name=%1Bremote-execution-p&class=%1Bbrowser "[SLOT of BROWSER] Auto-generated accessor function for slot REMOTE-EXECUTION-P."){.link
target="_blank"} of the remote instance must be non-nil:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (define-configuration browser
      ((remote-execution-p t)))
:::

To let know a private instance of Nyxt to load a foo.lisp script and run
its `foo`function:

::: {style="position: relative"}
        
         Act on codeSpinneret::Copy
         Funcall
        nyxt --profile nosave --remote --load foo.lisp --eval '(foo)' --quit
:::

Note that `--quit`at the end of each Nyxt CLI call here. If you don\'t
provide `--quit` when dealing with a remote instance, it will go into a
REPL mode, allowing an immediate communication with an instance:

       nyxt --remote
    (echo "~s" (+ 1 2)) ;; Shows '3' in the message area of remote Nyxt
:::

::: {#user-scripts .section .section}
::: {style="display: inline"}
## User scripts {#user-scripts style="display: inline"}

[\#](#user-scripts){.link}
:::

User scripts are a conventional and lightweight way to run arbitrary
JavaScript code on some set of pages/conditions. While not as powerful
as either WebExtensions on Lisp-native extensions to Nyxt, those hook
into the tenderer inner working and allow you to change the page and
JavaScript objects associated to it.

As an example, you can remove navbars from all the pages you visit with
this small configuration snippet (note that you\'d need to have
[`user-script-mode`](nyxt:describe-class?class=%1Bnyxt%2Fmode%2Fuser-script%3Auser-script-mode "[CLASS] Mode to manage user scripts such as GreaseMonkey scripts."){.link
target="_blank"} in your
[`buffer default-modes`](nyxt:describe-function?fn=%1Bdefault-modes "[FUNCTION] BUFFER's default modes."){.link
target="_blank"} ):

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (define-configuration web-buffer
      "Enable user-script-mode, if you didn't already."
      ((default-modes
        (pushnew 'nyxt/mode/user-script:user-script-mode %slot-value%))))

    (define-configuration nyxt/mode/user-script:user-script-mode
      ((nyxt/mode/user-script:user-scripts
        (list
         (make-instance 'nyxt/mode/user-script:user-script :code
                        "// ==UserScript==
                                  // @name          No navbars!
                                  // @description   A simple script to remove navbars
                                  // @run-at        document-end
                                  // @include       http://*/*
                                  // @include       https://*/*
                                  // @noframes
                                  // ==/UserScript==

                                  var elem = document.querySelector(\"header\") || document.querySelector(\"nav\");
                                  if (elem) {
                                  elem.parentNode.removeChild(elem);
                                  }"))
        :doc "Alternatively, save the code to some file and use
    :base-path #p\"/path/to/our/file.user.js\".
    Or fetch a remote script with
    url (quri:uri \"https://example.com/script.user.js\")")))
:::

[Greasemonkey documentation](https://wiki.greasespot.net/Metadata_Block)
lists all the possible properties that a user script might have. To Nyxt
implementation, only those are meaningful:

\@include and [`include`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fuser-script%3Ainclude "[FUNCTION] Auto-generated accessor function for slot INCLUDE."){.link target="_blank"}
:   Sets the URL pattern to enable this script for. Follows the pattern
    `scheme://host/path`, where scheme is either a literal scheme or and
    asterisk (matching any scheme), and host and path are any valid
    characters plus asterisks (matching any set of characters) anywhere.

\@match
:   Same as \@include.

\@exclude and [`exclude`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fuser-script%3Aexclude "[FUNCTION] Auto-generated accessor function for slot EXCLUDE."){.link target="_blank"}
:   Similar to \@include, but rather disables the script for the
    matching pages.

\@noframes and [`all-frames-p`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fuser-script%3Aall-frames-p "[FUNCTION] Auto-generated accessor function for slot ALL-FRAMES-P."){.link target="_blank"}
:   When present, disables the script for all the frames but toplevel
    ones. When absent, injects the script everywhere. The Lisp-side
    [`all-frames-p`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fuser-script%3Aall-frames-p "[FUNCTION] Auto-generated accessor function for slot ALL-FRAMES-P."){.link
    target="_blank"}works in an opposite way.

\@run-at and [`run-at`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Fuser-script%3Arun-at "[FUNCTION] Auto-generated accessor function for slot RUN-AT."){.link target="_blank"}
:   When to run a script. Allowed values: document-start, document-end,
    document-idle (in Nyxt implementation, same as document-end).

\@require
:   Allows including arbitrary JS files hosted on the Internet or loaded
    from the same place as the script itself. Neat for including some JS
    libraries, like jQuery.
:::

::: {#headless-mode .section .section}
::: {style="display: inline"}
## Headless mode {#headless-mode style="display: inline"}

[\#](#headless-mode){.link}
:::

Similarly to Nyxt\'s scripting functionality, headless mode runs without
a graphical user interface. Possible use-cases for this mode are web
scraping, automations and web page analysis.

To enable headless mode, simply start Nyxt with the `--headless` CLI
flag and provide a script file to serve as the configuration file:

::: {style="position: relative"}
        
         Act on codeSpinneret::Copy
         Funcall
        nyxt --headless --config /path/to/your/headless-config.lisp
:::

Note that you pass it a *configuration file*---headless mode is only
different from the regular Nyxt functions in that it has no GUI, and is
all the same otherwise, contrary to all the seeming similarities to the
`--script` flag usage.

The example below showcases frequent idioms that are found in the
mode\'s configuration file:

::: {style="position: relative"}
        
         Act on codeSpinneret::Copy
         Funcall
        #!/bin/sh
    #|
    exec nyxt --headless --no-auto-config --profile nosave --config "$0"
    |#

    (define-configuration browser
      "Disable session restoration to speed up startup and get more reproducible
    behavior."
      ((restore-session-on-startup-p nil)))

    (define-configuration browser
      "Load the URL of Nyxt repository by default in all new buffers.
    Alternatively, call buffer-load in after-startup-hook."
      ((default-new-buffer-url
        (quri.uri:uri "https://github.com/atlas-engineer/nyxt"))))

    (hooks:on (after-startup-hook *browser*) (browser)
      ;; Once the page's done loading, do your thing.
      (hooks:once-on (buffer-loaded-hook (current-buffer)) (buffer)
        ;; It's sometimes necessary to sleep, as `buffer-loaded-hook' fires when the
        ;; page is loaded, which does not mean that all the resources and scripts
        ;; are done loading yet. Give it some time there.
        (sleep 0.5)
        ;; All the Nyxt reporting happens in headless mode, so you may want to log
        ;; it with `echo' and `echo-warning'.
        (echo "Nyxt GitHub repo open.")
        ;; Updating the `document-model' so that it includes the most relevant
        ;; information about the page.
        (nyxt:update-document-model)
        ;; Click the star button.
        (nyxt/dom:click-element
         (elt (clss:select "[aria-label=\"Star this repository\"]"
                           (document-model buffer))
                           0))
        (echo "Clicked the star.")
        ;; It's good tone to `nyxt:quit' after you're done, but if you use nyxt
        ;; --no-socket, you don't have to. Just be ready for some RAM eating :)
        (nyxt:quit)))
:::

The contents of headless-config.lisp feature configuration forms that
make Nyxt perform some actions to the opened pages and/or on certain
hooks. Things you\'d most probably want to put there are:

-   Hook bindings, using the
    [`nhooks`](nyxt:describe-package?package=%1Bnhooks "[PACKAGE] A hook is an instance of the `nhooks:hook' class."){.link
    target="_blank"} library and hooks provided by Nyxt.

-   Operations on the page. Check the
    [`nyxt/dom`](nyxt:describe-package?package=%1Bnyxt%2Fdom "[PACKAGE] Nyxt-specific DOM classes and functions operating on them."){.link
    target="_blank"} library and the
    [`document-model`](nyxt:describe-function?fn=%1Bdocument-model "[FUNCTION] Auto-generated accessor function for slot DOCUMENT-MODEL."){.link
    target="_blank"} method.

-   -   The
        [`document-model`](nyxt:describe-function?fn=%1Bdocument-model "[FUNCTION] Auto-generated accessor function for slot DOCUMENT-MODEL."){.link
        target="_blank"} method has a reasonably fresh copy of the page
        DOM (Document Object Model, reflecting the dynamic structure of
        the page). It is a
        [`Plump`](nyxt:describe-package?package=%1Bplump "[PACKAGE]"){.link
        target="_blank"} DOM, which means that all
        [`Plump`](nyxt:describe-package?package=%1Bplump "[PACKAGE]"){.link
        target="_blank"} (and
        [`CLSS`](nyxt:describe-package?package=%1Bclss "[PACKAGE]"){.link
        target="_blank"}) functions can be used on it.
    -   [`update-document-model`](nyxt:describe-function?fn=%1Bupdate-document-model "[FUNCTION] Update BUFFER's `document-model' with the page source augmented with Nyxt"){.link
        target="_blank"} is a function to force DOM re-parsing for the
        cases when you consider the current
        [`document-model`](nyxt:describe-function?fn=%1Bdocument-model "[FUNCTION] Auto-generated accessor function for slot DOCUMENT-MODEL."){.link
        target="_blank"} too outdated.
    -   [`select`](nyxt:describe-function?fn=%1Bclss%3Aselect "[FUNCTION] Match the given selector against the root-node and possibly all its children."){.link
        target="_blank"} is a CLSS function to find elements using CSS
        selectors (a terse notation for web page element description).
    -   `clss:ordered-select` is the same as
        [`select`](nyxt:describe-function?fn=%1Bclss%3Aselect "[FUNCTION] Match the given selector against the root-node and possibly all its children."){.link
        target="_blank"}, except it guarantees that all the elements are
        returned in a depth-first traversal order.
    -   [`click-element`](nyxt:describe-function?fn=%1Bnyxt%2Fdom%3Aclick-element "[FUNCTION] Click the ELEMENT (Lisp object) on the page with JS."){.link
        target="_blank"} to programmatically click a certain element
        (including the ones returned by
        [`select`](nyxt:describe-function?fn=%1Bclss%3Aselect "[FUNCTION] Match the given selector against the root-node and possibly all its children."){.link
        target="_blank"}.)
    -   [`focus-select-element`](nyxt:describe-function?fn=%1Bnyxt%2Fdom%3Afocus-select-element "[FUNCTION] Focus the element matching ELEMENT on the page."){.link
        target="_blank"} to focus an input field, for example.
    -   [`check-element`](nyxt:describe-function?fn=%1Bnyxt%2Fdom%3Acheck-element "[FUNCTION] Toggle (to VALUE) the checkbox/radio button matching ELEMENT on the page."){.link
        target="_blank"} to check a checkbox or a radio button.
    -   [`select-option-element`](nyxt:describe-function?fn=%1Bnyxt%2Fdom%3Aselect-option-element "[FUNCTION] Select one of the <option> elements (ELEMENT) in PARENT <select>."){.link
        target="_blank"} to select an option from the `<select>` element
        options.

Additionally, headless mode gracefully interacts with other CLI toggles
the Nyxt has:

-   `--headless` itself! Notice that you can debug your script by
    omitting this CLI flag. When you\'re confident enough about it, put
    it back in. A good debugging tip, isn\'t it?
-   `--no-socket` flag allows starting as many Nyxt instances as your
    machine can handle. Useful to parallelize computations.
-   `--profile nosave` to not pollute your history and cache with the
    script-accessed pages.
:::

::: {#built-in-repl .section .section}
::: {style="display: inline"}
## Built-in REPL {#built-in-repl style="display: inline"}

[\#](#built-in-repl){.link}
:::

Nyxt has a built-in REPL, available with
[`repl (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Arepl "[COMMAND] Create a Nyxt REPL buffer."){.link
target="_blank"} command.The REPL can be used to try out some code
snippets for automation or quickly make some Lisp calculations. All the
packages Nyxt depends on are available in REPL with convenient
nicknames, and all the code is evaluated in
[`nyxt-user`](nyxt:describe-package?package=%1B%3Anyxt-user "[PACKAGE] Package left for the user to fiddle with.  If the"){.link
target="_blank"} package.

Once the REPL is open, there\'s only one input cell visible. This cell,
always present at the bottom of the screen, adds new cells to the
multi-pane interface of Nyxt REPL. You can type in
`(print "Hello, Nyxt!")` and press C-return to evaluate the cell. A new
cell will appear at the top of the buffer, with input area containing
familiar code, with some `v332 = "Hello, Nyxt!"` variable assignment,
and with a verbatim text outputted by your code:

       Hello, Nyxt!

This cell-based code evaluation is the basis of the Nyxt REPL. For more
features, see
[`REPL mode documentation`](nyxt:describe-package?package=%1B%3Anyxt%2Fmode%2Frepl "[PACKAGE] Common Lisp REPL mode for interactive programming."){.link
target="_blank"}.

::: {#extending-the-repl .section .section}
::: {style="display: inline"}
### Extending the REPL {#extending-the-repl style="display: inline"}

[\#](#extending-the-repl){.link}
:::

Nyxt REPL is made to be extensible and allow to make custom cell types
with their own display and functionality. The two cell types provided by
default are:

-   [`lisp-cell`](nyxt:describe-class?class=%1Bnyxt%2Fmode%2Frepl%3Alisp-cell "[CLASS] Cell intended for Lisp expressions evaluation."){.link
    target="_blank"}
-   and
    [`shell-cell`](nyxt:describe-class?class=%1Bnyxt%2Fmode%2Frepl%3Ashell-cell "[CLASS] A cell type for shell commands."){.link
    target="_blank"}

Both of these serve as examples of cell extension, but it may be more
illuminating to create one of a different type from the default ones. A
commentary cell, for example---the type of cell one can use as an
annotation to other cells.

First, define a new
[`cell`](nyxt:describe-class?class=%1Bnyxt%2Fmode%2Frepl%3Acell "[CLASS] The universal REPL cell, allowing to customize the REPL."){.link
target="_blank"} type:

::: {style="position: relative"}
          
           Act on codeCopy
           Add To Auto-Config
           Try In Repl
          (define-class comment-cell (nyxt/mode/repl:cell)
                  ((name "Commentary")) (:export-class-name-p t)
                  (:export-accessor-names-p t))
:::

There are methods of
[`cell`](nyxt:describe-class?class=%1Bnyxt%2Fmode%2Frepl%3Acell "[CLASS] The universal REPL cell, allowing to customize the REPL."){.link
target="_blank"} that can be redefined for a better display:

-   [`evaluate`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Aevaluate "[FUNCTION] Evaluate CELL and get its results."){.link
    target="_blank"} as a function to get results from the cell.
-   [`suggest`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Asuggest "[FUNCTION] Get a single most intuitive suggestion string for CELL contents."){.link
    target="_blank"} for choosing the most intuitive content to paste
    into the cell.
-   [`render-input`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Arender-input "[FUNCTION] Generate HTML for the input area of the CELL."){.link
    target="_blank"} as the one rendering the input area for the cell.
-   [`render-actions`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Arender-actions "[FUNCTION] Generate HTML for the `actions' of the CELL."){.link
    target="_blank"}, allowing to render a custom set of actions.
-   And
    [`render-results`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Arender-results "[FUNCTION] Generate HTML for the `results' and `output' of the CELL."){.link
    target="_blank"} to show cell results (the immediate values
    [`evaluation`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Aevaluate "[FUNCTION] Evaluate CELL and get its results."){.link
    target="_blank"} returns) and output (the text printed out while
    [`evaluating`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Aevaluate "[FUNCTION] Evaluate CELL and get its results."){.link
    target="_blank"} the cell).
-   And, in case none of those fits well,
    [`render-cell`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Arender-cell "[FUNCTION] Generate HTML for the CELL."){.link
    target="_blank"} to override all the rendering code.

The easiest thing is
[`render-input`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Arender-input "[FUNCTION] Generate HTML for the input area of the CELL."){.link
target="_blank"}: it\'s already defined as an input field updating the
cell
[`input`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Ainput "[FUNCTION] Auto-generated accessor function for slot INPUT."){.link
target="_blank"} at every keypress. The only change to it that is needed
for the commentary cell is to render as a \<pre\> tag when marked
[`ready-p`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Aready-p "[FUNCTION] Auto-generated accessor function for slot READY-P."){.link
target="_blank"}:

::: {style="position: relative"}
          
           Act on codeCopy
           Add To Auto-Config
           Try In Repl
          (defmethod nyxt/mode/repl:render-input ((cell comment-cell))
      "Render as a pre tag when ready, render as default input otherwise."
      (if (nyxt/mode/repl:ready-p cell)
          (spinneret:with-html-string
            (:pre (input cell)))
          (call-next-method)))
:::

[`render-results`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Arender-results "[FUNCTION] Generate HTML for the `results' and `output' of the CELL."){.link
target="_blank"} is another method useless for comment cell. It can
safely return the empty string:

::: {style="position: relative"}
          
           Act on codeCopy
           Add To Auto-Config
           Try In Repl
          (defmethod nyxt/mode/repl:render-results ((cell comment-cell))
      (declare (ignore cell))
      "")
:::

[`render-actions`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Arender-actions "[FUNCTION] Generate HTML for the `actions' of the CELL."){.link
target="_blank"} should stay as it is, because it produces an aesthetic
set of buttons near the input. No need to tweak it in this case.

Last but not least,
[`evaluate`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Aevaluate "[FUNCTION] Evaluate CELL and get its results."){.link
target="_blank"}. This method should produce the
[`results`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Aresults "[FUNCTION] Auto-generated accessor function for slot RESULTS."){.link
target="_blank"} and
[`output`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Aoutput "[FUNCTION] Auto-generated accessor function for slot OUTPUT."){.link
target="_blank"} of the cell. The REPL infrastructure sets
[`ready-p`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Aready-p "[FUNCTION] Auto-generated accessor function for slot READY-P."){.link
target="_blank"}to T when the evaluation ends, which enables the \<pre\>
rendering. Given that comment cells produce no result
[`evaluate`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Aevaluate "[FUNCTION] Evaluate CELL and get its results."){.link
target="_blank"} can stay empty:

::: {style="position: relative"}
          
           Act on codeCopy
           Add To Auto-Config
           Try In Repl
          (defmethod nyxt/mode/repl:evaluate ((cell comment-cell))
      (declare (ignore cell)))
:::

After all of these methods are defined in the configuration file and
Nyxt restarted, invoking
[`repl (unbound)`](nyxt:describe-function?fn=%1Bnyxt%2Fmode%2Frepl%3Arepl "[COMMAND] Create a Nyxt REPL buffer."){.link
target="_blank"} and pressing the `Add a cell` button will allow to
create a new comment cell.

Note that the display of the comment cell is not exactly concise. But
making it better is left as an exercise to the reader.
:::
:::

::: {#advanced-configuration .section .section}
::: {style="display: inline"}
## Advanced configuration {#advanced-configuration style="display: inline"}

[\#](#advanced-configuration){.link}
:::

While
[`define-configuration`](nyxt:describe-function?fn=%1Bdefine-configuration "[MACRO] Helper macro to customize the class slots of the CLASSES."){.link
target="_blank"} is convenient, it is mostly restricted to class slot
configuration. If you want to do anything else on class instantiation,
you\'ll have to specialize the lower-level
[`customize-instance`](nyxt:describe-function?fn=%1Bcustomize-instance "[FUNCTION] Specialize this method to customize the default values and"){.link
target="_blank"} generic function. Example:

::: {style="position: relative"}
        
         Act on codeCopy
         Add To Auto-Config
         Try In Repl
        (defmethod customize-instance ((buffer buffer) &key)
      (echo "Buffer ~a created." buffer))
:::

All classes with metaclass
[`user-class`](nyxt:describe-class?class=%1Buser-class "[CLASS] User-configurable value class."){.link
target="_blank"} call
[`customize-instance`](nyxt:describe-function?fn=%1Bcustomize-instance "[FUNCTION] Specialize this method to customize the default values and"){.link
target="_blank"} on instantiation, after
[`initialize-instance`](nyxt:describe-function?fn=%1Binitialize-instance "[FUNCTION]"){.link
target="_blank"} ` :after`. The primary method is reserved to the user,
however the `:after` method is reserved to the Nyxt core to finalize the
instance.
:::

::: {#extensions .section .section}
::: {style="display: inline"}
## Extensions {#extensions style="display: inline"}

[\#](#extensions){.link}
:::

To install an extension, copy inside the
[`*extensions-directory*`](nyxt:describe-variable?variable=%1B%2Aextensions-directory%2A "[VARIABLE] The directory where extensions are stored."){.link
target="_blank"} (default to `~/.local/share/nyxt/extensions`).

Extensions are regular Common Lisp systems.

A catalog of extensions is available in the `document/EXTENSIONS.org`
file in the source repository.
:::

::: {#troubleshooting .section .section}
::: {style="display: inline"}
## Troubleshooting {#troubleshooting style="display: inline"}

[\#](#troubleshooting){.link}
:::

::: {#debugging-and-reporting-errors .section .section}
::: {style="display: inline"}
### Debugging and reporting errors {#debugging-and-reporting-errors style="display: inline"}

[\#](#debugging-and-reporting-errors){.link}
:::

If you experience hangs or errors you can reproduce, you can use the
[`toggle-debug-on-error (unbound)`](nyxt:describe-function?fn=%1Btoggle-debug-on-error "[COMMAND] Toggle Nyxt-native debugging."){.link
target="_blank"} command to enable Nyxt-native debugger and see the
reasons of these. Based on this information, you can report a bug using
[`report-bug (unbound)`](nyxt:describe-function?fn=%1Breport-bug "[COMMAND] Report the bug on Nyxt GitHub, filling all the guessable information in the process."){.link
target="_blank"}.

You can also try to start the browser with the `--failsafe` command line
option and see if you can reproduce your issue then. If not, then the
issue is most likely due to your configuration, an extension, or some
corrupt data file like the history.

Note that often errors, hangs, and crashes happen on the side of
renderer and thus are not visible to the Nyxt-native debugger and
fixable on the side of Nyxt. See below.
:::

::: {#playing-videos .section .section}
::: {style="display: inline"}
### Playing videos {#playing-videos style="display: inline"}

[\#](#playing-videos){.link}
:::

Nyxt delegates video support to third-party plugins.

When using the WebKitGTK backends, GStreamer and its plugins are
leveraged. Depending on the video, you will need to install some of the
following packages:

-   gst-libav
-   gst-plugins-bad
-   gst-plugins-base
-   gst-plugins-good
-   gst-plugins-ugly

On Debian-based systems, you might be looking for (adapt the version
numbers):

-   libgstreamer1.0-0
-   gir1.2-gst-plugins-base-1.0

For systems from the Fedora family:

-   gstreamer1-devel
-   gstreamer1-plugins-base-devel

After the desired plugins have been installed, clear the GStreamer cache
at `~/.cache/gstreamer-1.0` and restart Nyxt.
:::

::: {#website-crashes .section .section}
::: {style="display: inline"}
### Website crashes {#website-crashes style="display: inline"}

[\#](#website-crashes){.link}
:::

If some websites systematically crash, try to install all the required
GStreamer plugins as mentioned in the \'Playing videos\' section.
:::

::: {#input-method-support-cjk-etc .section .section}
::: {style="display: inline"}
### Input method support (CJK, etc.) {#input-method-support-cjk-etc. style="display: inline"}

[\#](#input-method-support-cjk-etc){.link}
:::

Depending on your setup, you might have to set some environment
variables or run some commands before starting Nyxt, for instance

::: {style="position: relative"}
          
           Act on codeSpinneret::Copy
           Funcall
          GTK_IM_MODULE=xim
    XMODIFIERS=@im=ibus
    ibus --daemonize --replace --xim
:::

You can persist this change by saving the commands in your `.xprofile`
or similar.
:::

::: {#hidpi-displays .section .section}
::: {style="display: inline"}
### HiDPI displays {#hidpi-displays style="display: inline"}

[\#](#hidpi-displays){.link}
:::

The entire UI may need to be scaled up on HiDPI displays.

When using the WebKitGTK renderer, export the environment variable below
before starting Nyxt. Note that `GDK_DPI_SCALE` (not to be confused with
`GDK_SCALE`) scales text only, so tweaking it may be undesirable.

         export GDK_SCALE=2
    nyxt
:::

::: {#stumpwm-mouse-scroll .section .section}
::: {style="display: inline"}
### StumpWM mouse scroll {#stumpwm-mouse-scroll style="display: inline"}

[\#](#stumpwm-mouse-scroll){.link}
:::

If the mouse scroll does not work for you, see the [StumpWM
FAQ](https://github.com/stumpwm/stumpwm/wiki/FAQ#my-mouse-wheel-doesnt-work-with-gtk3-applications-add-the-following-to)
for a fix.
:::

::: {#blank-webkit-web-views .section .section}
::: {style="display: inline"}
### Blank WebKit web-views {#blank-webkit-web-views style="display: inline"}

[\#](#blank-webkit-web-views){.link}
:::

If you are experiencing problems with blank web-views on some sites you
can try to disable compositing. To disable compositing from your
initialization file, you can do the following:

::: {style="position: relative"}
          
           Act on codeCopy
           Add To Auto-Config
           Try In Repl
          (setf (uiop/os:getenv "WEBKIT_DISABLE_COMPOSITING_MODE") "1")
:::
:::

::: {#missing-cursor-icons .section .section}
::: {style="display: inline"}
### Missing cursor icons {#missing-cursor-icons style="display: inline"}

[\#](#missing-cursor-icons){.link}
:::

If you are having issues with the cursor not changing when hovering over
buttons or links, it might be because Nyxt can\'t locate your cursor
theme. To fix that, try adding the following to your `.bash_profile` or
similar:

::: {style="position: relative"}
          
           Act on codeSpinneret::Copy
           Funcall
          export XCURSOR_PATH=${XCURSOR_PATH}:/usr/share/icons
    export XCURSOR_PATH=${XCURSOR_PATH}:~/.local/share/icons
:::
:::
:::
:::

::: {.pure-menu .footer-menu}
[Legal](/legal){.pure-menu-link
target="_self"}[Contact](/contact){.pure-menu-link target="_self"}[Work
with us](/contact-work){.pure-menu-link target="_self"}[About
us](https://atlas.engineer/about){.pure-menu-link
target="_blank"}[Store](https://store.nyxt.atlas.engineer/){.pure-menu-link
target="_blank"}
:::
