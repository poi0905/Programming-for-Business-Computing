data = []
data = [int(i) for i in input().split(',')]
# n = data[0]
# k = data[1]


def prime(x):
    check = 0
    for j in range(2, x):
        if x % j == 0:
            check = 1
            break
    if check == 0:
        return True
    else:
        check2 = 0
        if x % data[1] == 0:
            check2 = 1
        if check2 == 1:
            return True

a = []
for i in range(2, data[0] + 1):
    if prime(i) is True:
        a.append(i)
# 考慮特殊情形(有1)
if data[1] == 1:
    a.append(1)
# 為了不要讓最後有逗號
b = len(a)
A = sorted(a)
for i in range(b - 1):
    print(A[i], end=',')
print(A[b - 1])
