from tkinter import *
import settings

# Create the root window
root = Tk()
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper")
root.resizable(False, False)

#Framing the window
top_frame = Frame(root, bg="red", width=settings.WIDTH, height=settings.height_percentage(25))
top_frame.place(x=0, y=0)

left_frame = Frame(root, bg="blue", width=settings.width_percentage(25), height=settings.height_percentage(75))
left_frame.place(x=0, y=settings.height_percentage(25))

game_frame = Frame(root, bg="green", width=settings.width_percentage(75), height=settings.height_percentage(75))
game_frame.place(x=settings.width_percentage(25), y=settings.height_percentage(25))

#Run the window
root.mainloop()
