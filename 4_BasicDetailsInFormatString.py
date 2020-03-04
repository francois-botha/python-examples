# This program will get basic information from the user and print out the information in a single sentence.

# Declaring variables and assigning them from the user input
name =  input("What is your name? ")
age = input("What is your age? ")
house_num = input("What is your house number: ")
street_name = input("What is the name of the street? ")

# Print out of information to the console using a format string
print(f"This is {name}, {age} years old. Home address is {house_num} {street_name}")
