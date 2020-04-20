#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:44:00 2020

@author: jameselijah
"""

'''
Program Name: battleship_game_no_self_import

Description: This file/module contains all the work done from login to ship
placement in a long chain, so as to avoid any problems involved in importing
functions from other python files.

This is really long, so be prepared.
'''
import tkinter as tk 
from tkinter import *
from tkinter import messagebox 
import os 
from random import randint
import random

Player = {'Carrier':[(1, 11, 1), (1, 12, 1), (1, 13, 1), (1, 14, 1)], 'Submarine': [(1, 0, 0), (1, 1, 0), (1, 2, 0)]}

AI_player = {'Carrier':[(12,12,1), (12,13,1), (12,14,1), (12,15,1)], 'Submarine': [(12,0,0), (12,1,0), (12,2,0)]}

AI_counter = 0
Player_counter = 0 

def redraw_boards():
    global redraw_gameboard
    global Player
    global AI_player
    
    print (Player)
    print (AI_player)
    
    Player["Player Surface"] = {}
    Player["Player Underwater"] = {}
    AI_player["AI Surface"] = {}
    AI_player["AI Underwater"] = {}
    
    redraw_gameboard = Tk()
    redraw_gameboard.title("Battleship Game")
    redraw_gameboard.geometry("1080x1240")
    redraw_gameboard.resizable(True, True)
    
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
            Player["Player Underwater"][i][j]["REF"] = None
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
            Player["Player Surface"][i][j]["REF"] = None
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
            AI_player["AI Underwater"][i][j]["REF"] = None
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
            AI_player["AI Surface"][i][j]["REF"] = None
            AI_surface_cell = Button(redraw_gameboard, 
                                     height = 2, 
                                     width = 4, 
                                     highlightbackground='white',
                                     command=lambda row=i, column=j, depth = 1: shoot(row, column, depth))
            
            AI_surface_cell.grid(row=i, column=j)
            
    

    redraw_gameboard.mainloop()

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


def End_prompt():
    
    global End_prompt
    End_prompt = Tk()
    End_prompt.title("You Won the Game")
    End_prompt.geometry("250x250")
    End_prompt.resizable(False, False)
    
    play_again = Button(End_prompt, 
                        height = 2, 
                        width = 10, 
                        command=redraw_boards,
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
    
    


def play_again ():
    global redraw_gameboard
    global End_prompt
    
    redraw_gameboard.destroy()
    End_prompt.destroy()
    
    
def quit_battleship():
    global redraw_gameboard
    global End_prompt
    
    End_prompt.destroy()
    redraw_gameboard.destroy()
    
    
    

def draw_new_button_hit(row, column):
    
    """
    ==========================
    RE DRAW NEW BUTTON FOR HIT
    ==========================
    """
    
    global redraw_gameboard  
    new_button = Button(redraw_gameboard, 
                        height = 2, 
                        width = 4, 
                        command= already_shot,
                        highlightbackground='red')
    
    new_button.grid(row = row, column = column)


def draw_new_button_miss(row, column):
    
    global redraw_gameboard

    new_button = Button(redraw_gameboard, 
                        height = 2, 
                        width = 4, 
                        command= already_shot,
                        highlightbackground='black')
    
    new_button.grid(row = row, column = column)


    
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
    
    print ("Player counter = %d | AI counter = %d." % (Player_counter, AI_counter))
    
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
