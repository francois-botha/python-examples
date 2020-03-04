# About this program:
# A program that can convert a binary number to a decimal number.
# A binary number is a number that is made up entirely of 0s and 1s (e.g101101). You can represent any amount you would like using binary.
# Ask the user to enter a binary number and convert that number to a decimal number.
# You can visit the following website to find out how to convert from binary to decimal:
# http://www.rapidtables.com/convert/number/how-binary-to-decimal.htm
# Print out the decimal value of the number.
# Remember to make use of the built-in functions found in the math module as well as lists (remember to import the math module into your program!).

import math

# Ask user to input binary code
binaryNumber = input("Please enter your binary number: ")

# Convert binary to decimal using the int() built-in function
print("Binary", binaryNumber, "in decimal is:", int(binaryNumber, 2))