# def my_function():
#     return 3*2
#
# output = my_function()
# print(output)

# def format_name(f_name, l_name):
#     """This function receives the name and last name inputs and format them with the .title() function"""
#     if f_name == "" or l_name == "":
#         return "You need to provide first name and last name"
#
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#
#     return f"Hello {formated_f_name} {formated_l_name}!"
#
#
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
#
# res = format_name(first_name, last_name)
# print(res)

print("Welcome to the PyCalculator!~")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    should_accumulate = True
    num1 = float(input("Enter your first number: "))

    while should_accumulate:
        operator = input("Enter your operator, could be +, -, * or /: ")
        if operator in operations:
            operation = operations[operator]
            num2 = float(input("Enter your second number: "))
            partial_result = operation(num1, num2)
            result = round(partial_result, 2)
            print(f"{num1} {operator} {num2} = {result}")
            print(f"Your result is: {result}")
        else:
            print("Invalid operator")
            break
        should_continue = input(f"Would you like to continue with the operation with the value {result}? (y/n) or type exit to terminate the program: ").lower()
        if should_continue == 'y':
            num1 = result
        elif should_continue == 'n':
            should_accumulate = False
            print("\n"*24)
            calculator()
        elif should_continue == 'exit':
            print("bye, bye")
            break
        else:
            print("Invalid input")
            calculator()


calculator()