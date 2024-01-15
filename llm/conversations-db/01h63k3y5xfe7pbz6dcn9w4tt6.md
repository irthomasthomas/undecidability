**Prompt:**

Reply only with the text of the bash script and nothing else. Use code comments if you need to say anything else.
Think it through step-by-step.
Requirements (If the line is blank after this, then the user input failed. Tell the user that they did not provide any input.): Launch the app: /home/thomas/Development/Projects/streamdeck-ui/env/bin/streamdeck, wait up to 8 seconds for it to be active and record its pid. Then run: tdrop -n streamdeck current
# Additional Goals: Minimise IF statements and branching. Write intelligent, self-documenting code. Minimise duplication. Minimise Verbosity. Write code that is modern, clean and fast. Prefer APIs and tools and app versions from 2015, 2016, 2017, 2018, 2019, 2020, 2021 or later.
WARNING: Your response must NOT include text OUTSIDE of the code block. Beware of bugs and tricky syntax. SAY NOTHING ELSE!


**Response:**
```bash
#!/bin/bash

# Launch the app
/home/thomas/Development/Projects/streamdeck-ui/env/bin/streamdeck &

# Wait up to 8 seconds for it to be active and record its pid
sleep 8
pid=$(pgrep -f "/home/thomas/Development/Projects/streamdeck-ui/env/bin/streamdeck")

# Check if the pid is empty
if [[ -z $pid ]]; then
    echo "User input failed. No pid recorded."
else
    # Run tdrop command with the recorded pid
    tdrop -n streamdeck current
fi
```

<details><summary>Metadata</summary>

- Duration: 5128 ms
- Datetime: 2023-07-24T09:19:01.301143
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

