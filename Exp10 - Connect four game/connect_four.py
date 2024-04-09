import numpy as np
import random

class ConnectFour:
    def __init__(self):
        self.board = np.zeros((6, 7), dtype=int)
        self.stacks = [[] for _ in range(7)]
        self.computer_piece = 1
        self.player_piece = 2

    def move(self, piece):
        if piece == self.computer_piece:
            column = random.randint(0, 6)
            while len(self.stacks[column]) == 6:  # Check if the column is full
                column = random.randint(0, 6)
            self.stacks[column].append(piece)
            self.update_board(column, piece)
        else:
            while True:
                try:
                    column = int(input("Enter column number (1-7): ")) - 1
                    if column < 0 or column > 6:
                        raise ValueError
                    if len(self.stacks[column]) == 6:  # Check if the column is full
                        print("Column is full, please choose another column.")
                    else:
                        self.stacks[column].append(piece)
                        self.update_board(column, piece)
                        break
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 7.")

    def update_board(self, column, piece):
        row = len(self.stacks[column]) - 1
        self.board[row][column] = piece

    def check_winner(self):
        # Check for horizontal win
        for row in range(6):
            for col in range(4):
                if (self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3]) and (self.board[row][col] != 0):
                    return self.board[row][col]

        # Check for vertical win
        for col in range(7):
            for row in range(3):
                if (self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col]) and (self.board[row][col] != 0):
                    return self.board[row][col]

        # Check for diagonal win (top-left to bottom-right)
        for row in range(3):
            for col in range(4):
                if (self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3]) and (self.board[row][col] != 0):
                    return self.board[row][col]

        # Check for diagonal win (bottom-left to top-right)
        for row in range(3, 6):
            for col in range(4):
                if (self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == self.board[row - 3][col + 3]) and (self.board[row][col] != 0):
                    return self.board[row][col]

        return 0  # Return 0 if no winner yet

    def print_board(self):
        for row in range(6):
            print("|", end="")
            for col in range(7):
                if self.board[row][col] == 0:
                    print(" ", end="|")
                elif self.board[row][col] == self.computer_piece:
                    print("O", end="|")
                else:
                    print("X", end="|")
            print()
        print("|-+-+-+-+-+-+-|")
        print("|1|2|3|4|5|6|7|")
        print()

def main():
    game = ConnectFour()
    game_over = False
    while not game_over:
        game.print_board()
        game.move(game.computer_piece)
        winner = game.check_winner()
        if winner:
            game.print_board()
            print("Computer wins!")
            game_over = True
            break
        game.print_board()
        game.move(game.player_piece)
        winner = game.check_winner()
        if winner:
            game.print_board()
            print("Player wins!")
            game_over = True
            break
    print("Game over.")

if __name__ == "__main__":
    main()
