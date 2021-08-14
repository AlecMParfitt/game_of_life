'''
simple implementation of Conway's Game of Life

@author Alec Parfitt

'''


from tkinter import *
from Tile import Tile
from functools import partial
import time
tiles = {}
widgets = {}

def make_key(x,y):
    return f'{x}, {y}'

def check_neighbors(x,y):
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
    weighted_board = {}
    for key in tiles.keys():
        x, y = tiles[key].x, tiles[key].y
        neighbors = check_neighbors(x,y)

        if tiles[key].get_status():
            print(key, neighbors)
        weighted_board[key] = neighbors

    for key in tiles.keys():
        y, x = tiles[key].x, tiles[key].y
        if weighted_board[key] == 3 and not tiles[key].get_status():
            tiles[key].live()
            Button(window, image=filled_tile, bg="grey", command=click_with_self).grid(row=x,column=y,sticky=E)
        if tiles[key].get_status() and (weighted_board[key] < 2 or weighted_board[key] > 3):
            tiles[key].die()
            Button(window, image=empty_tile, bg="grey", command=click_with_self).grid(row=x,column=y,sticky=E)
    window.update()


#key down function
def start_click():
    print('starting life...')
    i = 500
    while i > 0:
        time.sleep(.25)
        print(i)
        i -= 1
        cycle_board()
    for key, value in tiles.items():
        print(key, value)

def click_tile(tile):
    key = f'{tile.x}, {tile.y}'
    tiles[key].switch()
    click_with_self = partial(click_tile, tiles[key])

    if tiles[key].get_status():
        Button(window, image=filled_tile, bg="grey", command=click_with_self).grid(row=tile.y,column=tile.x,sticky=E)
    else:
        Button(window, image=empty_tile, bg="grey", command=click_with_self).grid(row=tile.y,column=tile.x,sticky=E)
    print(key, ':', tiles[key].get_status(), check_neighbors(tiles[key].x, tiles[key].y))




window = Tk()
window.title("Conway's Game of Life")

filled_tile = PhotoImage(file="filled_tile.gif")
empty_tile = PhotoImage(file="empty_tile.gif")
window.configure(background = "black")

# Initialize board
x, y = 10, 10

for i in range(x):
    for j in range(y):
        coords = f'{i}, {j}'
        tiles[coords] = Tile(i, j)
        click_with_self = partial(click_tile, tiles[coords])
        if tiles[coords].get_status():
            Button(window, image=filled_tile, bg="grey", command=click_with_self).grid(row=j,column=i,sticky=E)
        else:
            Button(window, image=empty_tile, bg="grey", command=click_with_self).grid(row=j,column=i,sticky=E)
#################################################################################################

Button(window, text="start", width=7, command=start_click).grid(row=y//2, column=x, sticky=S)




window.mainloop()
