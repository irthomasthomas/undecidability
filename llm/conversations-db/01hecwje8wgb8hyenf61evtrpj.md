**Prompt:**
#!/bin/bash
continue_or_delay() {
  while true; do
    kdialog --passivepopup "Break Time approaches. \n I noted you are working on ${current_task}."
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

continue_or_delay() {
  #New version no longer depends on KDE and kdialog to communicate to user.
  #Activates terminal window when needed.
while true; d

**Response:**
o
  printf '%s \n' "Break Time approaches. I noted you are working on ${current_task}."
  for i in 2:00 1:59 1:58 1:57 1:56
  do
    printf '%s \n' "$i"
    sleep 1
  done
    sleep 115
done
}

#Detect when user is idle. Any thoughts?
#replacement for kdialog?

#Set breaktime for 1 hour intervals.
for current_task in {"steno","neural_code"}; do continue_or_delay; done
#End of code


<details><summary>Metadata</summary>

- Duration: 2140 ms
- Datetime: 2023-11-04T10:03:01.183707
- Model: gpt-3.5-turbo-instruct

</details>

**Options:**
```json
{}
```

