logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)


def add(inpt1, inpt2):
    return inpt1 + inpt2


def subtract(inpt1, inpt2):
    return inpt1 - inpt2


def multiply(inpt1, inpt2):
    return inpt1 * inpt2


def divide(inpt1, inpt2):
    return inpt1 / inpt2


operators = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    num1 = float(input("Enter the first number: "))
    for operator in operators:
        print(operator)
    run_again = True

    while run_again:
        operator_input = input("Choose operator: ")
        num2 = float(input("Enter the next number: "))
        calculate_function = operators[operator_input]
        answer = calculate_function(num1, num2)

        print(f"{num1} {operator_input} {num2} = {answer}")

        if input(f"Type \'y\' to continue calculating with {answer} or type \'n\' to exit: ") == 'y':
            num1 = answer
        else:
            run_again = False
            calculator()


calculator()


