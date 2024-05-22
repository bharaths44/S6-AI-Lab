import random

def create_board():
    return [' ' for _ in range(9)]

def is_board_filled(board):
    return ' ' not in board

def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def print_board(board):
    print("\n")
    print(" ", board[0], " | ", board[1], " | ", board[2])
    print("-----------------")
    print(" ", board[3], " | ", board[4], " | ", board[5])
    print("-----------------")
    print(" ", board[6], " | ", board[7], " | ", board[8])
    print("\n")



def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return 1
    elif check_win(board, 'O'):
        return -1
    elif is_board_filled(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = float('-inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move


def start_game():
    board = create_board()
    players = ['X', 'O']
    current_player = random.choice(players)
    print("Player", current_player, "starts the game.")
    
    while True:
        print_board(board)
        
        if current_player == 'X':
            position = find_best_move(board)
        else:
            position = int(input("Enter position number (0-8): "))
        
        if board[position] != ' ':
            print("Spot already taken. Try again.")
            continue
        
        board[position] = current_player
        
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