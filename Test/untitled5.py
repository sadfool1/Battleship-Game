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

# Preparing a spacing between the two grids
Label(redraw_gameboard, text="", height = 20, width = 4).grid(row=1, column=10, rowspan=10)

for i in range(1, 11):
    Player["Player Underwater"][i] = {}
    for j in range(10):
        Player["Player Underwater"][i][j] = {}
        Player["Player Underwater"][i][j]["Presence"] = None
        player_underwater_cell = Button(redraw_gameboard, 
                                        height = 2, 
                                        width = 4, 
                                        command=cannot_shoot)
        player_underwater_cell.grid(row=i, column=j)
        
for i in range(1, 11):
    Player["Player Surface"][i] = {}
    for j in range(11, 21):
        Player["Player Surface"][i][j] = {}
        Player["Player Surface"][i][j]["Presence"] = None
        player_surface_cell = Button(redraw_gameboard, 
                                     height = 2, 
                                     width = 4, 
                                     command=cannot_shoot)
        player_surface_cell.grid(row=i, column=j) 
        
Label(redraw_gameboard, text="AI Underwater", height = 3, width = 40).grid(row=11, column=0, columnspan=10)
Label(redraw_gameboard, text="AI Surface", height = 3, width = 40).grid(row=11, column=11, columnspan=10)

Label(redraw_gameboard, text="", height = 4, width = 1).grid(row=11, column=0, columnspan=10)

        
for i in range(12, 22):
    AI_player["AI Underwater"][i] = {}
    for j in range(10):
        AI_player["AI Underwater"][i][j] = {}
        AI_player["AI Underwater"][i][j]["Presence"] = None
        AI_underwater_cell = Button(redraw_gameboard, 
                                    height = 2, 
                                    width = 4, 
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
                                 command=lambda row=i, column=j, depth = 1: shoot(row, column, depth))
        
        AI_surface_cell.grid(row=i, column=j) 

