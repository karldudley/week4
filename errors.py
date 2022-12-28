# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

# added brackets to print statement
print ("Welcome to the error program")

# added brackets to print statement and removed the indent
print ("\n")

# removed the double equals to assign variable correctly, also stripped it to the number only
age_str = "24" #I'm 24 years old
age = int(age_str)
# changed to age_str
print("I'm " + age_str + " years old.")

# changed it to a number
three = 3

answer_years = age + three

# added f string
print(f"The total number of years: {answer_years}")

# corrected answer variable to answer_years and added the extra 6 months
answer_months = (answer_years * 12) + 6

print("In 3 years and 6 months, I'll be " + str(answer_months) + " months old")

#HINT, 330 months is the correct answer

