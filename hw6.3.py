dic = input()
s1 = input()
dic_list = dic.split(',')
ans1 = []
ans2 = []
s2 = s1  # 因為等等s1會被清空

# 第一種要求
for i in range(len(s1)):
    if len(s1) >= 3:
        if (s1[0] + s1[1] + s1[2]) in dic_list:
            ans1.append(s1[0] + s1[1] + s1[2])
            s1 = s1[3:]
            continue
        if (s1[0] + s1[1]) in dic_list:
            ans1.append(s1[0] + s1[1])
            s1 = s1[2:]
            continue
        else:
            ans1.append(s1[0])
            s1 = s1[1:]
            continue
    if len(s1) == 2:
        if (s1[0] + s1[1]) in dic_list:
            ans1.append(s1[0] + s1[1])
            s1 = s1[2:]
            continue
        else:
            ans1.append(s1[0])
            s1 = s1[1:]
            continue
    if len(s1) == 1:
        ans1.append(s1[0])
        break

# 第二種要求
for i in range(len(s2)):
    if len(s2) >= 3:
        if (s2[-3] + s2[-2] + s2[-1]) in dic_list:
            ans2.append(s2[-3] + s2[-2] + s2[-1])
            s2 = s2[:-3]
            continue
        if (s2[-2] + s2[-1]) in dic_list:
            ans2.append(s2[-2] + s2[-1])
            s2 = s2[:-2]
            continue
        else:
            ans2.append(s2[-1])
            s2 = s2[:-1]
            continue
    if len(s2) == 2:
        if (s2[-2] + s2[-1]) in dic_list:
            ans2.append(s2[-2] + s2[-1])
            s2 = s2[:-2]
            continue
        else:
            ans2.append(s2[-1])
            s2 = s2[:-1]
            continue
    if len(s2) == 1:
        ans2.append(s2[0])
        break

for i in range(len(ans1) - 1):
    print(ans1[i], end='/')
print(ans1[len(ans1) - 1])
ans2 = list(reversed(ans2))
for i in range(len(ans2) - 1):
    print(ans2[i], end='/')
print(ans2[len(ans2) - 1])
