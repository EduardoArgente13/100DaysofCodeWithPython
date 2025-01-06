import random
from game_data import data

# Welcome to the game
print("Welcome to the Higher or Lower Game!\n")
print("In this game, you will compare two people. You need to guess who has more followers.\n")

# Get a random person from the game data
def getRandomPerson():
    return random.choice(data)

# Set the format to be used for printing the person
def personFormat(person):
    return f"{person['name']}, a {person['description']} from {person['country']}"

# Compare the number of followers between two people
def compareFollowers(person1, person2):
    return person1['follower_count'] > person2['follower_count']

# Initial variables
score = 0
playing = True

# Start the game
while playing:
    # Get two random people, ensuring they are not the same, check if the score is greater than 0 to use the second person from the previous round as the first person of the actual round to follow the standard of the original game
    person1 = person2 if score > 0 else getRandomPerson()
    person2 = getRandomPerson()
    
    # Ensure the two people are different
    while person1 == person2:
        person2 = getRandomPerson()

    # Display the two people to compare
    print(f"\nCompare A: {personFormat(person1)}")
    print("vs")
    print(f"Against B: {personFormat(person2)}\n")
    
    # Ask for the player's guess
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Check the guess and update the score
    if guess == 'A':
        if compareFollowers(person1, person2):
            score += 1
            print(f"Correct! Current score: {score}\n")
        else:
            print(f"Wrong! Final score: {score}\n")
            playing = False
    elif guess == 'B':
        if compareFollowers(person2, person1):
            score += 1
            print(f"\nCorrect! Current score: {score}\n")
        else:
            print(f"\nWrong! Final score: {score}\n")
            playing = False
    else:
        print("\nInvalid input! Please type 'A' or 'B'.\n")
