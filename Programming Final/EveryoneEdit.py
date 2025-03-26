# Programming Final Game --> Evelyn Chennault, Josy Ramirez, Maisha Paredes, and Zoey Sosa. Python

import random    
print("Welcome to a game of tic-tac-toe!\n")
  
def display_board(board):    
    print("Current Board:")    
    print(" | ".join(board[0:3]))    
    print("-" * 9)    
    print(" | ".join(board[3:6]))    
    print("-" * 9)    
    print(" | ".join(board[6:9]))    
  
def check_win(board, player):   
    winning_combinations = [    
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Row wins    
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Column wins  
        [0, 4, 8], [2, 4, 6]               # Diagonal wins  
    ]    
    for combo in winning_combinations:    
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:    
            return True    
    return False    
  
def computer(board):    
    empty_spaces = [i for i in range(9) if board[i] == " "]    
    return random.choice(empty_spaces)    
  
def play_game():    
    print("Welcome to Tic Tac Toe!")    #evelyn did descrption 
    board = [" " for _ in range(9)]    
    player = "X"  # Starting player    
    
    while True:    
        display_board(board)     
        print(f"Player {player}'s turn.")    
    
        if player == "X":    
            move = int(input("Enter your move (0-8): "))    
            while move >= 0 or move <= 8:
                if board[move] == " ":    
                    board[move] = player    
                else:    
                    print("Cell already taken! Try again.")    
                break    
        else:    
            move = computer(board)    
            board[move] = player    
            print(f"Computer's move: {move}")    
    
        if check_win(board, player):    
            display_board(board)    
            print(f"Player {player} wins!")    
            break    
        if " " not in board:    
            display_board(board)    
            print("It's a tie!")    
            break    
    
        player = "O" if player == "X" else "X"    
    
# Start the game    
play_game()  
