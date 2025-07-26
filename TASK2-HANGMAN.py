import random

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

# Predefined word list with hints
WORDS_WITH_HINTS = {
    "python": "A popular programming language known for readability.",
    "hangman": "Classic word guessing game.",
    "computer": "An electronic device for processing data.",
    "keyboard": "Input device with keys.",
    "internet": "Global system of interconnected computer networks."
}

MAX_ATTEMPTS = len(HANGMAN_PICS) - 1

def get_random_word():
    word = random.choice(list(WORDS_WITH_HINTS.keys()))
    hint = WORDS_WITH_HINTS[word]
    return word, hint

def display_game_state(word, guessed_letters, incorrect_guesses, hint):
    print(HANGMAN_PICS[len(incorrect_guesses)])
    print(f"Hint: {hint}")
    
    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(f"Word: {displayed_word}")
    
    print(f"Incorrect guesses: {', '.join(incorrect_guesses) if incorrect_guesses else 'None'}")
    print()

def get_player_guess(guessed_letters, incorrect_guesses):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
        elif guess in guessed_letters or guess in incorrect_guesses:
            print("You've already guessed that letter.")
        else:
            return guess

def play_game():
    word, hint = get_random_word()
    guessed_letters = []
    incorrect_guesses = []

    while True:
        display_game_state(word, guessed_letters, incorrect_guesses, hint)

        guess = get_player_guess(guessed_letters, incorrect_guesses)

        if guess in word:
            guessed_letters.append(guess)
            # Check for win
            if all(letter in guessed_letters for letter in word):
                display_game_state(word, guessed_letters, incorrect_guesses, hint)
                print("Congratulations! You've guessed the word!")
                break
        else:
            incorrect_guesses.append(guess)
            # Check for loss
            if len(incorrect_guesses) >= MAX_ATTEMPTS:
                display_game_state(word, guessed_letters, incorrect_guesses, hint)
                print(f"You lost! The word was '{word}'.")
                break

def main():
    print("Welcome to the Hangman Word Guessing Game!")
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
