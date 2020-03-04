# This program will get two number from the user, and will be stored in num1 and num2.
# Then the variables will be swopped around.
# The variables will be printed before swopping and afther swopping
# ===

# Getting two numbers from the user
num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")

# Printing before the swopping the variables
print ("Your original numbers: ")
print("Number 1: " + num1)
print("Number 2: " + num2)

# Swopping the variables around
temp = num2
num2 = num1
num1 = temp

# Printing numbers after the swopping the variables
print("Your new number order is: ")
print(num1)
print(num2)