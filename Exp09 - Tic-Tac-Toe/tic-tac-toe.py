import random

def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def is_board_filled(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def check_win(board, player):
    for row in board:
        if all(mark == player for mark in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-+-+-')

def start_game():
    board = create_board()
    players = ['X', 'O']
    current_player = random.choice(players)
    print("Player", current_player, "starts the game.")
    
    while True:
        print_board(board)
        
        row = int(input("Enter row number (0-2): "))
        col = int(input("Enter column number (0-2): "))
        
        if board[row][col] != ' ':
            print("Spot already taken. Try again.")
            continue
        
        board[row][col] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print("Player", current_player, "wins!")
            break
        
        if is_board_filled(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
    start_game()
