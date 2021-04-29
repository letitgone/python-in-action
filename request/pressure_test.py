# @Author ZhangGJ
# @Date 2021/01/06 14:29

import requests
import json

url = 'localhost'

body = {
    "grant_type": "password",
    "username": "ghac",
    "password": "hifm-admin",
    "userType": 1
}

headers = {'Content-Type': 'application/json',
           'Authorization': 'Basic aGlmbToxMjM0NTY='}

data = json.dumps(body)
response = requests.post(url=url, data=data, headers=headers)
print("Success-------------------")