# About this program:
# Create your own function that prints all the days of the week.
# Create your own function that takes in a sentence and replaces every second word with the word “Hello”

# Function that prints out all the days of the week
def days_of_the_week() :
    for day in daysList :
        print(day)

def wordReplacing() :
    mySentence = input("\nWhat is your sentence? ")
    # Split sentence into a list of words
    sentenceList = mySentence.split()
    for word in range(len(sentenceList)) :
        # Replace every 2nd word with Hello
        if word%2 != 0 :
            sentenceList[word] = "Hello"
    # Print back to a string
    mySentence = " ".join(sentenceList)
    print(mySentence)

# Declare list with days of the week
daysList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("Days of the week:")
print("=================")
# Calling function to print ou the days of the week
days_of_the_week()

# Calling function to replace every second word
wordReplacing()