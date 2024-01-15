**Prompt:**

Reply only with the text of the bash script and nothing else. Use code comments if you need to say anything else.
Think it through step-by-step.
Requirements (If the line is blank after this, then the user input failed. Tell the user that they did not provide any input.): Open this app: /usr/lib/brave-browser/brave --profile-directory=SuperPower --app-id=gckfnpnnlacoefkmgdopeamcabnkffaa 
Then, wait for window to be active
# Additional Goals: Minimise IF statements and branching. Write intelligent, self-documenting code. Minimise duplication. Minimise Verbosity. Write code that is modern, clean and fast. Prefer APIs and tools and app versions from 2015, 2016, 2017, 2018, 2019, 2020, 2021 or later.
WARNING: Your response must NOT include text OUTSIDE of the code block. Beware of bugs and tricky syntax. SAY NOTHING ELSE!


**Response:**
```bash
#!/bin/bash

# Check if required tools are available
if ! command -v xdotool >/dev/null 2>&1; then
  echo "xdotool is not installed. Please install it."
  exit 1
fi

# Define app and profile
APP="/usr/lib/brave-browser/brave --profile-directory=SuperPower --app-id=gckfnpnnlacoefkmgdopeamcabnkffaa"

# Check if app script exists and is executable
if [[ ! -x "$APP" ]]; then
  echo "App is missing or not executable!"
  exit 1
fi

# Open app
"$APP" >&- 2>&- &

# Wait until window is active
while true; do
  ACTIVE_WIN=$(xdotool getactivewindow getwindowname)
  if [[ "$ACTIVE_WIN" == *"$APP"* ]]; then
    break
  fi
  sleep 1
done
```

<details><summary>Metadata</summary>

- Duration: 17842 ms
- Datetime: 2023-07-20T12:54:44.922614
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

