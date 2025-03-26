#Programming Final Game --> Evelyn Chennault, Josy Ramirez, Maisha Paredes, and Zoey Sosa. Python

import random  # For the computer's random moves  
  
def display_board(board):  
    print("BOARD:")  
    print(" | ".join(board[0:3]))  
    print("-" * 9)  
    print(" | ".join(board[3:6]))  
    print("-" * 9)  
    print(" | ".join(board[6:9]))  
  
def check_win(board, player):  
    winning_combinations = [  
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Row wins  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Column wins  
        [0, 4, 8], [2, 4, 6]              # Diagonal wins  
    ]  
    for combo in winning_combinations:  
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:  
            return True  
    return False  
  
def computer(board):  
    empty_spaces = [i for i in range(9) if board[i] == " "]  
    return random.choice(empty_spaces)  
  
def play_game():  
    board = [" " for _ in range(9)]  # Initialize the board  
    print("Welcome to Tic Tac Toe!\n")  
    print("You will be player X. Let's begin!\n")  
  
    player = "X"  # Starting player  
  
    while True:  
        display_board(board)  # Show current board  
        print(f"\nPlayer {player}'s turn.")  
  
        # Player move  
        move = int(input("Enter a number from 0 to 8: "))      
        if move < 0 or move > 8 or board[move] != " ":      
            print("Invalid move! Try again.")  
            continue  # Restart the loop for a valid move  
  
        board[move] = player  # Valid move  
  
        if check_win(board, player):  # Check for a win  
            display_board(board)  # Show the board before announcing the winner  
            print(f"Player {player} is the winner!")  
            break  # Stop the game if the player wins  
  
        if " " not in board:  # Check for a tie  
            display_board(board)  # Show the board before announcing the tie  
            print("Oh! Looks like it's a tie!")  
            break  # Stop the game if it's a tie  
  
        # Switch to computer's turn  
        player = "O" if player == "X" else "X"  # Switch player  
        move = computer(board)  # Computer makes a move  
        board[move] = player  # Update board with computer's move  
        print(f"Computer's move: {move}")  
  
        if check_win(board, player):  # Check for a win  
            display_board(board)  # Show the board before announcing the winner  
            print(f"Player {player} is the winner!")  
            break  # Stop the game if the computer wins  
  
# Start the game  
play_game()  
