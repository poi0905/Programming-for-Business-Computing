oc = int(input())   # oc = opportunity cost
t = int(input())    # 產品種類數

earn = -oc  # 總金額
pay = 0  # 帳面價

for i in range(t):
    price = int(input())    # 價錢
    num = int(input())  # 人數
    if num >= 8:
        if num < 10:
            earn += num * 50 + (10 - num) * 0.1 * price
            pay += 10 * price * 0.9
        elif 18 > num >= 10:
            earn += num * 50
            pay += num * price * 0.9
        elif 20 > num >= 18:
            earn += num * 50 + (20 - num) * 0.2 * price
            pay += 20 * price * 0.8
        elif num >= 20:
            earn += num * 50
            pay += num * price * 0.8
    else:
        pay += price * num

if earn > 0:
    print(int(pay), int(earn))
else:
    print("Oops, you earn nothing.")
