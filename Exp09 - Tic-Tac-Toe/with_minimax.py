import random

# Constants
WIN_CONDITIONS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
PLAYER_X = 'X'
PLAYER_O = 'O'

def create_board():
    """Initialize the game board with empty spaces."""
    return [' ' for _ in range(9)]

def is_board_filled(board):
    """Check if the board is filled."""
    return ' ' not in board

def check_win(board, player):
    """Check if the current player has won."""
    return any(all(board[i] == player for i in condition) for condition in WIN_CONDITIONS)

def print_board(board):
    """Print the current state of the game board."""
    print("\n")
    for row in range(0, 9, 3):
        print(" ", board[row], " | ", board[row+1], " | ", board[row+2])
        if row < 6:
            print("-----------------")
    print("\n")

def minimax(board, depth, is_maximizing):
    """Implement the minimax algorithm to find the best move."""
    if check_win(board, PLAYER_X):
        return 1
    elif check_win(board, PLAYER_O):
        return -1
    elif is_board_filled(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = PLAYER_X
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = PLAYER_O
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    """Find the best move for the current player."""
    best_score = float('-inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = PLAYER_X
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def get_player_input(board):
    """Prompt the player for a position and validate the input."""
    while True:
        try:
            position = int(input("Enter position number (0-8): "))
            if position < 0 or position > 8 or board[position] != ' ':
                raise ValueError
            return position
        except ValueError:
            print("Invalid input. Please enter a valid position number that is not already taken.")

def start_game():
    """Start the Tic-Tac-Toe game."""
    board = create_board()
    current_player = random.choice([PLAYER_X, PLAYER_O])
    print("Player", current_player, "starts the game.")
    
    while True:
        print_board(board)
        
        if current_player == PLAYER_X:
            position = find_best_move(board)
        else:
            position = get_player_input(board)
        
        board[position] = current_player # type: ignore
        
        if check_win(board, current_player):
            print_board(board)
            print("Player", current_player, "wins!")
            break
        
        if is_board_filled(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

if __name__ == "__main__":
    start_game()