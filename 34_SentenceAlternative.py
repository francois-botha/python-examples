# This is a program that reads in a sting and makes each alternate character an uppercase character and each other alternate
# character a lowercase character.
# For example, the string “Hello World” would become “HeLlO WoRlD”
# ===

# Ask the user for a sentence and store it in strWord
# Upper case the sentence
strWord = input("Enter a sentence: ").upper()

# Declare a list called charList
charList = []

# For every character in the sentence, add it to the list
for char in strWord:
    charList.append(char)

# For every character in the range of the list, starting at character 2
# Replace the upper case with a lower case of that character
for char in range(1,len(charList),2):
    charList[char] = charList[char].replace(charList[char],charList[char].lower())

# Join the list to a string and print the results
strWord = "".join(charList)
print(strWord)
