fh = open('mbox-short.txt')
counts = dict()

for line in fh :
	if line.strip().startswith('From') is False or line.strip().startswith('From:') :
		continue
	
	words = line.split()
	
	#print words[5]
	time = words[5].split(':')
	
	counts[time[0]] = counts.get(time[0],0) + 1


lst = list()
for k, v in counts.items() :
	lst.append((k,v))
lst.sort()

for item in lst :
	print item[0], item[1]

	
	