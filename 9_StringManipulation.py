# This program will ask the user for a sentence, and will save the input in a variable: strManip.
# Using the variable it will:
# - Calculate and display the length
# - Find last letter, replace occurence of this letter with '@'
# - Print last 3 char backwards
# - Create 5 letter word, that is made up of the first 3 characters and the last 2 characters
# - Display each word in the sentence on new line
# ===

# Ask user for sentence and save to the variable
strManip = input("Please provide a full sentence: ")

# Calc and disp length of the sentence
print("The calculated length of your sentence is:", len(strManip))

# Find last letter, replace occurence of letter with @
print("The last letter in your sentence is:", strManip[len(strManip)-1])
print("Your new sentence will be:", strManip.replace(strManip[len(strManip)-1], "@"))

# Print last 3 char backwards
print("The last 3 characters backward is:", strManip[::-1][0:3])

# Create 5 letter word, that is made up of the first 3 characters and the last 2 characters
print("your new 5-letter word is:", strManip[0:3] + strManip[len(strManip)-2:len(strManip)-0])

# Display each word on new line
print("Displaying each word on a new line:\n",strManip.replace(" ",'\n'))