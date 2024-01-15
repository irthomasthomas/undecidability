**Prompt:**
manjaro computer accessible from the web with ssh

**Response:**
If you want your Manjaro computer to be accessible from the web with SSH (Secure Shell), you will need to install and set up an SSH server on the device. However, be warned that doing so can have security implications, so you should only proceed if you are sure about what you're doing.

Here's a simple guide to configure SSH on Manjaro:

1. Open the Terminal from your computer.

2. Type the following into the Terminal and press Enter: 
   `sudo pacman -S openssh`

3. Once installed, start the SSH service by typing: 
   `sudo systemctl start sshd`

4. To ensure the SSH service starts automatically at boot, type in: 
   `sudo systemctl enable sshd`

5. To confirm that the SSH service is running, type: 
   `sudo systemctl status sshd`

Now, your SSH server is set up and running. If you want to connect to it, you would use your device's IP address, or, if you're doing this over the internet, your public IP address, along with the port number (22 by default).

Note: When making your Manjaro computer accessible from the web with SSH, make sure to harden your SSH server. Use unique user names and strong passwords, limit the number of login attempts, use SSH keys instead of passwords, and keep your system up-to-date.

Also, if your Manjaro computer is behind a router, you will need to configure port forwarding on the router for port 22 to your computer's local IP address. 

Remember, exposing your SSH server to the Internet can make it a target for hackers, so make sure you follow security best practices, and consider setting up a firewall also.

<details><summary>Metadata</summary>

- Duration: 38215 ms
- Datetime: 2023-08-16T09:24:54.770718
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

