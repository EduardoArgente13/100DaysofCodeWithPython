import random

# ASCII art for the hangman stages
hangman_stages = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """
]

# Step 1: Create a list of words
word_list = ["aardvark", "camel", "baboon"]

# Step 2: Randomly choose a word from the list
rand_word = random.choice(word_list)
word_length = len(rand_word)

# Step 3: Initialize the display and the number of lives
display = ["_"] * word_length
lives = 6

# Step 4: Main game loop
while "_" in display and lives > 0:
    # Show the current progress of the word
    print("\nCurrent word:", " ".join(display))
    print(hangman_stages[lives])
    print(f"Lives left: {lives}")

    # Step 5: Get the player's guess
    guess_char = input("Guess a letter: ").lower()

    # Step 6: Check if the guessed letter is in the word
    if guess_char in rand_word:
        # Update the display with the correct guessed letter
        for i in range(word_length):
            if rand_word[i] == guess_char:
                display[i] = guess_char
    else:
        # Decrease lives if the guess was incorrect
        lives -= 1
        print("Wrong guess! You lose a life.")

# Step 7: End of game
if "_" not in display:
    print("\nCongratulations! You guessed the word:", rand_word)
else:
    print(hangman_stages[0])
    print("\nGame over! The word was:", rand_word)
