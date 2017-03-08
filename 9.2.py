fh = open('mbox-short.txt')
counts = dict()

for line in fh :
	line = line.rstrip()
	if line.startswith('From') is False or line.startswith('From:'):
		continue
	line = line.split()
	
	counts[line[2]] = counts.get(line[2],0) + 1
	
		
	
print counts
	