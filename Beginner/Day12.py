import random

print("Guess The number Game!")

rand_val = random.randint(1, 100)
attempts = 0
difficulty = input("Select you difficulty level, type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts = 10
    while attempts != 0:
        print(f"You have {attempts} attempts to get the guess the number!")
        guess_num = int(input("Guess the number between 1 and 100: "))
        if guess_num > rand_val:
            attempts -= 1
            print("Too high! Try Again")
        elif guess_num < rand_val:
            attempts -= 1
            print("Too low! Try Again")
        else:
            print(f"Congratulation! You got it! The answer was {guess_num}")
            break

elif difficulty == "hard":
    attempts = 5
    while attempts != 0:
        print(f"You have {attempts} attempts to get the guess the number!")
        guess_num = int(input("Guess the number between 1 and 100: "))
        if guess_num > rand_val:
            attempts -= 1
            print("Too high! Try Again")
        elif guess_num < rand_val:
            attempts -= 1
            print("Too low! Try Again")
        else:
            print(f"Congratulation! You got it! The answer was {rand_val}")
            break
else:
    print("Choose a valid difficulty!")




#Global Scope
# player_health = 100
#
# def drink_potion(cure):
#
#     return cure + 50
#
# player_health = drink_potion(player_health)
# print(player_health)

# game_level = 5
# enemies = ["Skeleton", "Zombies", "Alien"]
#
# def create_enemy():
#     new_enemy = ""
#     if game_level == 5:
#         new_enemy = enemies[0]
#
#     print(new_enemy)



