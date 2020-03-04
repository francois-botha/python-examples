# This program will declare a variable with the value of "Super Man".
# And will print out to the console in the following way: "S^U^P^E^R M^A^N"
# ===

# Delcaring and initiating variable
hero = "Super Man"

# Upper case word
hero = hero.upper()

# Print out word in a new way 
print(f"{hero[0]}^{hero[1]}^{hero[2]}^{hero[3]}^{hero[4]}{hero[5]}{hero[6]}^{hero[7]}^{hero[8]}")

# Or printing it in this way will also be more efficient
# chr(94) = ^ (Keyboard: ALT + 94)
# Below is shown that you can use both chr(94) or the actual "^" symbol
print(f'{chr(94).join(list(hero)[:5:1])} {"^".join(list(hero)[6::1])}')