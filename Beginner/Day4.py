import random

# Rock
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_imgs = [Rock, Paper, Scissors]

print("Rock, paper, scissors!")
user_choice = int(input("Enter your choice, Type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))
computer_choice = random.randint(0, 2)

print(f"Your Choice = {user_choice}")
if 0 <= user_choice <= 2:
    print(game_imgs[user_choice])
else:
    print("Enter a valid option, try again")
print(f"Computer Choice = {computer_choice}")
print(game_imgs[computer_choice])

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win! Rock beat Scissors")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose! Rock beat Scissors")
elif user_choice == 0 and computer_choice == 1:
    print("You Lose! Paper beat Rock")
elif user_choice == 1 and computer_choice == 0:
    print("You Win! Paper beat Rock")
elif user_choice == 2 and computer_choice == 1:
    print("You Win! Scissors beat Paper")
elif user_choice == 1 and computer_choice == 2:
    print("You Lose! Scissors beat Paper")



# random_int = random.randint(1, 10)
# print(random_int)
# random_number = random.random() * 10
# print(random_number)
# random_float = random.uniform(1, 10)
# print(random_float)

# coin = random.randint(1, 2)
# if coin == 1:
#     print(coin)
#     print("Head")
# else:
#     print(coin)
#     print("Tail")

# friends = ['lalo', 'poncho', 'caca', 'melaplas', 'comes', 'shot', 'guitrteas']
#
# who_will_pay = random.choice(friends)
# print(who_will_pay)
#
# print(friends[len(friends) - 1])

# fruits = ["Apple", "Banana", "Grape"]
# vegetables = ["Tomato", "Leek", "Celery"]
#
# combined = [fruits, vegetables]
# print(combined)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[1][1])
