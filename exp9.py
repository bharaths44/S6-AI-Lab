# Initialize the size of the matrix
n = int(input("Enter value of n: "))

# Create an n x n matrix filled with zeros
matrix = [[0] * n for _ in range(n)]

# Start position for the first number
i, j = 0, n // 2

# Fill the matrix with numbers 1 to n*n
for num in range(1, n * n + 1):
    matrix[i][j] = num  # Place current number in the matrix
    # Calculate next position
    next_i, next_j = (i - 1) % n, (j + 1) % n

    # If the next position is already filled, move down instead
    if matrix[next_i][next_j] == 0:
         i, j = next_i, next_j
    else:
       i=(i+1)%n
# Print the matrix
for row in matrix:
    print(sum(row))
    print(row)