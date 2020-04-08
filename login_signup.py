'''
Program Name: Login_Signup GUI

Description: This file/module assists players with signing up and logging
into their accounts used for the Python Battleship game.

Change history: 1/3/2020    V 1.0   Carissa     Created Program
                4/3/2020    V 1.1   Bryan       Added Username/DOB/Password Verification
                                                Added Number of tries support
                11/3/2020   V 1.2   Carissa     Added DOB integer check
                                                Added game command for gameplay screen

P.S.: Max 3 tries coding is hard-coded and user can simply quit and reopen
the application to bypass it. To be refined when time permits.
'''

import tkinter as tk
from tkinter import * #to import all names from tkinter
from tkinter import messagebox #for pop-up messages as part of the verification
import os #importing operating systems
from player_placement import *

#Making first main window:
def main_account_screen():
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

# Designing popup for login success
def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command = basegame).pack()

# Designing popup for login invalid password
def password_not_recognised():
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
        Button1.configure(state=NORMAL) #undisable the login button
        counter = 0 #reset the number of tries given to the user
        delete_reactivation()
    else:
        messagebox.showinfo("Invalid", "Date of Birth is incorrect, please try again")

def delete_reactivation():
    reactivate_screen.destroy()

# designing new screen for sign ups
def signup():
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
        messagebox.showinfo("Invalid", "Password should not contain the username")

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


# Uncomment the function below if you want to test the module alone.

## main_account_screen()
