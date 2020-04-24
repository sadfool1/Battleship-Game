
import tkinter as tk 
from tkinter import *
from tkinter import messagebox 
import os 
from random import randint
import random
from PIL import Image, ImageTk

Player = {'Carrier':[(1, 11, 1), (1, 12, 1), (1, 13, 1), (1, 14, 1)], 'Submarine': [(1, 0, 0), (1, 1, 0), (1, 2, 0)]}
AI_player = {'Carrier':[(12,12,1), (12,13,1), (12,14,1), (12,15,1)], 'Submarine': [(12,6,0), (12,7,0), (12,8,0)]}
button_height = 2
button_width = 4

def redraw_boards():
    global redraw_gameboard
    global Player
    global AI_player
    
    Player["Player Surface"] = {}
    Player["Player Underwater"] = {}
    AI_player["AI Surface"] = {}
    AI_player["AI Underwater"] = {}
    
    redraw_gameboard = tk.Tk()
    redraw_gameboard.title("Battleship Game")
    redraw_gameboard.geometry("1000x1000")
    redraw_gameboard.resizable(False, False)
    
    Label(redraw_gameboard, text="Player Underwater", height = 3, width = 15).grid(row=0, column=0, columnspan=10)
    Label(redraw_gameboard, text="Player Surface", height = 3, width = 15).grid(row=0, column=12, columnspan=10)

    # Preparing spacings between the grids
    Label(redraw_gameboard, text="", height = 20, width = 4).grid(row=1, column=10, rowspan=10)
    Label(redraw_gameboard, text="AI Underwater", height = 3, width = 15).grid(row=11, column=0, columnspan=10)
    Label(redraw_gameboard, text="AI Surface", height = 3, width = 15).grid(row=11, column=11, columnspan=10)
    #Label(redraw_gameboard, text="", height = 4, width = 1).grid(row=11, column=0, columnspan=10)


    for i in range(12, 22):
        AI_player["AI Underwater"][i] = {}
        for j in range(10):
            AI_player["AI Underwater"][i][j] = {}
            AI_player["AI Underwater"][i][j]["Presence"] = None
            AI_underwater_cell = Button(redraw_gameboard, 
                                        height = button_height, 
                                        width = button_width,
                                        highlightbackground="#000080",
                                        command=lambda row=i, column=j, depth = 0: shoot(row, column, depth))
            AI_underwater_cell.grid(row=i, column=j)
            AI_underwater_cell.lower()
            
    for i in range(1, 11):
        Player["Player Underwater"][i] = {}
        for j in range(10):
            Player["Player Underwater"][i][j] = {}
            Player["Player Underwater"][i][j]["Presence"] = None
            player_underwater_cell = Button(redraw_gameboard, 
                                            height = button_height, 
                                            width = button_width, 
                                            command=cannot_shoot,
                                            highlightbackground="#000080")
            player_underwater_cell.grid(row=i, column=j)
            player_underwater_cell.lower()
            
            
    for i in range(1, 11):
        Player["Player Surface"][i] = {}
        for j in range(11, 21):
            Player["Player Surface"][i][j] = {}
            Player["Player Surface"][i][j]["Presence"] = None
            player_surface_cell = Button(redraw_gameboard, 
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
            AI_surface_cell = Button(redraw_gameboard, 
                                     height = button_height, 
                                     width = button_width, 
                                     highlightbackground="#1E90FF",
                                     command=lambda row=i, column=j, depth = 1: shoot(row, column, depth))
            
            AI_surface_cell.grid(row=i, column=j)
            

    redraw_gameboard.mainloop()
def cannot_shoot():
    pass
def already_shot():
    pass
def hit_shot():
    pass
def hit_missed():
    pass
def AI_hit():
    pass
def AI_hit_missed():
    pass

def draw_new_button_hit(row, column):
    global redraw_gameboard
    global Player
    global AI_player
    
    new_button = Button(redraw_gameboard,
                        height = button_height, 
                        width = button_width,
                        command= already_shot, highlightbackground ='red')

    new_button.grid(row = row, column = column)


def draw_new_button_miss(row, column):
    
    global redraw_gameboard
    global Player
    global AI_player
    
    new_button = Button(redraw_gameboard, 
                        height = button_height, 
                        width = button_width, 
                        command= already_shot,
                        highlightbackground="#000000")
    
    new_button.grid(row = row, column = column)

def top_boundary_shot(row, column):
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
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
                
    elif row >= 12 and column <= 9:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Submarine"][0] or shots[i] == AI_player["Submarine"][1] or shots[i] == AI_player["Submarine"][2]:
                counter = counter + 1
                new_button = Button(redraw_gameboard, 
                        height = 2, 
                        width = 4, 
                        command= already_shot,
                        highlightbackground='red')
                new_button.grid(row = shots[i][0], column = shots[i][1])
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

    elif row <= 10 and column >= 11:
        counter = 0
        for i in range(len(shots)):
            Player["Player Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Carrier"][0] or shots[i] == Player["Carrier"][1] or shots[i] == Player["Carrier"][2] or shots[i] == Player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

    else:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Carrier"][0] or shots[i] == AI_player["Carrier"][1] or shots[i] == AI_player["Carrier"][2] or shots[i] == AI_player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

            
def bottom_boundary_shot(row, column):
    global redraw_gameboard
    
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
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
            
                
    elif row >= 12 and column <= 9:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Submarine"][0] or shots[i] == AI_player["Submarine"][1] or shots[i] == AI_player["Submarine"][2]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
                
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
    
    elif row <= 10 and column >= 11:
        counter = 0
        for i in range(len(shots)):
            Player["Player Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Carrier"][0] or shots[i] == Player["Carrier"][1] or shots[i] == Player["Carrier"][2] or shots[i] == Player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

    else:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Carrier"][0] or shots[i] == AI_player["Carrier"][1] or shots[i] == AI_player["Carrier"][2] or shots[i] == AI_player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

            
def left_boundary_shot(row, column):
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
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

                
    elif row >= 12 and column <= 9:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Submarine"][0] or shots[i] == AI_player["Submarine"][1] or shots[i] == AI_player["Submarine"][2]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

    
    elif row <= 10 and column >= 11:
        counter = 0
        for i in range(len(shots)):
            Player["Player Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Carrier"][0] or shots[i] == Player["Carrier"][1] or shots[i] == Player["Carrier"][2] or shots[i] == Player["Carrier"][3]:
                counter = counter + 1
                draw_new_button_hit(shots[i][0], shots[i][1])
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

        
    else:
        for i in range(len(shots)):
            AI_player["AI Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Carrier"][0] or shots[i] == AI_player["Carrier"][1] or shots[i] == AI_player["Carrier"][2] or shots[i] == AI_player["Carrier"][3]:
                draw_new_button_hit(shots[i][0], shots[i][1])
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])


