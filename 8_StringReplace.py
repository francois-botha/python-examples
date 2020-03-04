# This program will save a sentence: “The!quick!brown!fox!jumps!over!the!lazy!dog!” as single string.
# Using the replace() function to replace every “!”-exclamation mark with a blank space.
# Using the upper() function to print the sentence as: "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG".
# Finally print the sentence in reverse to the console.
# ===

# Declaring a sentance and assining the sentence value
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!"

# Reprint using the replace() function
sentence = sentence.replace("!"," ")
print(sentence)
print("\n")

# Reprint using the upper() function
sentence = sentence.upper()
print(sentence)
print("\n")

# Reprint in reverse
print(" ".join(sentence.split()[::-1]))