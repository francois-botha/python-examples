# This program will ask the user for 3 numbers.
# It will then print out the sum of all numnbers.
# The first less the second number.
# As well as thrid multiply by first number.
# And the sum of all 3 numbers divided by the third number.
# The results is then printed to the console.
# ===

# Ask the user for 3 numbers
int1 = int(input("Enter your first number: "))
int2 = int(input("Enter your second number: "))
int3 = int(input("Enter your third number: "))

# Print the sum of all numbers
print("Sum of all numbers:", int1 + int2 + int3)

# First less second number
print("1st number less 2nd number:", int1 - int2)

# Third multiply by first number
print("3rd number times 1st number:", int3 * int1)

# Sum of al 3 numbers divided by third number
print("Sum of all numbers divided by 3rd number:", float(int1 + int2 + int3) / int3)