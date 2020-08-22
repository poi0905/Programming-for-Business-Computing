import re
from collections import Counter  # 找最多次的函數
text = input()
dontwant = input().split(',')
words = re.split('[^a-zA-Z]', text)
a = words.count('')


def all_lower(words):   # 全變小寫
    return [s.lower() for s in words]
words = all_lower(words)
dontwant = all_lower(dontwant)
for i in range(a):  # 刪掉不要的
    words.remove('')
for i in range(len(dontwant)):
    try:    # 有的就全刪
        words.remove(dontwant[i])
        while (dontwant[i]) in words:
            words.remove(dontwant[i])
    except:  # 不在的話就繼續
        continue

word_counts = Counter(words)
top_one = word_counts.most_common(1000)  # 等等要防止有很多一樣多的
a = []
maxnum = 0
strmin = "zzzzzzzzzzzzzzzzzzz"  # 假設有一樣的按照字典順序輸出
for i in range(len(top_one)):
    if top_one[i][1] >= maxnum:
        maxnum = top_one[i][1]
        a.append(top_one[i])
if len(a) == 1:
    print(top_one[0][0], end=',')
    print(top_one[0][1])
else:   # 有數個一樣多次的
    for x in range(len(a)):
        if top_one[x][0] < strmin:
            strmin = top_one[x][0]
    print(strmin, end=',')
    print(top_one[x][1])
