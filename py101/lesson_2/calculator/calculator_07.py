# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

from pyfiglet import Figlet

text = Figlet(font='mini')
print(text.renderText('Welcome to Calculator'))

number_1 = int(input("What is your first number? "))
number_2 = int(input("What is your second number? "))
operator = input("What operation would you like to perform? Ints only, no floats. \n 1) Add 2) Subtract 3) Multiply 4) Divide ")
answer = None

if operator == '1':
    answer = number_1 + number_2

elif operator == '2':
    answer = number_1 - number_2
   
elif operator == '3':
    answer = number_1 * number_2

elif operator == '4':
    answer = number_1 // number_2

else: 
    print("Enter in a valid operator")
   
if answer != None:
    print(f"The result is {answer}. ")
