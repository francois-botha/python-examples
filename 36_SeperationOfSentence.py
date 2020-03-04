# This is a program which inputs a sentence and then displays each word of the sentence on a separate line.

# Ask user for a sentence and store in variable sentence
print("Welcome to the program - here you will enter a sentence and each word will be displayed on a new line.")
sentence = input("Enter a sentence: ")

# Split the words when a space is found in a list called wordsList
wordsList = sentence.split(" ")

# For every word in the wordsList, print out the word
for word in wordsList:
    print(word)