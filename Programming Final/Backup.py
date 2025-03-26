#Programming Final Game --> Evelyn Chennault, Josy Ramirez, Maisha Paredes, and Zoey Sosa. Python

import random    #evelyn did the import random, this will help for the computer
print("Welcome to a game of tic-tac-toe!\n")
  
def display_board(board):  
    print("Debug: Inside display_board function.")  # Check if this prints  
    print("BOARD:")  
    print(" | ".join(board[0:3]))  
    print("-" * 9)  
    print(" | ".join(board[3:6]))  
    print("-" * 9)  
    print(" | ".join(board[6:9]))  


#Evelyn Chennault completeted these winning combinations
def check_win(board, player):   
    winning_combinations = [    
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  #row wins    at should i
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  #the columnn wins  
        [0, 4, 8], [2, 4, 6]              #diagonal wins  
    ]    
    for combo in winning_combinations:    #josy completed these conditionals and boolean statements
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:    
            return True    
    return False    
  
def computer(board):   #zoey completed this computer function that creates the computer that will do random moves in empty spaces
    empty_spaces = [i for i in range(9) if board[i] == " "]    
    return random.choice(empty_spaces)    #computer will make a random choice (zoey)
  
def play_game():  
    board = [" " for _ in range(9)]
    print("Here's how to play--\nYou will take turns typing in a slot number to place your character.\n")  
    print("You will be player X. \nLet's begin!\n")  
    board = [" " for _ in range(9)]  # Initialize the board  
    player = "X"  
  
    while True:  # Main game loop  
        print("Debug: Displaying the board now.")  # Debugging statement  
        display_board(board)  # Show the current board  
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
          
        player = "O" if player == "X" else "X"  # Switch player  
  
        # Computer move  
        move = computer(board)  # Assume computer function is defined  
        board[move] = player  # Computer makes a move  
        print(f"Computer's move: {move}")  
  
        if check_win(board, player):  # Check for a win  
            display_board(board)  # Show the board before announcing the winner  
            print(f"Player {player} is the winner!")  
            break  # Stop the game if the computer wins  

 