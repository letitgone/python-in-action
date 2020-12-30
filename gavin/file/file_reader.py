# @Author ZhangGJ
# @Date 2020/12/30 17:19

with open('../../resources/pi_digits.txt') \
        as file_object:
    contents = file_object.read()
print(contents)
print(contents.rstrip())
