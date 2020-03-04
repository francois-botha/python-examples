# This program will ask the user to enter a number less than 100
# If they enter one above 100, ask them to try again (and continue to do so until they follow instructions)
# Once they have entered a valid number, check if it is even
# If it is even then multiply it by 2 and print it out
# If it odd, then multiply it by 3 and print it out
# ===

number = input("Please enter a number less than 100: ")

# When the input is not a whole number or more than 100 or a sting value, it will keep asking for the correct input
while number.isdigit() == False or int(number) > 100:
    number = input("You have to enter a whole number less than 100, please try again.\nEnter a number less than 100: ")

number = int(number)
if number % 2 == 0:
    print(f"Your number, {number} is even. The number will be multiplied by 2 and the answer is: {number * 2}")
else:
    print(f"Your number, {number} is odd. The number will be multiplied by 3 and the answer is: {number * 3}")

