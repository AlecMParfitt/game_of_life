'''
simple implementation of Conway's Game of Life

Rules:
    1. any dead cell with exactly 3 live neighbors comes to life
    2. any live cell with <2 or >3 live neighbors dies

@author Alec Parfitt

'''


from tkinter import *
from Tile import Tile
from functools import partial
import time
tiles = {}
widgets = {}

def make_key(x,y):
    """
    function to combine two coordinates into a valid dict key
    """
    return f'{x}, {y}'

def check_neighbors(x,y):
    """
    checks the grid around a tile at given x, y coords. Tkinter grid is laid out
    like quadrant IV of a graph
    """
    total = 0
    locations = {
        'ul' : make_key(x-1, y-1),
        'um' : make_key(x, y-1),
        'ur' : make_key(x+1, y-1),
        'ml' : make_key(x-1, y),
        'mr' : make_key(x+1, y),
        'bl' : make_key(x-1, y+1),
        'bm' : make_key(x, y+1),
        'br' : make_key(x+1, y+1),
    }
    for i in locations.keys():
        try:
            if tiles[locations[i]].get_status():
                total += 1
        except KeyError:
            pass
    return total



def cycle_board():
    """
    Definition for 1 round of the game of life. weighted_board is a dict<coord, num_neighbors>
    for all positions on the board. This dict is used to redraw the board quickly. Tkinter
    buttons must be redefined in order for changes to be reflected.
    """
    weighted_board = {}
    for key in tiles.keys():
        x, y = tiles[key].x, tiles[key].y
        neighbors = check_neighbors(x,y)

        if tiles[key].get_status():
            print(key, neighbors)
        weighted_board[key] = neighbors

    for key in tiles.keys():
        click_with_self = partial(click_tile, tiles[key])
        x, y = tiles[key].x, tiles[key].y
        if weighted_board[key] == 3 and not tiles[key].get_status():
            tiles[key].live()
            Button(window, image=filled_tile, bg="grey", command=click_with_self).grid(row=y,column=x,sticky=E)
        if tiles[key].get_status() and (weighted_board[key] < 2 or weighted_board[key] > 3):
            tiles[key].die()
            Button(window, image=empty_tile, bg="grey", command=click_with_self).grid(row=y,column=x,sticky=E)
    window.update()


#key down function
def start_click():
    """
    Key down function for beginning the game of life. proceeds through i rounds of the game
    """
    print('starting life...')
    i = 50
    while i > 0:
        time.sleep(.25)
        print(i)
        i -= 1
        cycle_board()
    for key, value in tiles.items():
        print(key, value)

def click_tile(tile):
    """
    key down function for a tile being clicked. When the tile is clicked, it is set to its
    opposite state and the button image is switched. filled == alive; empty == dead
    """
    key = f'{tile.x}, {tile.y}'
    tiles[key].switch()
    click_with_self = partial(click_tile, tiles[key])

    if tiles[key].get_status():
        Button(window, image=filled_tile, bg="grey", command=click_with_self).grid(row=tile.y,column=tile.x,sticky=E)
    else:
        Button(window, image=empty_tile, bg="grey", command=click_with_self).grid(row=tile.y,column=tile.x,sticky=E)
    print(key, ':', tiles[key].get_status(), check_neighbors(tiles[key].x, tiles[key].y))

def draw_board(width, height):
    for i in range(width):
    for j in range(height):
        coords = f'{i}, {j}'
        tiles[coords] = Tile(i, j)
        click_with_self = partial(click_tile, tiles[coords])
        if tiles[coords].get_status():
            Button(window, image=filled_tile, bg="grey", command=click_with_self).grid(row=j,column=i,sticky=E)
        else:
            Button(window, image=empty_tile, bg="grey", command=click_with_self).grid(row=j,column=i,sticky=E)

window = Tk()
window.title("Conway's Game of Life")

filled_tile = PhotoImage(file="filled_tile.gif")
empty_tile = PhotoImage(file="empty_tile.gif")
window.configure(background = "black")

# Initialize board
width, height = 10, 10

# TODO: replace with draw_board()
for i in range(width):
    for j in range(height):
        coords = f'{i}, {j}'
        tiles[coords] = Tile(i, j)
        click_with_self = partial(click_tile, tiles[coords])
        if tiles[coords].get_status():
            Button(window, image=filled_tile, bg="grey", command=click_with_self).grid(row=j,column=i,sticky=E)
        else:
            Button(window, image=empty_tile, bg="grey", command=click_with_self).grid(row=j,column=i,sticky=E)
#################################################################################################################

# start button
Button(window, text="start", width=7, command=start_click).grid(row=y//2, column=x, sticky=S)

window.mainloop()
