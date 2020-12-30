# @Author ZhangGJ
# @Date 2020/12/30 17:44

filename = '../../resources/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
