# About the program:
# A program that takes in a user’s input as a String.
# While the String is not “John”, add every String entered to a list until John” is entered. Then print out the list. This program basically stores all
# incorrectly entered Strings in a list where “John” is the only correct String.
# Example program run (what should show up in the Python Console when you run it):
#           Enter your name : <user enters Tim>
#           Enter your name : <user enters Mark>
#           Enter your name: <user enters John>
#           Incorrect names: [‘Tim’, ‘Mark’]

# Define list to store names in
nameList = []
name = ""

# Check name condition
while name != "John" : 
    name = input("Enter your name : ").capitalize()
    nameList.append(name)

# Print only incorrect names
print("Incorrect names: ", nameList[0:len(nameList) - 1])