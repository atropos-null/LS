
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

def addition(number1, number2, prompt="==>",  symbol='+'):
    result = number1 + number2
    print(f"{prompt} {number1} {symbol} {number2} = {result}")

def subtraction(number1, number2, prompt="==>", symbol='-'):
    result = number1 - number2
    print(f"{prompt} {number1} {symbol} {number2} = {result}")

def multiply(number1, number2, prompt="==>",symbol='*'):
    result = number1 * number2
    print(f"{prompt} {number1} {symbol} {number2} = {result}")

def floating_division(number1, number2, prompt="==>", symbol='/'):
    result = number1 / number2
    print(f"{prompt} {number1} {symbol} {number2} = {result}")

def integer_division(number1, number2, prompt="==>", symbol='//'):
    result = number1 // number2
    print(f"==>{number1} {symbol} {number2} = {result}")

def modulo(number1, number2, prompt="==>", symbol='%'):
    result = number1 % number2
    print(f"{prompt} {number1} {symbol} {number2} = {result}")

def exponent(number1, number2, prompt="==>", symbol='**'):
    result = number1 ** number2
    print(f"{prompt} {number1} {symbol} {number2} = {result}")

addition(number1, number2)
subtraction(number1, number2)
floating_division(number1, number2)
integer_division(number1, number2)
modulo(number1, number2)
exponent(number1, number2)        
