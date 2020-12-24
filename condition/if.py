# @Author ZhangGJ
# @Date 2020/12/24 08:05

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

for car in cars:
    if car == 'bmw' and car != '':
        print(car.upper())
    if car != 'bmw' or car != 'toyota':
        print(car.title())
