#Programming Final Game --> Evelyn Chennault, Josy Ramirez, Maisha Paredes, and Zoey Sosa. Python

import random  # For the computer's random moves  (evelyn) 
 
def display_board(board):    #josy did this board, and each print statement
    print("BOARD:")    
    print(" | ".join(board[0:3]))    
    print("-" * 9)    
    print(" | ".join(board[3:6]))    
    print("-" * 9)    
    print(" | ".join(board[6:9]))    
 
def check_win(board, player):   #EVELYN completed the winning combos
    winning_combinations = [    
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  #row wins  (evelyn)
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Column wins combos   (evelyn)
        [0, 4, 8], [2, 4, 6]              #diagonal winning combos (evelyn)
    ]    
    for combo in winning_combinations:    #josy completed these conditionals and boolean statements
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:    
            return True   
    return False    
 
def computer(board):     #zoey completed this computer function that creates the computer that will do random moves in empty spaces
    empty_spaces = [i for i in range(9) if board[i] == " "]    
    return random.choice(empty_spaces)    
 
def play_game():      #josy worked together on this function
    board = [" " for _ in range(9)]  #initializing the board, and saying intructions, (evelyn)    
    print("Welcome to Tic Tac Toe! Here's how to play--\nYou will take turns typing in a slot number to place your character.\n")    
    print("You will be player X. Let's begin!\n")    
 
    player = "X"  #this value ensures the user is always player X   (josy did this)
    computer_player = "O"  #this ensures the computer is always Player O  (josy did this)
 
    while True:    #maisha did this and EVELYN worked on this section together (all below until the except value error)
        display_board(board)  #this displays the current board, maisha did this
        print(f"\nPlayer {player}'s turn.")    
 
        while True:  #this is a loop for the player input maisha  did this
            user_input = input("Enter a number from 0 to 8!!: ")    
            try:    
                move = int(user_input)  #this converts to an integer maisha and evelyn worked out errors togther here, took a while
                if move < 0 or move > 8:    
                    print("Invalid move man! You gotta enter a number between 0 and 8.")    #maisha did some of these conditionals and print statements as well as evelyn
                elif board[move] != " ":    
                    print("That cell is already taken! Choose another.")    
                else:    
                    break  #this is the loop (maisha)
            except ValueError:    
                print("Invalid input! Please enter a valid number!")  #this catches any inputs that arent numbers maisha did this 
 
        board[move] = player  #user's move  (zoey worked on this section, josy did a small bit here too)
 
        #this checks for a win or tie after the users move (zoey did this)
        if check_win(board, player):    # 
            display_board(board)  #board before announcing the winner  zoey did this
            print(f"Congrats and good for you, {player}! You are the winner, and there's no trophy but your opponents frown!")    
            break  #this stops the game if the player wins (zoey did this)
         
        if " " not in board:  #checks for a tie (zoey)
            display_board(board)  #board before announcing the tie    
            print("Oh! Looks like it's a tie!")    
            break  #(zoey Stopping game if it's a tie    
 
        # Computer's turn    #(josy did all below but zoey worked a bit on this part below too)
        move = computer(board)  # Computer makes a move    
        board[move] = computer_player  # Updating board with computer's move    
        print(f"Computer's move is at position {move}.")

        # Check for win after computer's move  # (josy did this )
        if check_win(board, computer_player):   
            display_board(board)  # Show the board before announcing the winner    
            print(f"Congratulations, {computer_player}! You are the winner!")  # Announce winner    
            break  # Stop the game if the computer wins    
     
play_game()  #this starts the game 