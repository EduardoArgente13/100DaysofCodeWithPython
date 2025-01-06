print("Welcome tho the Graveyard, Where all dreams come to die")
print('''        
                 mo / )
                 |/)\)
                  /\_
                  \__|=
                 (    )
                 __)(__
_________+______/      \______+__________
  __--   |       R.I.P.       |-_-- __
_-- -    | ___ __________ ___ |
-_-- __  || | | | {|    /| | || __---  -_
 --__-   || | | | {|   /|| | ||--        -
         || | | | {|  /||| | ||__--
 __-- -__|| | | | {| |}||| | ||--   __--
         ||_|_|_|_{| |}|||_|_||  -__
 --__-  -|| | | | {& |}||/ | ||---   __--
         || | | | {| |}|/| | ||-__
--   __--|| | | | {| |}/|| | ||__-- -__
  --     || | | | {| &}||| | ||   __
---   __-|| | | | {| |}||| | ||_---__-  --
 -  -_   || | | | {| |}||| | || --
 __ejm 97|| | | | {| |}||| | ||_--__-   _---
_________||_|_|_|_{| |}|||_|_||______________
                     |}|/
                     |}/
                     |/''')

first_step = input("You enter to the Graveyard where you want to go left or right? Type l or r")



if first_step == "l":
    second_step = input("You see a lake what do you do swim or wait. Type s or w")
    if second_step == "w":
        third_step = input("3 Doors appear in front of you red, blue and yellow. Which one do you choose? Type r, b or y")
        if third_step == "y":
            print("You Win!")
        elif third_step == "r":
            print("Burned by fire. Game Over.")
        elif third_step == "b":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over :(")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")





# print("Hello Welcome to the rollercoaster!")
#
# height = int(input("Enter your height in centimeters, please: "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("Enter your age: "))
#     if age >= 45 and age <= 55:
#         bill = 0
#         print("Midlife crisis bums enter for free, you sorry fucks")
#     elif age >= 18:
#         bill = 12
#         print("Adult Ticket $12")
#     elif 18 > age >= 12:
#         bill = 9
#         print("Teen Ticket $9")
#     else:
#         bill = 5
#         print("Child Ticket $5")
#     wants_photo = input("Do you want a photo? Type y for Yes or n for No: ")
#     if wants_photo == "y":
#         bill += 3
#         print(f"Your Total Bill is ${bill}")
#     else:
#         print(f"Your Total Bill is ${bill}")
# else:
#     print("Sorry you have to be taller")

# print("Welcome to Pizza Deliveries")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# price = 0
#
# if size == "S":
#     price = 15
# elif size == "M":
#     price = 20
# elif size == "L":
#     price = 25
# else:
#     print("You have to choose a valid size, please try again")
#
# if pepperoni == "Y":
#     price += 2
# elif pepperoni == "N":
#     price = price
# else:
#     print("Invalid option, please try again")
#
# if extra_cheese == "Y":
#     price += 1
# elif extra_cheese == "N":
#     price = price
# else:
#     print("Invalid option, please try again")
#
# print(f"Your pizza price is ${price}")
