x = str(input())
data = input().split(',')
if data.count(x) == 0:
    print('0,0')
else:
    print(str(data.count(x)) + ',' + str(data.index(x) + 1))
    