# @Author ZhangGJ
# @Date 2021/08/05 17:21
import array

symbols = '$#&$I@&^'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

codes = [ord(symbol) for symbol in symbols]
print(codes)

beyond_ascii = [ord(s) for s in symbols if ord(s) < 127]
print(beyond_ascii)

beyond_ascii1 = list(filter(lambda c: c < 127, map(ord, symbols)))
print(beyond_ascii1)

tuple_1 = tuple(ord(symbol) for symbol in symbols)
print(tuple_1)

tuple_array = array.array('I', (ord(symbol) for symbol in symbols))
print(tuple_array)
