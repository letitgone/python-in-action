# @Author ZhangGJ
# @Date 2020/12/21 23:23

message = "i love you"
print(message.title())
print(message.upper())
print(message.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# f字符是Python3.6引入的，Python3.5或更早的版本需要使用format()方法。
full_name = "{} {}".format(first_name, last_name)
print(f"Hello, {full_name}!")

print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

favorite_language = 'python '
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)
favorite_language = favorite_language.lstrip()
favorite_language = favorite_language.strip()
