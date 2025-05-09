import random

from ascii_art import STAGES

WORDS = [
    "python",
    "git",
    "github",
    "snowman",
    "meltdown",
]


def get_random_word():
    """Select a random word from the WORDS list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the snowman stage and current guessed word state."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += f"{letter} "
        else:
            display_word += "_ "

    print(f"Word: {display_word}\n")


def play_game():
    """Run the Snowman Meltdown game loop."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    max_mistakes = len(STAGES) - 1

    while True:
        # Prompt until a valid single-letter guess is entered
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                break
            print("Invalid input. Enter exactly one letter.")

        if guess in secret_word:
            guessed_letters.append(guess)
            print(f"You guessed: {guess}")
        else:
            mistakes += 1
            print(f"Wrong guess: {guess}")

        if mistakes > max_mistakes:
            print("You lost the game. Sorry!")
            if input("Do you want to play again? (y/n): ").lower() == "y":
                play_game()
            else:
                print("Thank you for playing!")
            break

        display_game_state(mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print("You won! Congratulations!")
            if input("Do you want to play again? (y/n): ").lower() == "y":
                play_game()
            else:
                print("Thank you for playing!")
            break


if __name__ == "__main__":
    play_game()
