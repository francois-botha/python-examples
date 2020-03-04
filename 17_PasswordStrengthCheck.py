# This program will determine if your password is strong.
# First the varibales is delcared and assigned to false.
# The user is asked a series of yes and no questions.
# These values will be stored in a list and the list is checked if there are at least 3 true values to have a strong password.
# ===

# Declare boolean variables as false
haveLength = False
upCase = False
lowCase = False
haveNum = False

# Ask user yes-no questions for each variable
print("Please enter Y- for \"Yes\" or N- for \"No\" on the following questions")
question1 = input("Does your password have 6 characters or more? ").upper()
question2 = input("Does your password contain an UPPERCASE? ").upper()
question3 = input("Does your password contain a lowercase? ").upper()
question4 = input("Does your password contain numbers? ").upper()

# Check if questions is Y or N only
if (question1 == "Y" or question1 == "N") and (question2 == "Y" or question2 == "N") and (question3 == "Y" or question3 == "N") and (question4 == "Y" or question4 == "N"):
    if question1 == "Y":
        haveLength = True
    if question2 == "Y":
        upCase = True
    if question3 == "Y":
        lowCase = True
    if question4 == "Y":
        haveNum = True

    # Values are sored in a array list
    list = [] # Declare empty list
    list = (haveLength, upCase,  lowCase, haveNum)

    # The array list is check to validate if there is 3 or more true values
    if ((list.count(True)) >= 3):
      print("Your password is suitable")
else: print("Only \"Y\" or \"N\" accepted. Please retry.")