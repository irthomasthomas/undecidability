**Prompt:**
Help with samba on manjaro/arch linux: [2023/10/04 14:57:41,  0] ../../lib/util/debug.c:1263(reopen_one_log)
  reopen_one_log: Unable to open new log file '/usr/local/samba/var/log.%m': No such file or directory
[2023/10/04 14:57:41.978173,  0] ../../lib/util/debug.c:1263(reopen_one_log)
  reopen_one_log: Unable to open new log file '/usr/local/samba/var/log.%m': No such file or directory
[2023/10/04 14:57:41.978199,  0] ../../source4/samba/server.c:633(binary_smbd_main)
  samba version 4.19.0 started.
  Copyright Andrew Tridgell and the Samba Team 1992-2023
[2023/10/04 14:57:41.978226,  0] ../../lib/util/become_daemon.c:150(daemon_status)
  daemon_status: daemon 'samba' : Starting process...
[2023/10/04 14:57:42.000844,  0] ../../source4/samba/server.c:863(binary_smbd_main)
  At this time the 'samba' binary should only be used for either:
  'server role = active directory domain controller' or the rpc proxy with 'dcerpc endpoint servers = remote'
  You should start smbd/nmbd/winbindd instead for domain member and standalone file server tasks
[2023/10/04 14:57:42.000870,  0] ../../lib/util/become_daemon.c:119(exit_daemon)
  exit_daemon: daemon failed to start: Samba detected misconfigured 'server role' and exited. Check logs for details, error code 22
[2023/10/04 14:59:46,  0] ../../lib/util/debug.c:1263(reopen_one_log)
  reopen_one_log: Unable to open new log file '/usr/local/samba/var/log.%m': No such file or directory
[2023/10/04 14:59:46.257664,  0] ../../lib/util/debug.c:1263(reopen_one_log)
  reopen_one_log: Unable to open new log file '/usr/local/samba/var/log.%m': No such file or directory
[2023/10/04 14:59:46.257683,  0] ../../source4/samba/server.c:633(binary_smbd_main)
  samba version 4.19.0 started.
  Copyright Andrew Tridgell and the Samba Team 1992-2023
[2023/10/04 14:59:46.257713,  0] ../../lib/util/become_daemon.c:150(daemon_status)
  daemon_status: daemon 'samba' : Starting process...
[2023/10/04 14:59:46.278300,  0] ../../source4/samba/server.c:863(binary_smbd_main)
  At this time the 'samba' binary should only be used for either:
  'server role = active directory domain controller' or the rpc proxy with 'dcerpc endpoint servers = remote'
  You should start smbd/nmbd/winbindd instead for domain member and standalone file server tasks
[2023/10/04 14:59:46.278331,  0] ../../lib/util/become_daemon.c:119(exit_daemon)
  exit_daemon: daemon failed to start: Samba detected misconfigured 'server role' and exited. Check logs for details, error code 22
[2023/10/04 15:02:42,  0] ../../lib/util/debug.c:1263(reopen_one_log)
  reopen_one_log: Unable to open new log file '/usr/local/samba/var/log.%m': No such file or directory
[2023/10/04 15:02:42.297504,  0] ../../lib/util/debug.c:1263(reopen_one_log)
  reopen_one_log: Unable to open new log file '/usr/local/samba/var/log.%m': No such file or directory
[2023/10/04 15:02:42.297521,  0] ../../source4/samba/server.c:633(binary_smbd_main)
  samba version 4.19.0 started.
  Copyright Andrew Tridgell and the Samba Team 1992-2023
[2023/10/04 15:02:42.297543,  0] ../../lib/util/become_daemon.c:150(daemon_status)
  daemon_status: daemon 'samba' : Starting process...
[2023/10/04 15:02:42.347954,  0] ../../source4/samba/server.c:863(binary_smbd_main)
  At this time the 'samba' binary should only be used for either:
  'server role = active directory domain controller' or the rpc proxy with 'dcerpc endpoint servers = remote'
  You should start smbd/nmbd/winbindd instead for domain member and standalone file server tasks
[2023/10/04 15:02:42.347984,  0] ../../lib/util/become_daemon.c:119(exit_daemon)
  exit_daemon: daemon failed to start: Samba detected misconfigured 'server role' and exited. Check logs for details, error code 22

**Response:**
The error message suggests that Samba is unable to open the log files because they do not exist in the specified location '/usr/local/samba/var/log.%m'. 

To fix this issue, you can follow these steps:

1. Create the directory where the log files will be stored:
   ```bash
   sudo mkdir -p /var/log/samba
   ```

2. Change the log file directory in the Samba configuration file:
   ```bash
   sudo nano /etc/samba/smb.conf
   ```

   Locate the following lines (usually at the beginning of the file):
   ```
   # log directory = /usr/local/samba/var/log.%m
   # max log size = 1000
   ```

   Uncomment these lines and change the log directory to the newly created directory:
   ```
   log directory = /var/log/samba
   max log size = 1000
   ```

   Save the file and exit the text editor.

3. Restart the Samba service:
   ```bash
   sudo systemctl restart smb.service
   ```

   This will restart the Samba service and apply the changes.

After following these steps, the Samba service should be able to create and write to the log files without any errors.

<details><summary>Metadata</summary>

- Duration: 7989 ms
- Datetime: 2023-10-04T14:23:01.845805
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

