import random
from random import randint, shuffle

alphabet_letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
    '+', '[', ']', '{', '}', '|', ';', ':', '"', ',', '.',
    '<', '>', '/', '?', '`', '~'
]

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like to generate?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# password = ""
#
# for i in range(1, nr_letters + 1):
#     random_letter = random.choice(alphabet_letters)
#     password += random_letter
# for i in range(1, nr_numbers + 1):
#     random_number = random.choice(numbers)
#     password += random_number
# for i in range(1, nr_symbols + 1):
#     random_symbol = random.choice(symbols)
#     password += random_symbol
#
# print(password)

password_list = []

for i in range(1, nr_letters + 1):
    random_letter = random.choice(alphabet_letters)
    password_list += random_letter
for i in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password_list += random_number
for i in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password_list += random_symbol

shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")


# fruits =["Apple", "Peach", "Pear"]
#
# for fruit in fruits:
#     print(fruit + "pie")

# # List of student scores
# student_scores = [142, 254, 123, 147, 159, 862, 352, 125, 14, 257, 41, 1523, 1526, 1425, 187, 26, 13]
#
# # Initialize a variable to store the maximum value
# max_score = student_scores[0]
#
# # Loop through the list
# for score in student_scores:
#     if score > max_score:
#         max_score = score
#
# print(f"The highest score is: {max_score}")
#
# num = 0
#
# for number in range(1,101):
#     num += number
# print(num)
#
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         number = "FizzBuzz"
#     elif number % 3 == 0:
#         number = "Fizz"
#     elif number % 5 == 0:
#         number = "Buzz"
#
#     print(number)

