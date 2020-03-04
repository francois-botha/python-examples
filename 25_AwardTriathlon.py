# This program will determines the award a person competing in a triathlon will receive.
# It will read in the times in minutes for all three events of a triathlon, namely swimming, cycling and running and then calculate and
# display the total time taken to complete the triathlon.
# The award a participant receives is based on the total time taken to complete the triathlon. The qualifying time for awards is 100 minutes
# Display the award the participant will receive based on the following criteria:
# Total time                                          Award
# Within qualifying time                              Provincial Colours
# Within 5 minutes of qualifying time                 Provincial Half Colours
# Within 10 minutes of qualifying time                Provincial Scroll
# More than 10 minutes of qualifying time             No award

# Welcome
print("Welcome to the triathlon, here you will record the times for all 3 events: Swimming, Cucling and Running")

# Time reading
swimming = input("The first event is Swimming. Please enter the time in minutes for completing Swimming\n")
cycling = input("The second event is Cycling. Please enter the time in minutes for completing Cycling\n")
running = input("The third event is Running. Please enter the time in minutes for completing Running\n")

# Validating input
if swimming.isdigit() and cycling.isdigit() and running.isdigit():

    # Calculate and display total time
    totalTime = int(swimming) + int(cycling) + int(running)
    print("Good Stuff. You completed the triathlon.\nYour total time is:",totalTime,"minutes")

    # Calculate and display award
    if totalTime <= 100:
        print("Congrats you are within the qualifying time, you are awarded: Provincial Colours")
    elif totalTime <= 105:
        print("Congrats you are 5 min within the qualifying time, you are awarded: Provincial Half Colours")
    elif totalTime <= 110:
        print("Congrats you are 10 min within the qualifying time, you are awarded: Provincial Scroll")
    else: print("You did not meet the qualifying time, better luck next time!")
    
else: print("You have to record your times in minutes, please try again.")