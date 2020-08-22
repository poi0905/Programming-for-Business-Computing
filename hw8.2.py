data = []
data = [int(i) for i in input().split(',')]
map = []
row = data[0]
col = data[1]
for i in range(row):
    map.append(input().split(','))
    for j in range(col):
        map[i][j] = int(map[i][j])

a = 0
b = 0
now = map[a][b]
route = [map[0][0]]
while (a <= (row - 1)) and (b <= (col - 1)):
    if map[a][b + 1] < map[a + 1][b]:
        now = map[a][b + 1]
        route.append(now)
        b += 1
        if b == (col - 1):
            while a < (row - 1):
                a += 1
                route.append(map[a][b])
            break
    else:
        now = map[a + 1][b]
        route.append(now)
        a += 1
        if a == (row - 1):
            while b < (col - 1):
                b += 1
                route.append(map[a][b])
            break
print(sum(route))
