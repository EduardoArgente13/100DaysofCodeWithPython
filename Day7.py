# main.py

import random
from Day7_art import hangman_stages
from Day7_words import word_list

# Step 1: Randomly choose a word from the list
rand_word = random.choice(word_list)
word_length = len(rand_word)

# Step 2: Initialize the display and the number of lives
display = ["_"] * word_length
lives = 0  # Start with zero lives (no limbs drawn yet)
max_lives = len(hangman_stages) - 1  # Maximum number of incorrect guesses

# Step 3: Main game loop
while "_" in display and lives < max_lives:
    # Show the current progress of the word
    print("\nCurrent word:", " ".join(display))
    print(hangman_stages[lives])
    print(f"Incorrect guesses left: {max_lives - lives}")

    # Step 4: Get the player's guess
    guess_char = input("Guess a letter: ").lower()

    # Step 5: Check if the guessed letter is in the word
    if guess_char in rand_word:
        # Update the display with the correct guessed letter
        for i in range(word_length):
            if rand_word[i] == guess_char:
                display[i] = guess_char
    else:
        # Increase lives if the guess was incorrect (adding a limb)
        lives += 1
        print("Wrong guess! The hangman gains a limb.")

# Step 6: End of game
if "_" not in display:
    print("\nCongratulations! You guessed the word:", rand_word)
else:
    print(hangman_stages[lives])
    print("\nGame over! The hangman is complete. The word was:", rand_word)
