from tkinter import Button

WIDTH = 1440
HEIGHT = 720

def height_percentage(percentage):
    return (HEIGHT / 100) * percentage

def width_percentage(percentage):
    return (WIDTH / 100) * percentage

class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_button = None
        self.x = x
        self.y = y
        
        Cell.all.append(self)
        
    def create_button(self, location):
        button = Button(
            location,
            width=12,
            height=4,
            text=f"{self.x}, {self.y}",
        )
        button.bind("<Button-1>", self.left_click)
        button.bind("<Button-2>", self.right_click)
        self.cell_button = button
    
    def left_click(self, event):
        print(event)
        print("Left Clicked")
        
    def right_click(self, event):
        print(event)
        print("Right Clicked")
        
    @staticmethod
    def randomise_mines():
        pass
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"