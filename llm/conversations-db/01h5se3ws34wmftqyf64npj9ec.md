**Prompt:**
Think it through carefully. Using Manjaro/Arch Linux,Kernel 6,KDE Plasma 5.2,QT5,Python 3.10 

Write the commands needed to install this on linux. SAY NOTHING EXCEPT THE COMMANDS.

**Response:**
sudo pacman -Syu
sudo pacman -S base-devel
sudo pacman -S git
sudo pacman -S linux-headers
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
yay -S manjaro-kde-settings
yay -S qt5-base
yay -S python
yay -S python-pip
pip install pyqt5
pip install pyqt5-tools

<details><summary>Metadata</summary>

- Duration: 3429 ms
- Datetime: 2023-07-20T10:39:14.365829
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

