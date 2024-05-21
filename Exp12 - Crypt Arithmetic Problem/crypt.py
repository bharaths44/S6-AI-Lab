def evaluate(word, assigned):
    # Create an empty list to hold the digits
    digits = []

    # Loop over each character in the word
    for char in word:
        # Get the assigned digit for the character. If the character is not in the dictionary, use '0'
        digit = assigned.get(char, '0')
        # Add the digit to the list
        digits.append(digit)

    # Join the digits together to form a string
    number_string = ''.join(digits)

    # Convert the string to an integer
    result = int(number_string)

    return result

def _solve(word1, word2, result, letters, assigned):
    if not letters:
        return evaluate(word1, assigned) + evaluate(word2, assigned) == evaluate(result, assigned)
    cur_letter = letters.pop()
    for i in range(10):
        num = str(i)
        if num not in assigned.values() and not (num == '0' and cur_letter in (word1[0], word2[0], result[0])):
            assigned[cur_letter] = num
            if _solve(word1, word2, result, letters, assigned):
                return True
            del assigned[cur_letter]
    letters.append(cur_letter)
    return False

def solve(word1, word2, result):
    letters = list(set(word1 + word2 + result))  # unique letters in all words
    assigned = {}  # dictionary to hold the assigned letters and their corresponding values

    if _solve(word1, word2, result, letters, assigned):
        print(f"Assigned: {assigned}")
        print(f"{word1}({evaluate(word1, assigned)}) + {word2}({evaluate(word2, assigned)}) = {result}({evaluate(result, assigned)})")
    else:
        print("No solution found.")

# Example usage:
solve('BASE', 'BALL', 'GAMES')