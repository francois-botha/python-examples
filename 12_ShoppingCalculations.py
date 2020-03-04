# This program will ask the user to enter three products, as well as the price accepted as a decimal value.
# Caluslations is then performed:
# - Calculate the total of all products
# - Calculate average price of products
# After the calculations the results is printed to the console in a sentence.

# Aske user for products
product1 = input("Enter your first product: ")
product2 = input("Enter your second product: ")
product3 = input("Enter you third product: ")

# Price of each products - 2 decimal
price_prod1 = float(input(f"What is the price for {product1}? "))
price_prod2 = float(input(f"What is the price for {product2}? "))
price_prod3 = float(input(f"What is the price for {product3}? "))

# Calc total of all products
total = price_prod1 + price_prod2 + price_prod3

# Calc average price of products
average = total / 3

# Print out in sentence
print(f"The Total of {product1}, {product2}, {product3} is R{total:.2f} and the average price of the items are R{average:.2f}")