fh = open('mbox-short.txt') 

counts = dict()
findmax = 0

for line in fh :
	if line.strip().startswith('From') is False or line.strip().startswith('From:') :
		continue
	#print line.strip()
	line = line.split()
	counts[line[1]] = counts.get(line[1],0) + 1

for item in counts :
	if counts[item] > findmax : 
		maxperson = item
		findmax = counts[item]
		#print 'New max: ',item
	

print maxperson, findmax