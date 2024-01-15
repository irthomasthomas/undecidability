**Prompt:**
I have ssh working. Now how do I rdp through it?

**Response:**
To remotely connect to a machine using RDP (Remote Desktop Protocol) through an SSH tunnel, you can follow these steps:

1. Establish the SSH tunnel: Open a terminal or command prompt on your local machine and enter the following command:
```
ssh -L <local port>:<RDP server IP>:<RDP port> <SSH username>@<SSH server IP>
```
Replace `<local port>` with any available local port number of your choice (e.g., 8888), `<RDP server IP>` with the IP address of the machine you want to connect to via RDP, `<RDP port>` with the RDP port number (default: 3389), `<SSH username>` with your SSH username, and `<SSH server IP>` with the IP address of the SSH server.

2. Enter SSH credentials: After running the command, you will be prompted to enter your SSH account password.

3. Connect through RDP: Once the SSH tunnel is established, open the Remote Desktop client on your local machine (Windows: Start Menu -> Remote Desktop Connection, Mac: Finder -> Applications -> Remote Desktop Connection). In the Remote Desktop client, enter `localhost:<local port>` as the computer address, where `<local port>` is the port number you chose in step 1.

4. Enter RDP credentials: Click on connect, and you will be prompted to enter the username and password of the machine you are connecting to via RDP. Enter the credentials and click OK.

If everything is set up correctly, you should now be connected to the remote machine using RDP through the established SSH tunnel.

<details><summary>Metadata</summary>

- Duration: 13460 ms
- Datetime: 2023-09-24T12:01:16.267741
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

