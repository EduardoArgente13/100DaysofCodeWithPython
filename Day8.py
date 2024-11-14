alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get user input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar_cipher(original_text, shift_amount, mode):
    result_text = ""
    # Adjust the shift direction based on mode
    if mode == 'decode':
        shift_amount *= -1

    # Loop through each letter in the text
    for letter in original_text:
        if letter in alphabet_lower:
            position = alphabet_lower.index(letter)
            new_position = (position + shift_amount) % 26
            result_text += alphabet_lower[new_position]
        else:
            result_text += letter

    print(f"Resulting Text: {result_text}")

caesar_cipher(text, shift, direction)


# def greet():
#     print("Hello")
#     print("You Stupid Fuck")
#     print("Ready to waste another day?")
#
# greet()
            # Calculate the new position with the shift (wrap around usi
#
# def greet_new(name):
#     print(f"Hello {name} ")
#
# name = input("Enter your name: ")
# greet_new(name)

# def life_in_weeks(age_as_int):
#     years_remaining = 90 - age_as_int
#     weeks_remaining = years_remaining * 52
#     print(f"You have {weeks_remaining} weeks left.")
#
# age = int(input("Enter your age: "))
#
# life_in_weeks(age)

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"How is like to live in {location}?")
#
# greet_with(name = "Eddy", location = "London")