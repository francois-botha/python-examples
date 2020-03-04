# This program the will count the number of characters, words and lines in the file input.txt.
# Your program should also count the number of vowels (a's, e's, i's, o's and u's) in the file.
# Print out your results.
# ===

# Declare a lineList, wordsList and charList
lineCounter = 0
wordsCounter = 0
charCounter = 0

# Create a frequency
freq = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

print("\nWelcome to the program. This program will read the data that is stored in the input.txt file and will return some data on it.\n")
# Open the created file
with open("input.txt") as file_input:
    fullContent = file_input.read()
    content = file_input.readlines()
    print("The file input.txt:")
    print(fullContent)

# Open the created file
with open("input.txt") as file_input:

    # Read the contents of the file line by line
    content = file_input.readlines()

    # Count the character, words and lines in the file
    for line in content:
        lineCounter += 1
        wordsList = line.split()
        wordsCounter += len(wordsList)

        # Count the vowels in the content
        for char in line.lower():
            charCounter += 1
            if char in freq:
                freq[char] += 1

# Print results
print(f"\nThe total number of characters: {charCounter}\nThe total number of words: {wordsCounter}\nThe total number of lines: {lineCounter}\nThe total number of vowels: {freq}")