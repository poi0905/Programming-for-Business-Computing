import datetime
# filename = input()
filename = 'C:\\Users\\user\\OneDrive\\桌面\\test1234.csv'

date = []
hour = []
lent = []
WD = []
day = []

with open(filename, 'r') as infile:
    while True:
        line = infile.readlines()
        if not line:
            break
        data = str(line).split(',')

datanum = len(data)

for i in range(datanum):
    if(i % 4 == 0):
        date.append(data[i])
    if(i % 4 == 1):
        hour.append(data[i])
    if(i % 4 == 2):
        lent.append(data[i])
    if(i % 4 == 3):
        WD.append(data[i])

date.pop(0)
hour.pop(0)
lent.pop(0)
WD.pop(0)

datanum = len(date)

for i in range(datanum):
    date[i] = date[i][2:].split('/')
    hour[i] = int(hour[i])
    lent[i] = int(lent[i])
    WD[i] = int(WD[i][0])
    date[i][0] = int(date[i][0])
    date[i][1] = int(date[i][1])
    date[i][2] = int(date[i][2])
    day.append(datetime.datetime(date[i][0], date[i][1], date[i][2]).weekday())
    # print(date[i], hour[i], lent[i], WD[i], day[i])

searchnum = int(input())
search = []

wrong = 0

for i in range(searchnum):
    search.append(input())
    search[i] = str(search[i]).split(',')
    for j in range(len(search[i])):
        if(j != 0):
            if(search[i][j].isdigit()) is False:
                wrong = 1
# print(search)
total = 0
error = 0

if(wrong == 0):
    for i in range(datanum):
        fullcheck = [1, 1, 1, 1]
        # print(date[i], hour[i], lent[i], WD[i], day[i])
        for j in range(searchnum):
            check = 0
            if(search[j][0] == 'D'):
                for k in range(len(search[j])-1):
                    if(int(search[j][k + 1]) > 31 or int(search[j][k+1]) < 1):
                        error = 1
                    else:
                        if(date[i][2] == int(search[j][k+1])):
                            check = 1
                if(check != 1):
                    fullcheck[0] = 0
                    # print('D failed')
                check = 0
            if(search[j][0] == 'H'):
                for k in range(len(search[j])-1):
                    if(int(search[j][k + 1]) > 23 or int(search[j][k + 1]) < 0):
                        error = 1
                    else:
                        if(hour[i] == int(search[j][k + 1])):
                            check = 1
                if(check != 1):
                    fullcheck[1] = 0
                    # print('H failed')
                check = 0
            if(search[j][0] == 'W'):
                for k in range(len(search[j]) - 1):
                    if(int(search[j][k + 1]) > 1 or int(search[j][k + 1]) < 0):
                        error = 1
                    else:
                        if(WD[i] == int(search[j][k + 1])):
                            check = 1
                if(check != 1):
                    fullcheck[2] = 0
                    # print('W failed')
                check = 0
            if(search[j][0] == 'K'):
                for k in range(len(search[j])-1):
                    if(int(search[j][k + 1]) > 7 or int(search[j][k+1]) < 1):
                        error = 1
                    else:
                        if(day[i] + 1 == int(search[j][k + 1])):
                            check = 1
                if(check != 1):
                    fullcheck[2] = 0
                    # print('K failed')
                check = 0
        if(fullcheck == [1, 1, 1, 1]):
            total = total + lent[i]
    if(error == 0):
        print(total)
    else:
        print(-1)
else:
    print(-1)
