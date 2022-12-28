# initialise varaibles
name = ""
name_list = []

# loop until john is entered
while name != "john":
    name = input("Please enter your name:\t").lower()
    if (name != "john"):
        name_list.append(name)

# print list of incorrect names
print(f"Incorrect names: {name_list}")
