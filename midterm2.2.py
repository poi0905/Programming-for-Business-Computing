# 輸入資料
str = input().split(',')
str[0] = str[0].split(';')  # 幾個編號跟HW所占比例
num = str[0][0]
newstr = []
newstr.append(str[0][1])
newstr.append(str[1])
newstr.append(str[2])
newstr.append(str[3])
# print(newstr)

title = input().split(',')
a = title.index('HW')   # 作業的比重，以下類推
b = title.index('MT1')
c = title.index('MT2')
d = title.index('F')
# print(a,b,c,d)

data = []
list = []
# 把權重用成整齊的list
weight = []
weight.append(newstr[a-1])
weight.append(newstr[b-1])
weight.append(newstr[c-1])
weight.append(newstr[d-1])
# print(weight)

for i in range(int(num[0][0])):
    data.append(input().split(','))
    for j in range(5):
        data[i][j] = int(data[i][j])


class Grade():
    def __init__(self, number, grade1, grade2, grade3, grade4, weight):
        self.n = number
        self.g1 = grade1
        self.g2 = grade2
        self.g3 = grade3
        self.g4 = grade4
        self.g1w = int(weight[0])  # 成績一佔的比重
        self.g2w = int(weight[1])  # 成績二佔的比重
        self.g3w = int(weight[2])  # 成績三佔的比重
        self.g4w = int(weight[3])  # 成績四佔的比重
        if self.g2 > self.g3 and self.g2w < self.g3w:   # 換比重
            self.a = self.g2w
            self.g2w = self.g3w
            self.g3w = self.a
        if self.g2 < self.g3 and self.g2w > self.g3w:
            self.a = self.g2w
            self.g2w = self.g3w
            self.g3w = self.a
        self.sum = self.g1 * self.g1w + self.g2 * self.g2w + self.g3 * self.g3w + self.g4 * self.g4w

    def printout(self):
        # 自己測試
        print('')
        print(self.n)
        print(self.g1)
        print(self.g2)
        print(self.g3)
        print(self.g4)
        print(self.sum)


def ans(list):
    ans = []
    max = 0
    for x in range(len(list)):
        if list[x].sum > max:
            max = list[x].sum
            ans = []
            ans.append(x)
        elif list[x].sum == max:    # 把所有成績相同的蒐集進來
            ans.append(x)
    print(list[ans[0]].n, end=',')  # 印編號最小的
    print(list[ans[0]].sum // 100)


for i in range(int(num)):
    c = Grade(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], weight)
    list.append(c)

# for x in list:
    # x.printout()

ans(list)
