import sys
import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def main():

    print(MESSAGES['welcome'])

    while True:
        number_1 = get_number_1()
        number_2 = get_number_2()
        operator = get_operator()
        output = calculate(number_1, number_2, operator)
        print(f"The result is {output}.")
        reprompting = input(MESSAGES['reprompt']).lower()
        if reprompting != 'y':
            sys.exit()

def invalid_number(number_str):

    try:
        float(number_str)
    except ValueError:
        return True

    return False

def get_number_1():
    number_1 = input(MESSAGES['number_prompt_1'])
    while invalid_number(number_1):
        number_1 = input("Please enter a valid number. ")
    return number_1

def get_number_2():
    number_2 = input(MESSAGES['number_prompt_2'])
    while invalid_number(number_2):
        number_2 = input("Please enter a valid number. ")
    return number_2

def get_operator():
    operator = input(MESSAGES['operation_prompt'])
    while operator not in ["1", "2", "3", "4"]:
        operator = input("You must choose 1, 2, 3, or 4")
    return operator

def calculate(number_1, number_2, operator):

    number_1 = float(number_1)
    number_2 = float(number_2)

    match operator:
        case "1":
            output = number_1 + number_2
            return output
        case "2":
            output = number_1 - number_2
            return output
        case "3":
            output = number_1 * number_2
            return output
        case "4":
            output = number_1 / number_2
            return output

main()