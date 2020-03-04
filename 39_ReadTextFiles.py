# This is a program that reads the data from the text file called ‘DOB.txt’ and prints it out in two different sections

# Create 3 lists, tempList, fullNameList and birthdayList
tempList = []
fullNameList = []
birthdayList = []

lines = ""
print("Welcome to the program. Here you will see a list of full names as well as a list on their birthdates.\n")

# Open file called DOB.txt
with open("DOB.txt") as file:
    lines = file.readlines()

print("Name:")
print("-"*20)

# Read the file line by line and store the info in variable called lines
for line in lines:
    tempList = line.split()

    # Determine the length of the list
    # Split the name to the fullNameList until the date
    fullNameList = tempList[:len(tempList) - 3:]

    # Add the list back into a string and print the results
    name = " ".join(fullNameList)
    print(name)

print("\nBirthdate:")
print("-"*20)

# Read the file line by line and store the info in variable called lines
for line in lines:
    tempList = line.split()

    # Determine the length of the list
    # Split the last 3 items in the list to the bithhdayList
    birthdayList = tempList[len(tempList) - 3::]

    # Add the list back into a string and print the results
    birthdate = " ".join(birthdayList)
    print(birthdate)