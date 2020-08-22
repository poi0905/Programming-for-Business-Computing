man = int(input())
woman = int(input())
room1 = int(input())
room2 = int(input())
room3 = int(input())
money = int(input())

if man % 4 == 0 :
    manroom = man // 4
else :
	manroom = man // 4 + 1
	
if woman % 4 == 0 :
	womanroom = woman // 4
else :
	womanroom = woman // 4 + 1
    
expense = ( manroom + womanroom ) * min ( room1, room2, room3 )
t = money - expense
T = str(t)

if money < expense :
	print('Tonight, we had better find a nice place near the street.')
else :
	print('Hallelujah! we have ' + T  + ' left.')