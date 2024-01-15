**Prompt:**

Reply only with the text of the bash script and nothing else before or after. Use code comments if you need to draw attention to anything. 
Think it through step-by-step.
# Additional Goals: Minimise IF statements and branching. Write intelligent, self-documenting code. Minimise duplication. Minimise Verbosity. Write code that is modern, clean and fast. Prefer answers dated 2015, 2016, 2017, 2018, 2019, 2020, 2021.
WARNING: Your response must NOT include text OUTSIDE of the code block. Beware of bugs and tricky syntax. SAY NOTHING ELSE!


**Response:**
```bash
#!/bin/bash

# Check if the script is being run as root
if [[ $(id -u) -ne 0 ]]; then
    echo "This script must be run as root."
    exit 1
fi

# Store the current date and time
datetime=$(date +"%Y-%m-%d %H:%M:%S")

# Print the current date and time
echo "Current date and time: $datetime"

# Get the hostname
hostname=$(hostname)

# Print the hostname
echo "Hostname: $hostname"

# Get the current user
current_user=$(whoami)

# Print the current user
echo "Current user: $current_user"

# Get the number of CPUs
cpu_count=$(grep -c processor /proc/cpuinfo)

# Print the number of CPUs
echo "Number of CPUs: $cpu_count"

# Get the amount of free memory
free_memory=$(free -m | awk 'NR==2{print $4}')

# Print the amount of free memory
echo "Free memory: $free_memory MB"
```

<details><summary>Metadata</summary>

- Duration: 7849 ms
- Datetime: 2023-07-20T12:45:30.099893
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

