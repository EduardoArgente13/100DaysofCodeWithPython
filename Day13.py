import random 
import maths

# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it!")

# my_function()

# from random import randint

# dice_images = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
# dice_num = randint(0, 5)
# print(dice_images[dice_num])

# year = int(input("What's your year of birth? "))

# if year >= 1980 and year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:
#     print("you are a Gen Z.")

# try:
#     age = int(input("What is your age? "))
# except ValueError:
#     print("Please enter a valid number. e.g. 12")
#     age = int(input("What is your age? "))
# if age > 18:
#     print(f"You can drive at age {age}.")


# pages = int(input("Enter the number of pages: "))
# words_per_page = int(input("Enter the number of words per page: "))
# total_words = pages * words_per_page
# print(f"Pages: {pages}")
# print(f"Words per page: {words_per_page}")
# print(f"Total words: {total_words}")

# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#         b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])


# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# print(is_leap(2000))

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

