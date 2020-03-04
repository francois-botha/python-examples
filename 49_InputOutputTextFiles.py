# About this program:
# Write code to read the content of the text file input.txt.
# For each line in input.txt, write a new line in the new text file output.txt that computes the answer to some operation on a list of numbers.
# If the input.txt has the following:
# Min: 1,2,3,5,6
# Max: 1,2,3,5,6
# Avg: 1,2,3,5,6

# Your program should generate output.txt as follows:
# The min of [1, 2, 3, 5, 6] is 1.
# The max of [1, 2, 3, 5, 6] is 6.
# The avg of [1, 2, 3, 5, 6] is 3.4.

# Assume that the only operations given in the input file are min, max and avg, and that the operation is always followed by a list of comma separated integers.
# You should define the functions min, max and avg that take in a list of integers and return the min, max or avg of the list.
# Your program should handle any combination of operations and any length of input numbers.
# You can assume that the list of input numbers are always valid integers and that the list is never empty.

try :
    # Reading input.txt file
    inputFile = open('input.txt', 'r')
    listData = inputFile.read().splitlines()
    # Open output.txt file to write
    outputFile = open('output.txt', 'w')

    lineCount = 0
    for line in listData :
        lineCount += 1
        # Split the lines in to seperate the numbers
        lineList = line.split()
        # Split numbers into a list
        numbers = lineList[1].split(",")

        if lineCount == 1 :
            # Find the min number in the list and write to file
            minNum = min(numbers)
            outputFile.write(f"The min of [{lineList[1]}] is {minNum}\n")
        elif lineCount == 2 :
            # Find the max number in the list and write to file
            maxNum = max(numbers)
            outputFile.write(f"The max of [{lineList[1]}] is {maxNum}\n")
        else :
            # Convert the sting to an int for calulation on the numbers
            for num in range(len(numbers)) :
                numbers[num] = int(numbers[num])
            # Find the avg number of the list and write it to a file
            avgNum = sum(numbers) / len(numbers)
            outputFile.write(f"The avg of [{lineList[1]}] is {avgNum}\n")

    print("\nCheck the output.txt file for results")

except FileNotFoundError :
    print("File not fould, please open the folder to run the program!")

finally :
    # Close open files
    if not inputFile.closed :
        inputFile.close()
        outputFile.close()