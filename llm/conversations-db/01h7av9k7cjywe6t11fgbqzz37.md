**Prompt:**
reinstall nvidia after adding a second card on manjaro?

**Response:**
To reinstall Nvidia drivers after adding a second card on Manjaro, follow the steps below:

Step 1: Uninstall current Nvidia drivers

Open the terminal and run the following command:

```
sudo mhwd -r pci video-nvidia
```
This will remove the current Nvidia drivers installed on the system.

Step 2: Detect and install new drivers

Next, you want Manjaro to detect your cards and install the correct drivers. Run the following command in the terminal:

```
sudo mhwd -a pci nonfree 0300
```
This command tells Manjaro to automatically install the best proprietary drivers for all PCI devices of class 0300.

Step 3: Verify installation

To check if the correct drivers have been installed, run the following command:

```
mhwd -li
```
This command will list installed drivers. You should see 'video-nvidia' in the output indicating that Nvidia drivers have been installed successfully.

Step 4: Reboot your system

Reboot your system with the following command globally:

```
reboot
```
After the system reboots, your new card should be working properly.

<details><summary>Metadata</summary>

- Duration: 35210 ms
- Datetime: 2023-08-08T15:11:48.065301
- Model: gpt-4-0613

</details>

**Options:**
```json
{}
```

