'''
Program Name: battleship_game_no_self_import

Description: This file/module contains all the work done from login to ship
placement in a long chain, so as to avoid any problems involved in importing
functions from other python files.

This is really long, so be prepared.
'''

#import tkinter as tk # imports all names from tkinter as tk
from tkinter import * # to import all names from tkinter

# Note: It is assumed that both importing methods are used in the code.

from tkinter import messagebox # for pop-up messages as part of the verification

# AddNote: messagebox function doesn't seem to work without this line

import os # importing support for different operating systems
from random import randint # importing random module to generate random number
import random
from PIL import Image, ImageTk

'''
Program code starts here
'''

#Making first main window:
def main_account_screen():
    """
    ==========================
    Author: BRYAN LIM
    Initialise Main Menu
    ==========================
    """
    global window
    window = tk.Tk()
    window.title("Main Screen Battleship GUI")

    #making non-resizable window
    window.resizable(False, False)
    window.geometry("300x100")

    #main page button functions
    bt1 = Button(window, text="Login", command = login).pack()
    Label(text="").pack()
    bt2 = Button(window, text="Sign Up", command = signup).pack()
    Label(text="").pack()

    window.mainloop()

# designing new screen for log in
def login():
    """
    ===========================================
    Author: BRYAN LIM
    Initialise Log in button and command button
    ===========================================
    """
    global login_screen
    
    login_screen = Toplevel(window)
    login_screen.title("Login")

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen, textvariable= username_verify).pack()
    Label(login_screen, text="Password").pack()
    password_login_entry = Entry(login_screen, textvariable= password_verify, show = "*").pack()

    Label(login_screen, text = "").pack()
    Label(login_screen, text="Username and Password are case sensitive", font=("Calibri", 8)).pack()
    Label(login_screen, text = "").pack()

    global Button1
    
    Button1 = Button(login_screen, text="Login", width=10, height=1, command=login_verify)
    Button1.pack()

#login verification:

#counter for max 3 tries coding

counter = 0

def login_verify():
    """
    ==============================
    Author: BRYAN LIM
    Login credentials verification
    ==============================
    """
    global counter

    #case where 3 tries has been reached, to interrupt the rest of the function
    if counter == 3:
        Button1.configure(state=DISABLED) #disables the login button from use
        reactivate_account()
        return
    
    #Retrieving from file
    username_info = username_verify.get()
    password_info = password_verify.get()

    #listdir() returns a list containing the entries given
    #r means read mode
    list_of_files = os.listdir()

    if username_info in list_of_files:
        file1 = open(username_info, "r")
        verify = file1.read().splitlines()
        if password_info in verify:
            login_success()

        else:
            password_not_recognised()
                
    else:
        user_not_found()



def login_success():
    """
    ================================
    Author: BRYAN LIM
    Designing popup for login success
    =================================
    """
    global login_success_screen
    counter = 0 # reset the number of tries given to the user due to success
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command = basegame).pack()


def password_not_recognised():
    """
    ==========================================
    Author: BRYAN LIM
    Designing popup for login invalid password
    ==========================================
    """
    global password_not_recog_screen
    global counter
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Invalid")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password").pack()
    Label(password_not_recog_screen, text="Please Try Again").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
    counter += 1

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Handle exception if file not found -> open new file [means make new account]
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
    signup()

# designing new screen for reactivating account

def reactivate_account():
    global reactivate_screen
    reactivate_screen = Toplevel(login_screen)

    global dob_activation
    dob_activation = StringVar()
    
    reactivate_screen.title("Account Locked")
    reactivate_screen.geometry("480x360")
    Label(reactivate_screen, text="Security Question: Date of Birth").pack()
    dob_activation_entry = Entry(reactivate_screen, textvariable= dob_activation).pack()
    Button(reactivate_screen, text="Reactivate Account", command = dob_verify).pack()

def dob_verify():
    global dob_activation
    global Button1
    global counter
    
    dob_verify = dob_activation.get()
    username_info = username_verify.get()

    file1 = open(username_info, "r")
    verify = file1.read().splitlines()
    if dob_verify in verify:
        messagebox.showinfo("Success", "Account has been reactivated, your password is {}".format(verify[1]))
        Button1.configure(state=NORMAL) # reactivate the login button
        counter = 0 # reset the number of tries given to the user
        delete_reactivation()
    else:
        messagebox.showinfo("Invalid", "Date of Birth is incorrect, please try again")

def delete_reactivation():
    reactivate_screen.destroy()

# designing new screen for sign ups
def signup():
    """
    ==========================================
    Author: 
        BRYAN LIM 
        ODELIA
    Designing popup for login invalid password
    ==========================================
    """
    global signup_screen
    signup_screen = Toplevel(window)
    signup_screen.title("Sign Up")

    global username_signup
    global password_signup
    global dob_signup

    username_signup = StringVar()
    password_signup = StringVar()
    dob_signup = StringVar()

    global username_signup_entry
    global password_signup_entry
    global dob_signup_entry

    Label(signup_screen, text="New Username").pack()
    username_signup_entry = Entry(signup_screen, textvariable= username_signup).pack()
    Label(signup_screen, text="New Password").pack()
    password_signup_entry = Entry(signup_screen, textvariable= password_signup, show = "*").pack()
    Label(signup_screen, text="Date of Birth (DDMMYYYY)").pack()
    dob_signup_entry = Entry(signup_screen, textvariable= dob_signup, show = "*").pack()

    Label(signup_screen, text = "").pack()
    Label(signup_screen, text = "Password must contain more than 8 characters", font = ("Calibri", 8)).pack()
    Label(signup_screen, text = "Password must contain at least 1 capital case letter", font = ("Calibri", 8)).pack()
    Label(signup_screen, text = "Password must contain at least 1 lower case letter", font = ("Calibri", 8)).pack()
    Label(signup_screen, text = "Password must contain at least 1 digit from 0 to 9", font = ("Calibri", 8)).pack()
    Label(signup_screen, text = "Password must contain at least 1 special case", font = ("Calibri", 8)).pack()
    Label(signup_screen, text = "Password must not contain username", font = ("Calibri", 8)).pack()
    Label(signup_screen, text = "").pack()
    Button(signup_screen, text = "Register", width=10, height=1, command=signup_user).pack()

