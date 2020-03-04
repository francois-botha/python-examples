# This program will display a message based on their age.
# Ask the user’s age using input() and store their age in an integer variable called age
# Then check if the user’s age is over 18. If the user is over 18, print out the message “You are old enough!” else if they are over 16 print “Almost there”,
# otherwise print “You’re just too young!” You should use one if, elif and else statement to do this
# ===

# Getting user age
age = int(input("What is your age?\n"))

# Checking age conditions
if age > 18:
    print("You are old enough! ")
elif age > 16:
    print("Almost there ")
else:
    print("You\'re just too young! ")
