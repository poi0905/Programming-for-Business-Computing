x = input().split(',')
y = input().split(',')
# 安打數
a = x.count('o')
b = y.count('o')
# 保送數
c = x.count('-')
d = y.count('-')
# 打席
e = len(x)
f = len(y)
# 打數
g = e - c
h = f - d


if a * h > b * g:
    print('1,' + str(a))
if a * h < b * g:
    print('2,' + str(b))
if a * h == b * g:
    if a >= b:
        print('1,' + str(a))
    else:
        print('2,' + str(b))
