# @Author ZhangGJ
# @Date 2020/12/21 23:31

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
# 索引-1返回列表最后一个元素
print(bicycles[-1])
print(bicycles[-2])

message = f"My fist bicycle was a {bicycles[0].title()}"
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(1, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.pop(1)
print(motorcycles)

motorcycles.remove('suzuki')
print(motorcycles)

# sort永久排序
car = ['bmw', 'audi', 'toyota', 'subaru']
car.sort()
print(car)

car.sort(reverse=True)
print(car)
print("---------------------------------------")

# sorted临时排序
car = ['bmw', 'audi', 'toyota', 'subaru']
print(car)
print(sorted(car))
print(car)

# 反转列表
car.reverse()
print(car)

print(len(car))
