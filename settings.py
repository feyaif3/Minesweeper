from tkinter import Button
import random

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
            font = ("Arial", 15), 
        )
        button.bind("<Button-1>", self.left_click)
        button.bind("<Button-2>", self.right_click)
        self.cell_button = button
    
    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
            
    def get_cell_by_position(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    
    @property        
    def surrounded_cells(self):
        cells = [
        self.get_cell_by_position(self.x - 1, self.y - 1),
        self.get_cell_by_position(self.x - 1, self.y),
        self.get_cell_by_position(self.x - 1, self.y + 1),
        self.get_cell_by_position(self.x, self.y - 1),
        self.get_cell_by_position(self.x, self.y + 1),
        self.get_cell_by_position(self.x + 1, self.y - 1),
        self.get_cell_by_position(self.x + 1, self.y),
        self.get_cell_by_position(self.x + 1, self.y + 1),
        ]
        
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surrounded_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter
            
    def show_cell(self):
        self.cell_button.configure(text=self.surrounded_mines_length)
      
            
    def show_mine(self):
        self.cell_button["text"] = "X"
        self.cell_button["bg"] = "red"
        
    def right_click(self, event):
        print(event)
        print("Right Clicked")
        
    @staticmethod
    def randomise_mines():
        picked_cells = random.sample(Cell.all, 10)
        for cell in picked_cells:
            cell.is_mine = True
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"