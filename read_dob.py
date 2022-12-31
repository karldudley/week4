# open file
dobs_read = open('DOB.txt', 'r+')

# read file and assign to a variable
data = dobs_read.readlines()

# print Names title
print("NAMES")
# loop to print names
for line in data:
    split_line = line.split(' ')
    print(split_line[0], split_line[1])

# print Names title
print("\nBIRTHDATES")
# loop to print names
for line in data:
    split_line = line.split(' ')
    print(split_line[2], split_line[3], split_line[4].strip())      # strip to get rid of new line characters

# close file
dobs_read.close()
