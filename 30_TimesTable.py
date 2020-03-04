# This program will display the timetables for any number provided

print("Welcome to the program. To exit the program type \"exit\"")

# Ask the user for a whole number
number = input("Please enter a number or \"exit\" to quit: ")

while number != "exit":
    if number.isdigit():
        number = int(number)
        for table in range(1,13):
            print(f"{number} X {table} = {number * table}")
    else:
        number = input("Please input a whole number: ")
        continue
    number = input("Please enter a number or \"exit\" to quit: ")
else:
    print("Program terminated!")