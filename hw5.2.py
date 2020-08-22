def used_box(items, capacity):
    num = 1
    temp = items[0]
    for i in range(len(items)):
        if i < len(items) - 1:
            if temp + items[i + 1] <= capacity:
                temp = temp + items[i + 1]
                continue
            if temp + items[i + 1] > capacity:
                num += 1
                temp = items[i + 1]
                continue
        if i == len(items) - 1:
            return num

data = []
item = []
data = [int(i) for i in input().split(',')]
n = data[0]
W = data[1]
itemStr = input()
item = itemStr.split(",")
for i in range(n):
    item[i] = int(item[i])

print(used_box(item, W))
