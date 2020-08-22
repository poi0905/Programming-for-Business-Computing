r = 0   # 需求趨勢係數
y = 0   # 預測值
mae = 0  # 當分子
MAE = 0  # Mean Absolute Error
x = 0   # 等等裝答案
a = []  # 等等裝答案
n = int(input())    # 週數
recordStr = input()
record = recordStr.split(",")
for i in range(n):
    record[i] = int(record[i])

multiplierStr = input()
multiplier = multiplierStr.split(",")
for i in range(9):
    multiplier[i] = float(multiplier[i])

for i in range(6, n):
    data = (record[i - 4] + record[i - 3] + record[i - 2] + record[i - 1]) / 4
    r = (record[i - 3] + record[i - 2] + record[i - 1])/(record[i - 6] + record[i - 5] + record[i - 4])

    if 0 < r <= multiplier[0]:
        y = data * multiplier[4]
    elif multiplier[0] < r <= multiplier[1]:
        y = data * multiplier[5]
    elif multiplier[1] < r <= multiplier[2]:
        y = data * multiplier[6]
    elif multiplier[2] < r <= multiplier[3]:
        y = data * multiplier[7]
    elif multiplier[3] < r:
        y = data * multiplier[8]

    mae += abs(y - record[i])
    MAE = mae / (n - 6)

    if y * 10 % 10 == 0.0:
        b = int(y)
        a.append(b)
    else:
        b = int(y) + 1
        a.append(b)

if MAE * 10 % 10 == 0.0:
    x = int(MAE)
else:
    x = int(MAE) + 1

for i in range(n - 7):
    print(a[i], end = ',')
print(str(a[n - 7]) + ';' + str(x))
