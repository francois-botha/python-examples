# This program will help the user decide what to wear.
# To determine what to wear, you need to determine whether the temperature is greater than 20 degrees, whether it is the weekend, and whether it is sunny.
# It will declare varibles as false and
# ask the user yes-no questions on each variable and update the variable.
# ===

# Declare variables and assign it to false
temp = False
weekType = False
sunny = False

# Ask user questions on variables
print("Please enter Y- for \"Yes\" or N- for \"No\" on the following questions")
question1 = input("Is the temperature more than 20 degrees? ").upper()
question2 = input("Is it weekend? ").upper()
question3 = input("Is the sun shining outside? ").upper()

# Check if questions is Y or N only
if (question1 == "Y" or question1 == "N") and (question2 == "Y" or question2 == "N") and (question3 == "Y" or question3 == "N"):

    # What shirt to wear based on temperature
    if question1 == "Y":
        temp = True
        shirt = "short-sleeved shirt"
        tempDegree = "more than 20 degrees"
    else:
        Temp = False
        shirt = "long-sleeved shirt"
        tempDegree = "less than 20 degrees"

    # What pants to wear based on week type
    if question2 == "Y":
        weekType = True
        pants = "shorts"
        week = "the weekend"
    else:
        weekType = False
        pants = "jeans"
        week = "a weekday"

    # To wear a cap or raincoat based in sunshine
    if question3 == "Y":
        sunny = True
        head = "cap"
        sun = "shining"
    else:
        sunny = False
        head = "raincoat"
        sun = "not shining"

    # User instructions on what to wear
    print(f"Today the sun is {sun} and it\'s {week}. The temperature is {tempDegree}. You should wear your {shirt} and {pants}, together with your {head}.y")

else: print("Your input needs to be Y or N. Please retry")
