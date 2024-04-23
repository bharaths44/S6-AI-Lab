def create_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]

    # Step 4.1: Place the number 1 in the middle of the first row
    i, j = 0, n // 2
    num = 1

    while num <= n * n:
        magic_square[i][j] = num
        num += 1

        # Step 4.2: Move to the next position
        new_i, new_j = (i - 1) % n, (j + 1) % n

        # Step 4.2.1: Check if the next position is available
        if magic_square[new_i][new_j] == 0:
            i, j = new_i, new_j
        else:
            # Step 4.2.2: Handle when the next position is not available
            i = (i + 1) % n

    return magic_square

def display_magic_square(magic_square):
    print("-" * (4 * len(magic_square) + 3))
    for row in magic_square:
        print("| " + " | ".join(map(str, row)) + " |")
        print("-" * (4 * len(row) + 3))

# Step 2: Read the order of the matrix from the user and store it in n
n = int(input("Enter the order of the magic square: "))

# Step 3: Create an n by n array
magic_square = create_magic_square(n)

# Step 5: Display the magic square
print("Magic Square:")

display_magic_square(magic_square)
