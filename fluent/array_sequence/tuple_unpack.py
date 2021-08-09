# @Author ZhangGJ
# @Date 2021/08/09 10:00

import os

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

metro_areas = [
    ('Tokyo', 'JP', '36.933', (35.345, 139.3432)),
    ('Delhi Ncp', 'IN', '21.933', (328.345, 77.3432)),
    ('Mexico City', 'MX', '20.933', (19.345, -99.3432)),
    ('New York-Newark', 'US', '20.933', (40.345, -74.3432)),
    ('Sao Paulo', 'BR', '19.933', (-23.345, -46.3432)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
