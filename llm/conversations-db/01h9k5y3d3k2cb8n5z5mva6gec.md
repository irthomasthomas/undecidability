**Prompt:**
diff --git a/copy_file_tags.sh b/copy_file_tags.sh
new file mode 100755
index 0000000..31e33d1
--- /dev/null
+++ b/copy_file_tags.sh
@@ -0,0 +1,2 @@
+file:///home/thomas/Downloads/facebook (1).svg#!/bin/bash
+getfattr -n user.xdg.tags --only-values $1 | xclip -selection clipboard
diff --git a/llm_shell_functions.sh b/llm_shell_functions.sh
new file mode 100644
index 0000000..c9e2c70
--- /dev/null
+++ b/llm_shell_functions.sh
@@ -0,0 +1,60 @@
+explain() {
+  paste | llm -o temperature 0.1 "Using as few words as possible, explain:\n"
+  }
+
+cllm() {
+  echo "$1" | claude --key $CLAUD_SESS_KEY
+  }
+
+mkfilename() {
+  file_content="$1"
+  # Truncate to <=400 tokens
+  trunc_content=$(ttok "$file_content" -t 400)
+  llm_template="makefilename"
+  echo "$trunc_content" | llm -m 3.5 -t $llm_template -o temperature 0 -o max_tokens 15
+  }
+
+commit() {
+
+  msg="$1"
+
+  git add .
+
+  [[ ! -z "$msg" ]] && git commit -m "$msg"
+
+    while true; do
+      #     msg="$(llm -t commit335 -p comm1 $(git diff --cached | llm -t commit135 -o temperature 0.3) -p comm2 $(git diff --cached | llm -t commit135 -o temperature 0.3) -p comm3 $(git diff --cached | llm -t commit135 -o temperature 0.3))"
+
+      msg=$(llm -t commit135 -o temperature 0.3 "$(git diff --cached)") # -m 3.5-16k
+      echo "Commit Msg: "$msg""
+      echo "Confirm push to repo? [y] or regenerate msg? [n]"
+      read confirm
+      [[ "$confirm" == "y" ]] || continue
+      break
+    done
+
+    git commit -m ""$msg""
+}
+
+# TODO nolog() { llm  }
+
+help() { print -z $(llm -t shellhelp "$1" -o temperature 0) }
+
+help4() { print -z $(llm -t shellhelp "$1" -m 4 -o temperature 0) }
+
+mkscript() {
+  input="$1"
+  model="$2"
+  llm -t shellscript "$input" "$model" -o temperature 0.2
+}
+
+advisor() {
+  model="$2"
+  llm -t advisor "$1" "$model" -o temperature 0.2
+  }
+
+klippy() {
+  model="$2"
+  llm -t kde "$1" "$model" -o temperature 0.2
+  }
+
diff --git a/organise_dji_media_files.sh b/organise_dji_media_files.sh
index b91e328..736c99c 100755
--- a/organise_dji_media_files.sh
+++ b/organise_dji_media_files.sh
@@ -1,6 +1,6 @@
 #!/bin/bash
 #
-About_This_Script = "A script for organising DJI PANORAMA and HYPERLAPSE directories. Script expects to find at least a PANORAMA or HYPERLAPSE subdirectory. So pass in the parent path where those directories live, do not link directly to the directories themselves. The script traverses each child directory that contain the PANORAMA image files and renames each image file based on its creation date. Then the directory containing the images is renamed based on the first image file inside of it."
+About_This_Script = "A script for organising DJI PANORAMA and HYPERLAPSE directories. Script expects to find at least a PANORAMA or HYPERLAPSE subdirectory. So pass in the parent path where those directories live. Do not link directly to the directories themselves. The script traverses each child directory that contain the PANORAMA image files and renames each image file based on its creation date. Then the directory containing the images is renamed based on the first image file inside of it."
 
 printf 'About: %s\n' "$About_This_Script"
 # If no input paramater then use the current working directory
@@ -34,7 +34,6 @@ for dir in "$rootdir"/*/; do
         cd ..
         # rename dir to child filename
         mv "$subdir" "$foldername"
-#         mv "$rootdir""/PANORAMA/""$dir"  "$rootdir""PANORAMA/""$foldername"
     done
   elif [[ "$dir_name" == "HYPERLAPSE" ]]; then
     printf "HYPERLAPSE\n"
@@ -55,50 +54,6 @@ for dir in "$rootdir"/*/; do
     done
   else
     printf "%s\n" "$dir_name"
-#     exiftool -r -ext dng '-FileName<${filename;s/\.[^.]+$//}-${CreateDate;}' -d %Y_%m_%d__%H_%M_%S%%-c.%%e . -fast
   fi
   cd ..
 done
