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

**Response:**
The script you provided uses `tdrop` and `wmctrl` to manage window placement and Terminator for terminal emulation. The script is designed to position Terminator windows in the corners of the screen based on the argument provided (`TopLeft`, `TopRight`, `BottomLeft`, `BottomRight`).

If all windows are being centered instead of being placed in the corners, it's possible that the window manager or desktop environment is overriding the placement settings specified by `tdrop` and `wmctrl`. To address this, you may need to check the settings of your window manager or desktop environment to ensure that it allows for manual window placement.

Additionally, ensure that the `--geometry` option in the `terminator` command is being interpreted correctly. The `--geometry` option should follow the format `WIDTHxHEIGHT+X+Y`, where `WIDTH` and `HEIGHT` are the size of the window, and `X` and `Y` are the positions on the screen.

If the issue persists, you may need to consult the documentation for `tdrop`, `wmctrl`, and your window manager to find a solution that respects the placement commands.

<details><summary>Metadata</summary>

- Duration: 12865 ms
- Datetime: 2023-12-21T11:47:58.291808
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

