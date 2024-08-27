import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Variables to track the game state
current_player = "X"
buttons = []
game_over = False

# Function to reset the game
def reset_game():
    global current_player, game_over
    current_player = "X"
    game_over = False
    for button in buttons:
        button["text"] = ""
        button["state"] = tk.NORMAL

# Function to check for a win or draw
def check_winner():
    global game_over
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    
    for condition in win_conditions:
        if buttons[condition[0]]["text"] == buttons[condition[1]]["text"] == buttons[condition[2]]["text"] != "":
            for i in condition:
                buttons[i].config(bg="lightgreen")  # Highlight the winning combination
            game_over = True
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            return

    # Check for a draw
    if all(button["text"] != "" for button in buttons):
        game_over = True
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        return

# Function to handle a button click
def on_button_click(i):
    global current_player
    if not game_over and buttons[i]["text"] == "":
        buttons[i]["text"] = current_player
        check_winner()
        current_player = "O" if current_player == "X" else "X"

# Create the Tic Tac Toe grid (3x3)
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 40), width=5, height=2, command=lambda i=i: on_button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Add a reset button
reset_button = tk.Button(root, text="Reset", font=("Arial", 20), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

# Run the main loop
root.mainloop()
