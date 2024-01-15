**Prompt:**
Can I start manjaro linux in shellmode with no desktop running, and then start a qemu vm to use as my main desktop?


**Response:**
Yes, you can start Manjaro Linux in a shell mode without the desktop environment running. To do this, you would need to switch to a TTY (Terminal) by pressing Ctrl + Alt + F2 (or any function key from F2 to F6). Then, you can log in with your username and password.

Once you are in the shell mode, you can install and run QEMU to create a virtual machine. However, running a virtual machine as your primary desktop environment may not provide the best performance and user experience. Additionally, any graphical applications or desktop-specific features may not be fully functional within the virtual machine.

If you still want to proceed with this setup, you can install QEMU using the package manager. For example, you can use the following command to install QEMU on Manjaro:

```
sudo pacman -S qemu
```

After the installation, you can use QEMU commands to create and run a virtual machine. Keep in mind that you may need to allocate enough resources (CPU, RAM, storage) to the virtual machine for it to run smoothly.

Please note that this setup might not be officially supported, and it is recommended to have a graphical desktop environment for a more seamless experience.

<details><summary>Metadata</summary>

- Duration: 11058 ms
- Datetime: 2023-09-20T14:08:54.134643
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

