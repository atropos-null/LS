import json
import sys

with open('loan_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def main():

    print(MESSAGES['welcome'])

    while True:
        amount = get_amount()
        duration = get_duration()
        interest = get_apr()
        if interest is None:
            payment = calculate_zero(amount, duration)

        else:
            payment = calculate(amount, interest, duration)

        print(f"Your monthly payment is ${payment:.2f}.")
        reprompting = input(MESSAGES['reprompt']).lower()
        if reprompting != 'y':
            sys.exit()

def invalid_number(number_str):

    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f"Value must be > 0: {number}")
    except ValueError:
        return True
    return False

def get_numbersonly(number_str):

    numbers_only = ''
    for character in number_str:
        if character.isdigit() or character == '.':
            numbers_only += character
    return numbers_only

def get_amount():
    while True:
        amount = input(MESSAGES['loan_amount'])
        amount = get_numbersonly(amount)
        if not invalid_number(amount):
            return float(amount)

def get_apr():
    while True:
        apr = input(MESSAGES['apr'])
        apr = get_numbersonly(apr)
        if apr == '0':
            return None
        if not invalid_number(apr):
            interest = (1 + float(apr) / 100) ** (1 / 12) - 1
            return interest

def get_duration():
    while True:
        duration = input(MESSAGES['duration'])
        duration = get_numbersonly(duration)
        if not invalid_number(duration):
            duration = float(duration) * 12
            return duration

def calculate(amount, interest, duration):
    payment  = amount * (interest / (1 - (1 + interest) ** (-duration)))
    return payment

def calculate_zero(amount, duration):
    payment = amount / duration
    return payment

main()
