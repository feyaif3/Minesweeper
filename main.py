from tkinter import *
from settings import Cell
import settings

# Create the root window
root = Tk()
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper")
root.resizable(False, False)

#Framing the window
top_frame = Frame(root, bg="black", width=settings.WIDTH, height=settings.height_percentage(25))
top_frame.place(x=0, y=0)

left_frame = Frame(root, bg="black", width=settings.width_percentage(25), height=settings.height_percentage(75))
left_frame.place(x=0, y=settings.height_percentage(25))

game_frame = Frame(root, bg="black", width=settings.width_percentage(75), height=settings.height_percentage(75))
game_frame.place(x=settings.width_percentage(25), y=settings.height_percentage(25))

#Button Placement
for x in range(6):
    for y in range(6):
        c = Cell(x, y)
        c.create_button(game_frame)
        c.cell_button.grid(column=x, row=y)


#Call the label from the cell class
Cell.create_cell_counter_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomise_mines()

#Run the window
root.mainloop()
