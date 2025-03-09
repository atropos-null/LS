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
        if reprompting not in ['y', 'yes']:
            sys.exit()

def invalid_number(number_str):

    try:
        number = float(number_str)
        if number < 0:
            raise ValueError(f"Value must be more than 0: {number}")
    except ValueError:
        return True
    return False

def get_numbersonly(number_str):

    numbers_only = ''
    for character in number_str:
        if character.isdigit() or character in ['.', '-']:
            numbers_only += character
    return numbers_only

def get_amount():
    while True:
        amount = input(MESSAGES['loan_amount'])
        amount = get_numbersonly(amount)
        if not invalid_number(amount):
            return float(amount)
        print(MESSAGES['invalid_amount'])

def get_apr():
    while True:
        apr = input(MESSAGES['apr'])
        apr = get_numbersonly(apr)
        if apr == '':
            return None
        if not invalid_number(apr):
            if float(apr) == 0:
                return None
            interest = (1 + float(apr) / 100) ** (1 / 12) - 1
            return interest
        print(MESSAGES['invalid_apr'])

def get_duration():
    while True:
        duration_years = input(MESSAGES['duration_years'])
        duration_years = get_numbersonly(duration_years)
        if invalid_number(duration_years):
            print(MESSAGES['invalid_duration'])
            continue
        
        duration_months = input(MESSAGES['duration_months'])
        duration_months = get_numbersonly(duration_months)
        if invalid_number(duration_months):
            print(MESSAGES['invalid_duration'])
            continue
        
        duration = (float(duration_years) * 12) + float(duration_months)
        if duration <= 0:
            print(MESSAGES['invalid_duration'])
            continue

        return duration

def calculate(amount, interest, duration):
    payment  = amount * (interest / (1 - (1 + interest) ** (-duration)))
    return payment

def calculate_zero(amount, duration):
    payment = amount / duration
    return payment

main()
