**Prompt:**
Think carefully. As a Manjaro/Arch linux and KDE Plasma expert. What is the basic algorithm for getting ssh running so I can connect to this pc from outside the network?

**Response:**
To connect to the Manjaro/Arch Linux machine via SSH from an external network, there are a few steps you need to follow. The key steps involved are:

1. Installing the SSH server
2. Configuring the SSH server
3. Port forwarding
4. Finding the public IP of your network
5. Connecting via SSH

The detailed algorithm with a step-by-step guide is as follows:

Step 1: Install the SSH server

On Arch or Manjaro, you can install the OpenSSH package with a command like:
```
sudo pacman -Syu openssh
```

Step 2: Configuring the SSH server

1. Open the SSH config file (`/etc/ssh/sshd_config`) in a text editor (e.g., nano, vi, etc.).
2. Make sure that the following lines are in the config file and are uncommented:

```
PermitRootLogin no
PubkeyAuthentication yes
AllowUsers your-username
```
3. Save your changes and close the file when you are finished.

Step 3: Enable the SSH server to start automatically at boot 

This can be done with systemctl:
```
sudo systemctl enable sshd.service
```
To start the SSH service immediately, you can use:
```
sudo systemctl start sshd.service
```

Step 4: Set up port forwarding on your router

This process can vary by router manufacturer and model. You would add a rule to forward TCP port 22 (the standard SSH port) to the internal (private) IP address of your Arch/Manjaro machine.

Step 5: Find the public IP address of your network

Many websites can do this for you. Note that if your internet service provider uses dynamic IPs, this address may change.

Step 6: Connecting to the SSH Server

From a remote system, you can typically SSH into your Arch Linux system via the command:

```
ssh your-username@your-public-ip
```

Remember that security is paramount when exposing SSH to the public internet. Always use strong, unique passwords, and consider adding additional security measures such as using public key authentication and changing the default SSH port. 

**Important**: Make sure to follow all local and network policy regulations when exposing a local system to the public internet.

<details><summary>Metadata</summary>

- Duration: 29649 ms
- Datetime: 2023-09-24T09:23:20.878928
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

