"""

Problem: Convert integers to a numeric string representation
    - input: integer of various place values
    - output: string
    - explicit rules: no conversions
    - implicit rules: go right to left
    - implicit rules: use divmod

Example: 4321 == "-4321"

Data Structure: list to hold the numeric representations

Algorithm: 
    - function definition with number as parameter
    - dictionary to hold numeric representations
    - while number > 0
        - divmod(number, 10)
        - capture the second number in the tuple and store in a tuple
    - join and reverse list
    - return string



"""

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(number):
    if number == 0: 
        return '0'
    string = ''
    working_number = number
    while working_number > 0:
        quotient, remainder  = divmod(working_number, 10)
        string = DIGITS[remainder] + string
        working_number = quotient
    
    return string

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

