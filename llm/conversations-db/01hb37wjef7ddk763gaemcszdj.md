**Prompt:**
Think carefully. As a Manjaro/Arch linux and KDE Plasma expert. What is the basic algorithm for getting ssh running so I can connect to this pc from outside the network?

**Response:**
To enable SSH access to your computer from outside the network, you would need to perform the following steps:

1. Install the OpenSSH server: If you don't already have it, install the OpenSSH server on your Manjaro/Arch Linux system. You can do this by running the following command in the terminal:
   ```
   sudo pacman -S openssh
   ```

2. Configure the SSH server: Open the SSH server configuration file in a text editor. In Manjaro/Arch Linux, this file is located at `/etc/ssh/sshd_config`. Make sure the following settings are configured correctly:

   a. Set the `Port` directive to the desired port number (e.g., `Port 22`).

   b. Uncomment the `#PermitRootLogin` line and set it to `yes` if you wish to allow root login remotely. Otherwise, it is recommended to leave it as `no` and use a non-root user for SSH access.

   c. If you have a firewall enabled, ensure that it allows incoming connections on the SSH port.

   d. Save the changes and exit the editor.

3. Start and enable the SSH service: Run the following commands to start and enable the SSH service to run on system boot:
   ```
   sudo systemctl start sshd
   sudo systemctl enable sshd
   ```

4. Configure port forwarding on your router: To allow incoming SSH connections from outside the network, you need to configure port forwarding on your router. Typically, this involves accessing your router's settings web interface and adding a port forwarding rule that directs incoming SSH traffic on the specific port (e.g., 22) to your computer's local IP address.

5. Obtain your public IP address: Determine your public IP address, which will be needed when connecting remotely. You can search "What is my IP" on a search engine to find your public IP.

6. Test the SSH connection: From outside the network, open a terminal and use the `ssh` command, specifying your username and the public IP of your system. For example:
   ```
   ssh username@your_public_ip -p port_number
   ```
   Replace `username` with your actual username, `your_public_ip` with your public IP address, and `port_number` with the port you configured in the SSH server.

If all the steps are followed correctly, you should be able to establish an SSH connection to your Manjaro/Arch Linux system from outside the network.

<details><summary>Metadata</summary>

- Duration: 22327 ms
- Datetime: 2023-09-24T09:20:57.489074
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

