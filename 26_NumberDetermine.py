# This program asks the user to enter an integer and determine if it is:
# divisible by 2 and 5
# divisible by 2 or 5
# not divisible by 2 or 5
# Display your result to console
# ===

# Ask user for number
number = input("Please enter a whole number:\n")

# Validation
if number.isdigit():
    number = int(number)

    # divisible by 2 and 5
    if number % 2 == 0 and number % 5 == 0:
        answer = "Yes"
    else: answer = "No"
    print(f"The number {number} is divisible by 2 and 5? {answer}")

    # Divisible by 2 or 5
    if number % 2 == 0 or number % 5 == 0:
        answer = "Yes"
    else: answer = "No"
    print(f"The number {number} is divisible by 2 or 5? {answer}")

    # not divisible by 2 or 5
    if number % 2 == 0 or number % 5 == 0:
        answer = "No"
    else: answer = "Yes"
    print(f"The number {number} is not divisible by 2 or 5? {answer}")
    
else: print("Please only enter whole numbers")