total_ticket = int(input())
idbound = int(input())
registered = int(input())

quotaStr = input()
quota = quotaStr.split(",")
for i in range(3):
    quota[i] = int(quota[i])
# quota[0]:VIP會員至多能拿的票
# quota[1]:一般會員至多能拿的票
# quota[2]:民眾至多能拿的票
if registered != 0:
    if total_ticket != 0:
        IDStr = input()
        ID = IDStr.split(",")
        for i in range(registered):
            ID[i] = int(ID[i])

        wantStr = input()
        want = wantStr.split(",")
        get = wantStr.split(",")    # 屆時實際所拿
        for i in range(registered):
            want[i] = int(want[i])
            get[i] = 0

        upperbound = [idbound, 5000, 0]
        lowerbound = [0, idbound, -5001]
        # 等等要來分辨 VIP/會員/民眾

        # 會依序跑 VIP/會員/民眾
        for j in range(3):
            for i in range(registered):
                if lowerbound[j] <= ID[i] < upperbound[j]:   # 檢驗各ID身分
                    if want[i] <= quota[j]:  # 拿票狀況與剩多少票
                        if total_ticket >= want[i]:
                            total_ticket = total_ticket - want[i]
                            get[i] = want[i]
                        elif 0 < total_ticket < want[i]:
                            get[i] = int(total_ticket)
                            total_ticket -= total_ticket
                        else:
                            get[i] = 0
                    else:
                        if total_ticket >= quota[j]:
                            total_ticket = total_ticket - quota[j]
                            get[i] = quota[j]
                        elif 0 < total_ticket < quota[j]:
                            get[i] = int(total_ticket)
                            total_ticket -= total_ticket
                        else:
                            get[i] = 0

        print(total_ticket)
        for j in range(3):
            for i in range(registered):
                if j == 0:    # VIP
                    if 0 < ID[i] < idbound:
                        if get[i] != 0:
                            print(str(ID[i]) + ":" + str(get[i]))
                elif j == 1:  # 一般會員
                    if idbound <= ID[i]:
                        if get[i] != 0:
                            print(str(ID[i]) + ":" + str(get[i]))
                else:   # 民眾
                    if ID[i] < 0:
                        if get[i] != 0:
                            print(str(ID[i]) + ":" + str(get[i]))
    else:
        print("0")
else:
    print(total_ticket)
