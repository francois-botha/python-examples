# This is a program for a department store to calculate the monthly wage for two different types of employees.
# Employees can either be a salesperson or a manager.
# Determine if the user is a salesperson or a manager.
# Salespeople earn an 8% commission on their gross sales and a fixed salary of R2000.00 per month. Managers earn an hourly rate of R40.00.
# Then, depending on their answer, calculate the monthly wage for the employee.
# If the user is a salesperson, ask for their gross sales for the month.
# If the user is a manager, ask for the number of hours worked for the month.
# Display the total monthly wage for the employee.
# ===

# Determine if the user is a salesperson or a manager
role = input("Are you a Salesperson or a Manager? (S/M): ").upper()

# Validate user input
if (role != "S" or role != "M"):
    print("You have an invalid input. Please retry.")

# Salary for employee
elif role == "S":
    grossSales = float(input("What is your gross sales for the month? "))
    print("Your commission for the month is: R%.2f" % ((grossSales * 0.08) + 2000))
else:
    hoursWorked = float(input("What is the number of hours worked for the month? "))
    print("Your salary for the month is: R%.2f" % (40 * hoursWorked))