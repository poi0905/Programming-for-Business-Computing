n = int(input())    # 報酬從x變y的日門檻
m = int(input())    # 週報酬的bonus門檻   
x = int(input())    # 門檻前的報酬
y = int(input())    # 第n+1單後的報酬
b = int(input())    # bonus的金額
r1 = int(input()) 
r2 = int(input()) 
r3 = int(input()) 
r4 = int(input()) 
r5 = int(input()) 
r6 = int(input()) 
r7 = int(input())   # 星期一到日的完成件數

if r1 >= n:
    a1 = n*x + (r1-n)*y
else:
    a1 = r1*x

if r2 >= n:
    a2 = n*x + (r2-n)*y
else:
    a2 = r2*x
    
if r3 >= n:
    a3 = n*x + (r3-n)*y
else:
    a3 = r3*x
    
if r4 >= n:
    a4 = n*x + (r4-n)*y
else:
    a4 = r4*x
    
if r5 >= n:
    a5 = n*x + (r5-n)*y
else:
    a5 = r5*x

if r6 >= n:
    a6 = n*x + (r6-n)*y
else:
    a6 = r6*x
    
if r7 >= n:
    a7 = n*x + (r7-n)*y
else:
    a7 = r7*x
    
if r1 + r2 + r3 + r4 + r5 + r6 + r7 >= m:     
    print(a1 + a2 + a3 + a4 + a5 + a6 + a7 + b)
else:
    print(a1 + a2 + a3 + a4 + a5 + a6 + a7)
   