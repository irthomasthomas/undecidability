**Prompt:**
Explain HISTSIZE and SAVEHIST values in zsh config

**Response:**
HISTSIZE and SAVEHIST are two variables in the zsh configuration that control the behavior and size of the command history.

1. HISTSIZE:
   - HISTSIZE specifies the number of commands that the history file will retain in memory.
   - The value of HISTSIZE determines how many commands will be available for retrieval using the history mechanism.
   - Once the number of commands exceeds the HISTSIZE value, the oldest command will be removed from memory to make room for the new one.
   - By default, the value of HISTSIZE is set to 1000, meaning only the last 1000 commands executed will be stored in memory.
   - You can set a different value for HISTSIZE in your zsh configuration file (.zshrc) to suit your preferences or requirements.

2. SAVEHIST:
   - SAVEHIST determines the number of commands that will be saved to the history file on disk.
   - While HISTSIZE sets the number of commands to be stored in memory, SAVEHIST controls the number of commands that will persist across zsh sessions.
   - Once a command is removed from memory due to HISTSIZE limit, it can still be available in the history file if SAVEHIST is set accordingly.
   - By default, the value of SAVEHIST is set to 1000, meaning the last 1000 commands will be saved to the history file.
   - Similar to HISTSIZE, you can modify the SAVEHIST value in your .zshrc file to adjust the number of commands you want to retain in the history file.

It is worth noting that setting both HISTSIZE and SAVEHIST to zero effectively disables history-tracking and no commands will be saved.

<details><summary>Metadata</summary>

- Duration: 33025 ms
- Datetime: 2023-10-18T09:08:23.282538
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

