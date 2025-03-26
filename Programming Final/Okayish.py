#Programming Final Game --> Evelyn Chennault, Josy Ramirez, Maisha Paredes, and Zoey Sosa. Python

import random  # For the computer's random moves  
  
def display_board(board):  
    print("BOARD:")  
    print(" | ".join(board[0:3]))  #josy did this board, and each print statement
    print("-" * 9)  
    print(" | ".join(board[3:6]))  
    print("-" * 9)  
    print(" | ".join(board[6:9]))  
  
def check_win(board, player):  
    winning_combinations = [  
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Row wins  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Column wins  
        [0, 4, 8], [2, 4, 6]              # Diagonal wins  (Evelyn did this)
    ]  
    for combo in winning_combinations:  
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:  
            return True  
    return False  
  
def computer(board):  
    empty_spaces = [i for i in range(9) if board[i] == " "]  #zoey completed this computer function
    return random.choice(empty_spaces)  
  
def play_game():  
    board = [" " for _ in range(9)]  # Initialize the board  
    print("Welcome to Tic Tac Toe!\n")  
    print("You will be player X. Let's begin!\n")  
      
    player = "X"  # Starting player  
  
    while True: # Evenlyn and Zoey worked on this
        display_board(board)  # Show current board  
        print("Player " + player + "'s turn.")  
  
        while True:  # Inner loop for input validation  
            user_input = input("Enter a number from 0 to 8: ")  
            try:  
                move = int(user_input)  # Convert to integer  
                if move < 0 or move > 8:  
                    print("Invalid move! Please enter a number between 0 and 8.")  
                elif board[move] != " ":  
                    print("That cell is already taken! Choose another.")  
                else:  
                    break  # Valid move, exit the loop  
            except ValueError:  
                print("Invalid input! Please enter a valid number.")  
          
        board[move] = player  # Valid move  
  
        if check_win(board, player):  # Check for a win  # Maisha did this 
            display_board(board)  # Show the board before announcing the winner  
            print("Congratulations, " + player + "! You are the winner!")  
            break  # Stop the game if the player wins  
  
        if " " not in board:  # Check for a tie  # Maisha did this 
            display_board(board)  # Show the board before announcing the tie  
            print("Oh! Looks like it's a tie!")  
            break  # Stop the game if it's a tie  
  
        # Switch to computer's turn  # josy did this
        player = "O" if player == "X" else "X"  # Switch player  
        move = computer(board)  # Computer makes a move  
        board[move] = player  # Update board with computer's move  
        print("Computer's move is at position " + str(move) + ".")  # Announce computer's move  
  
        if check_win(board, player):  # Check for a win  (josy did this)
            display_board(board)  # Show the board before announcing the winner  
            print("Congratulations, " + player + "! You are the winner!")  # Announce winner  
            break  # Stop the game if the computer wins  
