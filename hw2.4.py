day_gap = int(input())
bf_pay = int(input())
af_pay = int(input())
D1 = int(input())
D2 = int(input())
D3 = int(input())   # 各時段單數
oc = int(input())   # oc = opportunity cost

t = 0   # 工作時數
profit = 0
a = -999999999  # 找一個很小的數，只是讓它被取代

for t in range(12):  # 來看每個工作時數(t)接了多少單
    t += 1
    if t <= 4:
        num = t * D1
    elif 8 >= t > 4:
        num = 4 * D1 + (t - 4) * D2
    elif 12 >= t > 8:
        num = 4 * (D1 + D2) + (t - 8) * D3

    if num >= day_gap:
        profit = day_gap * bf_pay + (num - day_gap) * af_pay - t * oc
    else:
        profit = num * bf_pay - t * oc

    if profit > a:
        a = profit
        A = str(a)
        t = t
        T = str(t)

print(T + ',' + A)
