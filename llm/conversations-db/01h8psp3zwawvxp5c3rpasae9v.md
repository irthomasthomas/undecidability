**Prompt:**
diff --git a/.idea/inspectionProfiles/Project_Default.xml b/.idea/inspectionProfiles/Project_Default.xml
new file mode 100644
index 0000000..8079ae6
--- /dev/null
+++ b/.idea/inspectionProfiles/Project_Default.xml
@@ -0,0 +1,8 @@
+<component name="InspectionProjectProfileManager">
+  <profile version="1.0">
+    <option name="myName" value="Project Default" />
+    <inspection_tool class="ShellCheck" enabled="true" level="ERROR" enabled_by_default="true">
+      <shellcheck_settings value="SC2164" />
+    </inspection_tool>
+  </profile>
+</component>
\ No newline at end of file
diff --git a/VideoClipper.sh b/VideoClipper.sh
index fc79a95..ddb48fc 100644
--- a/VideoClipper.sh
+++ b/VideoClipper.sh
@@ -13,10 +13,9 @@ time_input_error="The Start and End time parameters where not entered correctly.
 function initialise_file_tags() {
   # Error /run/user/1000/kio-fuse-*/tags/ does not exist. How can we consistently get the tags directory?
   # https://github.com/kde/kio-fuse/issues/4
-  dolphin /run/user/"$(id -u)"/kio-fuse-*/tags &
-  sleep 2
+  dolphin tags:/ &
   xdg_open_pid=$!
-  sleep 0.1
+  sleep 0.2
   kill $xdg_open_pid
 }
 
@@ -182,7 +181,8 @@ function manage_star_rating() {
 }
 
 function screen_dimensions() {
-  local SCREEN_WIDTH=$(xrandr | grep '*' | awk '{print $1}' | cut -d 'x' -f1 | head -n 1)
+  local SCREEN_WIDTH
+  SCREEN_WIDTH=$(xrandr | grep '*' | awk '{print $1}' | cut -d 'x' -f1 | head -n 1)
 
   local GEOMETRY_WIDTH="50%"
   local GEOMETRY_POSITION_X=$((SCREEN_WIDTH / 2))
@@ -195,7 +195,8 @@ function screen_dimensions() {
 
 function play_video() {
   local FILEPATH="$1"
-  local GEOMETRY_STRING=$(screen_dimensions)
+  local GEOMETRY_STRING
+  GEOMETRY_STRING=$(screen_dimensions)
   local lut=
   if [[ "$color_space" == "bt709" && "$pix_fmt" == "yuv420p10le" ]]; then
     lut="--lut=/home/thomas/Downloads/DJI-Mavic-3-D-Log-to-Rec-709-V1.cube"
@@ -246,10 +247,13 @@ function edit_filenames() {
 
 function copy_attributes() {
   source="$1"
-  target="$2"
- tags=$(getfattr -n user.xdg.tags --only-values "$source")
- setfattr -n user.xdg.tags -v "$tags" "$target"
- setfattr -n user.baloo.rating -v "$new_star_rating" "$target"
+  file_list="$2"
+  tags=$(getfattr -n user.xdg.tags --only-values "$source")
+  for target in $file_list; do
+    setfattr -n user.xdg.tags -v "$tags" "$target"
+    setfattr -n user.baloo.rating -v "$new_star_rating" "$target"
+  done
+
 }
 
 function time_dialog() {
@@ -302,10 +306,10 @@ function ffmpeg_trim_video() {
 function run_main(){
   local file_tags
   local FILEPATH="$1"
-  unset "$NEW_START_TIME"
+  local file_list=()
 
+  unset "$NEW_START_TIME"
   while [[ "$END_TIME" < "$runtime" ]]; do
-    edit_filenames "$FILEPATH"
     time_dialog
     local input_time_result=$?
     if [[ $input_time_result = 1 ]]; then
@@ -319,11 +323,12 @@ function run_main(){
       pkill -P $$
       return
     fi
+    edit_filenames "$FILEPATH"
+    file_list+=("$output_path")
 
     (echo '{ "command": ["set_property", "pause", true] }' | tee >(socat - /tmp/mpv1) >(socat - /tmp/mpv2)) >/dev/null 2>&1
 
     ffmpeg_trim_video "$FILEPATH" "$START_TIME" "$END_TIME"
-
     sleep 0.5
 #    mpv --input-ipc-server=/tmp/mpv4 --hwdec=auto-copy --script-opts=osc-timems=yes --script-opts=osc-visibility=always --speed=3 --osd-level=3 "$output_tmp_path" > /dev/null 2>&1
 #    kdialog --msgbox $output_tmp_path
@@ -359,7 +364,7 @@ function run_main(){
     unset NEW_START_TIME
     file_tags="$(select_tags "$FILEPATH")"
     (echo '{ "command": ["quit"] }' | tee >(socat - /tmp/mpv1) >(socat - /tmp/mpv2) >/dev/null 2>&1) >/dev/null 2>&1
-    copy_attributes "$FILEPATH" "$dir_final/$output_filename" &&
+    copy_attributes "$FILEPATH" "${file_list[@]}"
     sleep 0.1
     kdialog --title "video clip delete origin" --warningyesno "DELETE ORIGINAL?"
     delete_value=$?


**Response:**
Refactor code and fix file copying bug

<details><summary>Metadata</summary>

- Duration: 721 ms
- Datetime: 2023-08-25T16:50:50.794108
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

