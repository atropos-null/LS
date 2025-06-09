"""

Problem: Convert string of numeric characters to an actual integer representation
    - input: string of numeric characters
    - output: integer
    - explicit rules: no conversions
    - explicit rules: calculate the result by using the characters in the string.
    - explicit rules: assume all characters are numeric

    - Ascii! Ascii value of 0 is 48

Example: "4321" == 4321

Data Structure: List for holding?

Algorithm: 
    - get length of the string
    - iterate over the string character by character
        - append character to the holding list
    - each element of the list gets passed through ord() 
    - iterate over the second list with the number and establish place value
    - append place value to integer variable
    - return integer variable


"""

def string_to_integer(text):
    length = len(text)
    working = []
    numbers = []
    converted = 0
    for char in text:
        working.append(char)
    for i in working:
        number = ord(i) - ord('0')
        numbers.append(number)
    for number in range(len(numbers)):
       converted += numbers[number] * 10**(length-number-1)

    return converted
        
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

"""

Optimization options:

def string_to_integer(text):
    numbers = []
    for char in text:
        number = ord(char) - ord('0')
        numbers.append(number)
    # Rest of the function remains the same


def string_to_integer(text):
    result = 0
    for char in text:
        digit = ord(char) - ord('0')
        result = result * 10 + digit
    return result

"""