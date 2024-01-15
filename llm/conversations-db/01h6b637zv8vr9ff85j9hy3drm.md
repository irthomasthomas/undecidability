**Prompt:**
What does the STAT column mean in ps? eg ps $(pgrep ffmpeg) has STAT = T1

**Response:**
The `STAT` column in `ps` command output is a compact representation of the process status. It gives you information about the state of the process.

Here's what each character signifies:

1. The first character indicates the run state of the process:
   - D : Uninterruptible sleep (usually IO)
   - R : Running or runnable (on run queue)
   - S : Interruptible sleep (waiting for an event to complete)
   - T : Stopped by job control signal
   - t : Stopped by debugger during the tracing
   - W : Paging (not valid since the 2.6.xx kernel)
   - X : Dead (should never be seen)
   - Z : Defunct ("zombie") process, terminated but not reaped by its parent

2. The second character indicates:
   - < : high-priority (not nice to other users)
   - N : low-priority (nice to other users)
   - L : has pages locked into memory (for real-time and custom IO)
   - s : is a session leader
   - l : is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)
   - + : is in the foreground process group.

In your case, `T1` means the process is stopped by job control signal and it's multi-threaded.

<details><summary>Metadata</summary>

- Duration: 24226 ms
- Datetime: 2023-07-27T08:05:03.448387
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

