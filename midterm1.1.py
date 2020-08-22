x = int(input())
y = int(input())
a = x + y
c = []
if x > y:
    b = x - y
else:
    b = y - x
if a % 2 != 0:
    c.append(a)
if b % 2 != 0:
    c.append(b)
print(len(c))
