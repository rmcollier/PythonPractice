fh = open('words.txt')
words = fh.read().split()
wordsDict = dict()
someCount = 0

for ind in words :
	wordsDict[ind] = someCount
	someCount = someCount + 1
	
print wordsDict