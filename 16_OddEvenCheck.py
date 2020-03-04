# This program will test if a number if odd or even.
# It will ask the user for number and
# test if the number is odd or even using the modulus operator.
# ===

# Ask the user for number
number = input("Please enter a number: ")
if number != "":

    # Changing number from string to int
    number = int(number) 
    
    # Test if number is odd or even
    if ((number % 2) == 0):
        test = "Even"
    else:
        test = "Odd"

    # Print out the number and whether it is odd or even
    print(f"The number you entered was: {number}, and it is: {test}")

else: print("You did not enter any valid input.")