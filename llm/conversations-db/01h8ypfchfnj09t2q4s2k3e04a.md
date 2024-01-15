**Prompt:**
tdrop -n "$Activity - Top-left" --post-create-hook "autohide-tdrop &" -x 0% -y 8 --width=48% --height=48% --post-map-hook "wmctrl -r 'Alacritty - Drop Down - $Activity - Top' -b add,sticky" alacritty --class="$Activity - Top-left" --title "Alacritty - Drop Down - $Activity - Top-left"
 Think carefully. Write a similar command for chromebrowser, but make it full screen.

**Response:**
tdrop -n "$Activity - Top-left" --post-create-hook "autohide-tdrop &" -x 0% -y 8 --width=48% --height=48% --post-map-hook "wmctrl -r 'Alacritty - Drop Down - $Activity - Top' -b add,sticky" chromebrowser --start-fullscreen --class="$Activity - Top-left" --title "Chromebrowser - Drop Down - $Activity - Top-left"

<details><summary>Metadata</summary>

- Duration: 2655 ms
- Datetime: 2023-08-28T18:28:37.967113
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

