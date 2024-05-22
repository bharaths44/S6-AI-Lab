def printSolution():
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def isSafe(row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQ(col):
    if col >= N:
        return True

    for i in range(N):
        if isSafe(i, col):
            board[i][col] = 1

            if solveNQ(col + 1):
                return True

            board[i][col] = 0

    return False

def main():
    global N, board
    N = int(input("Enter the number of queens: "))
    board = [[0] * N for _ in range(N)]

    if solveNQ(0) == False:
        print("Solution does not exist")
        return False

    print("Queens placement:")
    printSolution()
    return True

if __name__ == "__main__":
    main()