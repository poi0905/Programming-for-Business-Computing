n = int(input())    # 報酬從x變y的門檻
x = int(input())    # 門檻前的報酬
y = int(input())    # 第n+1單後的報酬
r = int(input())    # 完成件數

if r >= n:
    print(n*x + (r-n)*y)
else:
    print(r*x)
