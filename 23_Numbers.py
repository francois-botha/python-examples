# This program will declare three variables called “num1”, “num2” and “num3”. Assign each variable a number value
# Then, compare “num1” and “num2” and display the larger value
# Next, determine whether “num1” is odd or even and display the result
# Next, write a conditional statement to sort the three numbers from largest to smallest
# ===

# Declare 3 var and assign them
num1 = 45
num2 = 60
num3 = 15

# Compare “num1” and “num2” and display the larger value
if num1 > num2:
    print(f"num1: {num1} is the larger value")
else: print(f"num2: {num2} is the larger value")

# Determine whether “num1” is odd or even and display the result
if (num1 % 2) == 0:
    print(f"num1: {num1} is even")
else: print(f"num1: {num1} is odd")

# Conditional statement to sort the three numbers from largest to smallest
# Small
if num1 < num2 and num1 < num3:
    small = num1
elif num2 < num1 and num2 < num3:
    small = num2
else: small = num3

# Large
if num1 > num2 and num1 > num3:
    large = num1
elif num2 > num1 and num2 > num3:
    large = num2
else: large = num3

# Middle
if (num1 < small or num1 > small) and (num1 < large or num1 > large):
    middle = num1
elif (num2 < small or num2 > small) and (num2 < large or num2 > large):
    middle = num2
else: middle = num3

print(f"The numbers are from largers to smallest: {large} {middle} {small}")

