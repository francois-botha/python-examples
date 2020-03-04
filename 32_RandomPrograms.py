# This program will:
# - Display a count down
# - Display all even numbers
# - Display an output of *
# - Compute the gratest common divisor
# ===

# Create a while loop that will display count down from 20 to 0
countDown = 20

while countDown != -1:
    print(countDown)
    countDown -= 1
tempVar = input("\nFirst part done, <enter> to continue\n")

# A loop that will display all the even numbers between 1 and 20
for counter in range(1,21):
    if counter % 2 == 0:
        print(f"{counter} is even")
tempVar = input("\nSecond part done, <enter> to continue\n")

# A loop that will produce the following output:
for mainCounter in range(1,6):
    for firstCounter in range(mainCounter):
        print("*", end = "")
    print()
tempVar = input("\nThird part done, <enter> to continue\n")

# To compute the greatest common divisor (GCD) of two positive integers

num1 = int(input("Please provide a positive number: "))
num2 = int(input("Please provide another positive number: "))

gcd = 0
# Checking smallest of the two numbers
if num1 > num2:
    smallNum = num2
    largeNum = num1
else:
    smallNum = num1
    largeNum = num2

# Check the greatest common divisor of the two numbers
for counter in range(smallNum, 0, -1):
    if smallNum % counter == 0 and largeNum % counter == 0:
        if counter > gcd:
            gcd = counter

print(f"{gcd} is the greatest common divisor of the numbers: {smallNum} and {largeNum}")
