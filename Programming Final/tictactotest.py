import random  
  #Programming Final Game, Evelyn, Josy, Maisha Paredes, and Zoey Sosa.

            
def display_board(board):  
    # Code to display the board  
     print("Welcome to our game of tic tac toe!") 
    #controls players turns and establishes the b
board = [    
    [1, 2, 3],    
    [4, 5, 6],    
    [7, 8, 9]    
]      
  
def check_win(board, player):  
  #josy (the winning combinations, all the combos the user can do to win)
    winning_combinations = [  
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],  # function called
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9], #some tweaks on the numbers (zoey)
        [3, 5, 7] 
    ]  
    for combo in winning_combinations:  
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:  
            return True  
    return False  

  
def computer(board):  
    # Code for the computer's move  
    empty_spaces = [i for i in range(9) if board[i] == " "]
  return random.choice(empty_spaces)


def play_game():#zoey worked on these functions 
  print("This is a Tic tac toe game. It is just like a normal game of Tic tac toe the difference is\ninstead of writing the X you would type in a number (0-8) to\nplace the X left to right and so on \nthis is for each of the rows.")


  board = [" " for _ in range(9)]
  player = "X"
  while True: #
      print (board)
      print(f"Player {player}'s turn.")

      if player == "X": #maisha did these conditionals
          while True:
              move = int(input("enter your move (0-8): "))
              if 0 <= move <= 8 and board[move] == " ":
                  board[move] = player
                  break
              else:
                  print("invalid bro try once more.") #Maisha
      else:
          move = computer(board) # the computer is putting move down (Zoey) 
          board[move] = player
          print(f"Computer's move: {move + 1}")

      if check_win(board, player):
          display_board(board)
          print(f"Player {player} is the winner!")
          break

      if " " not in board: #maisha (conditonals)
          display_board(board)
          print("It's a tie!")
          break

      player = "O" if player == "X" else "X"

def play_game():  
    print("Welcome to Tic Tac Toe!")  
      
    # Initialize the board  
    board = [" " for _ in range(9)]  # or use a 3x3 list  
    player = "X"  # Starting player  
  
    while True:  
        display_board(board)  
        print(f"Player {player}'s turn.")  
  
        if player == "X":  
            # Get user input for player X  
            move = int(input("Enter your move (0-8): "))  
            if board[move] == " ":  
                board[move] = player  
            else:  
                print("Cell already taken!



def display_board(board):  
    for row in board:  
        print(" | ".join(str(x) for x in row))  
        print("-" * 9)  



#Evelyn Chennault --> Interaction with the player
def make_move(player):    
    slot = int(input(f"Player {player}, enter a slot (0-8): "))   
    row = slot // 3  
    col = slot % 3  
  
    if board[row][col] == 0:  #Checking if the cell is empty (josy)    
        board[row][col] = player  #Updating the board  (josy)
    else:    
        print("Cell already taken! Try again.")    
        make_move(player)  #Ask again if the cell is taken    

    for turn in range(9):  #Maximum 9 moves    
        display_board(board)#Show the current board    
        player = "X"
        if turn % 2 == 0:
            make_move({player})
        else:
            print("O")#Alternate players    
            make_move(player)#Make the player's move    
  
display_board(board)#Show final board










#Zoey 
def computer(board): # the computer is putting a random movement in the empty spots (Zoey)
  empty_spaces = [i for i in range(9) if board[i] == " "]
  return random.choice(empty_spaces)


def play_game():#zoey worked on these functions 
  print("This is a Tic tac toe game. It is just like a normal game of Tic tac toe the difference is\ninstead of writing the X you would type in a number (0-8) to\nplace the X left to right and so on \nthis is for each of the rows.")


  board = [" " for _ in range(9)]
  player = "X"
  while True: #
      print (board)
      print(f"Player {player}'s turn.")

      if player == "X": #maisha did these conditionals
          while True:
              move = int(input("enter your move (0-8): "))
              if 0 <= move <= 8 and board[move] == " ":
                  board[move] = player
                  break
              else:
                  print("invalid bro try once more.") #Maisha
      else:
          move = computer(board) # the computer is putting move down (Zoey) 
          board[move] = player
          print(f"Computer's move: {move + 1}")

      if check_win(board, player):
          display_board(board)
          print(f"Player {player} is the winner!")
          break

      if " " not in board: #maisha (conditonals)
          display_board(board)
          print("It's a tie!")
          break

      player = "O" if player == "X" else "X"


