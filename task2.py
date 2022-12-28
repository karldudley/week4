# get a year from the user
year = int(input("What year do you want to start with?\t"))

# get years to look back
num_years = int(input("How many years do you want to check?\t"))

# loop though the years and check if its a leap year
for x in range (year, year + num_years):
    if (x % 4 == 0):
        print(f"{x} is a leap year")
    else:
        print(f"{x} isn't a leap year")
