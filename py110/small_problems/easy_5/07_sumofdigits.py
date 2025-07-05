""" 
Problem: Write a function that takes one argument, a positive integer, and returns the sum of its digits.
    - input: positive integer
    - output: sum of integers
    - rules:
        - positive only, no empties or negatives

Example: 123 => 6

Data Structure: Lists for holding

Algorithm:
    - convert number to string
    - split string into individual characters in a list
    - convert invidual characters back to integers
    - sum the integers list
    - return list

"""

def sum_digits(num):
    num_to_string = str(num)
    digits = [char for char in num_to_string]
    integers = [int(char) for char in digits]
    return sum(integers)

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True