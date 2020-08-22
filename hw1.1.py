Xl = int(input())
Xi = int(input())
y = float(input())

if 0 < y < 3.5 or Xi == 0 :
    print('0')
else :
    if Xl + Xi < 10 or Xi < 1 :
        print('0')
    else :
        if 15000 + 4000*Xi > 150000 :
            print ( 150000 )
        else :
            print ( 15000 + 4000*Xi )