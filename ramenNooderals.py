N = 1
P = 12
B = 144
C = 1024

quantity = input('Please enter the ramen nooderals you would like to purchase.')
isRamenNooderal = True

for x in range(0, len(quantity)):
	if (quantity[x] != 'N' and quantity[x] != 'P' and quantity[x] != 'B' and quantity[x] != 'C'):
		isRamenNooderal = False
