def create_magic_square(size):
    # Initialize the magic square with all zeros
    magic_square = [[0] * size for _ in range(size)]

    # Start position for the number 1 is in the middle of the first row
    row, col = 0, size // 2

    # Fill the magic square
    for number in range(1, size*size + 1):
        magic_square[row][col] = number

        # Calculate the next position
        next_row, next_col = (row - 1) % size, (col + 1) % size

        # If the next position is available, move to it
        if magic_square[next_row][next_col] == 0:
            row, col = next_row, next_col
        else:
            # If the next position is not available, move down one row
            row = (row + 1) % size

    return magic_square

def display_magic_square(magic_square):
    # Print the magic square in a nicely formatted way
    border_line = "-" * (4 * len(magic_square) + 3)
    for row in magic_square:
        print(border_line)
        print("| " + " | ".join(map(str, row)) + " |")
    print(border_line)

# Get the order of the magic square from the user
order = int(input("Enter the order of the magic square: "))

# Create the magic square
magic_square = create_magic_square(order)

# Display the magic square
print("Magic Square:")
display_magic_square(magic_square)