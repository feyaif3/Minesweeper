import tkinter as tk
import random

def create_board(rows, cols, num_mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    # Place mines
    for _ in range(num_mines):
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        while board[row][col] == 'X':
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        board[row][col] = 'X'

    # Calculate numbers
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'X':
                continue
            count = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols:
                        count += board[r + dr][c + dc] == 'X'
            if count > 0:
                board[r][c] = str(count)

    return board

def reveal_safe_cells(board, reveal, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board[0]) and not reveal[row][col]:
        reveal[row][col] = True
        if board[row][col] == ' ':
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    reveal_safe_cells(board, reveal, row + dr, col + dc)

def on_cell_click(row, col):
    global game_over

    if not game_over and not reveal[row][col]:
        if board[row][col] == 'X':
            game_over = True
            label.config(text='Game Over! You hit a mine!')
        else:
            reveal_safe_cells(board, reveal, row, col)
            if all(all(reveal[r][c] or board[r][c] == 'X' for c in range(cols)) for r in range(rows)):
                game_over = True
                label.config(text='Congratulations! You win!')
        draw_board()

def draw_board():
    for r in range(rows):
        for c in range(cols):
            cell = board[r][c]
            if reveal[r][c]:
                buttons[r][c].config(text=cell, state='disabled')
            else:
                buttons[r][c].config(text=' ', state='normal')

# Initialize the game
rows, cols, num_mines = 10, 10, 20
board = create_board(rows, cols, num_mines)
reveal = [[False for _ in range(cols)] for _ in range(rows)]
game_over = False

# Create the GUI
root = tk.Tk()
root.title('Minesweeper')
buttons = [[None for _ in range(cols)] for _ in range(rows)]
for r in range(rows):
    for c in range(cols):
        buttons[r][c] = tk.Button(root, text=' ', width=2, height=1, command=lambda r=r, c=c: on_cell_click(r, c))
        buttons[r][c].grid(row=r, column=c)
label = tk.Label(root, text='')
label.grid(row=rows, columnspan=cols)

root.mainloop()
