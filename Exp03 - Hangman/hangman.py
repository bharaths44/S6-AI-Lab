import random

def choose_word():
    words = ["python", "programming", "developer", "challenge", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_ "
    return display

def print_hangman(attempts):
    hangman_figures = [
        '''
           -----
           |   |
               |
               |
               |
               |
        -------'''
        ,
        '''
           -----
           |   |
           O   |
               |
               |
               |
        -------'''
        ,
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        -------'''
        ,
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        -------'''
        ,
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        -------'''
        ,
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        -------'''
        ,
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        -------'''
    ]

    print(hangman_figures[attempts])

def guess_word():
    print("Welcome to the Word Guessing Game!")
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}!")

    secret_word = choose_word()
    max_attempts = 6
    attempts = 0
    guessed_letters = []

    print("Try to guess the word!")

    while attempts < max_attempts:
        current_display = display_word(secret_word, guessed_letters)
        print(f"Current word: {current_display}")
        print(f"Attempts: {attempts + 1}/{max_attempts}")
        print_hangman(attempts)
        guess = input("Enter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess. Try again.")
                attempts += 1
        else:
            print("Invalid input. Please enter a single letter.")

        if set(secret_word) == set(guessed_letters):
            print(f"Congratulations, {user_name}! You guessed the word: {secret_word}")
            break

    if set(secret_word) != set(guessed_letters):
        print(f"Sorry, {user_name}. You ran out of attempts. The correct word was: {secret_word}")
        print_hangman(max_attempts)

if __name__ == "__main__":
    guess_word()
