# This isa program that strips a set of characters from a string.
# Ask the user to input a string and then ask the user which characters they would like to make disappear.
# For example:
# The quick brown fox jumps over the lazy dog.
# After stripping a,e,i,o,u
# Th qck brwn fx jmps vr th lzy dg.
# ===

# Ask user for a sentence and store in var sentence
sentence = input("Enter a sentence: ")

# Ask which characters needs to be removed store in var charToRemove
charToRemove = input("Which character would you like to remove? ")

# For each character in the charToRemove variable check to see if it exist in the sentence and remove
for char in charToRemove:
    sentence = sentence.replace(char, "")

# Print out the result
print(sentence)