**Prompt:**
#!/bin/bash

WATCH_DIRS="$HOME/Downloads:$HOME/Apps"
INOTIFY_EVENTS="moved_to,create"
EXTENSIONS="zip|gz|tar|bz2|xz|rar|7z"
DOLPHIN=$(which dolphin)

function is_file_complete() {
  local file="$1"
  # Check if the file is not a temporary/incomplete download file
  if [[ ! "$file" =~ \.part$ ]] && [[ ! "$file" =~ \.crdownload$ ]]; then
    return 0
  else
    return 1
  fi
}

function open_readme() {
  local output_dir="$1"
  local readme_file

  for file in "$output_dir"/*; do
    (printf 'file: %s
' "$file") > `tty`
    if [[ "$(basename "$file")" =~ ^readme\.md$|^README\.md$ ]]; then
      readme_file="$file"
      (printf 'readme_file: %s
' "$readme_file") > `tty`
      break
    fi
  done

  if [ -n "$readme_file" ]; then
    xdg-open "$readme_file" &>/dev/null &
  fi
}


function update_output_dir() {
  local output_dir="$1"
  local item_count=0
  local subdir

  for item in "$output_dir"/*; do
    item_count=$((item_count + 1))
    if [ -d "$item" ]; then
      subdir="$item"
    else
      return 1
    fi
  done

  if [ $item_count -eq 1 ] && [ -n "$subdir" ]; then
    echo "$subdir"
  else
    echo "$output_dir"
  fi
}


function extract_file() {
  local file="$1"
  local output_dir="$2"

  case "$file" in
    *.tar.gz|*.tgz) tar -xzf "$file" -C "$output_dir" --overwrite ;;
    *.tar.bz2|*.tbz2) tar -xjf "$file" -C "$output_dir" --overwrite ;;
    *.tar.xz) tar -xJf "$file" -C "$output_dir" --overwrite ;;
    *.tar) tar -xf "$file" -C "$output_dir" --overwrite ;;
    *.gz) gunzip -cf "$file" > "${output_dir}/${file%.*}" ;;
    *.bz2) bunzip2 -cf "$file" > "${output_dir}/${file%.*}" ;;
    *.xz) unxz -cf "$file" > "${output_dir}/${file%.*}" ;;
    *.zip) unzip -o -d "$output_dir" "$file" ;;
    *.rar) unrar x -ad -o+ "$file" "$output_dir" ;;
    *.7z) 7z x -aoa "$file" -o"$output_dir" ;;
    *) echo "Unsupported file format: $file" ;;
  esac
}


IFS=':' read -ra dirs <<< "$WATCH_DIRS"

for dir in "${dirs[@]}"; do
  inotifywait -m -e "$INOTIFY_EVENTS" --format "%w%f" "$dir" | while read -r file_path; do
    file=$(basename "$file_path")
    if [[ "$file" =~ \.($EXTENSIONS)$ ]]; then
      sleep 1
      if [ ! -f "$file_path" ]; then
        continue
      fi
#       if ! is_file_complete "$file_path"; then
#         continue
#       fi
      while ! is_file_complete "$file_path"; do
        sleep 1
      done
      subfolder_name="${file%.*}"
      output_dir="$(dirname "$file_path")/${subfolder_name}"

      mkdir -p "$output_dir"
      extract_file "$file_path" "$output_dir"
      output_dir=$(update_output_dir "$output_dir")
      sleep 0.5
      $DOLPHIN "$output_dir" &>/dev/null &
      open_readme "$output_dir" &
      mv "$file_path" "$(dirname "$file_path")/Archive/"
      echo "Extracted and opened $file_path in Dolphin"
    else
      dolphin --select $file_path
    fi

  done &
done

# Wait for all background processes to finish
wait

**Response:**
extract_and_open_files.sh

<details><summary>Metadata</summary>

- Duration: 1774 ms
- Datetime: 2023-08-25T15:52:32.151231
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

