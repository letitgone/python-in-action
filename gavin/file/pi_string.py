# @Author ZhangGJ
# @Date 2020/12/30 18:05

filename = '../../resources/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