#storing new data of username and password during sign up
def signup_user():
    
    """
    ==========================================
    Author: 
        BRYAN LIM 
        ODELIA
    Designing popup for login invalid password
    ==========================================
    """
    username_info = username_signup.get()
    password_info = password_signup.get()
    dob_info = dob_signup.get()

    list_of_files = os.listdir()

    #new lines of code added to account for incomplete entries

    if username_info == '' or password_info == '' or dob_info == '':
        messagebox.showinfo("Invalid", "Please fill in all fields")
        return

    #new lines of code added to check the validity of the username

    if username_info in list_of_files:
        messagebox.showinfo("Invalid", "Username has already been chosen")
        return

    #new lines of code added to check the validity of the date of birth

    if dob_info.isnumeric() == False:
        messagebox.showinfo("Invalid", "Invalid Date of Birth")
        return

    if len(dob_info) < 8:
        messagebox.showinfo("Invalid", "Please enter the Date of Birth in DDMMYYYY format")
        return

    if int(dob_info[2:4]) > 12 or int(dob_info[2:4]) < 0:
        messagebox.showinfo("Invalid", "Please enter the Date of Birth in DDMMYYYY format")
        return

    if int(dob_info[2:4]) in [4,6,9,11]:
        if int(dob_info[0:2]) > 30:
            messagebox.showinfo("Invalid", "Please enter the Date of Birth in DDMMYYYY format")
            return
        
    elif int(dob_info[2:4]) == 2:
        if int(dob_info[4:8]) % 4 != 0:
            if int(dob_info[0:2]) > 28:
                messagebox.showinfo("Invalid", "Please enter the Date of Birth in DDMMYYYY format")
                return
            
        elif int(dob_info[0:2]) > 29:
            messagebox.showinfo("Invalid", "Please enter the Date of Birth in DDMMYYYY format")
            return
        
    elif int(dob_info[0:2]) > 31:
        messagebox.showinfo("Invalid", "Please enter the Date of Birth in DDMMYYYY format")
        return

    #new lines of code added to check the validity of the password

    if len(password_info) < 8:
        messagebox.showinfo("Invalid", "Password is too short")
    elif not re.search("[a-z]", password_info):
        messagebox.showinfo("Invalid", "Password has no lower case letters")
    elif not re.search("[A-Z]", password_info):
        messagebox.showinfo("Invalid", "Password has no upper case letters")
    elif not re.search("[0-9]", password_info):
        messagebox.showinfo("Invalid", "Password has no numbers")
    elif not re.search("[!#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", password_info):
        messagebox.showinfo("Invalid", "Password has no special characters")
    elif username_info.lower() in password_info.lower():
        messagebox.showinfo("Invalid", "Password should not contain your username.")

    # Note: Python reads line by line so putting this at the end works
    else:
        # open file in write mode & write info into the file
        # w means write mode
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info + "\n")
        file.write(dob_info)
        file.close()

        Label(signup_screen, text="Registration Success").pack()

# Dictionary used to store the coordinates of the player's ships
Player = {}
# making the screen to choose to start a new game or continue an existing game
# imported from login/signup GUI
def basegame():
    global game_screen
    
    login_success_screen.destroy()
    login_screen.destroy()
    
    game_screen = Tk()
    game_screen.title("Battleship Game")
    game_screen.geometry("360x240")
    game_screen.resizable(False, False)
    Button(game_screen, text="Press here to start a new game.", command=player_boards).place(relx=0.5, rely=0.3, anchor=CENTER)
    Button(game_screen, text="Press here to load an existing game.").place(relx=0.5, rely=0.5, anchor=CENTER)
    game_screen.mainloop()
    
# making the boards used in the game        
def player_boards():
    global surface_screen
    global direction
    global shiptype

    # Setting properties of the grid window
    surface_screen = Tk()
    surface_screen.title("Battleship Game")
    surface_screen.geometry("1080x640")
    surface_screen.resizable(False, False)

    # showing that the carrier is going to be placed first
    Label(surface_screen, text='Placing Carrier', font='Calibri 12 bold', foreground='red').grid(row=0, column=25)

    # Setting the Radiobutton selection of direction for the ship (carrier/submarine)
    direction = IntVar(surface_screen, 1)
    Radiobutton(surface_screen, text='Ship stretches upwards', variable=direction, value=1).grid(row=1, column=25)
    Radiobutton(surface_screen, text='Ship stretches downwards', variable=direction, value=2).grid(row=2, column=25)
    Radiobutton(surface_screen, text='Ship stretches leftwards', variable=direction, value=3).grid(row=3, column=25)
    Radiobutton(surface_screen, text='Ship stretches rightwards', variable=direction, value=4).grid(row=4, column=25)

    # AddNote: "stretches" means that the ship will extend up/down/left/right from the chosen grid spot

    # Setting the labels for the underwater and surface boards
    Label(surface_screen, text="Underwater", height = 3, width = 40).grid(row=0, column=0, columnspan=10)
    Label(surface_screen, text="Surface", height = 3, width = 40).grid(row=0, column=12, columnspan=10)

    # Preparing a spacing between the two grids
    Label(surface_screen, text="", height = 20, width = 4).grid(row=1, column=10, rowspan=10)
    
    carrier_placing_button()


# Function used to place the grid of buttons for carrier flagship
def carrier_placing_button():
    for i in range(1, 11):
        for j in range(10):
            invalid_btn = Button(surface_screen, height = 2, width = 4, command=invalid_placement)
            invalid_btn.grid(row=i, column=j)

    # AddNote: Remember that carriers cannot be placed underwater

    for i in range(1, 11):
        for j in range(11, 21):
            valid_btn = Button(surface_screen, height = 2, width = 4, command=callback_carrier(i,j))
            valid_btn.grid(row=i, column=j) 

# Message box to tell players to not place carriers underwater
def invalid_placement():
    messagebox.showinfo("Invalid", "Carriers cannot be placed underwater.")

# "Link function" to allow tkinter buttons to have commands that need parameters
def callback_carrier(i, j):
    return lambda: carrier_button(i,j)

# Function determining the position of the carrier based on chosen radiobutton
def carrier_button(row, column):
    global carrier_btn
    global Player

    # If chosen direction is up
    if direction.get() == 1:
        if row >= 4:               
            close_button()

            # List created to store the tuples representing the coordinates
            Coordinates = []
            
            for x in range(row - 3, row + 1):
                carrier_btn = Button(surface_screen, bg='red', height = 2, width = 4)
                carrier_btn.grid(row=x, column=column)

                # AddNote: There are two pairs of brackets, one for the append function, one to make the data a tuple
                Coordinates.append((x,column,1))
                Player["Carrier"] = Coordinates

                # state = "disabled" stops the button from doing anything. This is to prevent players from pressing the grid instead of the pop-up box that appears.
                carrier_btn.config(state="disabled")
            carrier_alert_message()
        else:
            messagebox.showinfo("Invalid", "Invalid ship placement")

# The comments above apply to the bottom as well
# The four cases differ in the numbers and input parameters used (row vs column)

    # If chosen direction is down
    if direction.get() == 2:
        if row <= 7:
            close_button()
            Coordinates = []
            for x in range(row, row + 4):
                carrier_btn = Button(surface_screen, bg='red', height = 2, width=4)
                carrier_btn.grid(row=x, column=column)
                Coordinates.append((x,column,1))
                Player["Carrier"] = Coordinates
                carrier_btn.config(state="disabled")
            carrier_alert_message()
        else:
            messagebox.showinfo("Invalid", "Invalid ship placement")

    # If chosen direction is left
    if direction.get() == 3:
        if column >= 14:
            close_button()
            Coordinates = []
            for x in range(column - 3, column + 1):
                carrier_btn = Button(surface_screen, bg='red', height = 2, width=4)
                carrier_btn.grid(row=row, column=x)
                Coordinates.append((row,x,1))
                Player["Carrier"] = Coordinates
                carrier_btn.config(state="disabled")
            carrier_alert_message()
        else:
            messagebox.showinfo("Invalid", "Invalid ship placement")

    # If chosen direction is right
    if direction.get() == 4:
        if column <= 17:
            close_button()
            Coordinates = []
            for x in range(column, column + 4):
                carrier_btn = Button(surface_screen, bg='red', height = 2, width=4)
                carrier_btn.grid(row=row, column=x)
                Coordinates.append((row,x,1))
                Player["Carrier"] = Coordinates
                carrier_btn.config(state="disabled")
            carrier_alert_message()
        else:
            messagebox.showinfo("Invalid", "Invalid ship placement")

