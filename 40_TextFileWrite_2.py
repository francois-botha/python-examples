# About the program:
# Create a text file called ‘numbers1.txt’ that contains Integers which are sorted from smallest to largest.
# Create another text file called ‘numbers2.txt’ which also contains Integers that are sorted from smallest to largest.
# Write the numbers from both files to a third file called ‘allNumbers.txt’
# All the numbers in ‘allNumbers.txt’ should be sorted from smallest to largest.

numbersList = []

print("Welcome to the program. This program will load the integer values of numbers1.txt and numbers2.txt, sort from smallest to largest")
print("and wite the results back to a new file called allNumbers.txt")
exceptionRaised = False
try:
    # Open existing files called numbers1 and numbers2
    numbers1 = open('numbers1.txt', 'r')
    numbers2 = open('numbers2.txt', 'r')

    # New file to write result from both files
    allNumbers = open('allNumbers.txt', 'w')

    # Load numbers1 and numbers2 into a list called numbersList
    for number in numbers1.readlines() :
        numbersList += number.split()

    for number in numbers2.readlines() :
        numbersList += number.split()

    # Convert the list to an int value
    for number in range(len(numbersList)) :
        numbersList[number] = int(numbersList[number])

    # Sorting list from smallest to largest
    numbersList.sort()

    # Convert list back to string and writing to file allNumbers.txt
    for number in range(len(numbersList)) :
        allNumbers.write(str(numbersList[number]) + "\n")

    print("Program done!")
    print("Please check the results in allNumbers.txt")
except FileNotFoundError:
    print("File not found")
    exceptionRaised = True
except FileExistsError:
    print("File already exists")
    exceptionRaised = True
except:
    print("Something went wrong ")     
    exceptionRaised = True
finally:
    if not exceptionRaised:
    # Close files
        numbers1.close()
        numbers2.close()
        allNumbers.close()
