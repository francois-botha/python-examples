# This program will calculate the area of a triangle.
# It will ask the user to enter the lenghts of all sides of the triangle.
# The area of the triangle is then calculated and printed to the console.
# ===

# Importing the math package to calculate the are of the triangle
import math

# Ask to enter all 3 sides of triangle
side1 = float(input("What is the length of the first side? "))
side2 = float(input("What is the length of the second side? "))
side3 = float(input("What is the lenght of the third side? "))

# Calculate area of triangle
p = float((side1 + side2 + side3) / 2)
area = math.sqrt(p*(p-side1)*(p-side2)*(p-side3))
print(f"The area of the triangle is: {area:.2f}")