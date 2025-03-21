# Programming Final Game, Evelyn, Josy, Maisha, and Zoey S.

# Initialize the board  (Josy)
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
    player = "X" if turn % 2 == 0 else "O"  # Alternate players  
    make_move(player)  
  
display_board()  # Show final board  


  while True:
      print (board)
      print(f"Player {current_player}'s turn.")

      if current_player == "X":
          while True:
              move = int(input("Enter your move (0-8): "))
              if 0 <= move <= 8 and ttt_board[move] == " ":
                  ttt_board[move] = current_player
                  break
              else:
                  print("Invalid move. Try again.")
      else:
          move = computer(ttt_board)
          ttt_board[move] = current_player
          print(f"Computer's move: {move + 1}")

      if check_win(ttt_board, current_player):
          print_board(ttt_board)
          print(f"Player {current_player} wins!")
          break

      if " " not in ttt_board:
          print_board(ttt_board)
          print("It's a tie!")
          break

      current_player = "O" if current_player == "X" else "X"