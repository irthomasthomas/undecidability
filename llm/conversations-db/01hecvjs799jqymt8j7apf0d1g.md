**Prompt:**
Replace kdialog with a TUI in the following function.

continue_or_delay() {
  while true; do
    kdialog --passivepopup "Break Time approaches. 
 I noted you are working on ${current_task}."
    # Kill the pids and return, or sleep for two minutes and continue loop.
    if [ $? -eq 0 ]; then
      return
    else
      for i in 2:00 1:59 1:58 1:57 1:56
      do
        kdialog --passivepopup "$i" 1
        sleep 1
      done
        sleep 115
    fi
    done
}

**Response:**


<details><summary>Metadata</summary>

- Duration: 5429 ms
- Datetime: 2023-11-04T09:45:40.531555
- Model: Unknown

</details>

**Options:**
```json
{}
```

