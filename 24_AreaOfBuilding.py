# This program will be used to calculate the area that the foundation of a building covers.
# Ask the user to enter the shape of the building (square, rectangular or round)
# Based on the user’s input, prompt for the appropriate dimensions See what dimensions you need in the list of formulae below
# Calculate and display the area that will be taken up by the foundation of the building
# Formulae for area:
# Area of square = length of the square to the power of two (length 2 )
# Area of rectangle = length x width
# Area of circle = pi X radius squared (𝛱radius 2)
# ===

import math

# Get shape of the building
print("The follwoing shapes are available for a building foundation:\n1 - Square\n2 - Rectangular\n3 - Round\nPlease enter 1, 2 or 3")
shape = input()

# Validation on input
if shape.isdigit() and (int(shape) == 1 or int(shape) == 2 or int(shape) == 3):
    print("Thank you  - we need some more information to calculate the area requested.\n")
# Calculation on square and message print
    if shape == "1":
        square = float(input("You selected the area for a square building.\nWhat is the length in meters of the square?\n"))
        square = square * square
        print("The area that the foundation of a square bulding covers is %.2f m2" % square)

# Calculation on rectangle and message print
    elif shape == "2":
        rectLength = float(input("You selected the area of a rectangular building.\nWhat is the length in meters of the rectangle?\n"))
        rectWidth = float(input("What is the width in meters of the rectangle?\n"))
        rect = rectLength * rectWidth
        print("The area that the foundation of the rectangular building covers is %.2f m2" % rect)

# Calculation on circle and message print
    else:
        
        radius = float(input("You selected the area for a radius building.\nWhat is the radius in meters of the circle?\n"))
        areaCircle = math.pi * (radius * radius)
        print("The area that the foundation of a radius bulding covers is %.2f m2" % areaCircle)
else: print("Please try again, only 1, 2 or 3 are allowed")
