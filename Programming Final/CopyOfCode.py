# Programming Final Game, Evelyn, Josy, Maisha Paredes, and Zoey Sosa
import random  
  
def display_board(board):  
    # Displaying the board  
    print("Current Board:")  
    print(" | ".join(board[0:3]))  
    print("-" * 9)  
    print(" | ".join(board[3:6]))  
    print("-" * 9)  
    print(" | ".join(board[6:9]))  
  
def check_win(board, player):  
    # Winning combinations  
    winning_combinations = [  
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns  
        [0, 4, 8], [2, 4, 6]               # Diagonals  
    ]  
    for combo in winning_combinations:  
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:  
            return True  
    return False  
  
def computer(board):  
    # Computer's move  
    empty_spaces = [i for i in range(9) if board[i] == " "]  
    return random.choice(empty_spaces)  
  
def play_game():  
    print("Welcome to Tic Tac Toe!")  
    board = [" " for _ in range(9)]  
    player = "X"  # Starting player  
  
    while True:  
        display_board(board)  
        print(f"Player {player}'s turn.")  
  
        if player == "X":  
            move = int(input("Enter your move (1-9): "))  
            if board[move] == " ":  
                board[move] = player  
            else:  
                print("Cell already taken! Try again.")  
                continue  # Skip to the next iteration  
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