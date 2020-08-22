dataStr = input()
data = dataStr.split(",")
for i in range(5):
    data[i] = int(data[i])
# data[0] = day_gap
# data[1] = bf_pay
# data[2] = af_pay
# data[3] = c
# data[4] = n(工作時段時段總數)

# 各時段單數
DStr = input()
D = DStr.split(",")
for i in range(data[4]):
    D[i] = int(D[i])

profit = 0
a = -999999999  # 找一個很小的數，只是讓它被取代
num = 0

for i in range(data[4]):
    num += D[i]

    if num >= data[0]:
        profit = data[0] * data[1] + (num - data[0]) * data[2] - (i+1) * data[3]
    else:
        profit = num * data[1] - (i + 1) * data[3]

    if profit > a:
        a = profit
        A = str(a)
        i = i + 1
        T = str(i)

print(T + ',' + A)
