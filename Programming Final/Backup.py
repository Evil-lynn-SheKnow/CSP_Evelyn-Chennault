#Programming Final Game --> Evelyn Chennault, Josy Ramirez, Maisha Paredes, and Zoey Sosa. Python

import random    #evelyn did the import random, this will help for the computer
print("Welcome to a game of tic-tac-toe!\n")
  
def display_board(board):    #josy did this board, and each print statement
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
  
def play_game():    #zoey and josy worked together on this function
    print("Here's how to play--\nYou will take turns typing in a slot number to place your character.\n") #Evelyn: descrption and how-to-play
    print("You will be player X. \nLet's begin!\n")
    board = [" " for _ in range(9)]    #starting the player off(josy)
    player = "X"     
    
    while True:    #<-- maisha
        display_board(board)     
        print(f"\nPlayer {player}'s turn.")    #<--maisha and josy
    
    
    while True:  
        move = int(input("Enter a number from 0 to 8:"))  # Get input here  
      
        if move < 0 or move > 8:  
            print("Invalid move! Choose a number between 0 and 8.")  
        elif board[move] != " ":  
            print("This cell is already taken. Try again.")  
        else:  
            board[move] = player  # Valid move  
      break  # Exit the loop

                else:    
                    print("This cell already taken, you have to try again.")    
                continue    # these conditionals make sure the player does not take a square to do a move in a place they cannot go (maisha) 
        else:
            move = computer(board)    
            board[move] = player    
            print(f"Computer's move: {move}")    
    
        if check_win(board, player):    #this conditional checks for a win (maisha)
            display_board(board)    
            print(f"Player {player} is the winner!")    
            break    #this break statement stops the game if the player wins. (maisha)
        if " " not in board:    
            display_board(board)    
            print("Oh! Looks like it's a tie!")    
            break    
    
        player = "O" if player == "X" else "X"    
    
#Start the game    
play_game()  