**Prompt:**
Check which gpus are available in arch terminal?

**Response:**
To check which GPUs are available in Arch terminal, you can use the command `lspci` or `lsusb` along with the appropriate options. These commands list the PCI or USB devices respectively.

For GPU devices connected through the PCI bus, you can use the following command:

```
lspci | grep -i vga
```

This command lists all the PCI devices, and then filters the output to show only devices related to VGA (Video Graphics Adapter).

For GPU devices connected through USB, you can use the following command:

```
lsusb | grep -i -E 'vga|display|3d'
```

This command lists all the USB devices, and then filters the output to show devices that have "vga", "display", or "3d" in their descriptions.

These commands provide information about the available GPUs in your system.

<details><summary>Metadata</summary>

- Duration: 13842 ms
- Datetime: 2023-11-02T19:24:43.490491
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

