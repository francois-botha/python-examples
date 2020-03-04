# This program will ask the user for their favourite restaurant and store it in a variable: favRest.
# Then the user favourite number will be asked and casting will be used to store the value in intFav.
# Both of these variables will be printed to the console.
# Finally it will cast favRest to an int
# ===

# Ask the user for its favourite restaurant
favRest = input("What is the name of your favourite restaurant? ")

# Ask the user for its favourite number
intFav = int(input("What is your favourite number? "))

# Print both variables
print("Your restaurant is: ", favRest)
print("Your number is: ", intFav)

# Cast favRest into an int
print("Casting favRest to an int:", int(favRest)) # An error when casting. Casting will only work if the favRest consist of numerical values only