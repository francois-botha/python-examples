# Capstone Project III - Files

# About the program:
# A program for a small business that can help it to manage tasks assigned to each member of the team.
# Fist a user must login and the correct credentials needs to be entered in order to continue
# Once logged in, a menu will display options for the user to select.
# Only admin are allowed to register new users as well as a new menu item will be displayed for stats

# 1-Steps:
# Ask for username and password when program runs
# Open the user.txt file and read the information into a variable
# Split each line into 2 parts, first part before ", " is the username and the second part after is the password
# Compare the provided username and password with each line in the list
# When the correct info is captured break and continue to the main menu
# When valid username is provided with wrong password, a message will display
# When both values are wrong a message wil dispplay

# 2-Steps:
# Display easy to read menu
# Display an extra menu option when admin is logged in

# 3-Steps:
# r - to register an new user
# Check that the user admin is logged in, else display a message that you have to be admin to register a new user
# Ask for a new username and lower case the input to ensure that only unique usernames are created
# Check if the username entered are in the user.txt file
# If it does exist then the user need to enter a new username that does'nt exist
# Once a unique username is captured the user is asked to enter a password
# The user is asked to confirm the password, when entered incorrectly a message will be displayed to retype the password
# Once the password is confirmed the username and password will write to the user.txt file

# a - to add a task
# Ask the user for the username of the new task
# Validate that the username exist in the user.txt file
# Once validated ask the user for the title of the task as well as the description and due date
# The task will have the current date as the assigned date and by default the completion status will ne set to no
# Once all of the data is captured the task is write to the task.txt file

# va - to view all tasks
# Display all tasks in easy to read way

# vm - to view tasks to the current logged in user
# Displays task for the current user

# s - display stats only when admin is logged in
# Display stats to how many users are in the file as well as the number of tasks in the file

import os
import sys
import datetime

clear = lambda: os.system('cls')

clear()
print("\nWelcome to the program.")
print("=======================\n")

