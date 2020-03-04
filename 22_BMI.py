# This program calculates a person's BMI.
# Ask the user to enter their weight in kg and their height in m
# Use the formula below to calculate the user's BMI:
# BMI = (weight in kg) / ((height in m)*(height in m))
# If the users BMI is 30 or greater the user is obese
# If the users BMI is 25 or greater the user is overweight
# If the users BMI is 18.5 or greater the user is normal
# If the users BMI is less than 18.5 the user is underweight
# Display the users BMI and whether they are obese, overweight, normal or underweight
# ===

# Ask the user to enter their weight in kg and their height in m
print("To calculate your BMI, we need some information about you./")
weight = input("What is your current weight in kg? ")
height = input("What is your current height in m? ")

# Validate input
if weight != "" and height != "":
    # BMI calculation
    bmi = float(weight) / (float(height) * float(height))

    # BMI Check
    if bmi >= 30:
        bmiResult = "obese"
    elif bmi >= 25:
        bmiResult = "overweight"
    elif bmi >= 18.5:
        bmiResult = "normal"
    else:
        bmiResult = "underweight"
    
    # Print message to user
    print(f"Your BMI is: {bmi:.2f}, and you are {bmiResult}")
else: print("Retry")