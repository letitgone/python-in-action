# @Author ZhangGJ
# @Date 2020/12/25 22:00

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 在python3.7中，字段中的元素的排列顺序与定义时相同。
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'color': "green"}
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] = x_increment
print(f"New position: {alien_0['x_position']}")

del alien_0['speed']

alien_0 = {'color': 'green', 'speed': "slow"}
point_value = alien_0.get('point', 'No point value assigned')
print(point_value)

user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"value: {value}")

for key in user_0.keys():
    print(key.title())

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for key in sorted(favorite_language.keys()):
    print(key)

print("-----------------------------------------")
for value in favorite_language.values():
    print(value)
print("-----------------------------------------")
for value in set(favorite_language.values()):
    print(value)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
print("-----------------------------------------")
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')

print(f"Total number of aliens: {len(aliens)}")

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"You ordered a {pizza['crust']}-crust pizza"
      f"with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