-
-
-#
-# if cd PANORAMA; then
-#         echo Running exiftool -r -ext dng -ext jpg "-FileName<CreateDate" -d PANOPIECE-%Y_%m_%d__%H_%M_%S%%-c.%%e . -fast
-#         exiftool -r -ext dng -ext jpg "-FileName<CreateDate" -d PANOPIECE-%Y_%m_%d__%H_%M_%S%%-c.%%e . -fast
-#
-#
-#         ls . > $HOME/panodirfile
-#         readarray -t dirs < $HOME/panodirfile
-#
-#     for dir in "${dirs[@]}"
-#         do
-#             # Get first filename
-#             filename=$(ls "$rootdir""/PANORAMA/""$dir" | tail -1)
-#             filetime=$(exiftool -d "%Y_%m_%d__%H_%M_%S" -DateTimeOriginal -S -s $filename)
-#             # Strip extensions
-# #             filename=$(echo "$filename" | cut -f 1 -d '.')
-#             foldername="PANOGROUP-$filename"
-#              # rename dir to child filename
-#             mv "$rootdir""/PANORAMA/""$dir"  "$rootdir""PANORAMA/""$foldername"
-#         done
-#     cd ..
-# elif cd HYPERLAPSE; then
-#     echo Running exiftool -r -ext dng -ext jpg "-FileName<CreateDate" -d HYPERPIECE-%Y_%m_%d__%H_%M_%S%%-c.%%e . -fast
-#     exiftool -r -ext dng -ext jpg "-FileName<CreateDate" -d HYPERPIECE-%Y_%m_%d__%H_%M_%S%%-c.%%e . -fast
-#
-#     ls . > $HOME/hyperdirfile
-#     # ls $rootdir > ~/panodirfile
-#
-#     readarray -t hyperdirs < $HOME/hyperdirfile
-#
-#     echo begin loop over dirs
-#
-#     for dir in "${hyperdirs[@]}"
-#     do
-#         filename=$(ls $rootdir"HYPERLAPSE/""$dir" | tail -1) # get top dir name
-#         filename=$(echo "$filename" | cut -f 1 -d '.') # strip extensions
-#         mv $rootdir"HYPERLAPSE/""$dir"  $rootdir"HYPERLAPSE/""$filename" # rename dir to child filename
-#     done
-#     cd ..
-# fi
-#
diff --git a/organise_dji_media_files.sh.bak b/organise_dji_media_files.sh.bak
deleted file mode 100755
index e29172a..0000000
--- a/organise_dji_media_files.sh.bak
+++ /dev/null
@@ -1,103 +0,0 @@
-#!/bin/bash
-#
-About_This_Script = "A script for organising DJI PANORAMA and HYPERLAPSE directories. Script expects to find at least a PANORAMA or HYPERLAPSE subdirectory. So pass in the parent path where those directories live, do not link directly to the directories themselves. The script traverses each child directory that contain the PANORAMA image files and renames each image file based on its creation date. Then the directory containing the images is renamed based on the first image file inside of it."
-printf 'About: %s\n' "$About_This_Script"
-# If no input paramater then use the current working directory
-if test -z "$1"; then
-    printf 'no paramater passed %s\n'
-    rootdir=$PWD/
-else
-    rootdir="$1"
-fi
-printf 'rootdir %s\n' "$rootdir"
-
-
-for dir in "$rootdir"/*/; do
-  cd "$dir"
-  printf 'dir: %s\n' "$dir"
-  dir_name="$(basename "$dir")"
-  printf 'dir_name: %s\n' "$dir_name"
-  if [[ "$dir_name" == "PANORAMA" ]]; then
-    printf "PANORAMA\n"
-    exiftool -r -ext dng '-FileName<${filename;s/\.[^.]+$//}-${CreateDate;}' -d PANOPIECE-%Y_%m_%d__%H_%M_%S%%-c.%%e . -fast
-    for subdir in "$rootdir"/PANORAMA/*/; do
-        printf 'subdir: %s\n' "$subdir"
-        cd "$subdir"
-        filename=$(ls -1 | head -n 1)
-        printf 'filename: %s\n' "$filename"
-        filetime=$(exiftool -d "%Y_%m_%d__%H_%M_%S" -DateTimeOriginal -S -s "$filename")
-        printf 'filetime: %s\n' "$filetime"
-        # Strip extensions
-        filename=$(echo "$filename" | cut -f 1 -d '.')
-        foldername="PANOGROUP-$filename"
-        cd ..
-        # rename dir to child filename
-        mv "$subdir" "$foldername"
-#         mv "$rootdir""/PANORAMA/""$dir"  "$rootdir""PANORAMA/""$foldername"
-    done
-  elif [[ "$dir_name" == "HYPERLAPSE" ]]; then
-    printf "HYPERLAPSE\n"
-    exiftool -r -ext dng '-FileName<${filename;s/\.[^.]+$//}-${CreateDate;}' -d HYPERPIECE-%Y_%m_%d__%H_%M_%S%%-c.%%e . -fast
-    for subdir in "$rootdir"/HYPERLAPSE/*/; do
-        printf 'subdir: %s\n' "$subdir"
-        cd "$subdir"
-        filename=$(ls -1 | head -n 1)
-        printf 'filename: %s\n' "$filename"
-        filetime=$(exiftool -d "%Y_%m_%d__%H_%M_%S" -DateTimeOriginal -S -s "$filename")
-        printf 'filetime: %s\n' "$filetime"
-        # Strip extensions
-        filename=$(echo "$filename" | cut -f 1 -d '.')
-        foldername="HYPERGROUP-$filename"
-        cd ..
-        # rename dir to child filename
-        mv "$subdir" "$foldername"
-    done
-  else
-    printf "%s\n" "$dir_name"
-#     exiftool -r -ext dng '-FileName<${filename;s/\.[^.]+$//}-${CreateDate;}' -d %Y_%m_%d__%H_%M_%S%%-c.%%e . -fast
-  fi
-  cd ..
-done
-
-
-#
-# if cd PANORAMA; then
-#         echo Running exiftool -r -ext dng -ext jpg "-FileName<CreateDate" -d PANOPIECE-%Y_%m_%d__%H_%M_%S%%-c.%%e . -fast
-#         exiftool -r -ext dng -ext jpg "-FileName<CreateDate" -d PANOPIECE-%Y_%m_%d__%H_%M_%S%%-c.%%e . -fast
-#
-#
-#         ls . > $HOME/panodirfile
-#         readarray -t dirs < $HOME/panodirfile
-#
-#     for dir in "${dirs[@]}"


**Response:**
Add shell functions and scripts for organising DJI media files and copying file tags.

<details><summary>Metadata</summary>

- Duration: 1822 ms
- Datetime: 2023-09-05T17:23:38.244171
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.3}
```

