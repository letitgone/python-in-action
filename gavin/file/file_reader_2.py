# @Author ZhangGJ
# @Date 2020/12/30 17:41

with open('../../resources/pi_digits.txt') \
        as file_object:
    for line in file_object:
        print(line.rstrip())
