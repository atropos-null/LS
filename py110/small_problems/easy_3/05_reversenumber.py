"""
Problem: Write a function that takes a positive integer as an argument and returns that number with its digits reversed.
    - input: positive integer
    - output: integer with digits reversed

Example: 456 => 654

Data Structure: None?

Algo:
    - string = str(number)
    - reversed_string = string[-1:]
    - reversed_number = int(reversed_string)

"""

def reverse_number(number):
   string = str(number)
   reversed_string = string[::-1]
   return int(reversed_string)

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True