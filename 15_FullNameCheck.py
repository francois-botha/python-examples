# This program will validate that user enter at least two names as a full name.
# Ask user to enter their full name.
# Validate the user input and display an appropiate message.

# Ask user to enter a full name
full_name = input("Please enter your full name: ")

# Check to see if the input is not blank
# If the input is blank, it will display a message that the user did not enter anything
if full_name != "":

    # Split the full name to check if more than one name exist
    # Calculate the lenght of the full name
    name_count = len(full_name.split(" "))
    fullName_length = len(full_name)

    if (name_count < 2): # Check if the user have more than one name
        print("You only entered one name. Please enter your full name")
    elif (fullName_length < 4): # Check length of name less than 4 characters
        print("You have entered less than 4 characters. Please make sure that you have entered your name and surname")
    elif (fullName_length > 25): # Check length of name greater than 25 characters
        print("Please make sure that you have only entered your full name")
    else:
        print("Thank you for entering your name")
        
else: print("You did not enter anything, please enter your full name!")