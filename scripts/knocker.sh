#!/bin/bash

# Super simple script by nox :))
# sudo apt-get install knockd

IP=<Target-IP>
echo "$IP"
echo "[*] Knocking ports.."
for port in {0..65535}
do
	echo "[*] Knocking port $port"
	knock $IP $port
	sleep 0.5
done

echo "[+] Knocking done!"