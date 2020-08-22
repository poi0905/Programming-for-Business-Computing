day_gap = int(input())
week_gap = int(input())
bf_pay = int(input())
af_pay = int(input())
bonus = int(input())

sum1 = int(0)   # 報酬
sum2 = int(0)   # 一週的單數

for i in range(7):
    temp = int(input())
    sum2 += temp
    if temp >= day_gap:
        sum1 += day_gap*bf_pay + (temp-day_gap)*af_pay
    else:
        sum1 += temp*bf_pay

if sum2 >= week_gap:
    print(sum1 + bonus)
else:
    print(sum1)
