Xl = int(input())
Xi = int(input())
y = float(input())

if Xl + Xi < 10 or y < 3.5 or Xi == 0 :
    print('0')
if 1 <= Xi <= 9 and Xl + Xi >= 10 and y >= 3.5 :
    if 10000 + 3000*Xi > 150000 :
        print ('150000')
    else :
        print( 10000 + 3000*Xi )
if 10 <= Xi <= 29 and 3.5 <= y < 4 :
    if 15000 + 4000*Xi > 150000 :
        print ('150000')
    else :        
        print( 15000 + 4000*Xi)
if 10 <= Xi <= 29 and y >= 4 :
    if 20000 + 5000*Xi > 150000 : 
        print ( '150000' )
    else :
        print ( 20000 + 5000*Xi )
if Xi >= 30 and y >= 3.5 :
    if 30000 + 6000*Xi < 150000 :
        print ( 30000 + 6000*Xi)
    else :
        print ('150000')
    