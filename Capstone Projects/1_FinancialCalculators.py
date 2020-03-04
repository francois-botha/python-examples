# Capstone Project 1

# This program that allows the user to access two different financial calculators: an investment calculator and a homeloan repayment calculator.
# The user should be allowed to choose which calculation they want to do (Investment or Bond). How the user capitalises their selection should not affect how
# the program proceeds.
# If the user doesn’t type in a valid input, show an appropriate error message.

# Importing packages
import math

# This is to test if the string are numeric
def is_float(stringInput):
    try:
        floatNum = float(stringInput)
        return True

    except ValueError:
        return False

# Declaring a variable with a value to enter the while statement
menuOption = ""
print("\nWelcome to the program. This program is for financial calulations.\n")

# Checking input for investment, bond or exit
while menuOption != "exit":
    
    # Display menu and lowercase all inputs
    strLength = len("Choose either \'investment\' or \'bond\' from the menu below to proceed:")
    print("Choose either \'investment\' or \'bond\' from the menu below to proceed:")
    print("*"*strLength)
    print("investment   - to calculate the amount of interest you will earn on interest")
    print("bond         - to calculate the amount you\'ll have to pay on a home loan")
    print("exit         - to exit the program\n")
    menuOption = input("Your choice: ").lower()

    # When user select investment, the user must input the ammount of money depositing
    # and the interest rate as a % - only the number (e.g 8 and not 8%)
    # The number of years of investing
    # Ask user for simple or compound interest - store in var "interest"
    # Output the ammount based on the formulae applied
    if menuOption == "investment":

        # Sending the string input to the "def is_float" to check if the string have numeric values
        stringInput = input("Please enter the amount depositing: ")
        while is_float(stringInput) != True:
            stringInput = input("Please check that you enter the right information. Enter the amount depositing: ")
        else:
            depositAmount = float(stringInput)

        stringInput = input("Please enter the interest rate percentage (e.g 8): ")
        while is_float(stringInput) != True:
            stringInput = input("Please check that you enter the right information. Enter the interest rate percentage (e.g 8): ")
        else:
            interestRate = float(stringInput)/100

        stringInput = input("Please enter the number of year investing: ")
        while is_float(stringInput) != True or float(stringInput) == 0:
            stringInput = input("Please check that you enter the right information. Enter the number of years investing: ")
        else:
            investYears = float(stringInput)

        stringInput = input("Please select one of the following investment types: \'simple\' or \'compound\': ").lower()

        # Checking stringInput variable for simple or compound
        while stringInput != True:

            # Calculating the total amount with simple interest on the information provided
            if stringInput == "simple":
                interest = stringInput

                # Calculating the total amount with simmple interest on the information provided
                returnOnInvestment = depositAmount*(1 + interestRate * investYears)
                result = (f"The return on the investment is: R{returnOnInvestment :.2f}")
                print('='*len(result))
                print(result)
                print('='*len(result))

                # Setting stringInput to True to exit the while statement
                stringInput = True
                    
                # To return to the main screen
                menuOption = input("<enter> to go back to the main screen\n")
                menuOption = "mainMenu"

            elif stringInput == "compound":
                interest = stringInput

                # Calculating the total amount with compound interest on the information provided
                returnOnInvestment = depositAmount * math.pow(1 + interestRate, investYears)
                result = (f"The return on the investment is: R{returnOnInvestment :.2f}")
                print('='*len(result))
                print(result)
                print('='*len(result))

                # Setting stringInput to True to exit the while statement
                stringInput = True

                # To return to the main screen
                menuOption = input("<enter> to go back to the main screen\n")
                menuOption = "mainMenu"
            else:
                print("Please select a valid interest type from the menu only.")
                stringInput = input("Please select one of the following investment types: \'simple\' or \'compound\': ").lower()

    # When user select bond, the user must input the value of the property
    # and the interest rate as a % - only the number (e.g 7)
    # The user also need to specify the number of months to repay the loan
    # Output the result on the information provided
    elif menuOption == "bond":

        # Input of value of the property, interest rate, months and validating the information is numeric
        stringInput = input("What is the value of the property? R")
        while is_float(stringInput) != True:
            stringInput = input("Please check that you enter the right information, enter the value of the property: R")
        else:
            propertyValue = float(stringInput)

        stringInput = input("Please enter the interest rate percentage (e.g 8): ")
        while is_float(stringInput) != True:
            stringInput = input("Please check that you enter the right information, enter the interest rate percentage (e.g 8): ")
        else:
            interestRate = float(stringInput)/100

        stringInput = input("Please enter the number of months to repay the bond: ")
        while is_float(stringInput) != True or float(stringInput) == 0:
            stringInput = input("Please check that you enter the right information, enter the number of months to repay the bond: ")
        else:
            bondRepayMonth = float(stringInput)

        # Bond repayment calculation and display restult
        repayment = ((propertyValue * math.pow((interestRate/12)+1,bondRepayMonth))*(interestRate/12)) / ((math.pow(interestRate/12 + 1, bondRepayMonth) - 1))
        result = (f"You will need to repay R{repayment :.2f} per month for {bondRepayMonth :.0f} months.")
        print('='*len(result))
        print(result)
        print('='*len(result))

        menuOption = input("<enter> to go back to the main screen\n")
        menuOption = "mainMenu"


    elif menuOption == "exit":
        menuOption = "exit"

    else:
        print("-"*strLength)
        print("Please make a valid selection from the menu only.\n")
        
else:
    print("Thank you for using this program.")