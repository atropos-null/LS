"""

Problem: Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.
    - input: a positive integer
    - output: a list of digits in the number.

Example:  12345 = [1,2,3,4,5]

Data Structure: List

Algorithm:
    - initialize empty list
    - coerce integer to a string
    - for loop:
        - iterate over character
        - recoerce back to an integer
        - append list
    

"""

def digit_list(number):
    result = []
    string = str(number)
    for char in string:
        result.append(int(char))
    return result


print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True