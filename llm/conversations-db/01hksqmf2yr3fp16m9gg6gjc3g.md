**Prompt:**

TERMINATOR(1)                                                                                                                       TERMINATOR(1)

NAME
       Terminator - Multiple GNOME terminals in one window

SYNOPSIS
       terminator [options]

DESCRIPTION
       This manual page documents Terminator, a terminal emulator application.

       Terminator  is  a  program that allows users to set up flexible arrangements of GNOME terminals. It is aimed at those who normally arrange
       lots of terminals near each other, but don't want to use a frame based window manager.

OPTIONS
       This program follow the usual GNU command line syntax, with long options starting with two dashes (‘-').  A summary of options is included
       below.

       -h, --help
              Show summary of options

       -v, --version
              Show the version of the Terminator installation

       -m, --maximise
              Start with a maximised window -M, --maximize Start with a maximized window

       -f, --fullscreen
              Start with a fullscreen window

       -b, --borderless
              Instruct the window manager not to render borders/decoration on the Terminator window (this works well with -m)

       -H, --hidden
              Hide the Terminator window by default. Its visibility can be toggled with the hide_window keyboard  shortcut  (Ctrl-Shift-Alt-a  by
              default)

       -T, --title
              Force the Terminator window to use a specific name rather than updating it dynamically based on the wishes of the child shell.

       --geometry=GEOMETRY
              Specifies the preferred size and position of Terminator's window; see X(7).

       -e, --command=COMMAND
              Runs  the specified command instead of your default shell or profile specified command. Note: if Terminator is launched as x-termi‐
              nal-emulator -e behaves like -x, and the longform becomes --execute2=COMMAND

       -x, --execute COMMAND [ARGS]
              Runs the rest of the command line instead of your default shell or profile specified command.

       --working-directory=DIR
              Set the terminal's working directory

       -g, --config FILE
              Use the specified FILE for configuration

       -r, --role=ROLE
              Set a custom WM_WINDOW_ROLE property on the window

       -l, --layout=LAYOUT
              Start Terminator with a specific layout. The argument here is the name of a saved layout.

       -s, --select-layout=LAYOUT
              Open the layout launcher window instead of the normal terminal.

       -p, --profile=PROFILE
              Use a different profile as the default

       -i, --icon=FORCEDICON
              Set a custom icon for the window (by file or name)

       -u, --no-dbus
              Disable DBus

       -d, --debug
              Enable debugging output (please use this when reporting bugs). This can be specified twice to enable a  built-in  python  debugging
              server.

       --debug-classes=DEBUG_CLASSES
              If this is specified as a comma separated list, debugging output will only be printed from the specified classes.

       --debug-methods=DEBUG_METHODS
              If  this  is  specified  as  a comma separated list, debugging output will only be printed from the specified functions. If this is
              specified in addition to --debug-classes, only the intersection of the two lists will be displayed

       --new-tab
              If this is specified and Terminator is already running, DBus will be used to spawn a new tab in the first Terminator window.

KEYBINDINGS
       The following default keybindings can be used to control Terminator:

       F1     Launches the full HTML manual.

   Creation & Destruction
       The following items relate to creating and destroying terminals.

       Ctrl+Shift+O
              Split terminals Horizontally.

       Ctrl+Shift+E
              Split terminals Vertically.

       Ctrl+Shift+T
              Open new tab.

       Ctrl+Shift+I
              Open a new window. (Note: Unlike in previous releases, this window is part of the same Terminator process.)

       Super+I
              Spawn a new Terminator process.

       Alt+L  Open layout launcher.

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
              Move to next terminal within the same tab, use Ctrl+PageDown to move to the next tab.  If cycle_term_tab is False, cycle within the
              same tab will be disabled.

       Ctrl+Shift+P or Ctrl+Shift+Tab
              Move to previous terminal within the same tab, use Ctrl+PageUp to move to the previous tab.   If  cycle_term_tab  is  False,  cycle
              within the same tab will be disabled.

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
              The  layout  can be modified by moving terminals with Drag and Drop.  To start dragging a terminal, click and hold on its titlebar.
              Alternatively, hold down Ctrl, click and hold the right mouse button.  Then, **Release Ctrl**. You can now drag the terminal to the
              point in the layout you would like it to be.  The zone where the terminal would be inserted will be highlighted.

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
              Increase font size. Note: This may require you to press shift, depending on your keyboard.

       Ctrl+Minus (-)
              Decrease font size. Note: This may require you to press shift, depending on your keyboard.

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

       F11    Toggle window to fullscreen.

       Ctrl+Shift+X
              Toggle between showing all terminals and only showing the current one (maximise).

       Ctrl+Shift+Z
              Toggle between showing all terminals and only showing a scaled version of the current one (zoom).

       Ctrl+Shift+Alt+A
              Hide the initial window. Note that this is a global binding, and can only be bound once.

       The following items relate to grouping and broadcasting.

       Super+T
              Group all terminals in the current tab so input sent to one of them, goes to all terminals in the current tab.

       Super+Shift+T
              Remove grouping from all terminals in the current tab.

       Super+G
              Group all terminals so that any input sent to one of them, goes to all of them.

       Super+Shift+G
              Remove grouping from all terminals.

       Alt+A  Broadcast to All terminals.

       Alt+G  Broadcast to Grouped terminals.

       Alt+O  Broadcast Off.

       Most of these keybindings are changeable in the Preferences.

SEE ALSO
       terminator_config(5)

AUTHOR
       Terminator was written by Chris Jones <cmsj@tenshu.net> and others.

       This manual page was written by Chris Jones <cmsj@tenshu.net> and others.

                                                                   Jan 5, 2008                                                      TERMINATOR(1)
 
Turn this into nice markdown - dense and concise for quick scanning. use tables. SAY NOTHING ELSE

**Response:**
```markdown
# Terminator Manual

## Name
Terminator - Multiple GNOME terminals in one window

## Synopsis
```
terminator [options]
```

## Description
Terminator is a terminal emulator that allows setting up multiple GNOME terminal instances in one window, targeting users who arrange lots of terminals close together.

## Options

| Option                  | Description                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| `-h`, `--help`          | Show summary of options                                                                                          |
| `-v`, `--version`       | Show the version of the Terminator installation                                                                  |
| `-m`, `--maximise`<br>`-M`, `--maximize` | Start with a maximised window                                                                                 |
| `-f`, `--fullscreen`    | Start with a fullscreen window                                                                                    |
| `-b`, `--borderless`    | Window manager should not render borders/decoration                                                               |
| `-H`, `--hidden`        | Hide the Terminator window initially; toggle visibility with shortcut (Ctrl-Shift-Alt-a)                          |
| `-T`, `--title`         | Use a specific window name instead of a dynamic one                                                              |
| `--geometry=GEOMETRY`   | Set preferred size and position (see X(7))                                                                        |
| `-e`, `--command=COMMAND`<br>`-x`, `--execute COMMAND [ARGS]` | Run specific command instead of the default shell or specified command            |
| `--working-directory=DIR` | Set the terminal's working directory                                                                             |
| `-g`, `--config FILE`   | Use the specified config file                                                                                     |
| `-r`, `--role=ROLE`     | Set a custom WM_WINDOW_ROLE property                                                                              |
| `-l`, `--layout=LAYOUT` | Start with a specific layout                                                                                      |
| `-s`, `--select-layout=LAYOUT` | Open the layout launcher window instead of the normal terminal                       |
| `-p`, `--profile=PROFILE` | Use a different profile as the default                                                                            |
| `-i`, `--icon=FORCEDICON` | Set a custom icon for the window (by file or name)                                                               |
| `-u`, `--no-dbus`       | Disable DBus                                                                                                      |
| `-d`, `--debug`         | Enable debugging output (use when reporting bugs)                                                                 |
| `--debug-classes=DEBUG_CLASSES` | Limit debugging to specified classes                                              |
| `--debug-methods=DEBUG_METHODS` | Limit debugging to specified functions                                            |
| `--new-tab`             | Use DBus to spawn a new tab in the first Terminator window if it's already running                               |

## Keybindings

### Creation & Destruction

| Keybinding            | Action                                   |
|-----------------------|------------------------------------------|
| `Ctrl+Shift+O`        | Split terminals horizontally             |
| `Ctrl+Shift+E`        | Split terminals vertically               |
| `Ctrl+Shift+T`        | Open new tab                             |
| `Ctrl+Shift+I`        | Open new window in the same process      |
| `Super+I`             | Spawn new Terminator process             |
| `Alt+L`               | Open layout launcher                     |
| `Ctrl+Shift+W`        | Close current terminal                   |
| `Ctrl+Shift+Q`        | Close current window                     |

### Navigation

| Keybinding            | Action                                           |
|-----------------------|--------------------------------------------------|
| `Alt+Up/Down/Left/Right` | Move to terminal in specified direction          |
| `Ctrl+PageDown`       | Move to next tab                                 |
| `Ctrl+PageUp`         | Move to previous tab                             |
| `Ctrl+Shift+N` or `Ctrl+Tab` | Move to next terminal within the same tab       |
| `Ctrl+Shift+P` or `Ctrl+Shift+Tab` | Move to previous terminal within the same tab |

### Organisation

| Keybinding             | Action                                     |
|------------------------|--------------------------------------------|
| `Ctrl+Shift+Right/Left/Up/Down` | Move parent dragbar in specified direction |
| `Super+R`              | Rotate terminals clockwise                 |
| `Super+Shift+R`        | Rotate terminals counter-clockwise         |
| Drag and Drop          | Modify layout by moving terminals          |
| `Ctrl+Shift+PageDown`  | Swap tab position with next tab            |
| `Ctrl+Shift+PageUp`    | Swap tab position with previous tab        |

### Miscellaneous

| Keybinding            | Action                                      |
|-----------------------|---------------------------------------------|
| `Ctrl+Shift+C`        | Copy selected text to clipboard             |
| `Ctrl+Shift+V`        | Paste clipboard text                        |
| `Ctrl+Shift+S`        | Hide/Show scrollbar                         |
| `Ctrl+Shift+F`        | Search within terminal scrollback           |
| `Ctrl+Plus`, `Ctrl+Minus`, `Ctrl+Zero` | Adjust font size to increase, decrease, or reset |
| `Ctrl+Alt+W/A/X`      | Rename window, tab, or terminal title       |
| `Super+1` to `Super+12` | Insert terminal number or padded number    |

### Grouping & Broadcasting

| Keybinding             | Action                                      |
|------------------------|---------------------------------------------|
| `F11`                  | Toggle fullscreen                           |
| `Ctrl+Shift+X`         | Show only the current terminal (maximise)   |
| `Ctrl+Shift+Z`         | Show scaled version of the current one (zoom)|
| `Ctrl+Shift+Alt+A`     | Hide/show initial window                    |
| `Super+T/G`            | Group all terminals in the current tab/all tabs |
| `Super+Shift+T/G`      | Ungroup all terminals in the current tab/all tabs |
| `Alt+A/G/O`            | Broadcast to all/grouped/off terminals      |

Preferences can be used to change most keybindings.

## See Also
terminator_config(5)

## Author
Written by Chris Jones and others.
```


<details><summary>Metadata</summary>

- Duration: 117516 ms
- Datetime: 2024-01-10T13:03:26.033106
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

