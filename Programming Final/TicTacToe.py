#Programming Final Game, Evelyn, Josy, Maisha, and Zoey S.

# Initialize the board  
board = [  
    [0, 0, 0],  
    [0, 0, 0],  
    [0, 0, 0]  
]  
  
def display_board():  
    for row in board:  
        print(" | ".join(str(x) for x in row))  
        print("-" * 9)  
  
def make_move(player):  
    row = int(input(f"Player {player}, enter the row (0, 1, or 2): "))  
    col = int(input(f"Player {player}, enter the column (0, 1, or 2): "))  
      
    if board[row][col] == 0:  # Check if the cell is empty  
        board[row][col] = player  # Update the board  
    else:  
        print("Cell already taken! Try again.")  
        make_move(player)  # Ask again if the cell is taken  
  
# Example game loop  
for turn in range(9):  # Maximum 9 moves  
    display_board()  
    player = 1 if turn % 2 == 0 else 2  # Alternate players  
    make_move(player)  
  
display_board()  # Show final board  
