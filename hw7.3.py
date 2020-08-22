import datetime
w = int(input())  # 總票數
mn = input()  # 登記人數跟會員等級數
mn = mn.split(',')
m = int(mn[0])  # 登記人數
n = int(mn[1])  # 會員等級有幾種


def sortedDictValues2(adict):
    keys = adict.keys()
    keys.sort()
    return [dict[key] for key in keys]


def strTodatetime(datestr, format):
    return datetime.datetime.strptime(datestr, format)
name = input()  # 等級名(n個)
name = name.split(',')
can_ticket = input()  # 最多可以拿的票
can_ticket = can_ticket.split(',')

T = input()  # 開放拿票時間
day_later = input()  # 幾天之內
day_later = day_later.split(',')
if m != 0:
    regist_time = input()  # 每次截止時間
    ID = input()  # 每次截止時間
    level = input()  # 等級名字
    want_ticketStr = input()
    regist_time = regist_time.split(',')
    ID = ID.split(',')
    level = level.split(',')
    want_ticket = want_ticketStr.split(',')
    get_ticket = want_ticketStr.split(',')

new_time = []
T = strTodatetime(T, "%Y-%m-%d %H:%M:%S")

regist_t = []
for i in range(m):
    regist_t.append(strTodatetime(regist_time[i], "%Y-%m-%d %H:%M:%S"))

for i in range(n):
    can_ticket[i] = int(can_ticket[i])

for j in range(m):
    ID[j] = int(ID[j])
    want_ticket[j] = int(want_ticket[j])
real_ID = []
persons_time = dict()
person_want_ticket = dict()
same_ID = str()
time_dict = dict()
realreal = dict()
time_list = []
ansid = []
for i in range(m):  # 把重複登記的用掉 形成dict (ID:最早登記的那份資料)
    if ID[i] not in real_ID:
        ansid.append(ID[i])
        real_ID.append(ID[i])
        persons_time[ID[i]] = regist_t[i]
        person_want_ticket[ID[i]] = want_ticket[i]
        time_dict[ID[i]] = regist_t[i]
        time_list.append(regist_t[i])
    if ID[i] in real_ID:  # 看每個人的時間
        if T <= regist_t[i] <= time_dict[ID[i]]:  # 登記較早而且在時限後
            idx = real_ID.index(ID[i])
            persons_time[ID[i]] = regist_t[i]
            person_want_ticket[ID[i]] = want_ticket[i]
            time_list.remove(time_dict[ID[i]])
            time_list.insert(idx, regist_t[i])
            time_dict[ID[i]] = regist_t[i]
        elif time_dict[ID[i]] < T < regist_t[i]:  # 太早登記了(不能算)
            idx = real_ID.index(ID[i])
            persons_time[ID[i]] = regist_t[i]
            person_want_ticket[ID[i]] = want_ticket[i]
            time_list.remove(time_dict[ID[i]])  # 把不要的資料去掉
            time_list.insert(idx, regist_t[i])  # 插入要替代的資料
            time_dict[ID[i]] = regist_t[i]

timesort = []

for i in range(len(time_list)):   # 把時間變成str
    timesort.append(time_list[i].strftime("%Y-%m-%d %H:%M:%S"))

if m > 0:
    level_person = dict(zip(level, ID))
    person_level = dict(zip(ID, level))
    time_id = dict(zip(timesort, real_ID))  # 把他原本給的ID:日期排序變成ID:日期早的

id_time = dict()


ID_list = []
xs = dict()
new_lv_time = dict()
if m > 0:
    for x in sorted(time_id.keys()):  # 把日期排序(由前到後)
        xs[x] = time_id[x]
        ID_list.append(xs[x])  # 得到由日期排序的ID

name_can = dict(zip(name, can_ticket))  # 把每個id zip 可拿的票
new_person_want_ticket = dict()
new_can_ticket = dict()
if m > 0:
    for i in range(len(ID_list)):  # 用新的dict 都整理成照時間順序的樣子
        new_lv_time[ID_list[i]] = person_level[ID_list[i]]
        new_person_want_ticket[ID_list[i]] = person_want_ticket[ID_list[i]]
        new_can_ticket[ID_list[i]] = name_can[person_level[ID_list[i]]]


person_earlyt = dict(zip(xs.values(), xs.keys()))  # 把value,key互換
if m > 0:
    for i in range(len(time_id)):
        person_earlyt[real_ID[i]] = \
            strTodatetime(person_earlyt[real_ID[i]], "%Y-%m-%d %H:%M:%S")

if m > 0:
    for i in range(m):
        want_ticket[i] = 0

get_ticket = []
if m > 0:
    for i in range(len(persons_time)):
        get_ticket.append(0)


time_deadline = T
diff = []
if m > 0:
    for i in range(n):
        day_later[i] = int(day_later[i])
        diff.append(datetime.timedelta(days=day_later[i]))  # 把每次的天數以後存成diff


id_get = dict()
ans_dict = dict()
if m > 0:
    for j in range(len(ID_list)):
        id_get[ID_list[j]] = 0


ID___lis = []  # 紀錄拿過的ID(按照拿票順序)
com_dicID_list = dict()  # 之後用來比較已經拿過的人
zero = []
if m > 0:
    for i in range(len(ID_list)):
        zero.append(0)
    com_dicID_list = dict(zip(ID_list, zero))

get = []
if m > 0:
    for i in range(n):
        time_deadline = T + diff[i]  # 依據跑i來用新的時間截止
        for j in range(len(ID_list)):
            if new_lv_time[ID_list[j]] in name[:i+1]:  # 如果是可以拿票的人
                # 跑不同會員  #vipvipvip commom commom
                if com_dicID_list[ID_list[j]] > 0:  # 已經拿過了
                    continue
                if T <= person_earlyt[ID_list[j]] <= time_deadline:  # 找時間內登記的人
                        if w >= new_person_want_ticket[ID_list[j]]:
                            if new_person_want_ticket[ID_list[j]] \
                                    <= new_can_ticket[ID_list[j]]:
                                id_get[ID_list[j]] = \
                                    new_person_want_ticket[ID_list[j]]
                            else:  # 想要的比可以拿得多
                                id_get[ID_list[j]] = new_can_ticket[ID_list[j]]
                        elif new_person_want_ticket[ID_list[j]] > w > 0:
                            if new_person_want_ticket[ID_list[j]] \
                                    <= new_can_ticket[ID_list[j]]:
                                id_get[ID_list[j]] = w
                            else:  # 想要的比可以拿得多
                                if w >= new_can_ticket[ID_list[j]]:
                                    id_get[ID_list[j]] = \
                                        new_can_ticket[ID_list[j]]
                                else:  # 總票少於可拿的票
                                    id_get[ID_list[j]] = w
                        elif w <= 0:
                            if id_get[ID_list[j]] > 0:
                                continue
                            else:
                                id_get[ID_list[j]] = 0
                        a = id_get[ID_list[j]]
                        if id_get[ID_list[j]] > 0:
                            if ID_list[j] not in ID___lis:  # 還沒拿過
                                w = w - a  # 總票數-拿的
                                ID___lis.append(ID_list[j])
                                get.append(id_get[ID_list[j]])
                                com_dicID_list[ID_list[j]] = id_get[ID_list[j]]
                                # 紀錄已經拿過的人
print(w)

for j in range(0, len(ID___lis)):  # 照著拿票順序印
    print(str(ID___lis[j]) + ':' + str(get[j]))