############################################################
# Takes a file with a list of words
# Removes all instances of words which occur more than once
############################################################

FILENAME = 'allmods.txt'
OUTPUT = 'difference.txt'

adict = []
diff = []


file = open(FILENAME)

for item in file:
	adict.append(item)

for item in adict:
	if adict.count(item) ==1:
		diff.append(item)

outFile = open(OUTPUT,'w')
outFile.writelines(diff)