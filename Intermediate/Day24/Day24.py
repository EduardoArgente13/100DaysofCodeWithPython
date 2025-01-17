PLACEHOLDER = "[name]"

with open("Intermediate/Day24/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    print(names)
    

with open("Intermediate/Day24/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip() 
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Intermediate/Day24/Output/ReadyToSend/letter_for{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
        print(new_letter)