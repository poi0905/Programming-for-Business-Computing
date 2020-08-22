class scooter():
    def __init__(self, company, number, level, Blist):
        self.c = company
        self.n = number
        self.l = level
        self.b = 0  # 電池
        self.km = 0
        self.w = 0  # 清潔程度
        self.be = int(Blist[2 * int(self.l) - 2])
        self.bq = int(Blist[2 * int(self.l) - 1])

    def printout(self):
        # 自己測試
        print("\ncompany:" + self.c)
        print("number:" + self.n)
        print("level:" + self.l)
        print("battery:", end="")
        print(self.b)
        print("battery efficiency:", end="")
        print(self.be)
        print("battery quantity:", end="")
        print(self.bq)
        print("km:", end="")
        print(self.km)
        print("wash:", end="")
        print(self.w)

    def charge(self, num):
        # 充電
        self.b += int(num)
        if self.b > self.bq:
            self.b = self.bq

    def rent(self, num):
        # 出租
        if int(num) < 0:
            return
        if int(num) <= self.b:
            self.km += int(num) * self.be
            self.w += int(num) * self.be
        else:
            self.km += self.b * self.be
            self.w += self.b * self.be
        self.b -= int(num)
        if self.b < 0:
            self.b = 0

    def sell(self, num):
        # 賣車
        self.c = num

    def wash(self):
        # 洗車
        self.w = 0


def find(list, company, number):
    for num in range(len(list)):
        if list[num].c == company and list[num].n == number:
            return num


def answer(list):
    ans = []
    for scooter in list:
        if scooter.w >= 100:
            str = scooter.n
            ans.append(str)
    if len(ans) == 0:
        print("-1")
    else:
        ans = sorted(ans)
        for x in range(len(ans)-1):
            print(ans[x], end=",")
        print(ans[len(ans)-1])
    ans1 = []
    max = 0
    for x in range(len(list)):
        if list[x].km > max:
            max = list[x].km
            ans1 = []
            ans1.append(x)
        elif list[x].km == max:
            ans1.append(x)
    strmin = "ZZZZZZZZZZ"
    if len(ans1) > 1:
        for x in range(len(ans1)):
            str = list[x].n
            if str < strmin:
                strmin = str
        print(strmin)
    else:
        print(list[ans1[0]].n)

Blist = input().split(",")
str = input().split(",")
list = []

while str[0] != "BREAK":
    if str[0] == "A":
        c = scooter(str[1], str[2], str[3], Blist)
        list.append(c)
    elif str[0] == "R":
        num = find(list, str[1], str[2])
        list[num].charge(str[3])
    elif str[0] == "G":
        num = find(list, str[1], str[2])
        list[num].rent(str[3])
    elif str[0] == "S":
        num = find(list, str[1], str[3])
        list[num].sell(str[2])
    elif str[0] == "D":
        num = find(list, str[1], str[2])
        list.remove(list[num])
    elif str[0] == "W":
        num = find(list, str[1], str[2])
        list[num].wash()
    str = input().split(",")
    continue

# for x in list:
    # x.printout()

answer(list)
