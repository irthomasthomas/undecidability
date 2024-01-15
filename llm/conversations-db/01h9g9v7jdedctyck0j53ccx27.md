**Prompt:**
Help, in arch linux, how do I permenantly set the cpu governor?

**Response:**
To permanently set the CPU governor in Arch Linux, you can use the following steps:

1. Open a terminal.

2. Determine the available CPU governors by running the following command:
```shell
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_available_governors
```

3. Select the desired CPU governor from the list obtained in the previous step. For example, if you want to set the governor to "performance," run the following command:
```shell
sudo echo "governor_name" | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```
Replace "governor_name" with the selected governor from the list.

4. Verify the change by checking the CPU governor using the following command:
```shell
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```

The governor you set should appear for all CPU cores.

5. To make the changes persistent across reboots, you can create a systemd service. Open a text editor and create a file called `cpugovernor.service` with the following contents:
```shell
sudo systemctl edit --force --full cpugovernor.service
```
Insert the following lines into the file:
```shell
[Unit]
Description=Set CPU governor
After=systemd-modules-load.service

[Service]
ExecStart=/usr/bin/sh -c 'echo "governor_name" > /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor'

[Install]
WantedBy=multi-user.target
```
Replace "governor_name" with the governor of your choice.

6. Save and exit the text editor.

7. Enable and start the `cpugovernor` service by running the following commands:
```shell
sudo systemctl enable cpugovernor.service
sudo systemctl start cpugovernor.service
```
This will ensure the CPU governor is set at boot time.

Now, your selected CPU governor will be persistent across reboots in your Arch Linux system.

<details><summary>Metadata</summary>

- Duration: 19240 ms
- Datetime: 2023-09-04T14:33:57.796276
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

