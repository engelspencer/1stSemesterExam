strumber = input('Please enter a number: ')
isNumber = True
isIsogram = True

for x in range(0, len(strumber)):
	isNumber = strumber[x].isdigit()
	if (isNumber == False):
		break

if (isNumber == True):
	for x in range(0, len(strumber)):
		for y in range(0, len(strumber)):
			if ((x != y) and (strumber[x] == strumber[y])):
				isIsogram = False
if (isNumber == False):
	 print('This is not a number, please restart the program and enter a number.')

elif (isIsogram == True):
	print ('This number is an isogram.')

else:
	print ('This number is not an isogram.')