# subfunction to disable all buttons once a ship position is chosen
def close_button():
    for i in range(1, 11):
        for j in range(10):
            btn = Button(surface_screen, height = 2, width = 4)
            btn.grid(row=i, column=j)
            btn.config(state="disabled")

    # Separate loops to facilitate a column space between surface and underwater grids
    for i in range(1, 11):
        for j in range(11, 21):
            btn = Button(surface_screen, height = 2, width = 4)
            btn.grid(row=i, column=j)
            btn.config(state="disabled")

# message box to confirm selection of carrier spot
def carrier_alert_message():    
    CarrierMsg = messagebox.askquestion('Confirmation','Do you want to place your carrier flagship here?')

    if CarrierMsg == 'yes':
        carrier_row_extractor()
        carrier_column_extractor()
        submarine_placing_button()

        # This order of function calls is VERY IMPORTANT
        # The row and column extractors must be called before the submarine placing button is called
        
    else:
        Player["Carrier"] = "" # Restoring dictionary to empty value due to rejected spot
        carrier_placing_button()

# function to obtain the rows of the carrier to make sure the button color is not erased while placing the grid for submarines
def carrier_row_extractor():
    global Player
    global Carrier_Row
    
    Carrier_Row = []
    for x in range(4):
        Carrier_Row.append(Player['Carrier'][x][0])

# function to obtain the columns of the carrier to make sure the button color is not erased while placing the grid for submarines
def carrier_column_extractor():
    global Player
    global Carrier_Column
    
    Carrier_Column = []
    for x in range(4):
        Carrier_Column.append(Player['Carrier'][x][1])

# Function used to place the functions grid for submarines
def submarine_placing_button():
    global Carrier_Row
    global Carrier_Column

    # showing which ship type is being placed next
    Label(surface_screen, text='Placing Submarine', font='Calibri 12 bold', foreground='blue').grid(row=0, column=25)

    for i in range(1, 11):
        for j in range(10):
            btn = Button(surface_screen, height = 2, width = 4, command=callback_submarine(i,j))
            btn.grid(row=i, column=j)

    # Separate loops to facilitate a column space between surface and underwater grids
    for i in range(1, 11):
        for j in range(11, 21):

            # Preventing chosen buttons from being restored to "default" settings and retain their red coloring
            
            if not i in Carrier_Row or not j in Carrier_Column:
                btn = Button(surface_screen, height = 2, width = 4, command=callback_submarine(i,j))
                btn.grid(row=i, column=j)

# "Link function" to allow tkinter buttons to have commands that need parameters
def callback_submarine(i,j):
    return lambda: submarine_button(i,j)

'''
This function works the same as carrier_button, with a few changes:
1) If underwater board is chosen, coordinates will be stored in (x,y,0) format.
2) close_button2() omits the carrier flagship's position so as not to wipe the red coloring.
3) Submarines are blue instead of red and they have a length of 3.
4) Added checks are done to ensure that submarines don't overlap with carriers.
'''

# Function determining the position of the submarine based on chosen radiobutton
def submarine_button(row, column):
    global submarine_btn
    global Player
    global Carrier_Row
    global Carrier_Column

    # If chosen direction is up
    if direction.get() == 1:
        if row >= 3 and column <= 9:               
            close_button2()
            Coordinates = []
            for x in range(row - 2, row + 1):
                submarine_btn = Button(surface_screen, bg='blue', height = 2, width = 4)
                submarine_btn.grid(row=x, column=column)
                Coordinates.append((x,column,0))
                Player["Submarine"] = Coordinates
                submarine_btn.config(state="disabled")
            submarine_alert_message()
        elif row >= 3 and column > 9:

            for x in range(row - 2, row + 1):
                if x in Carrier_Row and column in Carrier_Column:
                    messagebox.showinfo("Invalid", "Invalid ship placement")
                    return

            close_button2()
            Coordinates = []
            for x in range(row - 2, row + 1):
                submarine_btn = Button(surface_screen, bg='blue', height = 2, width = 4)
                submarine_btn.grid(row=x, column=column)
                Coordinates.append((x,column,1))
                Player["Submarine"] = Coordinates
                submarine_btn.config(state="disabled")
            submarine_alert_message()
        else:
            messagebox.showinfo("Invalid", "Invalid ship placement")

    # If chosen direction is down
    if direction.get() == 2:
        if row <= 8 and column <= 9:
            close_button2()
            Coordinates = []
            for x in range(row, row + 3):
                submarine_btn = Button(surface_screen, bg='blue', height = 2, width=4)
                submarine_btn.grid(row=x, column=column)
                Coordinates.append((x,column,0))
                Player["Submarine"] = Coordinates
                submarine_btn.config(state="disabled")
            submarine_alert_message()
        if row <= 8 and column > 9:

            for x in range(row, row + 3):
                if x in Carrier_Row and column in Carrier_Column:
                    messagebox.showinfo("Invalid", "Invalid ship placement")
                    return

            close_button2()
            Coordinates = []
            for x in range(row, row + 3):
                submarine_btn = Button(surface_screen, bg='blue', height = 2, width=4)
                submarine_btn.grid(row=x, column=column)
                Coordinates.append((x,column,1))
                Player["Submarine"] = Coordinates
                submarine_btn.config(state="disabled")
            submarine_alert_message()
        else:
            messagebox.showinfo("Invalid", "Invalid ship placement")

    # If chosen direction is left
    if direction.get() == 3:
        if column > 9 and column >= 13:

            for x in range(column - 2, column + 1):
                if row in Carrier_Row and x in Carrier_Column:
                    messagebox.showinfo("Invalid", "Invalid ship placement")
                    return

            close_button2()
            Coordinates = []
            for x in range(column - 2, column + 1):
                submarine_btn = Button(surface_screen, bg='blue', height = 2, width=4)
                submarine_btn.grid(row=row, column=x)
                Coordinates.append((row,x,1))
                Player["Submarine"] = Coordinates
                submarine_btn.config(state="disabled")
            submarine_alert_message()
        elif column <= 9 and column >= 2:
            close_button2()
            Coordinates = []
            for x in range(column - 2, column + 1):
                submarine_btn = Button(surface_screen, bg='blue', height = 2, width=4)
                submarine_btn.grid(row=row, column=x)
                Coordinates.append((row,x,0))
                Player["Submarine"] = Coordinates
                submarine_btn.config(state="disabled")
            submarine_alert_message()
        else:
            messagebox.showinfo("Invalid", "Invalid ship placement")

    # If chosen direction is right
    if direction.get() == 4:
        if column > 9 and column <= 18:

            for x in range(column, column + 3):
                if row in Carrier_Row and x in Carrier_Column:
                    messagebox.showinfo("Invalid", "Invalid ship placement")
                    return

            close_button2()
            Coordinates = []
            for x in range(column, column + 3):
                submarine_btn = Button(surface_screen, bg='blue', height = 2, width=4)
                submarine_btn.grid(row=row, column=x)
                Coordinates.append((row,x,1))
                Player["Submarine"] = Coordinates
                submarine_btn.config(state="disabled")
            submarine_alert_message()
        elif column <= 9 and column <= 7:
            close_button2()
            Coordinates = []
            for x in range(column, column + 3):
                submarine_btn = Button(surface_screen, bg='blue', height = 2, width=4)
                submarine_btn.grid(row=row, column=x)
                Coordinates.append((row,x,0))
                Player["Submarine"] = Coordinates
                submarine_btn.config(state="disabled")
            submarine_alert_message()
        else:
            messagebox.showinfo("Invalid", "Invalid ship placement")

