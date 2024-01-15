**Prompt:**
This results in all windows always being centered, but they should be in a corner of the screen.

#!/bin/bash

get_activity() {
  active_activity_id=$(qdbus org.kde.ActivityManager /ActivityManager/Activities CurrentActivity)
  Activity=$(qdbus org.kde.ActivityManager /ActivityManager/Activities org.kde.ActivityManager.Activities.ActivityName "$active_activity_id")
}

get_activity

case "$1" in
  TopLeft|TopRight|BottomLeft|BottomRight) ;;
  *)
    echo "Error: Please provide either 'Top' or 'Bottom' as an argument."
    exit 1
    ;;
esac

if [ "$1" = "TopLeft" ]; then
  tdrop -n "$Activity - TopLeft" -x 0% -y 0% --width=48% --height=48% --post-map-hook "wmctrl -r '$Activity - TopLeft' -b add,sticky" terminator --title="$Activity - TopLeft" --geometry=48%x48%+0+0
elif [ "$1" = "TopRight" ]; then
  tdrop -n "$Activity - TopRight" -x 50% -y 0% --width=50% --height=48% --post-map-hook "wmctrl -r '$Activity - TopRight' -b add,sticky" terminator --title="$Activity - TopRight" --geometry=50%x48%+50%+0
elif [ "$1" = "BottomLeft" ]; then
  tdrop -n "$Activity - BottomLeft" -y 52% -x 0% --width=48% --height=48% --post-map-hook "wmctrl -r '$Activity - BottomLeft' -b add,sticky" terminator --title="$Activity - BottomLeft" --geometry=48%x48%+0+52%
elif [ "$1" = "BottomRight" ]; then
  tdrop -n "$Activity - BottomRight" -y 52% -x 50% --width=50% --height=48% --post-map-hook "wmctrl -r '$Activity - BottomRight' -b add,sticky" terminator --title="$Activity - BottomRight" --geometry=50%x48%+50%+52%
fi


#--post-create-hook "autohide-tdrop &"


**Response:**
The script you've provided is intended to open a `terminator` terminal window in one of the corners of the screen based on the argument provided (`TopLeft`, `TopRight`, `BottomLeft`, `BottomRight`). It uses `tdrop` to manage the dropdown terminal and `wmctrl` to adjust window properties.

However, you mentioned that windows are always being centered instead of being placed in the corners. This could be due to several reasons:

1. The window manager or KDE Plasma settings might be overriding the placement of new windows.
2. The `tdrop` and `wmctrl` commands might not be working as expected.
3. The geometry calculations might be incorrect or not taking into account the screen resolution or taskbar size.

To troubleshoot this issue, you can try the following steps:

1. Check KDE Plasma's window management settings to ensure that it's not set to center new windows by default.
2. Test the `tdrop` and `wmctrl` commands separately in the terminal to see if they behave as expected.
3. Ensure that the `--geometry` option in the `terminator` command is correct and corresponds to the desired screen position and size.

Additionally, the error message in your script is slightly misleading because it suggests providing either 'Top' or 'Bottom' as an argument, but the script actually expects 'TopLeft', 'TopRight', 'BottomLeft', or 'BottomRight'. You should update the error message to reflect the correct expected arguments.

Here's the corrected error message:

```bash
echo "Error: Please provide one of the following as an argument: 'TopLeft', 'TopRight', 'BottomLeft', 'BottomRight'."
```

If after these checks the issue persists, you might want to consider using KDE's built-in window rules to manage window placement instead of relying on external scripts and tools. Window rules in KDE Plasma can be very powerful and can be configured to apply to specific applications or window titles, allowing you to control the position and size of windows directly within the KDE environment.

<details><summary>Metadata</summary>

- Duration: 24241 ms
- Datetime: 2023-12-21T11:44:29.673207
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

**Prompt:**
How can I test tdrop and wmctrl

**Response:**
To test `tdrop` and `wmctrl`, you should first make sure they are installed on your system. If they are not, you can install them using your package manager.

**Install `tdrop` and `wmctrl` (if not already installed):**

For Arch Linux, use pacman to install them like so:

```bash
sudo pacman -Syu tdrop wmctrl
```

Since you're on Manjaro, the same command applies because Manjaro is based on Arch Linux.

**Test `tdrop`:**

1. Open a terminal.
2. Run a simple `tdrop` command to see if it can toggle a dropdown terminal. For example, you can use `xterm` or `konsole` if `terminator` is not your preference.

```bash
tdrop -a konsole
```

This should create a dropdown terminal. If you run the same command again, it should hide the terminal.

**Test `wmctrl`:**

1. Open a terminal.
2. Get the list of windows and their IDs:

```bash
wmctrl -l
```

You should see a list of window names and their identifiers.

3. Choose a window and try to move it using `wmctrl`. You need to replace `WINDOW_ID` with the actual window identifier or a window title from the list. The following command will move the window 100 pixels to the right and 100 pixels down from the top-left corner of your screen.

```bash
wmctrl -r WINDOW_ID -e 0,100,100,-1,-1
```

If you use the window title, it might look like this:

```bash
wmctrl -r "Terminal" -e 0,100,100,-1,-1
```

**Note:** Make sure to replace `"Terminal"` with the exact title of the window you want to move.

If the commands work correctly, the `tdrop` will toggle konsole visibility, and `wmctrl` will re-position a window on your desktop.

If `tdrop` and `wmctrl` are not working as expected, check their documentation or help pages with `tdrop --help` and `wmctrl --help` for more information and examples. You may also want to review the window manager's settings to ensure no conflicting rules are affecting their behavior.

<details><summary>Metadata</summary>

- Duration: 32598 ms
- Datetime: 2023-12-21T11:46:34.938194
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

