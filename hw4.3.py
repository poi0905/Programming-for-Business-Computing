d = int(input())
n = int(input())

stocks = []  # 用來存n*d+1的stocks特徵
result = []  # 存預測錯誤數
# 輸入資料
for i in range(n):
    stocks.append([int(j) for j in input().split(",")])

# for i in range (n):
#     print(stocks[i])

resultcount = 0
for j in range(d):  # d個特徵
    for i in range(n):  # n支股票
        x = stocks[i][j]    # 找到x，要比大小的特徵
        for l in range(2):  # 預測上漲或下跌(兩種狀況, 0是下跌, 1是上漲)
            result.append(int(0))   # 先加入初始錯誤數(0)
            for k in range(n):  # 預測n支股票
                if x >= stocks[k][j]:
                    if stocks[k][d] == -1 and l == 1:
                        result[resultcount] += 1
                    if stocks[k][d] == 1 and l == 0:
                        result[resultcount] += 1
                else:
                    if stocks[k][d] == 1 and l == 1:
                        result[resultcount] += 1
                    if stocks[k][d] == -1 and l == 0:
                        result[resultcount] += 1           
            resultcount += 1    # 有2d個可能的標準

# print(result)

print(min(result))
