# Capstone Project II - Nested Loops

# A program to check if a number inputted by the user is prime. A prime number is a positive integer greater than 1 whose only factors are 1
# and the number itself. Examples of prime numbers are: 2, 3, 5, 7, etc.
# Ask the user to enter an integer.
# First, check if the number is greater than 1.
# If it is greater than 1, check to see if it has any factors besides one and itself, i.e. if there are any numbers between 2 and the number itself that
# can divide the number without any remainders.
# If the number is a prime number, print out the number and ' is a prime number!'
# If the number is not a prime number, print out the number and ' is not a prime number'

print("This program will check if the following number you entered is a prime or not.")

number = int(input("Please enter a number: "))

if number > 1:
    for counter in range(2,number):
        modCheck = number % counter
        if modCheck == 0:
            print(f"{number} is not a prime number")
            break
        else:
            modCheck == True
    if modCheck == True:
        print(f"{number} is a prime number!")
else:
    print("Condition is not valid.")