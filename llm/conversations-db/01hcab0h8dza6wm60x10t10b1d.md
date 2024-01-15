**Prompt:**
Write a bash script to copy each directory to /usr/share/icons for each file:///run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/Backups/2023/manjaro/usr/share/icons/HighContrast
file:///run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/Backups/2023/manjaro/usr/share/icons/Humanity
file:///run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/Backups/2023/manjaro/usr/share/icons/KDE_Classic
file:///run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/Backups/2023/manjaro/usr/share/icons/manjaro
file:///run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/Backups/2023/manjaro/usr/share/icons/oxygen
file:///run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/Backups/2023/manjaro/usr/share/icons/Oxygen_Black
file:///run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/Backups/2023/manjaro/usr/share/icons/Oxygen_Blue
file:///run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/Backups/2023/manjaro/usr/share/icons/Oxygen_White
file:///run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/Backups/2023/manjaro/usr/share/icons/Oxygen_Yellow
file:///run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/Backups/2023/manjaro/usr/share/icons/Oxygen_Zion
file:///run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/Backups/2023/manjaro/usr/share/icons/ubuntu-mono-dark
file:///run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/Backups/2023/manjaro/usr/share/icons/ubuntu-mono-light

**Response:**
#!/bin/bash

# Define the source directory
source_directory="/run/media/thomas/bc9be617-d7f1-4348-9c91-abe485c61dd5/Backups/2023/manjaro/usr/share/icons"

# Define the target directory
target_directory="/usr/share/icons"

# Array of directories to copy
directories=(
  "HighContrast"
  "Humanity"
  "KDE_Classic"
  "manjaro"
  "oxygen"
  "Oxygen_Black"
  "Oxygen_Blue"
  "Oxygen_White"
  "Oxygen_Yellow"
  "Oxygen_Zion"
  "ubuntu-mono-dark"
  "ubuntu-mono-light"
)

# Loop through the directories array and copy each directory
for directory in "${directories[@]}"
do
  cp -r "$source_directory/$directory" "$target_directory"
done


<details><summary>Metadata</summary>

- Duration: 5262 ms
- Datetime: 2023-10-09T13:46:12.990244
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

