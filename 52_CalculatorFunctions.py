# About this program:
# A program that will act as a calculator.
# Create functions named addNum, subtractNum, multiplyNum and divideNum that asks the user to enter two numbers and adds, subtracts,
# multiplies or divides them respectively.
# Print out the following menu and ask the user to input a number that corresponds to the option they would like to choose:
#   Option 1 - add
#   Option 2 - subtract
#   Option 3 - multiply
#   Option 4 - divide
# If the user enters 1 call the addNum function
# If the user enters 2 call the subtractNum function
# If the user enters 3 call the multiplyNum function
# If the user enters 4 call the divideNum function
# Make sure that the result of the calculation is printed out to the screen.

# Function to add, subtract, multiply and divide 2 numbers
def addNum(num1, num2, answer):
    answer = int(num1) + int(num2)
    return answer

def subtractNum(num1, num2, answer):
    answer = int(num1) - int(num2)
    return answer

def multiplyNum(num1, num2, answer):
    answer = int(num1) * int(num2)
    return answer

def divideNum(num1, num2, answer):
    answer = float(num1) / float(num2)
    return answer

# Ask user for 2 numers
num1 = input("Please enter number 1: ")
num2 = input("Please enter number 2: ")
answer = 0

print("Calculator:\n"
      "===========")

# Calculator menu
print("""
1 - add
2 - subtract
3 - multiply
4 - divide
""")
calcOption = input("Please select an option: ")

# Check user input against the menu options
if calcOption == "1":
    print("\nAdd:")
    print(f"{num1} + {num2} = {addNum(num1, num2, answer)}")
elif calcOption == "2":
    print("\nSubtract:")
    print(f"{num1} - {num2} = {subtractNum(num1, num2, answer)}")
elif calcOption == "3":
    print("\nMultiply:")
    print(f"{num1} X {num2} = {multiplyNum(num1, num2, answer)}")
elif calcOption == "4":
    print("Divide:")
    print(f"{num1} / {num2} = {divideNum(num1, num2, answer):.2f}")
else:
    print("No valid calculation input")