**Debugging and Forensic Investigation Cheatsheet**

This cheatsheet outlines key commands and their purposes for investigating system issues, package changes, and suspicious activities based on Zaeem’s debugging workflow.

---

### **1. Inspect Package Installation and Updates**

#### **Check APT Package History**:
```bash
cat /var/log/apt/history.log
```
**Purpose**: View the history of packages installed or updated.

#### **Check Detailed Package Logs**:
```bash
cat /var/log/dpkg.log
cat /var/log/dpkg
```
**Purpose**: Analyze `dpkg` logs for detailed package management activities.

#### **Filter Logs for Specific Entries**:
```bash
grep -i systemd /var/log/dpkg.log
```
**Purpose**: Focus on entries related to `systemd` or other keywords.

#### **Inspect Post-Installation Scripts**:
```bash
ls -all /var/lib/dpkg/info/systemd.postinst
cat /var/lib/dpkg/info/systemd.postinst
```
**Purpose**: Check the post-installation script for suspicious or unauthorized changes.

#### **View APT Terminal Logs**:
```bash
cat /var/log/apt/term.log | grep -i systemd
```
**Purpose**: Analyze terminal outputs during package installations or updates.

#### **Check Last Successful APT Update**:
```bash
stat /var/lib/apt/periodic/update-success-stamp
```
**Purpose**: Verify the timestamp of the last successful APT update.

---

### **2. Analyze System Logs**

#### **APT Daily Service Logs**:
```bash
journalctl -u apt-daily.service --since today
journalctl -u apt-daily-upgrade.service
```
**Purpose**: View logs for automatic updates and upgrades.

#### **Search Authentication Logs**:
```bash
sudo grep "Jan 17" /var/log/auth.log
```
**Purpose**: Investigate login attempts, privilege escalations, or unauthorized access.

#### **Analyze Security Logs**:
```bash
cat /var/log/secure.log | grep -C 2 -i ubuntu
```
**Purpose**: Inspect security events and highlight occurrences related to a specific user.

---

### **3. Investigate User Activity**

#### **List Files in Home Directory**:
```bash
ls -all /home/ubuntu
```
**Purpose**: Check for suspicious files or altered permissions.

#### **Inspect Bash Command History**:
```bash
cat /home/ubuntu/.bash_history
```
**Purpose**: Review commands executed by the user for potential malicious activity.

#### **Search Command History for Specific Keywords**:
```bash
grep -iar C2 /home/ubuntu/.bash_history
grep -iar upgrade /home/ubuntu/.bash_history
```
**Purpose**: Locate potentially harmful or targeted commands.

---

### **4. Trace Process Execution**

#### **Filter Specific Processes**:
```bash
journalctl | grep adduser
```
**Purpose**: Focus on the `adduser` command and related logs.

#### **Trace Parent Process**:
```bash
cat /var/log/secure.log | grep "ParentProcessId"
```
**Purpose**: Identify the process chain leading up to the execution of a suspicious command.

---

### **5. Advanced Filtering and Analysis**

#### **Search Logs for Specific Events**:
```bash
cat /var/log/dpkg.log | grep -i postinst
cat /var/log/dpkg.log | grep -i configure | grep -i systemd
```
**Purpose**: Narrow down specific events related to package configuration or installation.

#### **Analyze Process Start Times**:
```bash
journalctl --since "YYYY-MM-DD HH:MM:SS" --until "YYYY-MM-DD HH:MM:SS"
```
**Purpose**: Narrow down logs to a specific timeframe.

#### **Sort and Identify Latest Events**:
```bash
ls -lt /var/log | head
```
**Purpose**: Identify and prioritize the latest log files for inspection.

---

### **6. General Log Management Commands**

#### **Display System Logs**:
```bash
journalctl -xe
```
**Purpose**: View recent system events with additional context.

#### **Export Logs for Offline Analysis**:
```bash
tar -czf logs.tar.gz /var/log
```
**Purpose**: Archive logs for external analysis or forensic review.

---

### **Best Practices During Investigation**

1. **Filter Noise**:
   - Use `grep`, `awk`, or `sed` to focus on relevant entries.
   - Exclude benign processes or keywords (e.g., `systemd`, `cron`).

2. **Trace Process Trees**:
   - Use `ParentProcessId` or process tree visualizations to understand execution chains.

3. **Correlate Timeframes**:
   - Match timestamps between different logs (e.g., `auth.log` and `dpkg.log`) to identify related events.

4. **Preserve Evidence**:
   - Avoid altering files or logs during investigation. Create backups before making changes.

5. **Report Findings**:
   - Document suspicious activities, processes, and log entries for incident reporting.

---

By following this cheatsheet, you can systematically investigate suspicious activities, trace commands, and ensure comprehensive forensic analysis.

