import tkinter as tk 
from tkinter import *
from tkinter import messagebox 
import os 
from random import randint
import random

Player = {'Carrier':[(3, 2, 1), (4, 2, 1), (5, 2, 1), (6, 2, 1)], 'Submarine': [(4, 10, 0), (5, 10, 0), (6, 10, 0)]}
AI_player = {'Carrier':[(12,12,1), (12,13,1), (12,14,1)], 'Submarine': [(0,12,0), (0,13,0), (0,14,0), (0,15,0)]}
redraw_boards()
def redraw_boards():
    global redraw_gameboard
    global Player
    global AI_player
    global player_underwater_cell
    global player_surface_cell
    global AI_underwater_cell
    global AI_surface_cell
    
    
    print (Player)
    print (AI_player)
    
    Player["Player Surface"] = {}
    Player["Player Underwater"] = {}
    AI_player["AI Surface"] = {}
    AI_player["AI Underwater"] = {}
    
    redraw_gameboard = Tk()
    redraw_gameboard.title("Battleship Game")
    redraw_gameboard.geometry("1080x1240")
    redraw_gameboard.resizable(False, False)
    
    Label(redraw_gameboard, text="Player Underwater", height = 3, width = 40).grid(row=0, column=0, columnspan=10)
    Label(redraw_gameboard, text="Player Surface", height = 3, width = 40).grid(row=0, column=12, columnspan=10)

    # Preparing spacings between the grids
    Label(redraw_gameboard, text="", height = 20, width = 4).grid(row=1, column=10, rowspan=10)
    Label(redraw_gameboard, text="AI Underwater", height = 3, width = 40).grid(row=11, column=0, columnspan=10)
    Label(redraw_gameboard, text="AI Surface", height = 3, width = 40).grid(row=11, column=11, columnspan=10)
    Label(redraw_gameboard, text="", height = 4, width = 1).grid(row=11, column=0, columnspan=10)

    
    for i in range(1, 11):
        Player["Player Underwater"][i] = {}
        for j in range(10):
            Player["Player Underwater"][i][j] = {}
            Player["Player Underwater"][i][j]["Presence"] = None
            player_underwater_cell = Button(redraw_gameboard, 
                                            height = 2, 
                                            width = 4, 
                                            command=cannot_shoot,
                                            highlightbackground='white')
            player_underwater_cell.grid(row=i, column=j)
            
    for i in range(1, 11):
        Player["Player Surface"][i] = {}
        for j in range(11, 21):
            Player["Player Surface"][i][j] = {}
            Player["Player Surface"][i][j]["Presence"] = None
            player_surface_cell = Button(redraw_gameboard, 
                                         height = 2, 
                                         width = 4, 
                                         command=cannot_shoot,
                                         highlightbackground='white')
            player_surface_cell.grid(row=i, column=j) 
            
    for i in range(12, 22):
        AI_player["AI Underwater"][i] = {}
        for j in range(10):
            AI_player["AI Underwater"][i][j] = {}
            AI_player["AI Underwater"][i][j]["Presence"] = None
            AI_underwater_cell = Button(redraw_gameboard, 
                                        height = 2, 
                                        width = 4,
                                        highlightbackground='white',
                                        command=lambda row=i, column=j, depth = 0: shoot(row, column, depth))
            AI_underwater_cell.grid(row=i, column=j)
    
    for i in range(12, 22):
        AI_player["AI Surface"][i] = {}
        for j in range(11, 21):
            AI_player["AI Surface"][i][j] = {}
            AI_player["AI Surface"][i][j]["Presence"] = None
            AI_surface_cell = Button(redraw_gameboard, 
                                     height = 2, 
                                     width = 4, 
                                     highlightbackground='white',
                                     command=lambda row=i, column=j, depth = 1: shoot(row, column, depth))
            
            AI_surface_cell.grid(row=i, column=j)
            
    

    redraw_gameboard.mainloop()
    #return AI_surface_cell, AI_underwater_cell, player_surface_cell, player_underwater_cell
    #referee()