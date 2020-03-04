# This progam will determine is the user is over 18 and allowed entry.
# It will ask user to enter year when born and calculate if the user is older than 18.
# If the user is older than 18, a message will be displayed on the console.
# ===

# Importing datetime to get the age of the user at this point in time
import datetime

# Ask user to enter year when born and calculate if user is older than 18
age_str = (input("Please enter the year that you were born: "))
if age_str != "":
    age = int(age_str)
    
    # If older than 18, display message
    if ((datetime.datetime.now().year - age) > 18):
        print("Congrats you are old enough")

else: print("Please enter a valid input")