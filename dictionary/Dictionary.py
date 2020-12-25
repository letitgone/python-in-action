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

