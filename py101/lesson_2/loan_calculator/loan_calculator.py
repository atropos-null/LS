import json
import sys

with open('loan_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def main():

    print(MESSAGES['welcome'])

    while True:
        amount = get_amount()
        interest = get_apr()
        duration = get_duration()
        payment = calculate(amount, interest, duration)
        print(f"Your monthly payment is ${payment:.2f}.")
        reprompting = input(MESSAGES['reprompt']).lower()
        if reprompting != 'y':
            sys.exit()

def invalid_number(number_str):

    try:
        float(number_str)
    except ValueError:
        return True

    return False

def get_amount():
    amount = float(input(MESSAGES['loan_amount']))
    while invalid_number(amount):
        amount = input(MESSAGES['reprompt'])
    return amount

def get_apr():
    apr = input(MESSAGES['apr']).strip("%")
    apr = float(apr)
    while invalid_number(apr):
        apr = input(MESSAGES['reprompt'])
    interest = (1 + apr / 100) ** (1 / 12) - 1
    return interest

def get_duration():
    duration = int(input(MESSAGES['duration']))
    while invalid_number(duration):
        duration = input("Please enter a valid number.")
    return duration

def calculate(amount, interest, duration):
    payment  = amount * (interest / (1 - (1 + interest) ** (-duration)))
    return payment

main()
