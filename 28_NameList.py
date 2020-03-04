# This program require the user to enter the names of all pupils in a class
# # When the user type “Stop” to indicate that the names of all the students have been entered
# It will print out all the names the users entered after the loop has been exited

# Declare variables and assign value to variables
name = ""
nameList = []
maxNameLength = 10

while name != "Stop":
    name = input("Please enter a name: ").title()
    nameList.append(name)
    # To get the max length of a name
    if len(name) > maxNameLength:
        maxNameLength = len(name)
else:
    # Remove "Stop" from the list and printing the list
    nameList.remove("Stop")
    print("-"*maxNameLength)
    print("Name List:")
    print("="*maxNameLength)
    print(*nameList, sep = "\n")