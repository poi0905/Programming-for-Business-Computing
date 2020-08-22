r = 0   # 需求趨勢係數
y = 0   # 預測值
recordStr = input()
record = recordStr.split(" ")
for i in range(6):
    record[i] = int(record[i])

r = (record[3] + record[4] + record[5])/(record[0] + record[1] + record[2])

multiplierStr = input()
multiplier = multiplierStr.split(" ")
for i in range(9):
    multiplier[i] = float(multiplier[i])

data = (record[2] + record[3] + record[4] + record[5]) / 4

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

if y * 10 % 10 == 0.0:
    print(int(y))
else:
    print(int(y) + 1)
