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

profit = 0
a = -999999999  # 找一個很小的數，只是讓它被取代
start = 0
end = 0

for i in range(data[4]):    # i當開始時段
    D[i] = int(D[i])
    num = 0  # 接單數
    for j in range(i, data[4]):    # j當結束時段
        D[j] = int(D[j])
        num += D[j]

        if num >= data[0]:
            profit = data[0] * data[1] + (num - data[0]) * data[2] - data[3] * (j - i + 1)
        else:
            profit = num * data[1] - data[3] * (j - i + 1)

        if profit > a:
            a = profit
            start = i
            end = j
        if profit == a:
            if j - i < end - start:  # 同profit找花較少時間
                end = j
                start = i
            if j - i == end - start:    # 同時數找較晚開始
                if i > start:
                    start = i
                    end = j

print(str(start + 1) + ',' + str(end + 1) + ',' + str(a))
