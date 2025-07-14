"""
Problem: Write a function that calculates and returns the index of the first Fibonacci number that has the number of digits 
specified by the argument. The first Fibonacci number has an index of 1. You may assume that the argument is always an 
integer greater than or equal to 2.
    - input: number
    - output: number that is a length of the number in the argument

Example: 2 ==> 7

Data Structure: List

Algorithm:
    - intialize list with first two numbers in it
    - a loop comparing the length of the last number in the sequence to the number in the parameter
    - if the length of the last number is less than the number, append the next fibonacci number
    - capture the last value of the sequence
    - get index of the last value and add 1 
    - 

"""

import sys

sys.set_int_max_str_digits(50_000)

def find_fibonacci_index_by_length(number):
  
    sequence = [1, 1] 
    while len(str(sequence[-1])) < number:
        sequence.append(sequence[-2]+sequence[-1])
        last_value = sequence[-1]
    result = sequence.index(last_value) + 1
    return result
  

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
#print(find_fibonacci_index_by_length(10000) == 47847)