# subfunction to close all button functions once a ship position is chosen accomodating for carrier button color
def close_button2():
    for i in range(1, 11):
        for j in range(10):
            btn = Button(surface_screen, height = 2, width = 4, command=callback_submarine(i,j))
            btn.grid(row=i, column=j)
            btn.config(state="disabled")

    # Separate loops to facilitate a column space between surface and underwater grids
    for i in range(1, 11):
        for j in range(11, 21):
            if not i in Carrier_Row or not j in Carrier_Column:
                btn = Button(surface_screen, height = 2, width = 4, command=callback_submarine(i,j))
                btn.grid(row=i, column=j)
                btn.config(state="disabled")

# message box to confirm selection of submarine spot
                
def submarine_alert_message():    
    SubmarineMsg = messagebox.askquestion('Confirmation','Do you want to place your submarine here?')

    if SubmarineMsg == 'yes':
        redraw_boards()
    else:
        Player["Submarine"] = "" # Restoring dictionary to empty value due to rejected spot
        submarine_placing_button()


"""
====================================================================
Author:
    
James Morillo 
Odelia

Initilise AI Carriers and it's Submarine in random horizontal line.
This is stored following the Dictionary below.
====================================================================
"""

AI_player_submarine_randomizer_row = random.randint(13,20)
AI_player_submarine_randomizer_column = random.randint(1,8)


AI_player_surface_randomizer_row = random.randint(12,21)
AI_player_surface_randomizer_column = random.randint(11,17)

AI_player = {'Carrier':[(AI_player_surface_randomizer_row,AI_player_surface_randomizer_column,1), 
                        (AI_player_surface_randomizer_row,AI_player_surface_randomizer_column+1,1), 
                        (AI_player_surface_randomizer_row,AI_player_surface_randomizer_column+2,1), 
                        (AI_player_surface_randomizer_row,AI_player_surface_randomizer_column+3,1)],
                        'Submarine': [(AI_player_submarine_randomizer_row,AI_player_submarine_randomizer_column-1,0), 
                                      (AI_player_submarine_randomizer_row,AI_player_submarine_randomizer_column,0), 
                                      (AI_player_submarine_randomizer_row,AI_player_submarine_randomizer_column+1,0)]}

"""
====================================================================
Author: James Morillo
Initilise AI Carriers and Player global counter for win/lose 
condition. First one to get 7 points win.
====================================================================
"""

AI_counter = 0
Player_counter = 0 

button_height = 2
button_width = 4

def redraw_boards():
    
    """
    =========================================================================
    Author: James Morillo
    Initilise New Board for actual game.
    
    Then initialise elements such as the root window, AI player frame, Player 
    Frame into a grid for convenient grid management.
    =========================================================================
    """

    global redraw_gameboard
    global Player
    global AI_player
    global AI_underwater_cell
    global player_underwater_cell
    global AI_frame
    global Player_frame
    global root
    global surface_screen
    
    
    #Destroy irrelevant windows that do not affect the gameplay
    surface_screen.destroy()
    game_screen.destroy()
    
    #initialise tuples for creating the board contents
    Player["Player Surface"] = {}
    Player["Player Underwater"] = {}
    AI_player["AI Surface"] = {}
    AI_player["AI Underwater"] = {}
    
    root = Tk()
    root.grid()
    
    Player_frame = LabelFrame(root, text = "Player Boards")
    Player_frame.grid()
    
    AI_frame = LabelFrame(root, text = "AI Boards")
    AI_frame.grid()
    
    #grid and frame system for root, AI_player_frame, Player_frame for convenient grid system
    
    root.title("Battleship Game")
    root.geometry("850x950")
    root.resizable(False, False)
    
    #individual boards labels for UI convenience
    Label(Player_frame, text="Player Underwater", height = 3, width = 15).grid(row=0, column=0, columnspan=10)
    Label(Player_frame, text="Player Surface", height = 3, width = 15).grid(row=0, column=12, columnspan=10)
    Label(AI_frame, text="AI Underwater", height = 3, width = 15).grid(row=11, column=0, columnspan=10)
    Label(AI_frame, text="AI Surface", height = 3, width = 15).grid(row=11, column=11, columnspan=10)
    
    # Preparing spacings between the grids to have a neater UI.
    Label(Player_frame, text="", height = 20, width = 4).grid(row=1, column=10, rowspan=10)
    Label(AI_frame, text="", height = 20, width = 4).grid(row=11, column=10, rowspan=10)
    

    """
    
    ====================================================================
    Initialising 4 Board of Buttons for actual.
    Store values AI_player["AI Underwater"][i][j]["Presence"] = None 
    so that when it is hit, this dictionary changes from None to "HIT"
    ====================================================================
    
    """
    
    for i in range(12, 22):
        AI_player["AI Underwater"][i] = {}
        for j in range(10):
            AI_player["AI Underwater"][i][j] = {}
            AI_player["AI Underwater"][i][j]["Presence"] = None
            AI_player["AI Underwater"][i][j]["REF"] = None
            AI_underwater_cell = Button(AI_frame, 
                                        height = button_height, 
                                        width = button_width,
                                        highlightbackground="#000080",
                                        command=lambda row=i, column=j, depth = 0: shoot(row, column, depth))
            AI_underwater_cell.grid(row=i, column=j)
            
            
    for i in range(1, 11):
        Player["Player Underwater"][i] = {}
        for j in range(10):
            Player["Player Underwater"][i][j] = {}
            Player["Player Underwater"][i][j]["Presence"] = None
            Player["Player Underwater"][i][j]["REF"] = None
            player_underwater_cell = Button(Player_frame, 
                                            height = button_height, 
                                            width = button_width, 
                                            command=cannot_shoot,
                                            highlightbackground="#000080")
            player_underwater_cell.grid(row=i, column=j)
            
            
    for i in range(1, 11):
        Player["Player Surface"][i] = {}
        for j in range(11, 21):
            Player["Player Surface"][i][j] = {}
            Player["Player Surface"][i][j]["Presence"] = None
            Player["Player Surface"][i][j]["REF"] = None
            player_surface_cell = Button(Player_frame, 
                                         height = button_height, 
                                         width = button_width, 
                                         command=cannot_shoot,
                                         highlightbackground="#1E90FF")
            player_surface_cell.grid(row=i, column=j) 
        
    
    for i in range(12, 22):
        AI_player["AI Surface"][i] = {}
        for j in range(11, 21):
            AI_player["AI Surface"][i][j] = {}
            AI_player["AI Surface"][i][j]["Presence"] = None
            AI_player["AI Surface"][i][j]["REF"] = None
            AI_surface_cell = Button(AI_frame, 
                                     height = button_height, 
                                     width = button_width, 
                                     highlightbackground="#1E90FF",
                                     command=lambda row=i, column=j, depth = 1: shoot(row, column, depth))
            
            AI_surface_cell.grid(row=i, column=j)
    
    
    #This 2 for loops are just to highlight the player's Ships in their own Battle Field
    for i in range(len(Player["Carrier"])):
        player_ship_location = Button(Player_frame,
                                      height = button_height, 
                                      width = button_width, 
                                      command=cannot_shoot,
                                      highlightbackground="#2E8B57")
        
        player_ship_location.grid(row = Player["Carrier"][i][0], column = Player["Carrier"][i][1])

    for i in range (len(Player["Submarine"])):
        player_ship_location = Button(Player_frame,
                                      height = button_height, 
                                      width = button_width, 
                                      command=cannot_shoot,
                                      highlightbackground="#2E8B57")
        
        player_ship_location.grid(row = Player["Submarine"][i][0], column = Player["Submarine"][i][1])
    
    root.mainloop()



