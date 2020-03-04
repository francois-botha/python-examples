# This is a program that determines whether a String is a palindrome.
# A palindrome is a string which reads the same backwards as forward.
# Some examples of palindromes are: racecar, dad, level and noon.
# Ask the user to enter a word and check if that word is a palindrome. If it is a palindrome, print out 'Your word is a palindrome'. If it is not a
# palindrome, print out 'Your word is not a palindrome'.
# ===

print("Welcome to the program. This program will determine if the word that you enter is a palindrome or not.")
# Input of your word
normalWord = input("Please enter a word: ")
# Your word in reversed
reversedWord = normalWord[::-1]

# Checking to see if the reversed word are the same as the original word, and printing out the result
if normalWord == reversedWord:
    print("Your word is a palindrome")
else:
    print("Your word is not a palindrome")