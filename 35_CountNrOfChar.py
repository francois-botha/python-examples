# This is a program to count the number of times a character occurs (character frequency) in a string.
# Store each letter followed by the number of occurrences in a list and print.
# ===

# Ask user for a sentence
sentence = input("Enter a sentence: ")

# Create a frequency
freq = {}

# Check for every character in the sentence if it is in the frequency, if it is then update the counter with 1 if not add the character to the frequency
for char in sentence:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Print the results
print(freq)