def cannot_shoot():
    print (messagebox.showinfo("Invalid","Cannot shoot yourself. lol :P"))
def already_shot():
    print (messagebox.showinfo("Invalid","It has already been shot here!"))
def hit_shot():
    print (messagebox.showinfo("HIT!", "Nice shot! AI Turn"))
def hit_missed():
    print (messagebox.showinfo("MISSED!", "Better Luck Next time! AI Turn"))
def AI_hit():
    print (messagebox.showinfo("HIT!", "AI managed to hit you! AI Turn"))
def AI_hit_missed():
    print (messagebox.showinfo("MISSED!", "AI did not hit you! your Turn"))


def draw_new_button_hit(row, column):
    
    global redraw_gameboard
    global Player
    global AI_player
    global AI_underwater_cell
    global player_underwater_cell
    global AI_frame
    global Player_frame
    global root
    
    script_dir = os.path.dirname(__file__)
    rel_path = "explode.png"
    image = Image.open(os.path.join(script_dir, rel_path))
    image = image.resize((50,50), Image.ANTIALIAS)
    
    imtk = ImageTk.PhotoImage(image, master = root)
    
    if row  <= 10 and column <= 10:
        new_button = Button(root,
                            image=imtk,
                            height = 20+10, 
                            width = 20+16,
                            command= already_shot, state = DISABLED)
        
        new_button.image = imtk
        
        new_button.lift()
        new_button.grid(row = row, column = column, in_ = Player_frame)
                
    elif row >= 12 and column <= 9:
        new_button = Button(root,
                            image=imtk,
                            height = 20+10, 
                            width = 20+16,
                            command= already_shot, state = DISABLED)
        AI_frame.lower()
        new_button.image = imtk
        new_button.lift()
        
        new_button.grid(row = row, column = column, in_ = AI_frame)
        
        
    elif row <= 10 and column >= 11:
        new_button = Button(Player_frame,
                            image=imtk,
                            height = 20+10, 
                            width = 20+16,
                            command= already_shot, state = DISABLED)
        
        new_button.image = imtk
        new_button.grid(row = row, column = column, in_ = Player_frame)
        new_button.lift()
        
    else:
        new_button = Button(AI_frame,
                            image=imtk,
                            height = 20+10, 
                            width = 20+16,
                            command= already_shot, state = DISABLED)
        
        new_button.image = imtk
        new_button.grid(row = row, column = column, in_ = AI_frame)
        new_button.lift()
        
        
        
        
def draw_new_button_miss(row, column):
    
    global redraw_gameboard
    global Player
    global AI_player
    global AI_underwater_cell
    global player_underwater_cell
    global AI_frame
    global Player_frame
    
    if row  <= 10 and column <= 10:
        
        new_button = Button(Player_frame,
                            height = button_height, 
                            width = button_width,
                            command= already_shot, 
                            highlightbackground='black')
        
        new_button.grid(row = row, column = column, in_ = Player_frame)
        new_button.lift()
                
    elif row >= 12 and column <= 9:
        new_button = Button(AI_frame,
                            height = button_height, 
                            width = button_width,
                            command= already_shot, 
                            highlightbackground='black')
        
        new_button.grid(row = row, column = column, in_ = AI_frame)
        new_button.lift()
        
    elif row <= 10 and column >= 11:
        new_button = Button(Player_frame,
                            height = button_height, 
                            width = button_width,
                            command= already_shot, 
                            highlightbackground='black')
        
        new_button.grid(row = row, column = column, in_ = Player_frame)
        new_button.lift()
        
    else:
        new_button = Button(AI_frame,
                            height = button_height, 
                            width = button_width,
                            command= already_shot, 
                            highlightbackground='black')
        
        new_button.grid(row = row, column = column, in_ = AI_frame)
        new_button.lift()


    
def top_boundary_shot(row, column):
    global AI_counter
    global Player_counter
    global Player
    global AI_player
    
    shots  = [(row,column,0), 
              (row+1, column,0), 
              (row+1, column +1,0), 
              (row, column +1,0), 
              (row, column -1,0), 
              (row+1, column-1,0),
              
              (row,column,1), 
              (row+1, column,1), 
              (row+1, column +1,1), 
              (row, column +1,1), 
              (row, column -1,1), 
              (row+1, column-1,1)]
    
    if row  <= 10 and column <= 10:
        counter = 0
        for i in range(len(shots)):
            Player["Player Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Submarine"][0] or shots[i] == Player["Submarine"][1] or shots[i] == Player["Submarine"][2]:
                draw_new_button_hit(shots[i][0], shots[i][1])
                counter = counter + 1
                
                if Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT"
                
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
                
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
                
    elif row >= 12 and column <= 9:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Submarine"][0] or shots[i] == AI_player["Submarine"][1] or shots[i] == AI_player["Submarine"][2]:
                
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            hit_shot()
        else:
            hit_missed()
    
    elif row <= 10 and column >= 11:
        counter = 0
        for i in range(len(shots)):
            Player["Player Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Carrier"][0] or shots[i] == Player["Carrier"][1] or shots[i] == Player["Carrier"][2] or shots[i] == Player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
                
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
        
    else:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Carrier"][0] or shots[i] == AI_player["Carrier"][1] or shots[i] == AI_player["Carrier"][2] or shots[i] == AI_player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            hit_shot()
        else:
            hit_missed()
            
