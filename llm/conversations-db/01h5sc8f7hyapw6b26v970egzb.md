**Prompt:**
Quickly, what is the exact bash command to Automatic Installation on Linux
Install the dependencies:
# Debian-based:
sudo apt install wget git python3 python3-venv
# Red Hat-based:
sudo dnf install wget git python3
# Arch-based:
sudo pacman -S wget git python3
Navigate to the directory you would like the webui to be installed and execute the following command:
bash <(wget -qO- https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh)
Run webui.sh.?
Reply only with the exact command text and nothing else before or after.

**Response:**
bash <(wget -qO- https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh)

<details><summary>Metadata</summary>

- Duration: 1555 ms
- Datetime: 2023-07-20T10:06:49.053696
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

