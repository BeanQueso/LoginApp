'''
Eshaan Tripathi
"Login app"
11/17/22
Log into the program and run the games you like.
'''

# import csv anad sys modules
import csv
import sys

# create runfile function that runs file based on a certain parameter


def runfile(program):
    # make program name lowercase
    program = program.lower()
    # execute file
    exec(open(f'games/{program}/{program}.py').read())

# create function to give users the option to register or log in


def option():
    # print message
    print("Sign Up|Sign In")

    # ask for input
    option_q = input("")

    # sign up if the user wants to
    if option_q.upper() == "SIGN UP":
        register()
    # sign in if the user wants to
    elif option_q.upper() == "SIGN IN":
        access()
    # else, restart program
    else:
        print("\nPlease enter either 'sign up or sign in'. Restarting.")
        option()

# create get function to get all information from the database


def get():
    # open the database in db variable
    db = open("database.csv", "r")
    # create two global variables to store the users and their passwords
    global users
    global passwords
    users = []
    passwords = []
    # convert dabase information into iterable item
    db = db.readlines()
    # loop through database lines indexed 1 and on
    for i in db[1:]:
        # get users and passwords
        a, b = i.split(",")
        b = b.strip()
        # add users and passwords into their lists
        users.append(a)
        passwords.append(b)

# create function register to add account


def register():
    # get database information
    get()
    # ask for username and password
    Username = input("Create username: ")
    Password = input("Create password: ")
    Password_confirm = input("Confirm password: ")
    # if the password is not equal to the confirm input, restart function
    if Password != Password_confirm:
        print("Passwords don't match. Restarting.")
        register()
    # else...
    else:
        # restart if password is less than 6 characters
        if len(Password) < 6:
            print("Password too short. Restarting.")
            register()
        # restart if the username already exists
        elif Username in users:
            print("Username already exists. Restarting.")
            register()
        # else...
        else:
            # open the database to append
            with open("database.csv", "a+") as f:
                # create line with username and password
                user_full = [Username, Password]
                # define writer
                writer = csv.writer(f)
                # write user info into database
                writer.writerow(user_full)
            # ask if the user wants to sign in after registering
            print("Would you like to sign in now? (Y/N)")
            sign_in_question = input("")
            # if the user does...
            if sign_in_question.upper() == "Y":
                # run log in function
                access()
            else:
                # else, exit program
                sys.exit()

# define log in function


def access():
    # get information
    get()
    # ask for username and password
    Username = input("Enter your Username: ")
    Password = input("Enter your Password: ")

    # if the username isnt anything or if the user does not exist..
    if len(Username) < 1 or Username not in users:
        # inform user and ask if they want to register
        print("Does not exist, would you like to register? (Y/N): ")
        register_question = input("")
        # if the user wants to register, run register function
        if register_question.upper() == "Y":
            register()
        # else, ask if they want to try again
        else:
            print("Would you like to try again or quit? (T/Q) ")
            try_question = input("")
            # if the user wants to try again, restart function
            if try_question == "T":
                access()
            # else, exit program
            else:
                sys.exit()
    # else...
    else:
        # go through each user
        for user in users:
            # if the user is equal to a username...
            if user == Username:
                # get index of username in the users list
                ind = users.index(user)
                # get the password of the user
                password = passwords[ind]
                # if the user-given password is equal to the actual password...
                if password == Password:
                    # print welcome message
                    print(f"\nWelcome, {user}")
                    # ask if they want to play a game
                    print("Would you like to play a game? (Y/N): ")
                    play = input("")
                    # if they do want to play a game...
                    if play.upper() == "Y":
                        # ask for the name of the program or enter nothing to exit
                        program = input(
                            "Enter the name of the game you want to run (or Enter to exit): ")
                        # while the program input isnt equal to just an enter...
                        while program != '':
                            # run the game
                            runfile(program)
                            # ask for next game
                            program = input(
                                "\n\nEnter the next name of the game you want to run (or Enter to exit): ")
                    # else just leave the session
                    else:
                        print("Leaving session...")


# run option function
option()
