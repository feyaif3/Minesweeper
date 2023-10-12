from tkinter import Button

WIDTH = 1440
HEIGHT = 720

def height_percentage(percentage):
    return (HEIGHT / 100) * percentage

def width_percentage(percentage):
    return (WIDTH / 100) * percentage

class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_button = None
        
    def create_button(self, location):
        button = Button(
            location,
            text="Text",
        )
        button.bind("<Button-1>", self.left_click)
        self.cell_button = button
    
    def left_click(self, event):
        print("Left Clicked")