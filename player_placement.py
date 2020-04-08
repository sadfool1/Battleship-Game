'''
Program Name: Player Placement GUI 2.1

Description: This file/module builds the grids and assists players in placing
ships to subsequently play the Python Battleship game.

Note:

V2.0 --> Version that would allow flexible choice of which ship to place first
(Undone due to complexity, so completing this simpler version, V2.1, first)

V2.1 --> Version that has a fixed order of ships being placed.
(Carrier placement first, submarine placement later)
'''

from tkinter import * # to import all names from tkinter
from tkinter import messagebox # for pop-up messages as part of the verification

# AddNote: messagebox function doesn't seem to work without this second import line

import os # importing support for different operating systems

# AddNote: Legacy importing from the Login GUI, not used here

from random import randint # importing random module to generate random number

# AddNote: Legacy importing from the Login GUI, not used here

'''
Program code starts here
'''

# Dictionary used to store the coordinates of the player's ships
Player = {}

# making the screen to choose to start a new game or continue an existing game
# imported from login/signup GUI
def basegame():
    global game_screen
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
    Label(surface_screen, text="", height = 20, width = 4).grid(row=1, column=11, rowspan=10)
    
    carrier_placing_button()


# Function used to place the grid of buttons for carrier flagship
def carrier_placing_button():
    for i in range(1, 11):
        for j in range(10):
            invalid_btn = Button(surface_screen, height = 2, width = 4, command=invalid_placement)
            invalid_btn.grid(row=i, column=j)

    # AddNote: Remember that carriers cannot be placed underwater

    for i in range(1, 11):
        for j in range(12, 22):
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
                Coordinates.append((x,column - 11,1))
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
                Coordinates.append((x,column - 11,1))
                Player["Carrier"] = Coordinates
                carrier_btn.config(state="disabled")
            carrier_alert_message()
        else:
            messagebox.showinfo("Invalid", "Invalid ship placement")

    # If chosen direction is left
    if direction.get() == 3:
        if column >= 15:
            close_button()
            Coordinates = []
            for x in range(column - 3, column + 1):
                carrier_btn = Button(surface_screen, bg='red', height = 2, width=4)
                carrier_btn.grid(row=row, column=x)
                Coordinates.append((row,x - 11,1))
                Player["Carrier"] = Coordinates
                carrier_btn.config(state="disabled")
            carrier_alert_message()
        else:
            messagebox.showinfo("Invalid", "Invalid ship placement")

    # If chosen direction is right
    if direction.get() == 4:
        if column <= 18:
            close_button()
            Coordinates = []
            for x in range(column, column + 4):
                carrier_btn = Button(surface_screen, bg='red', height = 2, width=4)
                carrier_btn.grid(row=row, column=x)
                Coordinates.append((row,x - 11,1))
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
        for j in range(12, 22):
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
        for j in range(12, 22):

            # Preventing chosen buttons from being restored to "default" settings and retain their red coloring
            
            if not i in Carrier_Row or not (j-11) in Carrier_Column:
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
                Coordinates.append((x,column + 1,0))
                Player["Submarine"] = Coordinates
                submarine_btn.config(state="disabled")
            submarine_alert_message()
        elif row >= 3 and column > 9:

            for x in range(row - 2, row + 1):
                if x in Carrier_Row and (column - 11) in Carrier_Column:
                    messagebox.showinfo("Invalid", "Invalid ship placement")
                    return

            close_button2()
            Coordinates = []
            for x in range(row - 2, row + 1):
                submarine_btn = Button(surface_screen, bg='blue', height = 2, width = 4)
                submarine_btn.grid(row=x, column=column)
                Coordinates.append((x,column - 11,1))
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
                Coordinates.append((x,column + 1,0))
                Player["Submarine"] = Coordinates
                submarine_btn.config(state="disabled")
            submarine_alert_message()
        if row <= 8 and column > 9:

            for x in range(row, row + 3):
                if x in Carrier_Row and (column - 11) in Carrier_Column:
                    messagebox.showinfo("Invalid", "Invalid ship placement")
                    return

            close_button2()
            Coordinates = []
            for x in range(row, row + 3):
                submarine_btn = Button(surface_screen, bg='blue', height = 2, width=4)
                submarine_btn.grid(row=x, column=column)
                Coordinates.append((x,column - 11,1))
                Player["Submarine"] = Coordinates
                submarine_btn.config(state="disabled")
            submarine_alert_message()
        else:
            messagebox.showinfo("Invalid", "Invalid ship placement")

    # If chosen direction is left
    if direction.get() == 3:
        if column > 9 and column >= 14:

            for x in range(column - 2, column + 1):
                if row in Carrier_Row and (x - 11) in Carrier_Column:
                    messagebox.showinfo("Invalid", "Invalid ship placement")
                    return

            close_button2()
            Coordinates = []
            for x in range(column - 2, column + 1):
                submarine_btn = Button(surface_screen, bg='blue', height = 2, width=4)
                submarine_btn.grid(row=row, column=x)
                Coordinates.append((row,x - 11,1))
                Player["Submarine"] = Coordinates
                submarine_btn.config(state="disabled")
            submarine_alert_message()
        elif column <= 9 and column >= 2:
            close_button2()
            Coordinates = []
            for x in range(column - 2, column + 1):
                submarine_btn = Button(surface_screen, bg='blue', height = 2, width=4)
                submarine_btn.grid(row=row, column=x)
                Coordinates.append((row,x + 1,0))
                Player["Submarine"] = Coordinates
                submarine_btn.config(state="disabled")
            submarine_alert_message()
        else:
            messagebox.showinfo("Invalid", "Invalid ship placement")

    # If chosen direction is right
    if direction.get() == 4:
        if column > 9 and column <= 19:

            for x in range(column, column + 3):
                if row in Carrier_Row and (x - 11) in Carrier_Column:
                    messagebox.showinfo("Invalid", "Invalid ship placement")
                    return

            close_button2()
            Coordinates = []
            for x in range(column, column + 3):
                submarine_btn = Button(surface_screen, bg='blue', height = 2, width=4)
                submarine_btn.grid(row=row, column=x)
                Coordinates.append((row,x - 11,1))
                Player["Submarine"] = Coordinates
                submarine_btn.config(state="disabled")
            submarine_alert_message()
        elif column <= 9 and column <= 7:
            close_button2()
            Coordinates = []
            for x in range(column, column + 3):
                submarine_btn = Button(surface_screen, bg='blue', height = 2, width=4)
                submarine_btn.grid(row=row, column=x)
                Coordinates.append((row,x + 1,0))
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
        for j in range(12, 22):
            if not i in Carrier_Row or not (j-11) in Carrier_Column:
                btn = Button(surface_screen, height = 2, width = 4, command=callback_submarine(i,j))
                btn.grid(row=i, column=j)
                btn.config(state="disabled")

# message box to confirm selection of submarine spot
def submarine_alert_message():    
    SubmarineMsg = messagebox.askquestion('Confirmation','Do you want to place your submarine here?')

    if SubmarineMsg == 'yes':
        print(Player) # Test function to make sure the dictionary is extracted correctly using the Python shell
    else:
        Player["Submarine"] = "" # Restoring dictionary to empty value due to rejected spot
        submarine_placing_button()

# Uncomment the function below if you want to test the module alone.

## basegame()
