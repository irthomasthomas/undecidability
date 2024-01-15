**Prompt:**

Reply only with the text of the bash script and nothing else. Use code comments if you need to say anything else.
Think it through step-by-step.
Requirements (If the line is blank after this, then the user input failed. Tell the user that they did not provide any input.): Launch the app: /home/thomas/Development/Projects/streamdeck-ui/env/bin/streamdeck, wait up to 8 seconds for it to be active and record its pid. Then run: tdrop -n streamdeck current
# Additional Goals: Minimise IF statements and branching. Write intelligent, self-documenting code. Minimise duplication. Minimise Verbosity. Write code that is modern, clean and fast. Prefer APIs and tools and app versions from 2015, 2016, 2017, 2018, 2019, 2020, 2021 or later.
WARNING: Your response must NOT include text OUTSIDE of the code block. Beware of bugs and tricky syntax. SAY NOTHING ELSE!


**Response:**
```bash
#!/bin/bash

# Path to the executable
executable_path="/home/thomas/Development/Projects/streamdeck-ui/env/bin/streamdeck"

# Check if the executable exists
if [[ ! -x "$executable_path" ]]; then
    echo "No executable found at $executable_path"
    exit 1
fi

# Launch the application in the background
"$executable_path" &

# Grab the PID of the last process launched in the background
streamdeck_pid=$!

# Wait up to 8 seconds for the application to load
for i in {1..8}; do
    # Check if the process is active
    if ps -p $streamdeck_pid > /dev/null; then
        break
    else
        sleep 1
    fi
done

# Check if the application launched successfully
if ! ps -p $streamdeck_pid > /dev/null; then
    echo "Unable to launch streamdeck"
    exit 1
fi

tdrop -n streamdeck current
```

<details><summary>Metadata</summary>

- Duration: 14427 ms
- Datetime: 2023-07-24T09:19:12.385085
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

