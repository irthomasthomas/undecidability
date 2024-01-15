**Prompt:**
Help, in arch linux, how do I permenantly set the cpu governor?

**Response:**
You can permanently set the CPU governor in Arch Linux by creating a service file that is linked to systemd, which will set the governor you want at each system boot. 

Here's an example for setting the CPU Governor to 'performance'. 

Firstly, create and edit a new service file:

```
sudo nano /etc/systemd/system/cpupower.service
```

Then copy and paste the following into the file:

```
[Unit]
Description=CPU governor to performance

[Service]
Type=oneshot
ExecStart=/usr/bin/cpupower frequency-set -g performance

[Install]
WantedBy=multi-user.target
```

Save the file and exit the editor (In nano, you can do this by pressing CTRL + X, then Y, then ENTER)

Now, enable the service so it starts automatically at boot:

```
sudo systemctl enable cpupower.service
```

And you can start it immediately without rebooting with:

```
sudo systemctl start cpupower.service
```

That's it! The 'cpupower' service will run at each boot and set the CPU governor to 'performance'.

Please replace 'performance' with your desired governor. Confirm the available governors on your system by entering the following command:

```
cpupower frequency-info --governors
```

Remember to check if you have `cpupower` program by running `cpupower --help`. If it's missing, you can install it by executing the following command:

```
sudo pacman -S cpupower
```
It's included in the linux-tools package which can be installed from the official repositories.

<details><summary>Metadata</summary>

- Duration: 34818 ms
- Datetime: 2023-09-04T14:34:22.100249
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

