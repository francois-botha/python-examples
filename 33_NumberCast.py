# This program will get the user to input a number and cast it to an int. Store it in a variable called num.
# Now, if the number is bigger than 10, use a for loop to output it as many times as its value. For example, if a user enters 11, the number 11 will be
# printed out 11 times.
# If the user enters anything less than or equal to 10, the program should output "Sorry, too small".
# ===

import os
clear = lambda: os.system("cls")

# Assigning num to enter the while loop
num = None

# To clear the screen
clear()
print("== Welcome to the program ==")
while num is None:
    num = input("Please enter a number: ")
    # Checking num for numeric value
    if num.isdigit():
        num = int(num)
    else:
        # Display message if input is invalid and assigning num to none to remain in the while loop
        print("please check that you input the right info.")
        num = None
        continue
    if num > 10:
        for counter in range(num):
            print(f"{counter + 1} - {num}")
    else:
        print("Sorry, too small")
else:
    print("Program terminated! Thanks for using this program!")