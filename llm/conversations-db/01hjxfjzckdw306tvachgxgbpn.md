**Prompt:**
Update the script like this: run in a perpetual loop. Get the active window and show an error msg if it is NOT a firefox window.

**Response:**
To update the script to run in a perpetual loop and show an error message if the active window is not a Firefox window, you can use the following code:

```python
import time
import win32gui

while True:
    # Get the active window
    active_window = win32gui.GetForegroundWindow()

    # Get the window class name
    class_name = win32gui.GetClassName(active_window)

    # Check if the active window is Firefox
    if "Firefox" not in class_name:
        # Show an error message
        print("Error: Active window is not Firefox!")

    # Wait for a short period of time before checking again
    time.sleep(1)
```

This code uses the `win32gui` module to get the active window and its class name. It then checks if the class name contains the string "Firefox". If it doesn't, it prints an error message. The script then waits for 1 second before checking again in a perpetual loop.

<details><summary>Metadata</summary>

- Duration: 4048 ms
- Datetime: 2023-12-30T13:45:57.954481
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.0}
```

