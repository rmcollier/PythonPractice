numbers = list()
while True:
	input = raw_input('Enter number or done ')
	
	if input == 'done':
		break

	try :
		input = float(input)
	except :
		print 'Invalid entry'
		quit()
		
	numbers.append(input)

print 'Maximum',max(numbers)
print 'Minimum',min(numbers)
	