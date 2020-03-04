# This is a program to calculate the cost of sending a parcel.
# It will ask the user to enter a price of the package,
# and it will ask user for the distance in km.
# It will calculate the delivery cost and
# calculate the total cost.
# ===

# Declaring variables


# Ask the user details about the sending of the package
packagePrice = float(input("Please enter the price of the package you would like to purchase: "))
totalDistance = float(input("Please enter the total distance of the delivery in km: "))

# Transport method
print("To transport by air is R0.36 per km, and by freight is R0.25 per km")
transport = input("Would you like to send it by air? (Y/N): ").upper()

# Insurance
print("Full insurance on your parcel is R50, or limited insurance is R25")
insurance = input("Would you like full insurance? (Y/N): ").upper()

# Gift
gift = input("Would you like to send it as a gift - only R15 extra? (Y/N) ").upper()

# Speedy sending
print("Sending with priority is R100 and standard is R20")
sending = input("Would you like to send it with Priority? (Y/N) ").upper()

# Calculate the total cost
totalCost = packagePrice
if transport == "Y":
    totalCost = totalCost + (totalDistance * 0.36)
else:
    totalCost = totalCost + (totalDistance * 0.25)

if insurance == "Y":
    totalCost += 50
else:
    totalCost += 25

totalCost += 15 if gift == "Y" else totalCost

if sending == "Y":
    totalCost += 100
else:
    totalCost += 20

print("The total cost of the package based on your selection is: R %.2f" % totalCost)