def bottom_boundary_shot(row, column):
    global AI_counter
    global Player_counter
    global Player
    global AI_player
    
    shots  = [(row,column,0), 
              (row-1, column,0), 
              (row-1, column +1,0), 
              (row, column +1,0), 
              (row-1, column-1,0), 
              (row, column-1,0),
              
              (row,column,1), 
              (row-1, column,1), 
              (row-1, column +1,1), 
              (row, column +1,1), 
              (row-1, column-1,1), 
              (row, column-1,1)]
    
    if row  <= 10 and column <= 10:
        counter = 0
        for i in range(len(shots)):
            Player["Player Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Submarine"][0] or shots[i] == Player["Submarine"][1] or shots[i] == Player["Submarine"][2]:
                draw_new_button_hit(shots[i][0], shots[i][1])
                counter = counter + 1
                
                if Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
                
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
                
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
                
    elif row >= 12 and column <= 9:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Submarine"][0] or shots[i] == AI_player["Submarine"][1] or shots[i] == AI_player["Submarine"][2]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])

                if AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        
        if counter > 0:
            hit_shot()
        else:
            hit_missed()
    
    elif row <= 10 and column >= 11:
        counter = 0
        for i in range(len(shots)):
            Player["Player Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Carrier"][0] or shots[i] == Player["Carrier"][1] or shots[i] == Player["Carrier"][2] or shots[i] == Player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
                
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
        
    else:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Carrier"][0] or shots[i] == AI_player["Carrier"][1] or shots[i] == AI_player["Carrier"][2] or shots[i] == AI_player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])

                if AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            hit_shot()
        else:
            hit_missed()
            
def left_boundary_shot(row, column):
    global AI_counter
    global Player_counter
    global Player
    global AI_player
    
    shots  = [(row,column,0), 
              (row+1, column,0), 
              (row+1, column +1,0), 
              (row, column +1,0), 
              (row-1, column+1,0), 
              (row-1, column,0),
              
              (row,column,1), 
              (row+1, column,1), 
              (row+1, column +1,1), 
              (row, column +1,1), 
              (row-1, column+1,1), 
              (row-1, column,1)]
    
    if row  <= 10 and column <= 10:
        counter = 0
        for i in range(len(shots)):
            Player["Player Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Submarine"][0] or shots[i] == Player["Submarine"][1] or shots[i] == Player["Submarine"][2]:
                draw_new_button_hit(shots[i][0], shots[i][1])
                counter = counter + 1
                
                if Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
                
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
                
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
                
    elif row >= 12 and column <= 9:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Submarine"][0] or shots[i] == AI_player["Submarine"][1] or shots[i] == AI_player["Submarine"][2]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            hit_shot()
        else:
            hit_missed()
    
    elif row <= 10 and column >= 11:
        counter = 0
        for i in range(len(shots)):
            Player["Player Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Carrier"][0] or shots[i] == Player["Carrier"][1] or shots[i] == Player["Carrier"][2] or shots[i] == Player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
                
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
        
    else:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Carrier"][0] or shots[i] == AI_player["Carrier"][1] or shots[i] == AI_player["Carrier"][2] or shots[i] == AI_player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
                    
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            hit_shot()
        else:
            hit_missed()

def right_boundary_shot(row, column):
    
    global AI_counter
    global Player_counter
    global Player
    global AI_player
    
    shots  = [(row,column,0), 
              (row+1, column,0), 
              (row+1, column-1,0), 
              (row, column-1,0), 
              (row-1, column-1,0), 
              (row-1, column,0),
              
              (row,column,1), 
              (row+1, column,1), 
              (row+1, column-1,1), 
              (row, column-1,1), 
              (row-1, column-1,1), 
              (row-1, column,1)]
    
    if row  <= 10 and column <= 10:
        counter = 0
        for i in range(len(shots)):
            Player["Player Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Submarine"][0] or shots[i] == Player["Submarine"][1] or shots[i] == Player["Submarine"][2]:
                draw_new_button_hit(shots[i][0], shots[i][1])
                counter = counter + 1
                
                if Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
                
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
                
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
                
    elif row >= 12 and column <= 9:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Submarine"][0] or shots[i] == AI_player["Submarine"][1] or shots[i] == AI_player["Submarine"][2]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            hit_shot()
        else:
            hit_missed()
    
    elif row <= 10 and column >= 11:
        counter = 0
        for i in range(len(shots)):
            Player["Player Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Carrier"][0] or shots[i] == Player["Carrier"][1] or shots[i] == Player["Carrier"][2] or shots[i] == Player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
                
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
        
    else:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Carrier"][0] or shots[i] == AI_player["Carrier"][1] or shots[i] == AI_player["Carrier"][2] or shots[i] == AI_player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            hit_shot()
        else:
            hit_missed()

    
def top_right_corner_shot(row, column):
    
    global AI_counter
    global Player_counter
    global Player
    global AI_player
    
    shots  = [(row,column,0), 
              (row, column-1,0), 
              (row+1, column-1,0), 
              (row+1, column,0),
              
              (row,column,1), 
              (row, column-1,1), 
              (row+1, column-1,1), 
              (row+1, column,1)]
    
    if row  <= 10 and column <= 10:
        """
        PLAYER UNDERWATER
        """
        counter = 0
        for i in range(len(shots)):
            Player["Player Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Submarine"][0] or shots[i] == Player["Submarine"][1] or shots[i] == Player["Submarine"][2]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"            
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
            
    elif row >= 12 and column <= 9:
        """
        AI Underwater
        """
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
        
            if shots[i] == AI_player["Submarine"][0] or shots[i] == AI_player["Submarine"][1] or shots[i] == AI_player["Submarine"][2]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            hit_shot()
        else:
            hit_missed()    
            
    elif row <= 10 and column >= 11:
        """
        Player Surface
        """
        counter = 0
        for i in range(len(shots)):
            Player["Player Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Carrier"][0] or shots[i] == Player["Carrier"][1] or shots[i] == Player["Carrier"][2] or shots[i] == Player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"        
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
            
    else:
        """
        AI Surface
        """
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Carrier"][0] or shots[i] == AI_player["Carrier"][1] or shots[i] == AI_player["Carrier"][2] or shots[i] == AI_player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"     
                    
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
    
    
    
