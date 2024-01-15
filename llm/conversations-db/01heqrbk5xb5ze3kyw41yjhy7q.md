**Prompt:**
When launching a program from the linux terminal, how can I detatch it, so that the child program crashing doesnt bring down the original terminal. Here is the solution:

**Response:**
 https://stackoverflow.com/questions/37591068/how-to-run-a-python-script-in-the-background-using-tmux

I want to be able to run a python script in the background using tmux, and if that crashes, it shouldn't bring down the entire terminal. How can I achieve this?

Answer: You could use `nohup` command which allows your process to continue running even after you log out of the terminal. It redirects its standard output and error outputs to a file named `nohup.out`. You can also specify specific files for input and output if needed. Here is an example usage,

```bash
nohup python your_script.py > /dev/null 2>&1 &
```

To make it more robust you could use `tmux` as well which will allow you to create a new session and keep the process running even after you disconnect from the terminal, also provides several other features like multiple panes, splitting of windows etc. Here is an example usage of `tmux`,

```bash
tmux new -s mysession -d
tmux send-keys "python your_script.py" Enter
```

In both cases, if the program crashes it won't bring down the entire terminal.

<details><summary>Metadata</summary>

- Duration: 28167 ms
- Datetime: 2023-11-08T15:20:35.253329
- Model: Unknown

</details>

**Options:**
```json
{}
```

