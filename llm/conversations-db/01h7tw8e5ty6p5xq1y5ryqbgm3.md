**Prompt:**
diff --git a/tdrop/window_assign_tdrop.sh b/tdrop/window_assign_tdrop.sh
index b7f7a1d..0a68fa9 100644
--- a/tdrop/window_assign_tdrop.sh
+++ b/tdrop/window_assign_tdrop.sh
@@ -2,7 +2,7 @@
 # for .desktop file in dir
 # exec_dot_desktop
 
-demo="/usr/share/applications/brave-browser.desktop"
+demo_desktop_file="/usr/share/applications/brave-browser.desktop"
 
 exec_dot_desktop() {
   desktop_file="$1"
diff --git a/tdrop/windows/Alacritty-tdrop.sh b/tdrop/windows/Alacritty-tdrop.sh
index be154a5..53f22dd 100644
--- a/tdrop/windows/Alacritty-tdrop.sh
+++ b/tdrop/windows/Alacritty-tdrop.sh
@@ -18,7 +18,7 @@ if [[ "$1" != "Top" && "$1" != "Bottom" ]]; then
 fi
 
 if [ "$1" = "Top" ]; then
-  tdrop -n "$Activity - Top" -x 50% --width=50% --height=50% --post-map-hook "wmctrl -r 'Alacritty - Drop Down - $Activity - Top' -b add,sticky" alacritty --title "Alacritty - Drop Down - $Activity - Top"
+  tdrop -n "$Activity - Top" --post-create-hook "autohide-tdrop &" -x 50% --width=50% --height=50% --post-map-hook "wmctrl -r 'Alacritty - Drop Down - $Activity - Top' -b add,sticky" alacritty --class="$Activity - Top" --title "Alacritty - Drop Down - $Activity - Top"
 elif [ "$1" = "Bottom" ]; then
-  tdrop -n "$Activity - Bottom" -y 50% -x 50% --width=50% --height=50% --post-map-hook "wmctrl -r 'Alacritty - Drop Down - $Activity - Bottom' -b add,sticky" alacritty --title "Alacritty - Drop Down - $Activity - Bottom"
+  tdrop -n "$Activity - Bottom" --post-create-hook "autohide-tdrop &" -y 50% -x 50% --width=50% --height=50% --post-map-hook "wmctrl -r 'Alacritty - Drop Down - $Activity - Bottom' -b add,sticky" alacritty --class="$Activity - Bottom" --title "Alacritty - Drop Down - $Activity - Bottom"
 fi
\ No newline at end of file


**Response:**
Refactor window_assign_tdrop.sh and Alacritty-tdrop.sh to improve readability and add functionality.

<details><summary>Metadata</summary>

- Duration: 1535 ms
- Datetime: 2023-08-14T20:37:03.290326
- Model: gpt-3.5-turbo-16k-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

