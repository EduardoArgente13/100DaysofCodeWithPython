# Second project
print("Hello! Welcome to the tip calculator!")
bill = float(input("Whats the total bill?: "))
tip = int(input("How much tip would you like to give?: "))
people = int(input("How many people to split the bill?: "))

total = (bill * ((tip / 100) + 1)) / people

roundabout = round(total, 2)

print(f"Each person should pay: ${roundabout}")