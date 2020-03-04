# About the program:
# A program that allows students to register for an exam venue.
# First, ask the user how many students are registering.
# Create a for loop that runs for that amount of students
# Each loop asks for the student to enter their ID number.
# Write each of the ID numbers to a Text File called “RegForm.txt”
# This will be used as an attendance register that they will sign when they arrive at the exam venue.
# ===

# Open a new file called RegForm.txt
regForm = open('RegForm.txt', 'w')

print("Welcome to the program, this will allow you to register students for exams\n")

studentCount = ""
while studentCount == "" :
    # Ask how many students are registering ans store in var studentCount
    studentCount = input("How many students will be attending? ")

    # Validate input is numerical
    if studentCount.isdigit():
        studentCount = int(studentCount)
    else:
        print("The input is incorrect, please try again.")
        studentCount = ""
else:
    print(f"\nThanks - you have {studentCount} students.\n")

# Create a for loop in studentCount, asking for their ID num
for studentNum in range(studentCount) :

    studentIdNum = ""
    while studentIdNum == "" :
        studentIdNum = input(f"What is the ID number for student {studentNum + 1}? ")

        # Validate input is numerical for ID
        if studentIdNum.isdigit():
            continue
        else:
            print("The input is incorrect, please try again.")
            studentIdNum = ""

    regForm.write(studentIdNum + "\n")

# Close RegForm.txt
regForm.close()