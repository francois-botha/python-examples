# This program will ask to input a year and a number of years.
# Then determine and display which of those years were or will be leap years.
# ===

# While variables to enter the while loop
startYearValidation = True
checkYearsValidation = True

# While loop to validate the start year input
while startYearValidation:
    print("-"*41)
    startYear = input("What year do you want to start with? ")
    if startYear.isdigit():
        startYear = int(startYear)
        startYearValidation = False
    else:
        print("\nThe information is incorrect. Please try again.")

# While loop to validate the all the years input
while checkYearsValidation:
    checkYears = input("How many years do you want to check? ")
    print("-"*41)
    if checkYears.isdigit():
        checkYears = int(checkYears)
        checkYearsValidation = False
    else:
        print("\nThe information is incorrect. Please try again.")

endYear = startYear + checkYears

# For loop to check leap year with the info provided
for startYear in range(startYear,endYear):
    if startYear % 4 == 0:
        print(f"{startYear} is a leap year")
    else:
        print(f"{startYear} isn’t a leap year")