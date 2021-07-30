# @Author ZhangGJ
# @Date 2021/03/29 14:30

import time

print(time.strftime('%Y%m%d%H%M', time.localtime()))

for n in range(2, 11):
    print(n)


s = [str(n) for n in range(2, 11)]
print(s)

ss = list('123123')
print(ss)
print(s + ss)

suits = 'spades diamonds clubs hearts'.split()
print(suits)