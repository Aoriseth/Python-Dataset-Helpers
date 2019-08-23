######### Configuration ########

FILE = "filename.txt" # Name of the file to sample
OUTPUT = "output.txt" # Name of the generated output file
NTH = 1000 # Sample each nth line
keepHeader = True # Set to True to keep the first line



######## Code #########

file = open (FILE,'r')
output = open(OUTPUT,'w')

count = 0
for line in file:
	if count == 0 and keepHeader == True:
		output.write(line)
	count+=1
	if count%1000 == 0:
		output.write(line)