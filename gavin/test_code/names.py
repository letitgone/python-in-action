# @Author ZhangGJ
# @Date 2020/12/31 14:22

from name_function import get_formatted_name

print("Enter 'q' at any time to quit. ")

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please gave me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly formatted name: {formatted_name}. ")
