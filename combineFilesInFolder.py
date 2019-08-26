import os

COMBINE_WITH_EXTENSION = '.csv'
ONLY_KEEP_FIRST_HEADER = True


cwd = os.getcwd()
listOfFiles = []
for dirpath,dirnames,filenames in os.walk(cwd):
	listOfFiles = filter(lambda x: x.endswith(COMBINE_WITH_EXTENSION), filenames)

first = True

combinedLines = []

for file in listOfFiles:
	reader = open(file,'r')

	if first:
		first = False
	else:
		reader.readline()

	for line in reader:
		combinedLines.append(line)

output = open("output"+COMBINE_WITH_EXTENSION,'w')
output.writelines(combinedLines)