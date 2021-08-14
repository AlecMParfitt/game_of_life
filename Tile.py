'''
Tile class for main.py
'''
from tkinter import PhotoImage

class Tile:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = False

    def switch(self):
        self.status = not self.status

    def live(self):
        self.status = True

    def die(self):
        self.status = False

    def get_status(self):
        return self.status

    def get_image(self):
        if self.status:
            return PhotoImage(file="filled_tile.gif")
        else:
            return PhotoImage(file="empty_tile.gif")
