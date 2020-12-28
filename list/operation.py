# @Author ZhangGJ
# @Date 2020/12/24 07:10

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

for value in range(1, 5):
    print(value)

numbers = list(range(1, 5))
print(numbers)

numbers = list(range(2, 11, 2))
print(numbers)

# **表示乘方运算
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

digits = range(0, 10)
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)
print('---------------------------------------------')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:2])
print(players[1:])
print(players[-3:])

for value in players[:3]:
    print(value)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)
my_foods[1] = 'noodle'
print(my_foods)
print(friend_foods)

friend_foods = my_foods
print(my_foods)
print(friend_foods)

# 元组：不可变的列表
dimensions = (200, 50)
print(dimensions)
