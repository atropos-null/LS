"""

Problem: Convert string of numeric characters to an actual integer representation
    - input: string of numeric characters
    - output: integer
    - explicit rules: no conversions
    - explicit rules: calculate the result by using the characters in the string.
    - Ascii! Ascii value of 0 is 48

Example: "-4321" == -4321

Data Structure: new integer variable

Algorithm: 
    - set new integer variable to 0
    - iterate over characters in text, looking only for alphanumeric characters
    - each element of the list gets passed through ord() 
    - iterate over the second list with the number and establish place value
    - append place value to integer variable
    - if original string had '-', return result * -1
    - return integer variable

"""

def string_to_signed_integer(text):
    result = 0
    for char in text:
        if char.isdigit():
            digit = ord(char) - ord('0')
            result = result * 10 + digit
    
    if text[0] == '-':
        return result * -1
    else:
        return result

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True