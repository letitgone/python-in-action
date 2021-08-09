# @Author ZhangGJ
# @Date 2021/08/09 10:00
lax_coordinates = (33.234, -118.2342)
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

print(divmod(20, 8))

t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)
print(quotient)
print(remainder)

import os

_, filename = os.path.split('/Users/zhanggj/Downloads/development-environment')
print(filename)

a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)
*head, b, c, d = range(5)
print(head, b, c, d)
