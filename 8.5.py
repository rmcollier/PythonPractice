hf = open('mbox-short.txt')
fromCount = 0
for line in hf :
	if not line.startswith('From ') :
		continue
	fromCount = fromCount + 1
	words = line.split()
	print words[1]
print 'There were',fromCount,'lines in the file with From as the first word'