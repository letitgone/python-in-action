# @Author ZhangGJ
# @Date 2020/12/31 10:56

import json

numbers = [2, 3, 5, 7, 11, 13]
filename = '../../resources/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

filename = '../../resources/numbers.json'
with open(filename) as f:
    number = json.load(f)

print(number)
