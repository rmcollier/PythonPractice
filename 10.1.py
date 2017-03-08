fh = open('mbox-short.txt')

counts = dict()

for line in fh :
	if line.strip().startswith('From') is False or line.strip().startswith('From:') :
		continue
	#print line.strip()
	words = line.split()
	counts[words[1]] = counts.get(words[1],0) + 1
	
results = list()
for k, v in counts.items() :
	results.append((v,k))

results.sort(reverse=True)
	
print results
	