def top_left_corner_shot(row, column):
    
    global AI_counter
    global Player_counter
    global Player
    global AI_player
    
    shots  = [(row,column,0), 
              (row+1, column,0), 
              (row+1, column +1,0), 
              (row, column +1,0),
              
              (row,column,1), 
              (row+1, column,1), 
              (row+1, column +1,1), 
              (row, column +1,1)]

    if row  <= 10 and column <= 10:
        """
        PLAYER UNDERWATER
        """
        counter = 0
        for i in range(len(shots)):
            Player["Player Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Submarine"][0] or shots[i] == Player["Submarine"][1] or shots[i] == Player["Submarine"][2]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
                
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
            
    elif row >= 12 and column <= 9:
        """
        AI Underwater
        """
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
        
            if shots[i] == AI_player["Submarine"][0] or shots[i] == AI_player["Submarine"][1] or shots[i] == AI_player["Submarine"][2]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            hit_shot()
        else:
            hit_missed()    
            
    elif row <= 10 and column >= 11:
        """
        Player Surface
        """
        counter = 0
        for i in range(len(shots)):
            Player["Player Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Carrier"][0] or shots[i] == Player["Carrier"][1] or shots[i] == Player["Carrier"][2] or shots[i] == Player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
            
    else:
        """
        AI Surface
        """
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Carrier"][0] or shots[i] == AI_player["Carrier"][1] or shots[i] == AI_player["Carrier"][2] or shots[i] == AI_player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])

                if AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
                
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

                
def bottom_left_corner_shot(row, column):
    
    global AI_counter
    global Player_counter
    global Player
    global AI_player
    
    shots  = [(row,column,0), 
              (row-1, column,0), 
              (row-1, column+1,0), 
              (row, column+1,0),
              
              (row,column,1), 
              (row-1, column,1), 
              (row-1, column+1,1), 
              (row, column+1,1)]
    
    if row  <= 10 and column <= 10:
        """
        PLAYER UNDERWATER
        """
        counter = 0
        for i in range(len(shots)):
            Player["Player Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Submarine"][0] or shots[i] == Player["Submarine"][1] or shots[i] == Player["Submarine"][2]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])

                if Player["Player Underwater"][shots[i][0]][shots[i][1]]["Presence"] == "HIT":
                    continue
                else:
                    AI_counter = AI_counter + 1
                
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
            
    elif row >= 12 and column <= 9:
        """
        AI Underwater
        """
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
        
            if shots[i] == AI_player["Submarine"][0] or shots[i] == AI_player["Submarine"][1] or shots[i] == AI_player["Submarine"][2]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            hit_shot()
        else:
            hit_missed()    
            
    elif row <= 10 and column >= 11:
        """
        Player Surface
        """
        counter = 0
        for i in range(len(shots)):
            Player["Player Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Carrier"][0] or shots[i] == Player["Carrier"][1] or shots[i] == Player["Carrier"][2] or shots[i] == Player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
            
    else:
        """
        AI Surface
        """
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Carrier"][0] or shots[i] == AI_player["Carrier"][1] or shots[i] == AI_player["Carrier"][2] or shots[i] == AI_player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
    
