def sales_sum(product_cnt, day_cnt, quantities, prices):
    # 計算所有商品所有日子合計總銷售金額（S），回傳值 S 為一個數值
    sales_sum = 0
    for i in range(product_cnt):
        for j in range(day_cnt):
            num = 0
            num += quantities[i][j]
            sales = prices[i] * num
            sales_sum += sales
    return sales_sum


def daily_sales(product_cnt, day_cnt, quantities, prices):
    # 計算每日銷售金額（D1,D1,...,Dt），傳回值為一個List
    daily_sales = []
    for j in range(day_cnt):
        num = 0
        for i in range(product_cnt):
            num += prices[i] * quantities[i][j]
        daily_sales.append(num)
    return daily_sales


def daily_avg(product_cnt, day_cnt, quantities, prices):
    # 計算平均每日銷售金額（AD），傳回值 AD 為一個數值
    daily_sales = []
    sum = 0
    daily_avg = 0
    for j in range(day_cnt):
        num = 0
        for i in range(product_cnt):
            num += prices[i] * quantities[i][j]
        daily_sales.append(num)
    for i in range(len(daily_sales)):
        sum += daily_sales[i]
    daily_avg = sum / day_cnt
    return daily_avg


def goods_sales(product_cnt, day_cnt, quantities, prices):
    # 計算各商品總銷售金額（G1,G2,...,Gn），傳回值為一個List
    good_sales = []
    for i in range(product_cnt):
        num = 0
        for j in range(day_cnt):
            num += quantities[i][j]
            sales = prices[i] * num
        good_sales.append(sales)
    return good_sales


def goods_avg(product_cnt, day_cnt, quantities, prices):
    # 計算各項商品平均每日銷售金額（AG1,AG2,...,AGn），傳回值為一個List
    goods_avg = []
    for i in range(product_cnt):
        num = 0
        for j in range(day_cnt):
            num += quantities[i][j]
            sales = prices[i] * num
            sales_avg = sales // day_cnt
        goods_avg.append(sales_avg)
    return goods_avg


def best_day(product_cnt, day_cnt, quantities, prices):
    # 平均銷售金額最高為星期幾（W），傳回值 W 為一個數值
    daily_sales = []
    for j in range(day_cnt):
        num = 0
        for i in range(product_cnt):
            num += prices[i] * quantities[i][j]
        daily_sales.append(num)
    b = len(daily_sales)
    c = b % 7   # 取餘數分類
    sales1 = []
    sales2 = []
    sales3 = []
    sales4 = []
    sales5 = []
    sales6 = []
    sales7 = []
    avg1 = 0
    a1 = 0
    avg2 = 0
    a2 = 0
    avg3 = 0
    a3 = 0
    avg4 = 0
    a4 = 0
    avg5 = 0
    a5 = 0
    avg6 = 0
    a6 = 0
    avg7 = 0
    a7 = 0
    avg = []
    for i in range(b):
        if i % 7 == 0:
            sales1.append(daily_sales[i])
        if i % 7 == 1:
            sales2.append(daily_sales[i])
        if i % 7 == 2:
            sales3.append(daily_sales[i])
        if i % 7 == 3:
            sales4.append(daily_sales[i])
        if i % 7 == 4:
            sales5.append(daily_sales[i])
        if i % 7 == 5:
            sales6.append(daily_sales[i])
        if i % 7 == 6:
            sales7.append(daily_sales[i])
    for i in range(len(sales1)):
        a1 += sales1[i]
        avg1 = a1 / len(sales1)
    for i in range(len(sales2)):
        a2 += sales2[i]
        avg2 = a2 / len(sales2)
    for i in range(len(sales3)):
        a3 += sales3[i]
        avg3 = a3 / len(sales3)
    for i in range(len(sales4)):
        a4 += sales4[i]
        avg4 = a4 / len(sales4)
    for i in range(len(sales5)):
        a5 += sales5[i]
        avg5 = a5 / len(sales5)
    for i in range(len(sales6)):
        a6 += sales6[i]
        avg6 = a6 / len(sales6)
    for i in range(len(sales7)):
        a7 += sales7[i]
        avg7 = a7 / len(sales7)
    avg.append(avg1)
    avg.append(avg2)
    avg.append(avg3)
    avg.append(avg4)
    avg.append(avg5)
    avg.append(avg6)
    avg.append(avg7)
    answer = max(avg)
    best_day = avg.index(answer) + 1
    return best_day


data = []
prices = []
quantities = []
required = []
data = [int(i) for i in input().split(',')]
product_cnt = data[0]
day_cnt = data[1]
prices = [int(i) for i in input().split(',')]
for i in range(product_cnt):
    quantities.append([int(j) for j in input().split(",")])
required = [int(i) for i in input().split(',')]

if 1 in required:
    print(sales_sum(product_cnt, day_cnt, quantities, prices))

if 2 in required:
    a = len(daily_sales(product_cnt, day_cnt, quantities, prices))
    for i in range(a - 1):
        print(daily_sales(product_cnt, day_cnt, quantities, prices)[i], end=',')
    print(daily_sales(product_cnt, day_cnt, quantities, prices)[a - 1])

if 3 in required:
    print(int(daily_avg(product_cnt, day_cnt, quantities, prices)))

if 4 in required:
    a = len(goods_sales(product_cnt, day_cnt, quantities, prices))
    for i in range(a - 1):
        print(goods_sales(product_cnt, day_cnt, quantities, prices)[i], end=',')
    print(goods_sales(product_cnt, day_cnt, quantities, prices)[a - 1])

if 5 in required:
    a = len(goods_avg(product_cnt, day_cnt, quantities, prices))
    for i in range(a - 1):
        print(goods_avg(product_cnt, day_cnt, quantities, prices)[i], end=',')
    print(goods_avg(product_cnt, day_cnt, quantities, prices)[a - 1])

if 6 in required:
    print(best_day(product_cnt, day_cnt, quantities, prices))
