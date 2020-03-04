# This is a program that always asks the user to enter a number
# When the user enters -1, the program should stop requesting the user to enter a number
# The program must then calculate the average of the numbers entered excluding the -1
# ===

# To test if the string is numeric
def is_float(stringInput):
    try:
        floatNum = float(stringInput)
        return True

    except ValueError:
        return False

# Declare and assign variables values to enter the while statement
mainLoop = True
numTotal = 0
numCount = 0

# Entering while statement
while mainLoop or numCount == 0:
    stringInput = input("Please enter a number: ")
    if is_float(stringInput):
        userNum = float(stringInput)
        if userNum != -1:
            numTotal += userNum
            numCount += 1
        else:
            mainLoop = False
            
    # An error occur when blank inputs are entered followed by -1 and then a numeric input
    # This is to exit the program when -1 is entered and no other information is captured
    if mainLoop == False and userNum == -1 and numCount == 0:
        print("No information is provided.\nProgram terminated without calculation.")
        break
else:
    # Printing results of the information captured
    printResult = (f"The average of all the numbers entered is: {numTotal/numCount:.2f}")
    print("-"*len(printResult))
    print(printResult)
    print("-"*len(printResult))
    print("Program Terminated!")