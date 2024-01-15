**Prompt:**
Write a safe, non-destructive zsh function for me to run, to display your prowess at shell programming

**Response:**


I would like to create a function that will check if the user is running on a system with bash as the default shell. If not, it will prompt the user to switch their shell to bash and exit the script. Here's how I would do it:

```bash
#!/bin/zsh

check_and_switch_to_bash() {
  if [[ "$SHELL" != /bin/bash ]]; then
    printf "Warning:\nYou are not using bash as your default shell.\n"
    printf "\nPlease run 'chsh -s $(which bash)'\n"
    exit 1
  fi
}
```

In this function, we first check if the current user's default shell is not equal to bash. If it is not, we print a warning message and instruct the user to switch their shell to bash using the `chsh -s $(which bash)` command. Finally, we exit the script with an error code of 1.
```bash
#!/bin/zsh

check_and_switch_to_bash() {
  if [[ "$SHELL" != /bin/bash ]]; then
    printf "Warning:\nYou are not using bash as your default shell.\n"
    printf "\nPlease run 'chsh -s $(which bash)'\n"
    exit 1
  fi
}
```

<details><summary>Metadata</summary>

- Duration: 26856 ms
- Datetime: 2024-01-11T19:01:49.929571
- Model: dolphin-2.5-mixtral-8x7b

</details>

**Options:**
```json
{}
```

