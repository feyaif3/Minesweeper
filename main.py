from tkinter import *

# Create the root window
root = Tk()
root.configure(bg="black")
root.geometry("1440x720")
root.title("Minesweeper")
root.resizable(False, False)

#Framing the window
top_frame = Frame(root, bg="red", width=1440, height=180)
top_frame.place(x=0, y=0)

left_frame = Frame(root, bg="blue", width=360, height=540)
left_frame.place(x=0, y=180)




#Run the window
root.mainloop()