def right_boundary_shot(row, column):
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
        for i in range(len(shots)):
            Player["Player Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Submarine"][0] or shots[i] == Player["Submarine"][1] or shots[i] == Player["Submarine"][2]:
                draw_new_button_hit(shots[i][0], shots[i][1])
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

                
    elif row >= 12 and column <= 9:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Underwater"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Submarine"][0] or shots[i] == AI_player["Submarine"][1] or shots[i] == AI_player["Submarine"][2]:
                draw_new_button_hit(shots[i][0], shots[i][1])
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

    elif row <= 10 and column >= 11:
        counter = 0
        for i in range(len(shots)):
            Player["Player Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            if shots[i] == Player["Carrier"][0] or shots[i] == Player["Carrier"][1] or shots[i] == Player["Carrier"][2] or shots[i] == Player["Carrier"][3]:
                draw_new_button_hit(shots[i][0], shots[i][1])
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

    else:
        counter = 0
        for i in range(len(shots)):
            AI_player["AI Surface"][shots[i][0]][shots[i][1]]["Presence"] = "HIT"
            
            if shots[i] == AI_player["Carrier"][0] or shots[i] == AI_player["Carrier"][1] or shots[i] == AI_player["Carrier"][2] or shots[i] == AI_player["Carrier"][3]:
                draw_new_button_hit(shots[i][0], shots[i][1])
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

    
def top_right_corner_shot(row, column):
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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
            
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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
   
            
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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
            
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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
    
    
    
def top_left_corner_shot(row, column):
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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

            
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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

            
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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

                
def bottom_left_corner_shot(row, column):
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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

            
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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
  
            
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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

            
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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
    
def bottom_right_corner_shot(row, column):
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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

            
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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

            
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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])

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
            
            else:
                draw_new_button_miss(shots[i][0], shots[i][1])
 
    
def scatter_shot(row, column, depth):    
    global redraw_gameboard
    global Player
    global AI_player
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
            
                else:
                    draw_new_button_miss(shots[i][0], shots[i][1])
                    

    
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
                else:
                    draw_new_button_miss(shots[i][0], shots[i][1])
                    
                    
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
                
                else:
                    draw_new_button_miss(shots[i][0], shots[i][1])

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
                
                else:
                    draw_new_button_miss(shots[i][0], shots[i][1])


def shoot(row, column, depth):
    global redraw_gameboard
    global Player
    global AI_player
    global player_underwater_cell
    global player_surface_cell
    global AI_underwater_cell
    global AI_surface_cell
    
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
    pass

redraw_boards()