try:
    # Reading data from file to variable
    userFile = open('user.txt', 'r')
    userList = userFile.read().splitlines()
    userFile.close()

    taskFile = open('tasks.txt', 'r')
    taskList = taskFile.read().splitlines()
    taskFile.close()

    # Program needs login data to continue to the main menu
    validLogin = False
    while validLogin == False :
        print("\nLogin: ")
        print("======")

        # Username input is lowered to ensure that username are unique
        loginUsername = input("Username: ").lower()
        loginPassword = input("Password: ")

        # Run every line in userList to compare username and password with the values entered
        for line in userList :
            # Split line into username and password
            usernameAndPassword = line.split(", ")

            # Check loginUsername equal to username and password value entered
            if loginUsername == usernameAndPassword[0] and loginPassword == usernameAndPassword[1] :
                validLogin = True
                break
            
            # If username is equal to login username and wrong password
            elif loginUsername == usernameAndPassword[0] and loginPassword != usernameAndPassword[1] :
                validLogin = "Partial"
                break

        if validLogin == "Partial" :
            print("\nYour password does not match the username.\nHit <enter> to try again")
            input()
            validLogin = False
            clear()
        elif validLogin == False:
            print("\nYou have entered the wrong information.\nHit <enter> to try again")
            input()
            clear()

    else:
        clear()
        print("\nYour login is confirmed!\n")

    # Program menu
    while validLogin:
        print(f"You are logged in as {loginUsername.upper()}. Welcome to the program!")
        print("Please select one on the following options:")
        print("-------------------------------------------")
        print("r  - register user")
        print("a  - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        # Menu option only visable when admin is logged in
        if loginUsername == "admin" :
            print("\nAdmin Options:")
            print("--------------")
            print("s  - Statistics")
        print("\ne  - exit")
        menuSelect = input().lower()

        # To register a new user
        if menuSelect == "r" :
            # Admin needs to be login to access this part of the program
            if loginUsername == "admin" :
                duplicateUser = True
                while duplicateUser == True :
                    clear()
                    print("Register a new user")
                    print("-------------------")
                    print("Please provide the following information to register a new user.")
                    # Username input is converted to lower case to ensure no duplicates can be created
                    newUsername = input("Username: ").lower()
                    usernameCheck = False
                    # While the usernameCheck is not True i.e new username is not all checked against the usernames in the list
                    while not usernameCheck : 
                        for line in userList :
                            usernameAndPassword = line.split(", ")
                            if newUsername == usernameAndPassword[0] :
                                duplicateUser = True
                                break
                            else:
                                duplicateUser = False
                        if duplicateUser:
                            print(f"The username \"{newUsername}\" is already in use...")
                            newUsername = input("Please enter a unique username: ").lower()
                        else:
                            duplicateUser == False
                            usernameCheck = True
                    
                    # A unique username is entered and can continue asking for the password
                    newPassword = input("Password: ")

                    # To confirm the password
                    passwordCheck = False
                    while not passwordCheck : 
                        confirmNewPassword = input("Please confirm your password: ")
                            
                        if newPassword == confirmNewPassword :
                            paswwordCheck = True
                            break

                        else:
                            clear()
                            print("\nThe password does not match, please try again.")

                    # After the newUsername is checked and password is confirmed it will write data to a file
                    print("Writing data to file...")            
                    userFile = open('user.txt', 'a+')
                    userFile.write("\n" + newUsername + ", " + newPassword)
                    userFile.close()

                    # The list that contains the data of all the users are updated as well to be used later in the program
                    userList.append(newUsername + ", " + newPassword)
                    print(f"\nUser, {newUsername.upper()} accepted and added to the users list.\n")

                    print("Hit <enter> to return to the main screen.")
                    input()
                    clear()
            # When you are not logged in as admin, a message will be displayed
            else:
                clear()
                print(":-( Sorry but...")
                print("You need to be logged in as admin to register a new user. Please logout and login as admin.")
                print("Hit <enter> to return to the main screen.")
                input()
                clear()
        # To add a new task
        elif menuSelect == "a" :
            clear()
            print("Add a new task")
            print("--------------")
            print("Please provide the following information to add a new task.")

            # Checking if username assigned are in the user.txt file
            usernameCheck = False
            while not usernameCheck :
                assignedUser = input("Username for the task? ").lower()
                for line in userList :
                    usernameAndPassword = line.split(", ")
                    if assignedUser == usernameAndPassword[0] :
                        usernameCheck = True
                        break
                    else:
                        usernameCheck = False
                if usernameCheck == False :
                    print(f"The username, {assignedUser}, does not exist in the database. Please select another user.")
            # Task details required
            taskTitle = input("Title for the task? ")
            taskDescription = input("Description of the task? ")
            taskDueDate = input("Due date of the task? (yyyy-mm-dd) ")
            taskSignOnDate = datetime.datetime.now().strftime('%Y-%m-%d')
            taskCompleted = "no"
            clear()

            # Task data to write to file
            print("Writing data to file...\n")
            taskFile = open('tasks.txt','a+')
            taskFile.write(f"\n{assignedUser} : {taskTitle} : {taskDescription} : {taskDueDate} : {taskSignOnDate} : {taskCompleted}")
            taskFile.close()

            # Task is added to the task list for user later in the program
            taskList.append(f"{assignedUser} : {taskTitle} : {taskDescription} : {taskDueDate} : {taskSignOnDate} : {taskCompleted}")
            print("Hit <enter> to return to the main screen.")
            input()
            clear()
        # To view all tasks
        elif menuSelect == "va" :
            clear()
            print("This is a list of all tasks in the database.")
            print("--------------------------------------------")
            print("Username" + 5*" " + "Title" + 15*" " + "Description" + 50*" " + "Due Date" + 5*" " + "Assigned Date" + 5*" " + "Completed")
            print("-"*134)
            # To display the data in a easy to read way
            for task in taskList :
                taskItems = task.split(":")
                print(taskItems[0] + (12-len(taskItems[0]))*" " + 
                taskItems[1] + (20-len(taskItems[1]))*" " + 
                taskItems[2] + (61-len(taskItems[2]))*" " +
                taskItems[3] + (13-len(taskItems[3]))*" " +
                taskItems[4] + (18-len(taskItems[4]))*" " +
                taskItems[5])
            print("Hit <enter> to return to the main screen.")
            input()
        # Tasks is filtered by the user that is currently logged in
        elif menuSelect == "vm" :
            clear()
            print("This is a list of all tasks assigned to you in the database.")
            print("------------------------------------------------------------")
            print("Task" + 5*" " + "Title" + 15*" " + "Description" + 50*" " + "Due Date" + 5*" " + "Assigned Date" + 5*" " + "Completed")
            print("-"*134)
            count = 0
            for task in taskList :
                taskItems = task.split(":")
                if loginUsername.strip() == taskItems[0].strip() :
                    print(str(count+1) + (8-len(str(count+1)))*" " + 
                    taskItems[1] + (20-len(taskItems[1]))*" " + 
                    taskItems[2] + (61-len(taskItems[2]))*" " +
                    taskItems[3] + (13-len(taskItems[3]))*" " +
                    taskItems[4] + (18-len(taskItems[4]))*" " +
                    taskItems[5])
                    # This counter provides feedback if there is no tasks filtered for the username
                    count += 1
                
            if count == 0:
                print("You don\'t have any tasks listed.")
                
            print("Hit <enter> to return to the main screen.")
            input()
            clear()
        # To view stats only when the admin is logged in
        elif menuSelect == "s" and loginUsername == "admin":
            clear()
            print("Statistics:")
            print("-----------")
            taskCount = 0
            userCount = 0
            for task in taskList :
                taskCount += 1
            for user in userList :
                userCount += 1
            print(f"The total number of tasks listed is: {taskCount} tasks")
            print(f"The total number of users registered is: {userCount} users")
            print("\nHit <enter> to return to the main screen.")
            input()
            clear()
        # To exit the menu
        elif menuSelect == "e":
            clear()
            print("Program Terminiated!")
            os._exit(1)

    else:
        print("Terminated")

except FileNotFoundError :
    print("File not found!")

except IOError as err :
    print(err)

except KeyboardInterrupt as err :
    print(err)

except AttributeError as err:
    print(err)

except NameError as err :
    print(err)

except :
    print("Something else.")
    print(sys.exc_info()[0])

finally :
    if not userFile.closed :
        userFile.close()
        taskFile.close()