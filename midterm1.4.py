data = [int(i) for i in input().split(',')]
m = data[0]  # 作業數量
n = data[1]  # 學生個數
t = data[2]  # 門檻
score = []
a = []
b = 0
passnumber = 0
c = 0

for i in range(m):
    score.append([int(j) for j in input().split(",")])

for i in range(m):
    x = score[i]
    x.append(t)
    X = sorted(x)
    b = X.index(t)  # 標準所在位置
    passnumber = n - b
    # print(passnumber)
    if passnumber > c:
        c = passnumber
        I = i + 1
    if passnumber == c:
        c = passnumber
        I = i + 1
print(str(I) + ',' + str(c))
