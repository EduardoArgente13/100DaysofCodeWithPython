# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it!")

# my_function()

from random import randint

dice_images = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
dice_num = randint(0, 5)
print(dice_images[dice_num])