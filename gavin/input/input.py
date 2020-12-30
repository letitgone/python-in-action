# @Author ZhangGJ
# @Date 2020/12/28 11:41

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}")

prompt = "If you tell us who are you, wo can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}")

age = input("How old are you? ")
print(age)

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride! ")
else:
    print("\nYou'll be able to ride when you're a little older.")

number = int(input("Enter a number, and I'll tell you if it's even or odd: "))
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd. ")
