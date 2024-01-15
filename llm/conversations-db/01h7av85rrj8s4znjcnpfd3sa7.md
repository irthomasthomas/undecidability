**Prompt:**
reinstall nvidia after adding a second card on manjaro?

**Response:**
To reinstall Nvidia drivers after adding a second card on Manjaro, you can follow these steps:

1. Start by booting into your Manjaro system with the first Nvidia card already installed.

2. Open a terminal by pressing Ctrl + Alt + T.

3. Update your system's package database by executing the following command:
```
sudo pacman -Sy
```

4. Install the necessary packages for Nvidia drivers:
```
sudo mhwd -a pci nonfree 0300
```

5. Reboot your system:
```
sudo reboot
```

6. After the system restarts, it should be back up using the Nvidia drivers. Confirm by checking the driver status using the following command:
```
nvidia-smi
```

7. Now that Nvidia drivers are up and running, you can proceed to add your second Nvidia card physically to your system.

8. Shut down your system and add the second Nvidia card to an available PCI slot.

9. Restart your system.

10. Once the system is back up, open a terminal and update your package database again:
```
sudo pacman -Sy
```

11. Install the necessary drivers for the second Nvidia card:
```
sudo mhwd -a pci nonfree 0300
```

12. Reboot your system once more:
```
sudo reboot
```

13. After the system restarts, it should detect the second Nvidia card and load the appropriate drivers. You can verify the status of both cards using the `nvidia-smi` command.

That's it! You have successfully reinstalled Nvidia drivers after adding a second card on Manjaro.

<details><summary>Metadata</summary>

- Duration: 13028 ms
- Datetime: 2023-08-08T15:11:23.699919
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

