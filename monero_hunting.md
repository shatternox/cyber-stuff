# Key Commands and Their Purpose

## Process Investigation (ps -aux or ps -fp):
Lists all processes to identify suspicious ones with high CPU usage or unusual names like "manager."

## Memory and File Descriptors (ls -l /proc/[pid]/fd):
Inspects file descriptors to locate memory-backed files or deleted binaries still in use.

## Inspect Deleted Files (`find /proc/*/fd -lname '*memfd:*'`):
Detects files loaded in memory but deleted, a common technique used by crypto miners to hide.

## Network Analysis (netstat -antp):
Checks open ports and active network connections related to the suspicious process.

## Dump Process Memory (cat /proc/[pid]/fd/[fd] > /tmp/memfd_deleted):
Extracts memory content for further analysis.

## Hashing Files (sha256sum):
Computes hashes of suspicious binaries for threat intelligence and comparison with known malware.

## Log Analysis (grep):
Searches logs for terms like "xmr" or "Monero" to identify crypto mining activities.

## Container Inspection (crictl):
Inspects Kubernetes containers to trace the source of malicious activity in containerized environments.


# CrowdStrike RTR Commands for Crypto Miner Detection

## 1. Process Investigation

- List all running processes to locate suspicious ones:
```bash
ps -aux | grep suspicious_name
ps -fp [pid]

ps -aux | grep manager
ps -fp 2327285
```

## 2. Inspect Memory and File Descriptors

- Check file descriptors of a specific process:
```bash
ls -l /proc/[pid]/fd

ls -l /proc/2327285/fd
```

- Find memory-backed files:
```bash
find /proc/*/fd -lname '*memfd:*' -ls
```

## 3. Check Deleted Memory Files

- List deleted memory files:
```bash
find /proc/*/fd -lname '*memfd:*' -exec ls -l {} \;

ls -alR /proc/*/exe 2>/dev/null | grep memfd:.*\(deleted\)
```

## 4. Network Analysis

- Check network connections for a specific process:
```bash
netstat -antp | grep [pid]
ss -tulnp

netstat -antp | grep 2327285
ss -aen | grep 2327285
```

## 5. Extract Memory for Analysis

-  Dump memory contents to a file:
```bash
cat /proc/[pid]/fd/[fd] > /tmp/memfd_deleted

cat /proc/2327285/fd/7 > /tmp/memfd_deleted
```

## 6. Compute File Hash

- Generate a SHA-256 hash of a suspicious file:
```bash
sha256sum /path/to/suspicious/file

sha256sum /tmp/memfd_deleted
```

## 7. Search Logs for Indicators

- Look for "xmr" (Monero) references in logs:
```bash
grep -ir 'xmr' /var/log/*
grep -ir 'supportxmr' /var/log/pods/
```

## 8. Container and Pod Investigation

- List running containers:
```bash
crictl ps
```

- Inspect a container for details:
```bash
crictl inspect [container_id]

crictl inspect 267feb78ebfbc
```

- Find Kubernetes pods:
```bash
kubectl get pods --all-namespaces
kubectl describe pod [pod_name] -n [namespace]

kubectl get pods --all-namespaces
kubectl describe pod kong-apps-public-tcp-controller-678798ff7c-cxm66 -n gateway
```

## 9. Dump and Analyze Suspicious Binary

- Search for Monero references in memory dump:
```bash
strings /tmp/memfd_deleted | grep -i monero
```

## 10. Identify Kubernetes Resources

- Get logs of a specific pod:
```bash
cat /var/log/pods/gateway_kong-apps-public-tcp-controller-678798ff7c-cxm66/ingress-controller/0.log

grep -i webhook /var/log/pods/gateway_kong-apps-public-tcp-controller-678798ff7c-cxm66/ingress-controller/0.log
```





















