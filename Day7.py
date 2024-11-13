import random

word_list = ["aardvark", "camel", "baboon"]

rand_word = random.choice(word_list)
word_length = len(rand_word)

display = ["_"] * word_length
lives = 6

while "_" in display and lives > 0:
    print("\nCurrent word:", " ".join(display))
    print(f"Lives left: {lives}")

    guess_char = input("Guess a letter: ").lower()

    if guess_char in rand_word:
        for i in range(word_length):
            if rand_word[i] == guess_char:
                display[i] = guess_char
    else:
        lives -= 1
        print(f"Wrong guess! You lose a life.")

if "_" not in display:
    print("\nCongratulations! You guessed the word:", rand_word)
else:
    print("\nGame over! The word was:", rand_word)