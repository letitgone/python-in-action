# @Author ZhangGJ
# @Date 2021/08/06 09:34

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color, size))

tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
