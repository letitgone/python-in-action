# @Author ZhangGJ
# @Date 2021/01/27 23:24

lists = ['test0', 'test1', 'test2', 'test3', 'test4', 'test5']

print(f"访问索引位置元素:{lists[3]}")

print(f"访问倒数第一个元素:{lists[-1]}")
print(f"访问倒数第二个元素:{lists[-2]}")

lists.append('test6')
print(f"list末尾添加元素:{lists}")

lists.insert(3, 'insert')
print(f"固定索引位置添加:{lists}")

del lists[3]
print(f"删除固定索引位置元素:{lists}")

pop = lists.pop()
print(f"lists:{lists}")
print(f"弹出list末尾元素，并赋值给pop:{pop}")

pop = lists.pop(5)
print(f"lists:{lists}")
print(f"弹出固定索引位置元素，并赋值给pop:{pop}")

# remove只删除第一个指定的值
lists.remove('test4')
print(f"删除给定元素值的元素:{lists}")

print('===========================================================================================')

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(f"sort()永久修改列表元素顺序:{cars}")
