####### Configuration ######

INPUT = 'inputList.txt' # Input list 
REMOVE = 'linesToRemove.txt' # List with lines to remove from input list
OUTPUT = 'cleanedList.txt' # Name of output file


####### Code #######

total = open(INPUT,'r')
remove = open(REMOVE,'r')

totalList = []

for line in total:
	totalList.append(line)

for line in remove:
	try:
		totalList.remove(line)
	except ValueError:
		pass

updatedlist = open(OUTPUT,'w')
updatedlist.writelines(totalList)