def bottom_right_corner_shot(row, column):
    
    global AI_counter
    global Player_counter
    global Player
    global AI_player
    
    shots  = [(row,column,0), 
              (row-1, column,0), 
              (row-1, column-1,0), 
              (row, column-1,0),
              
              (row,column,1), 
              (row-1, column,1), 
              (row-1, column-1,1), 
              (row, column-1,1)]
    
    if row  <= 10 and column <= 10:
        """
        PLAYER UNDERWATER
        """
        counter = 0
        for i in range(len(shots)):
            Player["Player Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Submarine"][0] or shots[i] == Player["Submarine"][1] or shots[i] == Player["Submarine"][2]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
            
    elif row >= 12 and column <= 9:
        """
        AI Underwater
        """
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
        
            if shots[i] == AI_player["Submarine"][0] or shots[i] == AI_player["Submarine"][1] or shots[i] == AI_player["Submarine"][2]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            hit_shot()
        else:
            hit_missed()    
            
    elif row <= 10 and column >= 11:
        """
        Player Surface
        """
        counter = 0
        for i in range(len(shots)):
            Player["Player Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Carrier"][0] or shots[i] == Player["Carrier"][1] or shots[i] == Player["Carrier"][2] or shots[i] == Player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
                if Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    AI_counter = AI_counter + 1
                
                Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
        if counter > 0:
            AI_hit()
        else:
            AI_hit_missed()
            
    else:
        """
        AI Surface
        """
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Carrier"][0] or shots[i] == AI_player["Carrier"][1] or shots[i] == AI_player["Carrier"][2] or shots[i] == AI_player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])

                if AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                    pass
                else:
                    Player_counter = Player_counter + 1
                
                AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"           
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
 
    
def scatter_shot(row, column, depth):
    
    global Player
    global AI_player
    global AI_counter
    global Player_counter
    
    shots = [(row-1,column-1,0), 
             (row+1, column+1,0), 
             (row, column+1,0), 
             (row, column-1,0), 
             (row -1, column+1,0), 
             (row+1, column-1,0), 
             (row -1, column,0),
             (row + 1, column,0),
             (row, column, 0),
             
             (row-1,column-1,1), 
             (row+1, column+1,1), 
             (row, column+1,1), 
             (row, column-1,1), 
             (row -1, column+1,1), 
             (row+1, column-1,1), 
             (row -1, column,1),
             (row + 1, column,1),
             (row, column, 1)]
    

    if row >= 12 and column >= 11: 
        """
        AI SURFACE
        ======================
        Corner and Boundary shot
        ======================
        """

        if (row,column) == (12,11): 
            top_left_corner_shot(row, column)
        elif (row,column) == (12,20):
            top_right_corner_shot(row, column)
        elif (row,column) == (21,20):
            bottom_right_corner_shot(row, column)
        elif (row, column) == (21,11):
            bottom_left_corner_shot(row, column)
        
        elif (row, column) == (12, column):
            top_boundary_shot(12, column)
        elif (row, column) == (21, column):
            bottom_boundary_shot(21, column)
        elif (row, column) == (row, 11):
            left_boundary_shot(row, 11)      
        elif (row, column) == (row, 20):
            right_boundary_shot(row, 20)           
            
        else:
            counter = 0
            for i in range(len(shots)):
                AI_player["AI Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
                if shots[i] == AI_player["Carrier"][0] or shots[i] == AI_player["Carrier"][1] or shots[i] == AI_player["Carrier"][2] or shots[i] == AI_player["Carrier"][3]:
                    counter = counter + 1
                    draw_new_button_hit(shots[i][0], shots[i][1])
                    
                    if AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                        pass
                    else:
                        Player_counter = Player_counter + 1
                    
                    AI_player["AI Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"         
            
                else:
                    draw_new_button_miss(shots[i][0], shots[i][1])
                    
            if counter > 0:
                hit_shot()
            else:
                hit_missed()
                
    
    elif row >= 12 and column <= 9:
        """
        AI UNDERWATER
        """
        
        if (row,column) == (12,0):
            top_left_corner_shot(row,column)
        elif (row,column) == (12,9):
            top_right_corner_shot(row,column)
        elif (row,column) == (21,0):
            bottom_left_corner_shot(row, column)
        elif (row, column) == (21,9):
            bottom_right_corner_shot(row, column)
            
        elif (row, column) == (12, column):
            top_boundary_shot(12, column)
        elif (row, column) == (21, column):
            bottom_boundary_shot(21, column)
        elif (row, column) == (row, 0):
            left_boundary_shot(row, 0)      
        elif (row, column) == (row, 9):
            right_boundary_shot(row, 9)
        else:
            counter = 0
            for i in range(len(shots)):
                AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
                
                if shots[i] == AI_player["Submarine"][0] or shots[i] == AI_player["Submarine"][1] or shots[i] == AI_player["Submarine"][2]:
                    counter = counter + 1
                    draw_new_button_hit(shots[i][0], shots[i][1])
                    
                    if AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                        pass
                    else:
                        Player_counter = Player_counter + 1
                    
                    AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
                    
                else:
                    draw_new_button_miss(shots[i][0], shots[i][1])
                    
            if counter > 0:
                hit_shot()
            else:
                hit_missed()
                    
    elif row <= 10 and column <= 9:
        """
        Player UNDERWATER
        """
        if (row,column) == (1,0):
            top_left_corner_shot(row, column)
        elif (row,column) == (1,9):
            top_right_corner_shot(row, column)
        elif (row,column) == (10,9):
            bottom_right_corner_shot(row, column)
        elif (row, column) == (10,0):
            bottom_left_corner_shot(row, column)
            
        elif (row, column) == (1, column):
            top_boundary_shot(1, column)
        elif (row, column) == (10, column):
            bottom_boundary_shot(10, column)
        elif (row, column) == (row, 0):
            left_boundary_shot(row, 0)      
        elif (row, column) == (row, 9):
            right_boundary_shot(row, 9) 
        else:
            counter = 0
            for i in range(len(shots)):
                Player["Player Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
                if shots[i] == Player["Submarine"][0] or shots[i] == Player["Submarine"][1] or shots[i] == Player["Submarine"][2] :
                    counter = counter + 1
                    draw_new_button_hit(shots[i][0], shots[i][1])
                    
                    if Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                        pass
                    else:
                        AI_counter = AI_counter + 1
                    
                    Player["Player Underwater"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
                
                else:
                    draw_new_button_miss(shots[i][0], shots[i][1])
            if counter > 0:
                AI_hit()
            else:
                AI_hit_missed()
       
    else:
        """
        Player SURFACE
        """
        
        if (row,column) == (1,11):
            top_left_corner_shot(row, column)
        elif (row,column) == (1,20):
            top_right_corner_shot(1,20)
        elif (row,column) == (10,11):
            bottom_left_corner_shot(10,11)
        elif (row, column) == (10,20):
            bottom_right_corner_shot(10,20)

        elif (row, column) == (1, column):
            top_boundary_shot(1, column)
        elif (row, column) == (10, column):
            bottom_boundary_shot(10, column)
        elif (row, column) == (row, 11):
            left_boundary_shot(row, 11)      
        elif (row, column) == (row, 20):
            right_boundary_shot(row, 20) 
        else:
            counter = 0
            for i in range(len(shots)):
                Player["Player Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
                if shots[i] == Player["Carrier"][0] or shots[i] == Player["Carrier"][1] or shots[i] == Player["Carrier"][2] or shots[i] == Player["Carrier"][3]:
                    counter = counter + 1
                    draw_new_button_hit(shots[i][0], shots[i][1])
                    
                    if Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] == "SHIP HIT":
                        pass
                    else:
                        AI_counter = AI_counter + 1
                    
                    Player["Player Surface"][shots[i][0]][shots[i][1]]["REF"] = "SHIP HIT"
                
                else:
                    draw_new_button_miss(shots[i][0], shots[i][1])
            if counter > 0:
                AI_hit()
            else:
                AI_hit_missed()
            

def shoot(row, column, depth):
    global redraw_gameboard
    global Player
    global AI_player
    
    if depth == 1: #means AI_surface
        while AI_player["AI Surface"][row][column]["Presence"] == "HIT":
            already_shot()
            break
        else:
            scatter_shot(row, column, 1)
            AI_player_turn()
                    
    else:
        while AI_player["AI Underwater"][row][column]["Presence"] == "HIT":
            already_shot()
            break
            
        else:
            scatter_shot(row, column, 0)
            AI_player_turn()
 

def AI_player_turn():
    
    global AI_counter
    global Player_counter
    global Player
    global AI_player
    
    print ("Player Score = %d | AI Score = %d. First hit 7 wins." % (Player_counter, AI_counter))
    
    if Player_counter <= 6 and AI_counter <= 6:
        
        random_surface = random.randint(0,1)
        if random_surface == 0:
            random_underwater_x = random.randint(1,10)
            random_underwater_y = random.randint(0,9)
            row = random_underwater_x
            column = random_underwater_y
        
            if Player["Player Underwater"][random_underwater_x][random_underwater_y]["Presence"] == "HIT":
                print ("Bot Thinking...")
                AI_player_turn()
        
            else:
                print("AI shooting Player Underwater", end = '')
                print (" at coordinate %d row %d column"%(row,column))
                scatter_shot(row, column, 0)
                
                
        else:
            random_surface_x = random.randint(1,10)
            random_surface_y = random.randint(11,20)
            row = random_surface_x
            column = random_surface_y
            
            if Player["Player Surface"][random_surface_x][random_surface_y]["Presence"] == "HIT":
                print ("Bot Thinking...")
                AI_player_turn()
                
        
            else:
                print("AI shooting Player Surface", end = '')
                print (" at coordinate %d row %d column"%(row,column))
                scatter_shot(row, column, 1)
    else:
        if Player_counter == 7:
            print ("Player Won")
            End_prompt()
        else:
            print ("AI Won, better luck next time")
            End_prompt()



def End_prompt():
    
    global redraw_gameboard
    global End_prompt
    global AI_counter
    global Player_counter
    global Player
    global AI_player
    global game_screen
    
    root.destroy()
    
    AI_counter = 0
    Player_counter = 0
    
    Player = {}
    AI_player = AI_player
    
    End_prompt = Tk()
    End_prompt.title("Game Over")
    End_prompt.geometry("250x250")
    End_prompt.resizable(False, False)
    
    if AI_counter == 7:
        Win_announcer = Label(End_prompt, text = "BOT WON.")
        Win_announcer.pack()
    else:
        Win_announcer = Label(End_prompt, text = "YOU WON!")
        Win_announcer.pack()
        
    
    play_again = Button(End_prompt, 
                        height = 2, 
                        width = 10, 
                        command=basegame,
                        highlightbackground='white', text = "Play Again")
    
    play_again.place(relx = 0, rely = 0.5, anchor = W)
    play_again.pack()
    
    quit_game = Button(End_prompt, 
                        height = 2, 
                        width = 10, 
                        command=quit_battleship,
                        highlightbackground='white', text = "Quit")
    
    quit_game.place(relx = 1, rely = 0.5, anchor = E)
    quit_game.pack()
    
def quit_battleship():
    global redraw_gameboard
    global End_prompt
    global window
    global login_screen
    global main_account_screen
    
    End_prompt.destroy()
    window.destroy()
    

main_account_screen()