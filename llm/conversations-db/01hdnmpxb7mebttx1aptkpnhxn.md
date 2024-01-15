**Prompt:**
#!/bin/bash
nyxt_wm_class_string=("nyxt")

window_id=`xdotool search --class ${nyxt_wm_class_string} | head -1`

if [ "$window_id" != "" ]; then
  echo "The window with class ${nyxt_wm_class_string} exists."
  if xwininfo -id $window_id | grep "Map State: IsViewable"; then
    echo "The window is mapped (visible)"
    xdotool windowminimize $window_id
  else
    echo "The window is unmapped (hidden)"
    xdotool windowmap $window_id
    xdotool windowactivate $window_id
  fi
else
  echo "The window with class ${nyxt_wm_class_string} does not exist."
  nyxt
fi


For finding the terminal, first search for WM_CLASS(STRING) = "konsole", "konsole", then search within those for WM_NAME(STRING) = "~ : nyxt". 

**Response:**
#!/bin/bash
terminal_wm_class_string=("konsole")
terminal_wm_name_string=("~ : nyxt")

terminal_window_id=`xdotool search --class ${terminal_wm_class_string} | xargs -I {} xprop -id {} WM_NAME | grep "${terminal_wm_name_string}" | awk -F'=' '{print $2}' | sed 's/^[[:space:]]*//' | sed 's/"//g' | head -1`

if [ "$terminal_window_id" != "" ]; then
  echo "The terminal window with class ${terminal_wm_class_string} and name ${terminal_wm_name_string} exists."
  if xwininfo -id $terminal_window_id | grep "Map State: IsViewable"; then
    echo "The terminal window is mapped (visible)"
    xdotool windowminimize $terminal_window_id
  else
    echo "The terminal window is unmapped (hidden)"
    xdotool windowmap $terminal_window_id
    xdotool windowactivate $terminal_window_id
  fi
else
  echo "The terminal window with class ${terminal_wm_class_string} and name ${terminal_wm_name_string} does not exist."
fi

<details><summary>Metadata</summary>

- Duration: 31349 ms
- Datetime: 2023-10-26T09:22:37.937650
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.1}
```

