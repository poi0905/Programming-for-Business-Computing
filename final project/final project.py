import csv
start = input('歡迎光臨來到臺大周邊咖啡廳小幫手，請問你要執行何種動作(查詢咖啡廳/新增咖啡廳/離開):')

if start == '查詢咖啡廳':
    fn = str('C:\\Users\\user\\OneDrive\\桌面\\coff.csv')
    fh1 = open(fn, 'r+')
    data = []
    for a in fh1:
        data.append(a.split(','))

    class Cshop():
        def __init__(self, company, area, socket, wifi, seatsize, atmosphere, snack, meal, animal, info):
            self.c = company
            self.a = area
            self.s = socket
            self.w = wifi
            self.ss = seatsize
            self.at = atmosphere
            self.sn = snack
            self.m = meal
            self.an = animal
            self.i = info

        def printout(self):
            # 自己測試
            print('\ncompany:' + self.c)
            print('area:' + self.a)
            print('socket:' + self.s)
            print('wifi:' + self.w)
            print('seatsize:' + self.ss)
            print('atmosphere:' + self.at)
            print('snack:' + self.sn)
            print('meal:' + self.m)
            print('animal:' + self.an)
            print('info:' + self.i)

    def answer(list):
        for Cshop in list:
            if Area == Cshop.a or Area == '不拘':
                if (Socket == '要' and Cshop.s == '有') or Socket == '都可以':
                    if (Wifi == '要' and Cshop.w == '有') or Wifi == '都可以':
                        if (Seatsize == '要' and Cshop.ss == '寬敞') or Seatsize == '都可以':
                            if (Atmosphere == '要' and Cshop.at == '適合讀書') or Atmosphere == '都可以':
                                if (Snack == '要' and Cshop.sn == '有') or Snack == '都可以':
                                    if (Meal == '要' and Cshop.m == '有') or Meal == '都可以':
                                        if (Animal == '要' and Cshop.an == '有') or (Animal == '不要' and Cshop.an == '無') or Animal == '都可以':
                                            print(Cshop.c)
                                            print(Cshop.i)
        print('*若空白，代表你太嚴格了喔!*')

    list = []
    for i in range(1, 10000):
        try:
            c = Cshop(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7], data[i][8], data[i][9])
            list.append(c)
        except:
            break
    # for x in list:
        # x.printout()

    Area = input('請輸入咖啡廳的區域(羅斯福路/新生南路/汀洲路/溫州街/後門/不拘):')
    Socket = input('是否要有插座?(要/都可以):')
    Wifi = input('是否要有wifi?(要/都可以):')
    Seatsize = input('店內座位是否要寬敞?(要/都可以):')
    Atmosphere = input('是否要適合讀書?(要/都可以):')
    Snack = input('是否要有點心?(要/都可以):')
    Meal = input('是否要有正餐?(要/都可以):')
    Animal = input('店內是否要有寵物?(要/不要/都可以):')

    answer(list)
    fh1.close()

if start == '新增咖啡廳':
    Name = input('咖啡廳店名?')
    Area = input('請輸入咖啡廳的區域(羅斯福路/新生南路/汀洲路/溫州街/後門):')
    Socket = input('是否有插座?(有/無):')
    Wifi = input('是否有wifi?(有/無):')
    Seatsize = input('店內座位大小?(寬敞/普通):')
    Atmosphere = input('適合讀書嗎?(適合讀書/不適合讀書):')
    Snack = input('是否有點心?(有/無):')
    Meal = input('是否有正餐?(有/無):')
    Animal = input('店內有寵物?(有/無):')
    Info = input('相關資訊?(可以填入地址、營業時間等等喔!):')

    def write_csv():
        path = 'C:\\Users\\user\\OneDrive\\桌面\\coff.csv'
        with open(path, 'a+') as f:
            csv_write = csv.writer(f)
            data_row = [Name, Area, Socket, Wifi, Seatsize, Atmosphere, Snack, Meal, Animal, Info]
            csv_write.writerow(data_row)
    write_csv()
    print('感謝您的新增!')

if start == '離開':
    print('881')
