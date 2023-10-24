from tkinter import Button, Label
import random

WIDTH = 1440
HEIGHT = 720
GRID_SIZE = 6
CELL_COUNT = GRID_SIZE ** 2

def height_percentage(percentage):
    return (HEIGHT / 100) * percentage


def width_percentage(percentage):
    return (WIDTH / 100) * percentage

class Cell:
    all = []
    cell_count = CELL_COUNT
    cell_count_label_object = None
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
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
        button.bind("<Button-1>", self.left_click)#Left click
        button.bind("<Button-2>", self.right_click)#Right click
        self.cell_button = button
    
    @staticmethod
    def create_cell_counter_label(location):
        label = Label(
            location,
            bg="black",
            fg="white",
            text=f"Cells Left:{Cell.cell_count}",
            width=12,
            height=4,
            font=("Arial", 30),
        )
        Cell.cell_count_label_object = label
        
    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_mines_length == 0:
                for cell in self.surrounded_cells:
                    cell.show_cell()
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
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_button.configure(text=self.surrounded_mines_length)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Squares Left:{Cell.cell_count}")
        self.is_opened = True
      
            
    def show_mine(self):
        self.cell_button.configure(text="*", bg="red")
        
        
    def right_click(self, event):
        if not self.is_mine_candidate:
            self.cell_button.configure(bg="yellow", text="?")
            self.is_mine_candidate = True
        else:
            self.cell_button.configure(bg="SystemButtonFace", text="")
            self.is_mine_candidate = False

        
    @staticmethod
    def randomise_mines():
        picked_cells = random.sample(Cell.all, 10)
        for cell in picked_cells:
            cell.is_mine = True
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"