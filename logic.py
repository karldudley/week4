# get three numbers from the user to average
num1 = int(input("Number 1:\t"))
num2 = int(input("Number 2:\t"))
num3 = int(input("Number 3:\t"))

# incorrectly calculate the average - logic error
average = num1 + num2 + num3 / 3

print(f"The average of {num1}, {num2} and {num3} is {round(average,2)}.")
