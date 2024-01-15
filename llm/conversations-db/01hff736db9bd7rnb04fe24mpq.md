**Prompt:**
TERMINATOR(1) TERMINATOR(1)

NAME
Terminator - Multiple GNOME terminals in one window

SYNOPSIS
terminator [options]

DESCRIPTION
This manual page documents Terminator, a terminal emulator application.

Terminator is a program that allows users to set up flexible arrangements of GNOME
terminals. It is aimed at those who normally arrange lots of terminals near each
other, but don't want to use a frame based window manager.

OPTIONS
This program follow the usual GNU command line syntax, with long options starting
with two dashes (â€˜-'). A summary of options is included below.

-h, --help
Show summary of options

-v, --version
Show the version of the Terminator installation

-m, --maximise
Start with a maximised window -M, --maximize Start with a maximized window

-f, --fullscreen
Start with a fullscreen window

-b, --borderless
Instruct the window manager not to render borders/decoration on the Terminator
window (this works well with -m)

-H, --hidden
Hide the Terminator window by default. Its visibility can be toggled with the
hide_window keyboard shortcut (Ctrl-Shift-Alt-a by default)

-T, --title
Force the Terminator window to use a specific name rather than updating it dyâ€�
namically based on the wishes of the child shell.

--geometry=GEOMETRY
Specifies the preferred size and position of Terminator's window; see X(7).

-e, --command=COMMAND
Runs the specified command instead of your default shell or profile specified
command. Note: if Terminator is launched as x-terminal-emulator -e behaves
like -x, and the longform becomes --execute2=COMMAND

-x, --execute COMMAND [ARGS]
Runs the rest of the command line instead of your default shell or profile
specified command.

--working-directory=DIR
Set the terminal's working directory

-g, --config FILE
Use the specified FILE for configuration

-r, --role=ROLE
Set a custom WM_WINDOW_ROLE property on the window

-l, --layout=LAYOUT
Start Terminator with a specific layout. The argument here is the name of a
saved layout.

-s, --select-layout=LAYOUT
Open the layout launcher window instead of the normal terminal.

-p, --profile=PROFILE
Use a different profile as the default

-i, --icon=FORCEDICON
Set a custom icon for the window (by file or name)

-u, --no-dbus
Disable DBus

-d, --debug
Enable debugging output (please use this when reporting bugs). This can be
specified twice to enable a built-in python debugging server.

--debug-classes=DEBUG_CLASSES
If this is specified as a comma separated list, debugging output will only be
printed from the specified classes.

--debug-methods=DEBUG_METHODS
If this is specified as a comma separated list, debugging output will only be
printed from the specified functions. If this is specified in addition to
--debug-classes, only the intersection of the two lists will be displayed

--new-tab
If this is specified and Terminator is already running, DBus will be used to
spawn a new tab in the first Terminator window.

KEYBINDINGS
The following default keybindings can be used to control Terminator:

F1 Launches the full HTML manual.

Creation & Destruction
The following items relate to creating and destroying terminals.

Ctrl+Shift+O
Split terminals Horizontally.

Ctrl+Shift+E
Split terminals Vertically.

Ctrl+Shift+T
Open new tab.

Ctrl+Shift+I
Open a new window. (Note: Unlike in previous releases, this window is part of
the same Terminator process.)

Super+I
Spawn a new Terminator process.

Alt+L Open layout launcher.

Ctrl+Shift+W
Close the current terminal.

Ctrl+Shift+Q
Close the current window.

Navigation
The following items relate to moving between and around terminals.

Alt+Up Move to the terminal above the current one.

Alt+Down
Move to the terminal below the current one.

Alt+Left
Move to the terminal left of the current one.

Alt+Right
Move to the terminal right of the current one.

Ctrl+PageDown
Move to next Tab.

Ctrl+PageUp
Move to previous Tab.

Ctrl+Shift+N or Ctrl+Tab
Move to next terminal within the same tab, use Ctrl+PageDown to move to the
next tab. If cycle_term_tab is False, cycle within the same tab will be disâ€�
abled.

Ctrl+Shift+P or Ctrl+Shift+Tab
Move to previous terminal within the same tab, use Ctrl+PageUp to move to the
previous tab. If cycle_term_tab is False, cycle within the same tab will be
disabled.

Organisation
The following items relate to arranging and resizing terminals.

Ctrl+Shift+Right
Move parent dragbar Right.

Ctrl+Shift+Left
Move parent dragbar Left.

Ctrl+Shift+Up
Move parent dragbar Up.

Ctrl+Shift+Down
Move parent dragbar Down.

Super+R
Rotate terminals clockwise.

Super+Shift+R
Rotate terminals counter-clockwise.

Drag and Drop
The layout can be modified by moving terminals with Drag and Drop. To start
dragging a terminal, click and hold on its titlebar. Alternatively, hold down
Ctrl, click and hold the right mouse button. Then, **Release Ctrl**. You can
now drag the terminal to the point in the layout you would like it to be. The
zone where the terminal would be inserted will be highlighted.

Ctrl+Shift+PageDown
Swap tab position with next Tab.

Ctrl+Shift+PageUp
Swap tab position with previous Tab.

Miscellaneous
The following items relate to miscellaneous terminal related functions.

Ctrl+Shift+C
Copy selected text to clipboard.

Ctrl+Shift+V
Paste clipboard text.

Ctrl+Shift+S
Hide/Show Scrollbar.

Ctrl+Shift+F
Search within terminal scrollback.

Ctrl+Shift+R
Reset terminal state.

Ctrl+Shift+G
Reset terminal state and clear window.

Ctrl+Plus (+)
Increase font size. Note: This may require you to press shift, depending on
your keyboard.

Ctrl+Minus (-)
Decrease font size. Note: This may require you to press shift, depending on
your keyboard.

Ctrl+Zero (0)
Restore font size to original setting.

Ctrl+Alt+W
Rename window title.

Ctrl+Alt+A
Rename tab title.

Ctrl+Alt+X
Rename terminal title.

Super+1
Insert terminal number, i.e. 1 to 12.

Super+0
Insert padded terminal number, i.e. 01 to 12.

Grouping & Broadcasting
The following items relate to helping to focus on a specific terminal.

F11 Toggle window to fullscreen.

Ctrl+Shift+X
Toggle between showing all terminals and only showing the current one (maxâ€�
imise).

Ctrl+Shift+Z
Toggle between showing all terminals and only showing a scaled version of the
current one (zoom).

Ctrl+Shift+Alt+A
Hide the initial window. Note that this is a global binding, and can only be
bound once.

The following items relate to grouping and broadcasting.

Super+T
Group all terminals in the current tab so input sent to one of them, goes to
all terminals in the current tab.

Super+Shift+T
Remove grouping from all terminals in the current tab.

Super+G
Group all terminals so that any input sent to one of them, goes to all of
them.

Super+Shift+G
Remove grouping from all terminals.

Alt+A Broadcast to All terminals.

Alt+G Broadcast to Grouped terminals.

Alt+O Broadcast Off.

Most of these keybindings are changeable in the Preferences.

SEE ALSO
terminator_config(5)

AUTHOR
Terminator was written by Chris Jones  and others.

This manual page was written by Chris Jones  and others.

Jan 5, 2008 TERMINATOR(1)
 Rewrite this in a few words as possible, formatted for input to an LLM, it will not be read by humans and does not need be pretty. Just functional. Ensure you include everything and the command description.

**Response:**
Terminator is a terminal emulator that allows for arranging multiple GNOME terminals in one window. It's useful for users who need many terminals open at once without using a frame-based window manager.

Options:
- `-h`, `--help`: Show options
- `-v`, `--version`: Show version
- `-m`, `--maximise`, `-M`, `--maximize`: Start maximized
- `-f`, `--fullscreen`: Start fullscreen
- `-b`, `--borderless`: No window borders/decoration
- `-H`, `--hidden`: Hide window by default
- `-T`, `--title`: Set window name
- `--geometry=GEOMETRY`: Set window size/position
- `-e`, `--command=COMMAND`: Run command instead of shell
- `-x`, `--execute COMMAND [ARGS]`: Run command line instead of shell
- `--working-directory=DIR`: Set working directory
- `-g`, `--config FILE`: Use config file
- `-r`, `--role=ROLE`: Set WM_WINDOW_ROLE property
- `-l`, `--layout=LAYOUT`: Start with layout
- `-s`, `--select-layout=LAYOUT`: Open layout launcher
- `-p`, `--profile=PROFILE`: Use different profile
- `-i`, `--icon=FORCEDICON`: Set window icon
- `-u`, `--no-dbus`: Disable DBus
- `-d`, `--debug`: Enable debugging output
- `--debug-classes=DEBUG_CLASSES`: Debug specific classes
- `--debug-methods=DEBUG_METHODS`: Debug specific functions
- `--new-tab`: Open new tab in running Terminator

Keybindings:
- `F1`: Open manual
- `Ctrl+Shift+O`: Split horizontally
- `Ctrl+Shift+E`: Split vertically
- `Ctrl+Shift+T`: New tab
- `Ctrl+Shift+I`: New window
- `Super+I`: New process
- `Alt+L`: Layout launcher
- `Ctrl+Shift+W`: Close terminal
- `Ctrl+Shift+Q`: Close window
- `Alt+Up/Down/Left/Right`: Move between terminals
- `Ctrl+PageDown/Up`: Move between tabs
- `Ctrl+Shift+N/P`: Move to next/previous terminal
- `Ctrl+Shift+Right/Left/Up/Down`: Move dragbar
- `Super+R`: Rotate clockwise
- `Super+Shift+R`: Rotate counter-clockwise
- `Ctrl+Shift+PageDown/Up`: Swap tabs
- `Ctrl+Shift+C/V`: Copy/Paste
- `Ctrl+Shift+S`: Toggle scrollbar
- `Ctrl+Shift+F`: Search
- `Ctrl+Shift+R`: Reset terminal
- `Ctrl+Shift+G`: Reset and clear
- `Ctrl+Plus/Minus/Zero`: Font size adjust
- `Ctrl+Alt+W/A/X`: Rename window/tab/terminal
- `Super+1/0`: Insert terminal number
- `F11`: Fullscreen toggle
- `Ctrl+Shift+X`: Show one/maximize terminal
- `Ctrl+Shift+Z`: Show one/zoom terminal
- `Ctrl+Shift+Alt+A`: Hide window
- `Super+T/G`: Group all in tab/all terminals
- `Super+Shift+T/G`: Ungroup in tab/all terminals
- `Alt+A/G/O`: Broadcast to all/grouped/off

Preferences can change keybindings. 

See also: `terminator_config(5)`

Author: Chris Jones and others.

<details><summary>Metadata</summary>

- Duration: 39579 ms
- Datetime: 2023-11-17T18:00:29.199088
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

