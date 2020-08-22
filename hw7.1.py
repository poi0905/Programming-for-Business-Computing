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
    date[i][0] = int(date[i][0])    # year
    date[i][1] = int(date[i][1])    # month
    date[i][2] = int(date[i][2])    # day
    day.append(datetime.datetime(date[i][0], date[i][1], date[i][2]).weekday())
    # print(date[i], hour[i], lent[i], WD[i], day[i])

search = input()
search = search.split(',')
total = 0
error = 0

if(search[1].isdigit()):
    if(search[0] == 'D'):
        if(int(search[1]) > 31 or int(search[1]) < 1):
            error = 1
        else:
            for i in range(datanum):
                if(date[i][2] == int(search[1])):
                    total = total + lent[i]
    if(search[0] == 'H'):
        if(int(search[1]) > 23 or int(search[1]) < 0):
            error = 1
        else:
            for i in range(datanum):
                if(hour[i] == int(search[1])):
                    total = total + lent[i]

    if(search[0] == 'W'):
        if(int(search[1]) > 1 or int(search[1]) < 0):
            error = 1
        else:
            for i in range(datanum):
                if(WD[i] == int(search[1])):
                    total = total + lent[i]

    if(search[0] == 'K'):
        if(int(search[1]) > 7 or int(search[1]) < 1):
            error = 1
        else:
            for i in range(datanum):
                if(day[i] + 1 == int(search[1])):
                    total = total + lent[i]

if(error == 0):
    if(total == 0):
        if(search[1].isdigit()):
            print(0)
        else:
            print(-1)
    else:
        print(total)
else:
    print(-1)
