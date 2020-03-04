# About this program:
# You will need to create four functions:
#    HotelCost - This function will take the number of nights a user will be staying at a hotel as an argument and return a total cost for the
#    hotel stay (You can choose the price per night charged at the hotel).

#    PlaneCost - This function will take the city you are flying to as an argument and return a cost for the flight (Hint: use if/else if
#    statements in the function to retrieve a price based on the chosen city).

#    CarRental - This function will take the number of days the car will be hired for as an argument and returns the total cost of the car rental.

#    HolidayCost - This function will take three arguments: the number of nights a user will be staying in a hotel, the city the user will be
#    flying to and the number of days that the user will be hiring a car for. Using these three arguments, you can call all three of the
#    above functions with respective arguments and finally return a total cost for your holiday.

# Print out all the details about the holiday in a meaningful way!
# Try using your app with different combinations of input to show it’s compatibility with different options.

# Function to calculate the hotel cost
def hotelCost(numNights):
    totalCost = int(numNights) * 550
    return totalCost

# Function to calculate the destination cost
def planeCost(destination):
    if destination == "1":
        return 5000
    elif destination == "2":
        return 7500
    elif destination == "3":
        return 8000
    elif destination == "4":
        return 9000
    else:
        return 10000

# Function to calculate the car rental cost
def carRental(carDays):
    return int(carDays) * 150

# Function to calculate the total cost
def holidayCost(numNights, destination, carDays):
    return (hotelCost(numNights) + planeCost(destination) + carRental(carDays))

print("Hotel Accommodation @ R550 per night")
print("====================================")
numNights = input("How many nights would you like to stay? ")
print()

print("Holiday destinations:")
print("=====================")
print(
    "1 - South Africa\n"
    "    R5000\n"
    "\n2 - Egypt\n"
    "    R7500\n"
    "\n3 - Greece\n"
    "    R8000\n"
    "\n4 - Italy\n"
    "    R9000\n"
    "\n5 - All other locations\n"
    "    R10 000"
    )
destination = input("Please select an option: ")

print("\nCar Rental")
print("==========")
carDays = input("\nHow many days is a rental car required? ")

print("\nHoliday Summary")
print("===============")

# Calling functions created to calculate cost
print(f"Hotel Cost: R{hotelCost(numNights)} for {numNights} nights.")
print(f"Plane Cost: R{planeCost(destination)}")
print(f"Rental Cost: R{carRental(carDays)} for {carDays} days.\n")
print("Total Holiday Cost: R", holidayCost(numNights, destination, carDays))