# About the program:
# A program that will give you the meaning of a given abbreviation.
# Create a dictionary that contains some abbreviations and their meanings.
# Let the abbreviation be the key and the meaning of the abbreviation be the value (e.g. ADSL: Asymmetric Digital Subscriber Line).
# Make sure that your dictionary has at least 4 abbreviations and their meanings. If you need ideas on some abbreviations, go to
# https://blog.hyperiondev.com/index.php/2017/11/17/8-software-development-acronyms-you-need-to-know/
# After you have created your dictionary add 2 more abbreviations and their meanings to it.
# Now ask the user to enter an abbreviation and check if that abbreviation is in your dictionary.
# If it is, print out the abbreviation and its meaning.
# If it is not in the dictionary, print out "Abbreviation not found"

# Define dictionary
dictAbbreviations = {
    'ADSL': 'Asymmetric Digital Subscriber Line',
    'API': 'Application Programming Interface',
    'IDE': 'Integrated Development Environment',
    'UI': 'User Interface',
    'OOP': 'Object-Oriented Programming',
    'SSH': 'Secure Shell'
}

# Ask user for abbreviation
abbreviation = input("Please enter an abbreviation: ").upper()

# Check if .get returns false
if not dictAbbreviations.get(abbreviation) :
    print(f"Abbreviation, {abbreviation} is not found")
else :
    print(abbreviation, "-", dictAbbreviations.get(abbreviation))