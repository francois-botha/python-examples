# Capstone Project II - Nested Loops

# A program that uses nested for loops to create a number pyramid.

print("This is a number pyramid\n")
for row in range(1,10):
    for col in range(1,row + 1):
        print(row * col, end = " ")
    print()