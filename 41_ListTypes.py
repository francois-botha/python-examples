# About the program:
# Imagine you want to store the names of three of your friends in a list of Strings. Create a list variable called friends_names, and write the syntax to
# store the full names of three of your friends.
# Now, write statements to print out the name of the first friend, then the name of the last friend, and finally the length of the list.
# Now, define a list called friends_ages, that stores the age of each of your friends in a corresponding manner, i.e., the first entry of this list is the age
# of the friend named first in your other list.

# Define a list for friends names
friends_names = []

# Ask for the name 3 times and append the result to the names list
for num in range(3) :
    name = input(f"What is the name of friend nr: {num+1}? ")
    friends_names.append(name)

# Print out the 1st and last friend name and print out the length of the list
print("The first friend name is:", friends_names[0], "and the third friend name is:", friends_names[2])
print("The length of the friends_names list is:", len(friends_names))

# Define a list for friends ages
friends_ages = []

# For every friend in the friends_names list, ask how old they are
for friend in friends_names : 
    age = input(f"How old is {friend}? ")
    friends_ages.append(age)

# Print out the results to see that the 2 lists correspond
print(friends_names)
print(friends_ages)