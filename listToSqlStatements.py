#######################################
#       Example configurations        #
#######################################

# FILE = "input"
# OUTPUT = "deleteAttributesByEventID.sql"
# BEFORE = "DELETE FROM ATTR_TBL \nWHERE CEV_OID='"
# AFTER = "';\n"

# FILE = "input"
# OUTPUT = "deleteEventsByEventID.sql"
# BEFORE = "DELETE FROM EVENT_TBL \nWHERE CEV_OID='"
# AFTER = "';\n"

# FILE = "all vins to delete.csv"
# OUTPUT = "findAllVinsNotFromMigration.sql"
# BEFORE = "SELECT VIN_VINNR FROM EVENT_TBL \nWHERE VIN_VINNR = '"
# AFTER = "' \nAND CEV_APP_CODE <> ‘VHF-MIG’;\n"

# FILE = "updatedList.txt"
# OUTPUT = "deleteVehiclesByVin.sql"
# BEFORE = "DELETE FROM VEHID_TBL \nWHERE VIN_VINNR='"
# AFTER = "';\n"



####### Configuration ########

FILE = "input.txt" # Input file with ids/codes/whatever on each line
OUTPUT = "output.sql" # Output file with sql statements.
BEFORE = "DELETE FROM Table \nWHERE id='" # Text to put before input
AFTER = "';\n" # Text to put after input
COMMIT = True # Setting this to True will generate commit statements every 100 lines + at the end.



###### Code ######

file = open(FILE,"r")
output = open(OUTPUT,"w")

count = 0
for line in file:
	output.write(BEFORE+line.rstrip()+AFTER)
	count+=1
	if count%100==0:
		if COMMIT:
			output.write("COMMIT;\n")
		
if COMMIT:
	output.write("COMMIT;")
