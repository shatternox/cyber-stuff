# Linux

Linux Incident Response and Forensics: 

Linux Incident Response and Forensics is the systematic process of detecting, analyzing, and mitigating security incidents on Linux systems while preserving and examining digital evidence.

Here are some essential commands and tools for investigating user activity, system resources, network settings, processes, services, log entries, and files.

User Accounts:
```cmd
$ echo $USER
$ passwd -S <USER>
$ grep :0: /etc/passwd
$ cat /etc/passwd
$ cat /etc/shadow
$ cat /etc/group
$ cat /etc/sudoers
```

General Information:
```cmd
$ date
$ cat /etc/timezone
$ uname -a
$ uname -m
$ cat /etc/*-release
$ hostname
$ cat /etc/hostname
```

System Resources:
```cmd
$ uptime
$ free
$ df
$ cat /proc/meminfo
$ cat /proc/mounts
```

Network Settings:
```cmd
$ ifconfig
$ lsof -i
$ netstat -ano
$ netstat -nap
$ netstat -antp
$ netstat -antp | grep "ESTAB"
$ netstat -rn
$ route
$ cat /etc/hosts
$ arp -a
$ echo $PATH
```

Processes:
```cmd
$ ps -aux
$ ps aux --sort=-%mem | head -n 10
$ top
$ htop
$ vmstat -s
$ lsof -p <PID>
$ pstree
```

Services:
```cmd
$ service --status-all
$ more /etc/hosts
$ more /etc/resolv.conf
$ cat /etc/crontab
$ crontab -u <USER> -l
$ tail -f /etc/cron.*/*
$ cat /etc/cron.daily
$ cat /etc/cron.hourly
$ cat /etc/cron.monthly
$ cat /etc/cron.weekly
```

Log Entries:
```cmd
$ lastlog
$ last
$ cat /var/log/lastlog
$ grep -v cron /var/log/auth.log* | grep -v sudo | grep -i user
$ grep -v cron /var/log/auth.log* | grep -v sudo | grep -i Accepted
$ grep -v cron /var/log/auth.log* | grep -v sudo | grep -i failed
$ grep -v cron /var/log/auth.log* | grep i "login:session"
```

Files:
```cmd
$ find /home/ -type f -size +512k -exec ls -lh {} \;
$ find /etc/ -readable -type f 2>/dev/null
$ find / –perm -4000 -user root -type f
$ find / -mtime -0 -ctime -7
$ find / -atime 2 -ls 2>/dev/null
$ find / -mtime -2 -ls 2>/dev/null
```

Review Activities:
```cmd
$ history
$ cat /home/$USER/.*_history
$ cat /home/$USER/.bash_history
$ cat /root/.bash_history
$ cat /root/.mysql_history
$ cat /home/$USER/.ftp_history
```
Persistence areas:

# Directories
/etc/cron*/
/etc/incron.d/*
/etc/init.d/*
/etc/rc*.d/*
/etc/systemd/system/*
/etc/update.d/*
/var/spool/cron/*
/var/spool/incron/*
/var/run/motd.d/*

# Files
/etc/passwd
/etc/sudoers
/home/<user>/.ssh/authorized_keys
/home/<user>/.bashrc

Tools for Linux Incident Response and Forensics:

• Network Monitoring: tcpdump, Wireshark, Bro/Zeek
• Log Analysis: logwatch, splunk, ELK stack
• Filesystem Analysis: sleuthkit, autopsy, extundelete
• Memory Analysis: volatility, lime
• Disk Imaging: dd, dcfldd
• System Monitoring: top, htop, ps, sar


