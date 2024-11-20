import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack_game():
    """Function to run a single round of Blackjack."""
    print("Welcome to Python Black Jack!")

    random.shuffle(cards)
    my_cards = random.sample(cards, 2)
    computer_cards = random.sample(cards, 2)
    add_up = sum(my_cards)
    computer_total = sum(computer_cards)

    print(f"Your Cards: {my_cards}, Total: {add_up}")
    print(f"Computer's first card: {computer_cards[0]}")

    # Player's turn
    while True:
        another_card = input("Do you want another card? (y/n)").lower()
        if another_card == "y":
            new_card = random.choice(cards)
            my_cards.append(new_card)
            add_up = sum(my_cards)

            # Ace adjustment
            if add_up > 21 and 11 in my_cards:
                my_cards[my_cards.index(11)] = 1
                add_up = sum(my_cards)

            print(f"Your Cards: {my_cards}, Total: {add_up}")

            # Check for bust
            if add_up > 21:
                print("You went over 21! You lose.")
                return
        else:
            break

    # Computer's turn
    print("Now it's the computer's turn.")
    while computer_total < 17:
        new_card = random.choice(cards)
        computer_cards.append(new_card)
        computer_total = sum(computer_cards)

        # Ace adjustment
        if computer_total > 21 and 11 in computer_cards:
            computer_cards[computer_cards.index(11)] = 1
            computer_total = sum(computer_cards)

    print(f"Computer's final hand: {computer_cards}, Total: {computer_total}")

    # Determine the winner
    if computer_total > 21:
        print("The computer went over 21! You win!")
    elif add_up > computer_total:
        print("You win!")
    elif add_up < computer_total:
        print("The computer wins!")
    else:
        print("It's a draw!")


while True:
    choice = input("Do you want to play a game of Blackjack? (y/n): ").lower()
    if choice == "y":
        blackjack_game()
    else:
        print("Thank you for playing! Goodbye!")
        break
