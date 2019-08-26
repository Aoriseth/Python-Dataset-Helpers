FILE = 'output.csv'

# Read in the file
with open(FILE, 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace(',', '.')
filedata = filedata.replace(';', ',')

# Write the file out again
with open(FILE, 'w') as file:
  file.write(filedata)