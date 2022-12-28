# while loop
print("While Loop - 20 to 0")
i = 20
while (i >=0 ):
    print(i)
    i -= 1

# even numbers
print("Even Numbers - 1 to 20")
for j in range (1,20):
    if (j % 2 == 0):
        print(j)

# stars
print("Stars")
for x in range(1,6):
    for y in range (1,x+1):
        print("*", end = '')
    print("\n")

# Python program to find H.C.F of two numbers

# HCF
# get two numbers
num1 = int(input("Number 1:\t"))
num2 = int(input("Number 2:\t"))

# work out which number is lower
if num1 > num2:
    lower = num2
else:
    lower = num1

for i in range(1, lower+1):
    if((num1 % i == 0) and (num2 % i == 0)):
        highest_common_factor = i 

print(f"The Highest Common Factor is {highest_common_factor}")
