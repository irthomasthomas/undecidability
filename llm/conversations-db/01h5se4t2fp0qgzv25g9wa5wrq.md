**Prompt:**
Think it through carefully. Using Manjaro/Arch Linux,Kernel 6,KDE Plasma 5.2,QT5,Python 3.10 

Write the commands needed to install this on linux. SAY NOTHING EXCEPT CODE.

**Response:**
sudo pacman -Syu
sudo pacman -S base-devel git
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
yay -S linux=6
yay -S kde-plasma-desktop
yay -S qt5-base
yay -S python3.10

<details><summary>Metadata</summary>

- Duration: 2668 ms
- Datetime: 2023-07-20T10:39:45.122300
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

