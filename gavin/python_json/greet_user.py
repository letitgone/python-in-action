# @Author ZhangGJ
# @Date 2020/12/31 11:24

import json

filename = '../../resources/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
