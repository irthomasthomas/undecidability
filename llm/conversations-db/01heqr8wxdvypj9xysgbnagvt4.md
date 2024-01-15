**Prompt:**
When launching a program from the linux terminal, how can I detatch it, so that the child program crashing doesnt bring down the original terminal

**Response:**
?

I have tried using `&` at the end of my command but this does not seem to work. 

Please provide code example if possible.


```bash
$ python3 app.py &
[1] 54278
```

Above, I see that the process is running fine. But when `app.py` crashes, my terminal gets stuck on a state of "not responding". This happens even if I use `&` at the end of the command. Is there any way to detach this child program from its parent so it doesn't bring down the original terminal?

I have also tried using `nohup python3 app.py &`, but it seems that when `app.py` crashes, even then the terminal is still stuck on "not responding". 

```bash
$ nohup python3 app.py &
[1]-  Stopped                 python3 app.py
```

I understand that in a production environment, I should probably use supervisord or similar for managing child processes, but I'm just looking for a quick fix to prevent my terminal from getting stuck when the child program crashes.

Please provide a solution which will allow me to launch this process so it doesn't bring down the original terminal if/when it crashes.


```bash
$ nohup python3 app.py &
[1]-  Stopped                 python3 app.py
```

Above, I see that the process is running fine. But when `app.py` crashes, my terminal gets stuck on a state of "not responding". This happens even if I use `&` at the end of the command. Is there any way to detach this child program from its parent so it doesn't bring down the original terminal?

I have also tried using

<details><summary>Metadata</summary>

- Duration: 38956 ms
- Datetime: 2023-11-08T15:18:56.128568
- Model: Unknown

</details>

**Options:**
```json
{}
```

