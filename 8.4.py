fhandle = open('romeo.txt')
uniques = []
found = False

for line in fhandle :
	words = line.split()
	#print words
	#print uniques
	if not uniques :
		uniques.append(words[0])
		#print 'First word:',uniques[0]
	
	for word in words :
		for unique in uniques :
			if word == unique :
				found = True
				#print 'Found duplicate:',word
				
		if not found :
			uniques.append(word)
	
		found = False
		
	
print sorted(uniques)

	
	
fhandle.close()
