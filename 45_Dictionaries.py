# About the program:
# Create a list called menu, which should contain at least 4 items in the cafe.
# Next, create a dictionary called stock, which should contain the stock value for each item on your menu.
# Create another dictionary called price, which should contain the prices for each item on your menu.
# Next, create a function which will calculate the total stock worth in the cafe. You will need to remember to loop through the appropriate
# dictionaries and lists to do this.
# Finally, print out the result of your function.

def totalStock(stockWorth):
    for item in menu:
        # Work out the total value of the cafe and print out the results
        stockWorth = stockWorth + (dictStock[item] * dictPrice[item])
    return stockWorth

# Define a list with values
menu = ["Coffee", "Tea", "Milkshake", "Cupcakes"]

# Declare 2 dictionaries
dictStock = {}
dictPrice = {}
stockWorth = 0

for item in menu :
    # For every item in the menu, add the item in the stock dictionary together with its stock level
    dictStock[item] = int(input(f"How many stock for {item.lower()}? "))
    # For every item in the menu, add the item in the price dictionary together with its price
    dictPrice[item] = int(input(f"What is the price for {item.lower()}? "))
    print()

print("The total stock worth is R", totalStock(stockWorth))